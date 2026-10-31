#!/usr/bin/env bash
# Audita a governanca do repositorio (AGENTS.md, docs/adr, intent/, .agents/skills).
# Uso: scripts/governance-audit.sh [--template]
# Sai com codigo != 0 se encontrar qualquer inconsistencia.

set -euo pipefail
cd "$(dirname "$0")/.."

usage() {
  echo 'Uso: scripts/governance-audit.sh [--template]'
  echo 'Padrao: exige bootstrap done. --template: valida o harness generico ainda pending.'
  echo 'O modo template nao autoriza desenvolver uma aplicacao sem bootstrap.'
}

mode=project
if [ "$#" -gt 1 ]; then
  usage >&2
  exit 2
fi
case "${1:-}" in
  '') ;;
  --template) mode=template ;;
  --help|-h) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

fail=0

# Aceita declaracao canonica ou valor da secao Markdown, sem ler a enumeracao.
# Multiplas declaracoes permanecem em linhas distintas e nao casam com um estado valido.
bootstrap_status=''
if [ -r .ai/context/project-status.md ]; then
  bootstrap_status=$(awk '
    /^bootstrap:[[:space:]]*/ {
      sub(/^bootstrap:[[:space:]]*/, "")
      sub(/[[:space:]]*$/, "")
      print "status:" $0
      in_bootstrap = 0
      next
    }
    /^##[[:space:]]+bootstrap[[:space:]]*$/ { in_bootstrap = 1; next }
    /^##[[:space:]]/ { in_bootstrap = 0 }
    in_bootstrap && NF {
      if ($0 ~ /^[[:space:]]*`[^`]+`[[:space:]]*$/) {
        sub(/^[[:space:]]*`/, "")
        sub(/`[[:space:]]*$/, "")
      }
      print "status:" $0
      in_bootstrap = 0
    }
  ' .ai/context/project-status.md)
fi

echo "== 0. Bootstrap (modo: $mode) =="
case "$bootstrap_status" in
  status:done) echo 'OK: bootstrap concluido.' ;;
  status:pending)
    if [ "$mode" = template ]; then
      echo 'OK: template com bootstrap pending; nao libera desenvolvimento de aplicacao.'
    else
      echo 'FALHA: bootstrap pendente. Rode $bootstrap-project antes de entregar uma aplicacao.'
      fail=1
    fi
    ;;
  *)
    echo 'FALHA: bootstrap ausente, invalido, ambiguo ou in_progress.'
    fail=1
    ;;
esac

echo
echo "== 1. Numeros de ADR duplicados =="
if [ -d docs/adr ] && ls docs/adr/ADR-*.md >/dev/null 2>&1; then
  dupes=$(ls docs/adr | grep -E '^ADR-[0-9]+-' | grep -oE '^ADR-[0-9]+' | sort | uniq -d)
  if [ -n "$dupes" ]; then
    echo "FALHA: numero(s) de ADR duplicado(s):"
    for d in $dupes; do
      ls docs/adr/"${d}"-*.md
    done
    fail=1
  else
    echo "OK: nenhum numero de ADR duplicado."
  fi
else
  echo "OK: nenhuma ADR criada ainda."
fi

echo
echo "== 2. ADRs ausentes do indice docs/adr/README.md =="
missing_from_index=0
if ls docs/adr/ADR-*.md >/dev/null 2>&1; then
  for f in docs/adr/ADR-*.md; do
    num=$(basename "$f" | grep -oE '^ADR-[0-9]+')
    if ! grep -q "| $num |" docs/adr/README.md 2>/dev/null; then
      echo "FALHA: $f nao esta listado em docs/adr/README.md"
      missing_from_index=1
    fi
  done
fi
if [ "$missing_from_index" -eq 0 ]; then
  echo "OK: todas as ADRs estao no indice."
else
  fail=1
fi

echo
echo "== 3. Sufixos inconsistentes em intent/ (underscore em vez de hifen) =="
bad_suffix=$(ls intent/ 2>/dev/null | grep -E '_(architecture|implementation|business|security|observability)_review\.md$|_impact-analysis\.md$|_impact_analysis\.md$' || true)
if [ -n "$bad_suffix" ]; then
  echo "FALHA: arquivos com sufixo fora do padrao (deveriam usar hifen e '_impact.md'):"
  echo "$bad_suffix"
  fail=1
else
  echo "OK: nenhum sufixo divergente encontrado."
fi

echo
echo "== 4. Skills em .agents/skills/ ausentes da lista em AGENTS.md =="
actual_skills=$(ls .agents/skills | sort)
listed_skills=$(grep -oE '\$[a-z0-9-]+' AGENTS.md | sed 's/^\$//' | sort -u)
missing_skills=$(comm -23 <(echo "$actual_skills") <(echo "$listed_skills"))
if [ -n "$missing_skills" ]; then
  echo "FALHA: skill(s) existente(s) em .agents/skills/ mas nao listada(s) em AGENTS.md:"
  echo "$missing_skills"
  fail=1
else
  echo "OK: toda skill em .agents/skills/ esta listada em AGENTS.md."
fi

echo
if [ "$fail" -eq 0 ]; then
  echo "Auditoria de governanca: TUDO OK."
else
  echo "Auditoria de governanca: FALHOU. Corrigir os itens acima antes de aprovar a entrega."
fi
exit "$fail"
