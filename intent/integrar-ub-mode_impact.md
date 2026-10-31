# Impact Analysis — integrar-ub-mode

Data: 2026-10-31. Referências: [Intent](integrar-ub-mode.md), [PRD](integrar-ub-mode_prd.md).

## Resumo e sistemas impactados

Complexidade técnica média; negócio e operação baixos. Único repositório: `god_harness`. Branch `codex/integrar-ub-mode`, criada da main limpa após `git fetch --prune origin`; base `3902eca620ffa1cbd6333e50d933ab2c7db88ea8`, contendo `origin/main`. Nenhuma pendência local preexistente.

| Componente | Impacto |
|---|---|
| AGENTS e README | Registro, chamada obrigatória e explicação da adaptação |
| Coding/testing standards | Base genérica de padrões e configuração de gates; placeholders de stack preservados |
| Skill ub-mode | Nova orientação local com fonte e revisão fixadas |
| Orchestrator, bootstrap, generate-tests, implementation-review, validate-delivery | Seleção, configuração, verificação e evidências da skill |
| Auditoria e testes | Status interpretado pela declaração efetiva; modo explícito de template e regressões |
| intent/ | Rastreabilidade desta manutenção |
| Template de Validation Report | Registro explícito de não aplicabilidade fundamentada; sem dispensar gates pertinentes |
| Aplicação, dados, integrações, banco, produção | Sem impacto: o harness ainda não define uma aplicação |

## Riscos e mitigações

| Risco | Probabilidade / impacto | Mitigação |
|---|---|---|
| Regras upstream suplantarem permissões e escopo | Média / alto | Adaptação subordinada ao harness; sem instalação, limpeza ou refatoração fora de escopo |
| Gate indisponível aparecer aprovado | Média / alto | Estado, justificativa, comando, limiar e evidência; gate obrigatório ausente/falho bloqueia |
| Modo de template virar liberação de aplicação | Média / alto | Flag explícita com aviso, modo normal estrito; status inválido/em andamento reprovado em ambos |
| Auditoria confundir enumeração com status | Alta / médio, já observado na leitura | Interpretar apenas linha canônica ou seção bootstrap; rejeitar múltiplas declarações; testes negativos |
| Dependência de licença upstream não declarada | Média / médio | Texto local de integração, sem cópia integral; registrar procedência e ausência de licença identificada |
| Alterar scaffolding de aplicação | Baixa / médio | Preservar status e placeholders, conferir diff |

## Segurança, observabilidade e performance

Sem consulta a dados de usuários, autenticação, tenant, segredo ou banco. A leitura da fonte não executa código remoto. Mensagens da auditoria e relatório são a evidência operacional; nenhuma telemetria nova. Processamento local pequeno, sem requisito de benchmark.

## ADR e decisões

Não há mudança de arquitetura de aplicação ou nova dependência de runtime. A adaptação local é reversível e não atende aos três critérios de ADR de `$domain-modeling`; decisão e limites registrados neste relatório e na procedência da skill. Não criar ADR apenas para adicionar documentação.

## Testes, regressões e rollback

Cobrir todos os riscos de auditoria com subprocessos em fixtures temporárias; revisão de instruções cobre conflitos de escopo e gates. Reexecutar auditoria real e validador de skill. Build de aplicação e E2E não aplicáveis; `bash -n` valida o executável alterado. Reverter os commits da Intent desfaz a entrega sem dados ou serviços a migrar.

## Parecer

Implementar no escopo do PRD. Exceção de bootstrap autorizada somente nesta sessão; não alterar a regra padrão do harness.

## Ajuste identificado na review

A avaliação independente encontrou exigências incondicionais de build/ambiente conflitantes com a orientação de não criar testes artificiais para documentação. Clarificada a aplicabilidade em orchestrator, testing-standards, validate-delivery e seu template. A dispensa se limita a trabalho exclusivamente documental sem impacto executável, exige justificativa e verificação de artefatos e preserva gates obrigatórios pertinentes. O script Bash alterado nesta entrega continua sujeito a execução e testes reais.
