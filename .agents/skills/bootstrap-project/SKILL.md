---
name: bootstrap-project
description: "Entrevista inicial que transforma este harness vazio no contexto de um projeto real, gerando .ai/context/business.md, architecture.md, coding-standards.md e testing-standards.md. Use sempre que .ai/context/project-status.md indicar bootstrap pendente, ou quando o usuário pedir para configurar/inicializar o projeto."
---

# Skill: Bootstrap Project

## Objetivo

Este harness começa como um balão vazio: nenhuma skill de desenvolvimento pode rodar antes de sabermos o que estamos construindo.

Esta skill existe para preencher, uma única vez (e revisitar quando o projeto mudar substancialmente), os quatro documentos que todas as outras skills leem como fonte de verdade:

* `.ai/context/business.md`
* `.ai/context/architecture.md`
* `.ai/context/coding-standards.md` (seção "Convenções Específicas do Projeto")
* `.ai/context/testing-standards.md` (seção "Configuração Específica do Projeto")

E então marcar `.ai/context/project-status.md` como `bootstrap: done`.

---

## Quando executar

* Sempre que `.ai/context/project-status.md` indicar `bootstrap: pending` ou `bootstrap: in_progress` — nenhuma outra skill de desenvolvimento deve rodar antes disso.
* Quando o usuário pedir explicitamente para "configurar o projeto", "inicializar", "começar do zero", ou equivalente.
* Quando o usuário indicar que o projeto mudou de forma relevante (nova tecnologia, novo módulo, pivot de negócio) e pedir para atualizar o contexto — nesse caso, tratar como uma revisão, não como uma entrevista do zero: ler o que já existe, mostrar o que mudou e perguntar só a diferença.

## Regra Zero desta skill

Nunca inventar respostas de negócio, arquitetura ou stack no lugar do usuário. Fatos que podem ser **descobertos** (ex.: "este repositório já tem um `package.json`? qual framework ele usa?") devem ser investigados pelo próprio agente, em paralelo, sem perguntar ao usuário. Decisões que dependem de **preferência, prioridade ou contexto de negócio** são sempre do usuário.

---

## Processo

### Etapa 0 — Verificar estado atual

1. Ler `.ai/context/project-status.md`.
2. Ler `.ai/context/business.md` e `.ai/context/architecture.md` para saber se ainda estão no placeholder de bootstrap ou já têm conteúdo real.
3. Rodar uma varredura rápida do repositório (arquivos de manifesto como `package.json`, `pyproject.toml`, `go.mod`, `pom.xml`, `Gemfile`, `Cargo.toml`, `*.csproj`, pastas de app mobile, `docker-compose.yml`, CI existente) para levantar fatos que não precisam ser perguntados. Isso é investigação do agente, não pergunta ao usuário.
4. Marcar `project-status.md` como `bootstrap: in_progress`.

### Etapa 1 — Entrevista em rodadas

Use o mesmo mecanismo de `$grilling`: pergunte em rodadas, numerando as perguntas da fronteira atual, dê sua recomendação quando fizer sentido, e espere a resposta do usuário antes da próxima rodada. Não faça todas as perguntas de uma vez de forma desorganizada — agrupe por tema e avance conforme as respostas desbloqueiam a próxima rodada.

Os temas obrigatórios a cobrir (adapte a ordem e o agrupamento ao que fizer sentido para o projeto):

#### Bloco 1 — Identidade e negócio (→ `business.md`)

* Nome do projeto/produto.
* Pitch de uma frase: que problema ele resolve e para quem.
* É um produto novo (greenfield) ou este harness está sendo adicionado a um projeto já existente?
* Quem são os usuários/perfis principais (ex.: admin, cliente final, operador interno)?
* Modelo de negócio, se houver (SaaS, interno, open source, app consumidor, etc.) — só perguntar se for relevante; projetos internos/ferramentas podem pular isso.
* Quais indicadores importam para julgar se uma mudança é boa (ex.: retenção, ativação, tempo de resposta, redução de suporte, ou métricas técnicas se não houver contexto comercial)?

#### Bloco 2 — Arquitetura e stack (→ `architecture.md`)

* Estrutura do repositório: monorepo com múltiplos módulos, ou vários repositórios? Se monorepo, quais são as pastas/projetos principais e o papel de cada um?
* Stack de cada módulo relevante: linguagem, framework, banco de dados, infraestrutura/deploy.
* Como os módulos se comunicam entre si (API REST, eventos, chamada direta, etc.), se houver mais de um.
* É multi-tenant? Se sim, qual é o identificador de isolamento (ex.: `tenant_id`, `owner_id`, `organization_id`) e a regra é absoluta (nenhum dado pode atravessar tenants)?
* Existem convenções de nomenclatura já estabelecidas (ex.: sufixos de classe, padrão de pastas) que devem ser preservadas?
* Existem restrições de compatibilidade retroativa (sistema legado em produção, clientes existentes) que limitam mudanças arquiteturais?

#### Bloco 3 — Padrões de código (→ `coding-standards.md`)

* Convenções de nomenclatura e organização específicas da stack escolhida (ex.: camadas obrigatórias, padrão de sufixo de arquivos/classes).
* Gerenciador de dependências e política para adicionar novas bibliotecas.
* Se houver migração de banco de dados: qual ferramenta (Liquibase, Flyway, Prisma Migrate, Alembic, etc.)?

#### Bloco 4 — Testes e ambiente (→ `testing-standards.md`)

* Framework(s) de teste unitário/integração.
* Framework de E2E, se houver, e como ele é executado.
* Comando de build do projeto (ou de cada módulo).
* Como subir o ambiente local para testes manuais/E2E (comando, porta, dependências como banco local).
* Se houver testes de integração com banco: qual é o banco autorizado para isso, e existe uma regra dura contra rodar teste em produção/homologação?
* Cobertura mínima esperada, se o time já tiver um padrão.
* Gates do `$ub-mode`: investigar ferramentas de complexidade/cobertura, duplicação e mutação existentes e sua compatibilidade com a stack. Definir com o usuário ferramenta/versão ou equivalente, comando, escopo, limiar, obrigatoriedade, exclusões e evidências; quando não configurado ou não aplicável, registrar justificativa e limitação. Não instalar ferramentas nem inventar comandos para completar o bootstrap.

#### Bloco 5 — Processo e governança

* O fluxo completo descrito em `AGENTS.md` (Intent → PRD → Impact Analysis → Architecture Review → Business Review → Tickets → Implementação → Testes → Reviews → Reintegração → Validação) deve valer para toda mudança, ou o usuário quer um modo simplificado por padrão para este projeto (ex.: só para mudanças grandes)? Registrar a decisão — o padrão recomendado é: fluxo completo para funcionalidades novas e mudanças arquiteturais, fluxo simplificado (Intent leve → PRD leve → implementação → testes → validação) para bugs pequenos, conforme a Matriz de Decisão do `AGENTS.md`.
* Rastreador de tickets: arquivos locais em `.scratch/` (padrão) ou um tracker real (GitHub Issues, Linear, etc.)? Isso configura `$to-tickets`.
* Convenção de branch e regra de merge na `main` (branch protegida? PR obrigatório? push direto liberado?).
* Existe alguma regra sobre versionamento de credenciais/segredos neste repositório que deva ser deixada explícita em `AGENTS.md` (ex.: "credenciais podem ser versionadas em arquivo local X, nunca remover")?

Investigue via ferramentas (não pergunte) qualquer coisa que já esteja visível no repositório — por exemplo, se já existe um `package.json` com scripts de teste, leia-o em vez de perguntar "qual é o comando de teste?".

### Etapa 2 — Confirmar entendimento compartilhado

Antes de escrever qualquer arquivo, resuma o que foi entendido em um bloco compacto e peça confirmação explícita do usuário. Só prossiga após o "sim".

### Etapa 3 — Gerar os documentos

Reescrever (não apenas anexar) os placeholders:

* `.ai/context/business.md` — seguir a estrutura do bloco de negócio: visão geral, missão, público-alvo/personas, modelo de negócio (se houver), indicadores importantes, princípios de produto. Se o projeto não tiver contexto comercial (ferramenta interna, biblioteca), adaptar a estrutura para "quem usa isso e por quê" em vez de forçar um modelo de negócio.
* `.ai/context/architecture.md` — listar cada módulo/repositório com sua stack e responsabilidade, convenções de nomenclatura, regras de comunicação entre módulos, regra de multi-tenancy se aplicável, e uma seção de "critério de escolha de módulo" quando houver mais de um candidato óbvio para uma mudança.
* `.ai/context/coding-standards.md` — manter a base genérica já existente no arquivo e preencher/expandir apenas a seção final "Convenções Específicas do Projeto" com o que foi coletado.
* `.ai/context/testing-standards.md` — manter a base genérica já existente e preencher/expandir apenas a seção final "Configuração Específica do Projeto", incluindo a configuração ou justificativa dos gates do `$ub-mode`.
* `AGENTS.md` — atualizar a seção "Estrutura do Projeto" (ver marcador `<!-- BOOTSTRAP:PROJECT-STRUCTURE -->`) com a lista real de módulos/repositórios, e a seção "Configuração do Fluxo" (ver marcador `<!-- BOOTSTRAP:FLOW-CONFIG -->`) com as decisões do Bloco 5. Não reescrever o restante de `AGENTS.md` — ele é genérico por design.
* `.ai/context/project-status.md` — marcar `bootstrap: done`, preencher data, nome do projeto e data da última revisão do contexto.

### Etapa 4 — Encerramento

Informar ao usuário que o harness está pronto para uso e qual é a próxima ação recomendada (normalmente: descrever a primeira funcionalidade/tarefa e deixar o `$orchestrator` coordenar o fluxo a partir daí).

---

## Revisão posterior (não é bootstrap do zero)

Quando o bootstrap já está `done` e o usuário quer atualizar o contexto (nova tecnologia adotada, novo módulo, mudança de modelo de negócio), não repita a entrevista inteira: leia os arquivos atuais, pergunte só o que mudou (mesmo mecanismo de rodadas), atualize os arquivos afetados e registre a nova data em "Última revisão do contexto" em `project-status.md`. Se a mudança for arquitetural e irreversível o suficiente, considere sugerir um ADR via `$domain-modeling` em vez de só editar `architecture.md` silenciosamente.

---

## Regra Suprema

Um harness com contexto errado é pior do que um harness vazio: ele passa confiança falsa para todas as skills seguintes. Esta skill só termina quando o usuário confirmou, explicitamente, que o resumo está correto — nunca quando o agente "acha que entendeu".
