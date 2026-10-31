# Test Plan — integrar-ub-mode

Data: 2026-10-31. Referências: [PRD](integrar-ub-mode_prd.md), [Impact Analysis](integrar-ub-mode_impact.md).

| Requisito | Cenário positivo | Cenário negativo / regressão | Evidência |
|---|---|---|---|
| RF001 | Skill válida e com fonte fixa | Frontmatter incompleto; instrução indevida de instalação/limpeza | quick_validate e revisão documental |
| RF002 | Chamada do ub-mode nas etapas previstas | Skill fora da lista ou implementação sem revisão dos padrões | Auditoria e revisão dos pontos de integração |
| RF003 | Gates configurados têm comando, limiar e evidência | Ferramenta ausente, falha, teste artificial, documentação sem runtime | Avaliação de cenários na review; sem alegar execução de ferramentas externas |
| RF004 | `done` no modo padrão; `pending` em `--template` | `pending` normal, `in_progress`, desconhecido/ausente/duplicado, argumento inválido | Testes Python via subprocess |
| RF004 | Estrutura consistente passa em ambos os modos | ADR duplicada/ausente do índice, sufixo incorreto, skill não listada continuam falhando | Fixtures temporárias, sem modificar repo real |
| RF005 | README explica uso e limitações; entrega publicada | Relatório sem evidência ou publicação pendente não recebe aprovação final | Auditoria, diff, logs e Git |

## Execução planejada

1. Criar e executar os testes da auditoria antes da mudança de implementação; observar falhas pelas causas esperadas.
2. Ajustar auditoria e executar novamente os testes.
3. Executar `bash -n scripts/governance-audit.sh`, `scripts/governance-audit.sh --template` e `git diff --check`.
4. Executar o `quick_validate.py` de skill-creator para a skill local, com PyYAML em ambiente temporário, se necessário.
5. Revisar cenários: bug com teste significativo; documentação sem código; gate obrigatório ausente; código legado sem refatoração fora de escopo; preservação de worktrees/credenciais.

## Não aplicáveis e limitações

Build de aplicação, banco, multi-tenancy, UI e E2E não existem neste template. Crapper, Dryer e Mutator não foram configurados nem serão instalados nesta entrega. Testes estruturais da governança e avaliação de cenários não provam adesão futura de todo agente; constituem evidência da integração e de seus limites.

## Evidências

Resultados reais serão registrados no Validation Report, incluindo a falha esperada da auditoria padrão enquanto o bootstrap permanece pendente.
