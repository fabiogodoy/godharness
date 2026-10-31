---
name: generate-tests
description: "Gera um plano de testes focado para as mudanças, incluindo cenários unitários, integração, E2E, regressão e validação. Use depois de requisitos e análise de impacto para definir o trabalho de verificação."
---

# Skill: Generate Tests

## Objetivo

Gerar uma estratégia completa de testes para validar a implementação, garantindo que todo requisito do PRD tenha evidência objetiva de funcionamento. Nenhuma funcionalidade é considerada pronta sem testes.

Todo requisito deve responder: "como provaremos que isso funciona?"

---

## Referências Obrigatórias

* `AGENTS.md`
* `.ai/context/testing-standards.md`
* `.ai/context/coding-standards.md`
* `.ai/context/architecture.md`
* Intent, PRD, Impact Analysis

## Entrada / Saída

Entrada: `intent/<slug>.md`, `intent/<slug>_prd.md`, `intent/<slug>_impact.md`
Saída: `intent/<slug>_test_plan.md`, usando `.ai/templates/test_plan_template.md`

---

## Processo

1. **Ler o PRD** e extrair RF (requisitos funcionais), RN (regras de negócio) e RNF (não funcionais).
2. **Mapear cobertura** — para cada requisito, "como será validado?"
3. **Matriz de testes** — para cada RF, gerar cenário feliz, cenário alternativo e cenário de erro, com evidência esperada.
4. **Testes unitários** — obrigatórios para toda regra de negócio nova ou alterada. Pergunta: "qual regra está sendo validada?"
5. **Testes de integração** — obrigatórios quando houver integração entre camadas ou com banco/serviços externos. Se acessar banco, usar exclusivamente o banco autorizado em `.ai/context/testing-standards.md`.
6. **Testes E2E** — usar a ferramenta definida em `.ai/context/testing-standards.md`. Obrigatórios para alteração com impacto visual ou de fluxo. Antes da execução: rodar o build do projeto afetado (comando de `.ai/context/testing-standards.md`); se falhar, parar.
7. **Regressão** — "o que pode parar de funcionar?" Criar cenário específico para cada risco levantado no Impact Analysis.
8. **Multi-tenancy** (quando aplicável) — cenário garantindo que um tenant não visualiza dados de outro.
9. **Segurança** — cenário garantindo que usuário sem permissão não acessa recurso protegido.
10. **Performance** (quando aplicável) — cenários para consultas, relatórios ou dashboards sensíveis a volume.
11. **Padrões do `$ub-mode`** — prever teste de comportamento antes da correção quando aplicável, regressão de refatoração e gates configurados em `.ai/context/testing-standards.md`. Para cada gate, registrar comando/versão, escopo, limiar, obrigatoriedade e evidência esperada; ausência ou não aplicabilidade recebe justificativa e limitação, nunca aprovação automática. Para trabalho sem comportamento executável, definir a verificação adequada ao artefato em vez de teste artificial.

---

## Cobertura Mínima

Requisitos funcionais: 100%. Regras de negócio: 100%. Multi-tenancy (quando aplicável): 100%. Segurança: 100%.

---

## Checklist

* [ ] Todos RF cobertos
* [ ] Todas RN cobertas
* [ ] Cenários positivos e negativos definidos
* [ ] Regressão definida
* [ ] Multi-tenancy definida (quando aplicável)
* [ ] Segurança definida
* [ ] E2E definido quando aplicável

## Critérios de Reprovação

RF ou RN sem teste, ausência de cenário negativo, de regressão, de validação de segurança ou de multi-tenancy quando aplicável.

## Critérios de Aprovação

Todo requisito e toda regra possuem cobertura, toda validação possui evidência esperada definida.

---

## Próxima Etapa

Após a implementação, executar os testes deste plano e seguir para `$validate-delivery`.

---

## Regra Suprema

Se um requisito não possui teste, ele não possui evidência. Sem evidência, não há garantia de funcionamento. Todo requisito deve ser testado.
