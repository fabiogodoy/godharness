# Intent — Padrões de escrita de código com ub-mode

## Metadados

- Slug: `integrar-ub-mode`
- Data: 2026-10-31
- Origem: solicitação do mantenedor para incorporar `https://github.com/unclebob/ub-mode` à governança e explicar a atualização após testes.
- Status: aprovada para implementação no escopo confirmado nesta conversa.

## Problema e contexto

O harness já declara Clean Code, mas não conecta o ub-mode à implementação nem exige que seus resultados sejam examinados nas revisões. Apenas copiar uma skill deixa seu uso dependente de lembrança manual. Mantenedores e agentes precisam de orientação integrada, rastreável e compatível com qualquer stack.

O repositório é o template genérico; negócio e arquitetura de uma aplicação ainda não foram definidos. O usuário confirmou expressamente a manutenção do harness com `bootstrap: pending`, como exceção à trava desta sessão. Essa autorização não inicializa uma aplicação nem altera a regra padrão para futuros usuários.

## Objetivo e resultado esperado

Tornar os padrões de escrita de código aplicáveis durante a execução e verificáveis na entrega, sem inventar stack, instalar ferramentas externas ou produzir evidência de qualidade fictícia.

## Processo atual e dores

O orchestrator direciona a implementação aos padrões genéricos. Não há skill local ub-mode, configuração dos seus gates ou orientação sobre indisponibilidade das ferramentas. A auditoria atual procura `pending` em todo o documento de status, inclusive na enumeração dos valores possíveis, causando falso bloqueio mesmo com bootstrap concluído.

## Benefícios e indicadores

- Agentes: ponto explícito de entrada para aplicar os padrões.
- Mantenedores: evidências, limitações e procedência disponíveis na revisão.
- Indicadores: integração presente em todas as etapas afetadas; testes positivos e negativos da auditoria aprovados; bootstrap e placeholders preservados.

## Restrições, riscos e regras conhecidas

- RN001: preservar o harness genérico e o status pendente.
- RN002: a skill complementa a hierarquia e as permissões existentes; não autoriza limpeza, refatoração ampla ou instalação.
- RN003: ferramenta não executada não equivale a gate aprovado.
- Riscos: regras conflitantes, ferramentas incompatíveis com stack futura e falsa aprovação da auditoria. Mitigação: adaptação local, gates configurados por projeto, testes de falha e modo de template explícito.
- Dados, banco, APIs, multi-tenancy e produção: não aplicáveis a esta manutenção.

## Critérios de sucesso

- CS001: skill local discoverable e referenciada em AGENTS, execução, testes e reviews.
- CS002: auditoria do template aprovada, sem flexibilizar a auditoria normal de aplicação.
- CS003: documentação explica uso, origem, adaptações e ferramentas não executadas.
- CS004: entrega testada, revisada, reintegrada e publicada em `origin/main`.

## Alternativas e critérios para não implementar

Somente documentar um link não garante aplicação. Copiar upstream sem adaptação conflita com o template sem stack. Não implementar se a solução exigir concluir artificialmente o bootstrap ou executar ferramentas sem configuração.

## Perguntas em aberto

Nenhuma no escopo confirmado. As escolhas de ferramentas de cada aplicação pertencem ao bootstrap futuro.
