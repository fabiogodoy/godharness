---
name: implementation-review
description: "Revisa a implementação quanto a corretude, regressões, requisitos faltantes, manutenibilidade, segurança e cobertura de testes. Use depois das mudanças de código e antes da validação final."
---

# Skill: Implementation Review

## Objetivo

Realizar uma revisão técnica completa da implementação antes da validação final. Esta skill atua como um Senior Engineer Reviewer.

Seu objetivo não é validar requisitos de negócio, nem validar cobertura do PRD (isso é `$validate-delivery`). Seu objetivo é validar a qualidade técnica da implementação.

---

## Referências Obrigatórias

* `AGENTS.md`
* `.ai/context/architecture.md`
* `.ai/context/coding-standards.md`
* `.ai/context/testing-standards.md`
* `.agents/skills/ub-mode/SKILL.md`
* Intent, PRD, Impact Analysis, ADR (quando existir)

## Entrada / Saída

Entrada: `intent/<slug>.md`, `intent/<slug>_prd.md`, `intent/<slug>_impact.md`, mais toda a implementação.
Saída: `intent/<slug>_implementation-review.md`

---

## Processo

1. **Ler os artefatos** — Intent, PRD, Impact Analysis, ADR.
2. **Revisar as alterações** — arquivos criados, alterados, removidos.
3. **Complexidade** — a implementação é mais complexa do que deveria? Classificar baixa/média/alta.
4. **Reutilização** — o código reutiliza implementações existentes (serviços, utilitários, componentes)? Reprovar duplicação desnecessária.
5. **Aderência à stack e camadas** — conforme `.ai/context/coding-standards.md` e `.ai/context/architecture.md`. Reprovar regra de negócio na camada errada (ex.: em endpoint/controller ou em camada de persistência).
6. **Dados/banco** — migrations presentes quando necessário, índices adequados; existe N+1, consulta desnecessária, loop acessando banco?
7. **Clean Code** — nomes claros, métodos pequenos, responsabilidades claras, ausência de código morto. "Outro desenvolvedor conseguiria manter isso?"
8. **Segurança** — checklist: autenticação, autorização e permissões preservadas; dados sensíveis protegidos; logs adequados.
9. **Multi-tenancy** (quando aplicável) — checklist: identificador de tenant validado, isolamento preservado, sem vazamento de dados.
10. **Performance** — classificar baixa/média/alta.
11. **Dependências novas** — eram realmente necessárias? O ganho compensa o custo?
12. **Débito técnico** — identificar atalhos/workarounds/limitações e documentar motivo, impacto e plano futuro.
13. **Aplicação do `$ub-mode`** — confrontar o diff com os padrões, Test Plan e evidências: comportamento validado, causa corrigida, refatoração no escopo e gates configurados executados. Registrar por gate comando/resultado/evidência ou motivo de ausência/não aplicabilidade. Gate obrigatório ausente ou falho reprova, salvo exceção expressamente aprovada e registrada na governança; gate não obrigatório pendente permanece como limitação no Validation Report. Cobertura, CRAP, duplicação e mutação não se substituem entre si.

---

## Checklist de Qualidade

* [ ] arquitetura respeitada
* [ ] padrões respeitados
* [ ] `$ub-mode` verificado; resultados dos gates e limitações registrados
* [ ] código reutilizado
* [ ] segurança revisada
* [ ] multi-tenancy revisada (quando aplicável)
* [ ] performance revisada
* [ ] dependências revisadas
* [ ] débito técnico identificado

## Critérios de Reprovação

Quebra arquitetural, regra de negócio na camada errada, duplicação relevante, falha de segurança ou multi-tenancy, problema crítico de performance.

## Critérios de Aprovação

Implementação simples, sustentável, segura e aderente à arquitetura.

---

## Classificação Final

Qualidade técnica (excelente/boa/regular/ruim), risco técnico (baixo/médio/alto), débito técnico (nenhum/baixo/médio/alto).

## Parecer Final

Status (APROVADO / APROVADO COM RESSALVAS / REPROVADO), justificativa, recomendações.

## Próxima Etapa

Se aprovado, executar `$security-review` e `$observability-review`, e então `$validate-delivery`.

---

## Regra Suprema

Código que funciona não é necessariamente código aprovado. Uma implementação só é concluída quando funciona, é sustentável, é segura, respeita a arquitetura e pode ser mantida pela equipe.
