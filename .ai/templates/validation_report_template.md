# Delivery Validation Report

> Este documento valida se a implementação atende integralmente a Intent e o PRD.
>
> Nenhuma funcionalidade é considerada concluída sem este relatório.
>
> O objetivo não é validar código. O objetivo é validar entrega.

> Para trabalho exclusivamente documental sem alvo/impacto executável, registrar não aplicabilidade fundamentada de build, ambiente e testes de aplicação, conforme `$validate-delivery`. Exigir evidência da verificação dos artefatos. Gate obrigatório pertinente ausente/falho não é "não aplicável".

---

# Metadados

## Funcionalidade

## Slug

## Data da Validação

## Responsável

## Intent

`intent/<slug>.md`

## PRD

`intent/<slug>_prd.md`

---

# Resumo Executivo

Resumo da funcionalidade implementada.

---

# Status Geral

* APROVADO
* APROVADO COM RESSALVAS
* REPROVADO

---

# Cobertura da Intent

## Problema Original

## O problema foi resolvido?

* Sim / Parcialmente / Não

## Evidências

---

# Cobertura do PRD

## Total de Requisitos Funcionais

## Requisitos Implementados

## Requisitos Pendentes

## Cobertura

[%]

---

# Validação dos Requisitos Funcionais

## RF001

### Implementado

* Sim / Não

### Evidência

### Observações

---

# Validação das Regras de Negócio

## RN001

### Atendida

* Sim / Não

### Evidência

---

# Validação dos Requisitos Não Funcionais

## Performance

Atendido? Sim / Não — Observações.

## Segurança

Atendido? Sim / Não — Observações.

## Multi-Tenancy (quando aplicável)

Atendido? Sim / Não — Observações.

## Compatibilidade

Atendido? Sim / Não — Observações.

## Observabilidade

Atendido? Sim / Não — Observações.

---

# Validação de Multi-Tenancy (quando aplicável)

* [ ] identificador de tenant validado
* [ ] isolamento preservado
* [ ] consultas revisadas
* [ ] permissões revisadas
* [ ] sem vazamento de dados

---

# Validação de Segurança

* [ ] autenticação validada
* [ ] autorização validada
* [ ] permissões revisadas
* [ ] sem exposição de dados sensíveis
* [ ] logs adequados

---

# Validação Técnica

Para cada sistema/módulo impactado (ver `.ai/context/architecture.md`):

## [Sistema/Módulo]

Status: OK / NOK — Observações.

---

# Validação dos Testes

## Testes Unitários

Executados? Sim / Não — Resultado.

## Testes de Integração

Executados? Sim / Não — Resultado.

## Testes E2E

Executados? Sim / Não — Resultado.

---

# Evidências de Teste

## Screenshots / Vídeos / Logs

Links ou caminhos.

---

# Build

## Build Executado

* Sim / Não / Não aplicável — Justificativa.

## Resultado

* Sucesso / Falha / Não aplicável — Justificativa.

---

# Ambiente Validado

## Projeto

## Ambiente

* Local / Homologação / Produção

---

# Reintegração na Main

## Branch de Entrega

## Main de Origem (SHA de `origin/main` usado para sincronizar)

## Tipo de Integração

* Fast-forward / Merge commit / Alteração direta na main

## SHA Final da Main

## Evidência de Publicação (`git push origin main`)

* Sucesso / Falha — Observações.

---

# Pendências Externas ao Escopo

Listar alterações encontradas no worktree que não pertencem à Intent atual. Não reprovam a entrega quando não entraram no commit e foram registradas aqui para tratamento em Intent própria.

---

# Regressões Encontradas

## RG001

Descrição. Status.

---

# Divergências Encontradas

Listar qualquer divergência entre Intent, PRD e código.

---

# Pendências

---

# Débito Técnico Gerado

---

# Riscos Residuais

---

# Parecer Final

## A funcionalidade atende a Intent?

* Sim / Parcialmente / Não

## A funcionalidade atende ao PRD?

* Sim / Parcialmente / Não

## Todos os testes passaram?

* Sim / Não

## Existe risco impeditivo?

* Sim / Não

---

# Decisão Final

## Status

* APROVADO
* APROVADO COM RESSALVAS
* REPROVADO

## Justificativa

---

# Checklist de Liberação

* [ ] Intent atendida
* [ ] PRD atendido
* [ ] RFs implementados
* [ ] RNs implementadas
* [ ] Build executado
* [ ] Testes executados
* [ ] E2E executado quando aplicável
* [ ] Multi-tenancy validada quando aplicável
* [ ] Segurança validada
* [ ] Validation Report aprovado
* [ ] Branch de entrega mesclada na `main`, quando aplicável
* [ ] `origin/main` publicada com a integração final, quando aplicável
* [ ] Pendências externas registradas ou ausência confirmada

---

# Regra Suprema

Se um requisito estiver no PRD e não estiver implementado: STATUS = REPROVADO.

Se os testes não foram executados: STATUS = REPROVADO.

Se houver risco crítico sem mitigação: STATUS = REPROVADO.

A implementação somente é considerada concluída quando o relatório estiver APROVADO.
