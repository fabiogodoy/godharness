---
name: validate-delivery
description: "Valida uma entrega contra Intent, PRD, Impact Analysis, comportamento implementado, testes e critérios de release. Use ao final de uma mudança, antes de considerar a tarefa concluída."
---

# Skill: Validate Delivery

## Objetivo

Validar se a implementação entregue atende integralmente a Intent, o PRD e os critérios de qualidade do projeto. Esta é a etapa final do processo — nenhuma funcionalidade é considerada concluída sem esta validação.

## Regra Principal

A implementação não é a fonte da verdade. A fonte da verdade é: Intent → PRD → Código. Em caso de divergência, o PRD prevalece.

---

## Referências Obrigatórias

* `AGENTS.md`
* `.ai/context/business.md`, `architecture.md`, `coding-standards.md`, `testing-standards.md`
* Intent, PRD, Impact Analysis, ADR (quando existir), Test Plan, Implementation Review

## Entrada / Saída

Entrada: `intent/<slug>.md`, `intent/<slug>_prd.md`, `intent/<slug>_impact.md`, `intent/<slug>_test_plan.md`, `intent/<slug>_implementation-review.md`, mais toda a implementação.
Saída: `intent/<slug>_validation_report.md`, usando `.ai/templates/validation_report_template.md`.

## Aplicabilidade das validações

As exigências de build, testes de aplicação e ambiente executado, inclusive nos critérios/checklists abaixo, pressupõem alvo executável ou impacto em seu comportamento/configuração. Para mudança exclusivamente documental sem esse impacto, aceitar não aplicabilidade fundamentada no Test Plan/Validation Report e exigir evidência da verificação dos artefatos alterados. Gates obrigatórios pertinentes, inclusive documentais, continuam bloqueantes; indisponibilidade não justifica não aplicabilidade.

---

## Processo

1. **Validar o problema original** — a implementação resolve o problema da Intent? Sim/parcialmente/não.
2. **Validar objetivos** — o resultado esperado foi alcançado?
3. **Validar Requisitos Funcionais** — para cada RF: implementado (sim/não), evidência, observações. Todo RF precisa de evidência (código, teste, execução, screenshot, log).
4. **Validar Regras de Negócio** — para cada RN: atendida (sim/não), evidência. Reprovar se qualquer RN não implementada.
5. **Validar Requisitos Não Funcionais** — segurança, multi-tenancy (quando aplicável), performance, compatibilidade, observabilidade.
6. **Validar Build** — foi executado? Resultado sucesso/falha. Sem build executado: STATUS = REPROVADO.
7. **Auditoria de governança** — se a entrega criou ou renomeou Intent, PRD, ADR ou skill, executar `scripts/governance-audit.sh`. Script falhando (código de saída ≠ 0): STATUS = REPROVADO até correção.
   Para manutenção do template expressamente autorizada pelo solicitante com bootstrap pendente, usar `scripts/governance-audit.sh --template`, registrar autorização, modo e resultado. Isso não dispensa bootstrap de aplicações. Nesta manutenção sem aplicação, build/ambiente/E2E de aplicação são não aplicáveis com justificativa; executar a validação dos artefatos e scripts alterados.
8. **Validar testes** — unitários, integração, E2E realmente executados (não apenas escritos). Reprovar se não executados, falhando ou inexistentes.
9. **Validar ambiente** — a aplicação foi de fato executada (não só compilada), conforme o procedimento em `.ai/context/testing-standards.md`.
10. **Validar multi-tenancy** (quando aplicável) — identificador de tenant validado, isolamento preservado, sem vazamento de dados.
11. **Validar segurança** — autenticação, autorização, permissões, dados sensíveis.
12. **Validar regressões** — comparar Impact Analysis com o resultado real; alguma regressão prevista ocorreu?
13. **Validar evidências** — screenshots, vídeos, logs, testes, build. Sem evidência, não considerar validado.
14. **Validar reintegração na main** — quando a entrega usar branch própria, confirmar com evidência de Git que a branch foi atualizada com `origin/main` antes do merge final, que o commit final pertence à `main` local, e que `origin/main` foi atualizada. Ver `$reintegrar-main`.
15. **Validar `$ub-mode`** — conferir a Implementation Review e evidências dos gates contra `.ai/context/testing-standards.md`. Exigir estado, resultado ou justificativa e limitações; gate obrigatório ausente/falho reprova sem exceção expressamente aprovada e registrada. Documentar gates não configurados/não aplicáveis e testes impraticáveis sem inventar aprovação.

---

## Matriz de Aprovação

Intent, PRD, RF, RN, Segurança, Multi-Tenancy (quando aplicável), Build, Testes, Regressão, Reintegração na Main — cada item: OK / NOK.

## Checklist Final

* [ ] Intent e objetivos atendidos
* [ ] Todos RF implementados
* [ ] Todas RN implementadas
* [ ] Segurança validada
* [ ] Multi-tenancy validada (quando aplicável)
* [ ] Build executado
* [ ] Testes executados
* [ ] E2E executado quando aplicável
* [ ] Aplicação executada
* [ ] Evidências coletadas
* [ ] Branch de entrega mesclada na `main`, quando aplicável
* [ ] `origin/main` publicada com o merge final, quando aplicável

## Critérios de Reprovação

RF ou RN não implementado, build ou testes falhando, aplicação não executada, falha de segurança ou multi-tenancy, ausência de evidências, branch própria não mesclada/publicada.

## Critérios de Aprovação

Todos os requisitos e regras atendidos, todas as evidências presentes, todos os testes passando, reintegração comprovada quando aplicável.

---

## Pendências Externas ao Escopo

Alterações no worktree que não pertencem à Intent atual não reprovam a entrega por si só, desde que não tenham entrado no commit e estejam registradas no relatório para tratamento em Intent própria.

---

## Parecer Final

Status: APROVADO / APROVADO COM RESSALVAS / REPROVADO, com justificativa, pendências e recomendações.

---

## Regra Suprema

Código implementado não significa funcionalidade entregue. Funcionalidade entregue significa: problema resolvido, requisitos atendidos, testes executados, evidências coletadas, validação aprovada. Somente então a entrega pode ser considerada concluída.
