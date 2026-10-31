---
name: ub-mode
description: "Aplica padrões de escrita, alteração e revisão de código, com testes de comportamento e gates de qualidade. Use na implementação e na implementation-review, sob as regras e o escopo do harness."
---

# ub-mode no God Harness

Adaptação local das práticas de engenharia do [ub-mode de unclebob](https://github.com/unclebob/ub-mode), não uma cópia integral. Consulte [procedência e diferenças](references/upstream.md) ao atualizar esta skill.

## Contrato com a governança

Leia `AGENTS.md`, a Intent/PRD/Impact Analysis, `architecture.md`, `coding-standards.md`, `testing-standards.md` em `.ai/context/` e o Test Plan da entrega. O `$orchestrator` aciona esta skill para escrever/alterar código; `$implementation-review` verifica sua aplicação. Ela complementa essas etapas e não substitui requisitos, aprovações ou regras de segurança. Invocação direta também respeita o bootstrap e a ordem mínima antes de codar.

## Durante a implementação

1. Defina o resultado observável da menor fatia do PRD. Reproduza o defeito quando houver. Planeje como conferir cada fatia antes da próxima.
2. Use TDD quando houver comportamento executável: teste relevante falhando pela causa esperada, correção mínima, teste passando e refatoração validada. Se um teste honesto for impraticável, registre motivo e verificação alternativa no Test Plan; não crie teste de texto para simular cobertura de comportamento.
3. Mantenha nomes e dados coerentes com o domínio; consulte `$domain-modeling` quando termos ou decisões precisarem de registro. Evite estados inválidos com os recursos da stack, valide entradas nas fronteiras e preserve autenticação, autorização e isolamento em cada operação protegida.
4. Mantenha lógica de negócio separada de I/O, responsabilidades claras e estado mutável com proprietário definido. Avalie concorrência e idempotência onde houver repetição/retry. Não acrescente abstrações ou ferramentas sem ganho verificável.
5. Corrija causas e remova complexidade ou duplicação no trecho alterado. Após tentativas que repetem a mesma falha, reavalie a premissa antes de outra correção. Redesenhos amplos voltam ao orchestrator para avaliar escopo/ADR. Refatoração preserva comportamento comprovado.

## Gates e revisão

A configuração oficial fica em `.ai/context/testing-standards.md`; não invente comandos nem instale ferramentas para preencher lacunas. O bootstrap define ferramenta compatível ou equivalente, versão, comando, escopo, limiar e obrigatoriedade de cada gate.

Referências upstream: Crapper para CRAP por função (`< 10`), Dryer para similaridade de duplicação (`< 0.8`) e Mutator para avaliar lacunas dos testes e mutantes sobreviventes. São métricas distintas; um teste passando não comprova esses gates. Limiares diferentes, equivalentes e exclusões precisam de justificativa na configuração do projeto.

Registre no Test Plan e na review, para cada gate, um dos estados:

| Estado | Uso e consequência |
|---|---|
| Aprovado | Comando executado, resultado dentro do limiar e evidência anexada |
| Falhou | Execução fora do limiar ou com erro; bloqueia quando obrigatório |
| Não configurado | Falta comando, compatibilidade ou ferramenta; registrar motivo, limitação e próxima ação; bloqueia quando obrigatório |
| Não aplicável | Ausência de alvo pertinente justificada, como documentação sem código executável |

Investigue código não coberto, mutantes sobreviventes/equivalentes e código morto com base no comportamento exigido. Não elimine requisitos ou enfraqueça testes apenas para satisfazer números. Gate obrigatório ausente/falho bloqueia a entrega, salvo exceção expressamente aprovada e registrada na governança do projeto; gate não obrigatório pendente permanece como limitação no Validation Report.

## Evidências e encerramento

Use os artefatos da Intent para registrar decisões, comandos relevantes, resultados e limitações; mantenha no chat o resumo necessário para continuar. Reutilize o mecanismo de delegação apenas quando autorizado no ambiente.

Execute `$implementation-review` com o diff, Test Plan e evidências dos gates. A reintegração, commits e push pertencem a `$reintegrar-main`. A skill não autoriza apagar worktrees, descartar pendências, alterar credenciais, instalar dependências ou refatorar fora da Intent. Remova somente temporários criados pela própria execução e confirmados sem uso.
