# PRD — Integração do ub-mode

## Metadados e escopo

Slug: `integrar-ub-mode`. Data: 2026-10-31. Origem: [Intent](integrar-ub-mode.md). Status: aprovado para implementação.

Manutenção do template explicitamente autorizada com bootstrap pendente. Público: mantenedores e agentes que usam o harness. Uma única integração na main comporta a skill, seus pontos de chamada, documentação e auditoria; tickets separados não são necessários.

## Requisitos funcionais e aceite

| ID | Requisito | Critério de aceite |
|---|---|---|
| RF001 | Adicionar `.agents/skills/ub-mode/SKILL.md` com adaptação local e procedência fixa | Frontmatter válido; origem e SHA registrados; escrita, testes e revisão cobertos; sem copiar integralmente upstream |
| RF002 | Integrar a skill à governança | AGENTS lista e exige `$ub-mode`; orchestrator a aciona antes/durante implementação; implementation-review verifica evidências |
| RF003 | Definir aplicação de testes e gates | Coding/testing standards, bootstrap, generate-tests e validate-delivery distinguem aprovado, falhou, não configurado e não aplicável; gates obrigatórios ausentes/falhos bloqueiam; não configurados têm justificativa e limitação explícitas |
| RF004 | Validar manutenção do template sem mudar seu status | `scripts/governance-audit.sh --template` aceita apenas status válido `pending` ou `done`; modo padrão exige `done`; status em andamento, ausente, inválido ou ambíguo reprova; demais verificações permanecem ativas |
| RF005 | Explicar e comprovar a atualização | README atualizado; plano, testes comportamentais, reviews e Validation Report com evidências; entrega publicada na main |

## Regras de negócio

RN001 — Preservar `.ai/context/project-status.md`, os placeholders de negócio/arquitetura e as seções específicas de stack.

RN002 — Prevalecem AGENTS, Intent/PRD e convenções do projeto. A skill não amplia escopo, permissões ou acesso a credenciais; commits/push seguem `$reintegrar-main`.

RN003 — Crapper, Dryer e Mutator são referências para gates configuráveis, sem instalar ou executar automaticamente. Gates obrigatórios não podem receber aprovação sem execução. Exceções devem estar documentadas e aprovadas na governança do projeto.

## Requisitos não funcionais

- Compatibilidade: skill em Markdown, sem dependência de runtime de aplicação; auditoria continua Bash; testes usam Python 3 padrão.
- Segurança: nenhuma alteração de segredo ou execução de código upstream; nenhuma limpeza automática.
- Performance: apenas análise de arquivos locais; sem serviço ou banco.
- Observabilidade: auditoria informa modo, status e motivo das falhas; resultados são registrados no relatório.
- Multi-tenancy, UI, APIs e migrations: não aplicáveis.

## Fluxos e erros

Após bootstrap real, orchestrator lê a skill, planeja testes/gates, aplica padrões durante implementação, executa os comandos configurados e revisa evidências antes da entrega. Sem ferramenta configurada, registra a limitação; se obrigatória, bloqueia. Documentação sem código executável recebe revisão proporcional, sem teste artificial.

Nesta manutenção autorizada, o modo `--template` valida a estrutura mantendo pendente a configuração de uma aplicação. Não concede autorização para desenvolver uma aplicação sem bootstrap. Argumento desconhecido ou status inválido reprova.

## Fora do escopo

Inicializar aplicação, instalar skills globais, executar ferramentas companheiras, ativar CI, criar lint de texto para provar qualidade semântica, mudar fluxo de produção ou reformatar código alheio.

## Testes e evidências esperadas

Testes com repositórios mínimos temporários: status válidos/inválidos, modo padrão/template, argumentos, skills ausentes da lista, ADR duplicada/fora do índice e sufixos divergentes. Validar skill com `quick_validate.py`, sintaxe Bash com `bash -n`, diff com `git diff --check` e auditoria real com `--template`. Revisar cenários de aplicação das instruções, sem alegar que análise documental executou Crapper/Dryer/Mutator.

## Riscos e rollback

Reverter os commits desta Intent, preservando alterações posteriores. Nenhuma migração ou rollback de produção necessário. Revisão e publicação são condições de aceite; detalhes de execução constarão no Validation Report.
