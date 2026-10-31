---
name: orchestrator
description: "Coordena o fluxo completo de governança do projeto antes da implementação: entendimento, Intent, PRD, análise de impacto, reviews, testes e validação. Use quando a solicitação mudar produto, código, arquitetura, integrações ou comportamento operacional."
---

# Skill: Orchestrator

## Objetivo

Esta é a skill principal do harness. Nenhuma implementação deve iniciar sem passar por ela. O Orchestrator coordena todo o fluxo de engenharia, produto, arquitetura, implementação, testes e validação — atuando como um CTO virtual.

## Pré-requisito

`.ai/context/project-status.md` deve indicar `bootstrap: done`. Se não indicar, parar aqui e executar `$bootstrap-project` primeiro.

---

## Missão

Garantir que toda alteração resolva um problema real, possua documentação adequada, respeite a arquitetura, seja testada, validada, e não gere regressões desnecessárias.

## Regra Principal

É proibido iniciar implementação diretamente. Toda solicitação passa pelo fluxo, no nível de rigor apropriado ao seu tamanho (ver Matriz de Decisão).

---

## Fluxo Oficial

```text
Solicitação
  ↓
Entendimento ($grilling, direto ou via $grill-me para pedidos não técnicos)
  ↓
Intent ($create-intent)
  ↓
PRD ($create-prd)
  ↓
Impact Analysis ($impact-analysis)
  ↓
ADR (quando necessário — ver $impact-analysis / $domain-modeling)
  ↓
Architecture Review ($architecture-review)
  ↓
Business Review ($business-review)
  ↓
Tickets, quando a entrega exigir mais de uma integração segura na main ($to-tickets)
  ↓
Implementação ($ub-mode)
  ↓
Testes ($generate-tests, executados de verdade)
  ↓
Implementation Review ($implementation-review)
  ↓
Security Review ($security-review)
  ↓
Observability Review ($observability-review)
  ↓
Reintegração na main ($reintegrar-main)
  ↓
Validation Report ($validate-delivery)
  ↓
Entrega
```

---

## Etapa 1 — Entendimento

Objetivo: estabelecer entendimento compartilhado antes de registrar a Intent.

Executar `$grilling` diretamente para mudanças técnicas (software, arquitetura, integrações, código); usar `$grill-me` como ponto de entrada para solicitações não técnicas/operacionais (ele delega à `$grilling`).

Regras de execução:

* Conduzir a entrevista em rodadas: perguntar toda decisão cuja dependência já está resolvida, aguardar resposta antes de seguir.
* Investigar fatos disponíveis no repositório, nas ferramentas e em `.ai/context/*` sem transferi-los ao usuário; apresentar somente as decisões que exigem direção do usuário.
* Não assumir decisões pendentes. Não iniciar Intent, PRD, análise, ADR ou implementação antes da confirmação do usuário.
* Se o termo/vocabulário do domínio estiver em jogo, usar `$domain-modeling` para manter o glossário (`CONTEXT.md`, se o projeto tiver um) consistente.

Após a confirmação, executar `$create-intent`. Resultado esperado: `intent/<slug>.md`.

---

## Etapa 2 — PRD

Executar `$create-prd`. Resultado esperado: `intent/<slug>_prd.md`.

## Etapa 3 — Impact Analysis

Executar `$impact-analysis`. Resultado esperado: `intent/<slug>_impact.md`.

## Etapa 4 — Necessidade de ADR

Avaliar se a alteração cria nova estrutura de dados relevante, altera arquitetura, adiciona dependência importante, altera autenticação/autorização/multi-tenancy, adiciona integração externa, ou gera débito técnico consciente.

Se sim: gerar `docs/adr/ADR-XXXX-<slug>.md`. Consultar `docs/adr/README.md` para o próximo número livre antes de criar o arquivo, e adicionar a entrada ao índice na mesma entrega. Usar `.ai/templates/adr_template.md` para decisões grandes, ou o formato leve de `.agents/skills/domain-modeling/ADR-FORMAT.md` para decisões pequenas e reversíveis.

Se não: prosseguir.

## Etapa 5 — Architecture Review

Executar `$architecture-review`.

## Etapa 6 — Business Review

Executar `$business-review`.

## Etapa 7 — Planejamento de Tickets e Testes

Antes do plano de testes, avaliar se a entrega exige mais de uma integração segura na `main`. Se sim, executar `$to-tickets` — os tickets devem ser fatias verticais verificáveis, com bloqueios explícitos. Se não, registrar no PRD por que a entrega cabe em uma única integração.

Executar `$generate-tests`. Resultado esperado: `intent/<slug>_test_plan.md`.

## Etapa 8 — Implementação

Somente após todas as etapas anteriores. Seguir `.ai/context/coding-standards.md`, `architecture.md` e `business.md`.

Acionar `$ub-mode` antes e durante a escrita/alteração de código. O Test Plan deve prever testes de comportamento e os gates configurados em `.ai/context/testing-standards.md`. Avaliar testes antes da alteração de comportamento e refatorar dentro da Intent; não ampliar escopo para satisfazer uma métrica. Ferramentas ausentes e não aplicabilidades têm justificativa e limitação explícitas; gate obrigatório ausente/falho bloqueia, salvo exceção aprovada na governança do projeto.

## Etapa 9 — Build Obrigatório

As exigências de build, ambiente e testes de aplicação nas etapas e critérios deste fluxo se aplicam quando a entrega possui alvo executável ou afeta seu comportamento/configuração. Para alteração exclusivamente documental sem esse impacto, registrar no Test Plan a não aplicabilidade de cada item e executar a verificação adequada aos artefatos. Essa regra não dispensa validações documentais ou gates obrigatórios pertinentes definidos pelo projeto.

Executar o build do projeto/módulo impactado (comando definido em `.ai/context/testing-standards.md`). Se falhar: PARAR. Não prosseguir.

## Etapa 10 — Ambiente

Subir o ambiente local conforme `.ai/context/testing-standards.md` e validar que a aplicação está funcionando.

## Etapa 11 — Testes

Executar unitários, integração e E2E conforme o Test Plan. Se houver teste de integração com banco, validar a datasource efetiva contra o que está definido em `.ai/context/testing-standards.md` antes de rodar — qualquer divergência bloqueia o teste. Nenhum teste pode ser marcado como executado sem execução real.

## Etapa 12 — Reviews Pós-Implementação

Executar, nesta ordem: `$implementation-review`, `$security-review`, `$observability-review`.

## Etapa 13 — Reintegração na Main

Executar `$reintegrar-main`. A entrega deve estar em `main` e `origin/main`. Pendências externas ao escopo não bloqueiam a etapa, mas ficam fora do commit e constam no relatório final.

## Etapa 14 — Validation Report

Executar `$validate-delivery`. Resultado esperado: `intent/<slug>_validation_report.md`.

---

## Critérios de Reprovação (bloqueiam a entrega imediatamente)

RF não implementado, RN não implementada, build falhou, testes falharam, segurança comprometida, multi-tenancy comprometida (quando aplicável).

## Critérios de Aprovação

Intent atendida, PRD atendido, impactos avaliados, ADR criado quando necessário, build executado, testes executados, todas as reviews aprovadas, Validation Report aprovado, branch de entrega mesclada na `main` quando houver branch própria, `origin/main` enviada com o merge final.

---

## Matriz de Decisão

### Bug pequeno / correção pontual

Executar: Intent simplificada → PRD simplificado → implementação → testes → `$validate-delivery`. As demais reviews podem ser dispensadas se o risco for baixo — registrar essa decisão no PRD.

### Nova funcionalidade

Executar o fluxo completo.

### Refatoração

Executar: Intent → Impact Analysis → Architecture Review → implementação → testes → `$validate-delivery`.

### Mudança arquitetural

Executar o fluxo completo. ADR obrigatório.

A decisão sobre qual modo usar por padrão para este projeto foi registrada pelo `$bootstrap-project` em `AGENTS.md` (seção "Configuração do Fluxo"); esta matriz é o padrão quando não houver configuração específica.

---

## Autoridade

O Orchestrator pode bloquear implementação, exigir ADR, exigir testes, exigir revisão.

## Proibições

Nunca implementar sem Intent, sem PRD, aprovar sem testes, aprovar sem validação, ignorar impacto em multi-tenancy (quando aplicável) ou em usuários já em produção.

---

## Regra Suprema

A missão do Orchestrator não é produzir código. É garantir que a entrega esteja correta. Código é apenas uma das etapas do processo.
