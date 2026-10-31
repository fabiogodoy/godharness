# AGENTS.md

## Regra Zero — Leitura Obrigatória

Antes de qualquer análise, proposta, edição, execução de teste, geração de documento ou implementação neste repositório, o agente deve ler e respeitar este `AGENTS.md`.

Esta leitura não é opcional e não pode ser substituída por memória de conversas anteriores.

### Verificação de Bootstrap (obrigatória, antes de tudo)

Ler `.ai/context/project-status.md`.

* Se `bootstrap: pending` ou `bootstrap: in_progress` → **a única ação permitida é executar `$bootstrap-project`**. Nenhuma Intent, PRD, análise ou implementação pode começar. Este repositório ainda é um harness vazio: ele não sabe qual é o projeto, a arquitetura ou a stack.
* Se `bootstrap: done` → prosseguir normalmente com este documento.

Depois de confirmar que o bootstrap está concluído, consultar também, conforme a natureza da tarefa:

* `.ai/context/business.md`
* `.ai/context/architecture.md`
* `.ai/context/coding-standards.md`
* `.ai/context/testing-standards.md`
* A skill aplicável em `.agents/skills/<skill>/SKILL.md`

Se houver conflito entre código existente e os documentos oficiais, a ordem de verdade é:

```text
AGENTS.md
  ↓
Intent
  ↓
PRD
  ↓
ADR
  ↓
Código
```

O código existente nunca justifica violar uma regra arquitetural documentada.

---

## Missão

Este repositório é um **harness genérico** de desenvolvimento assistido por IA: um processo seguro e rastreável (Intent → PRD → Impact Analysis → Reviews → Implementação → Testes → Validação) que se aplica a qualquer projeto de software, mais um conjunto de skills que o agente aciona em cada etapa.

Na primeira execução ele não conhece nada sobre a aplicação — isso é resolvido pela skill `$bootstrap-project`, que entrevista o usuário e preenche `.ai/context/*.md` com o contexto real do projeto.

<!-- BOOTSTRAP:PROJECT-STRUCTURE -->
### Estrutura do Projeto

*(preenchido pelo `$bootstrap-project` com a lista real de módulos/repositórios e o papel de cada um — ver `.ai/context/architecture.md` para o detalhamento completo)*
<!-- /BOOTSTRAP:PROJECT-STRUCTURE -->

---

## Estrutura de Governança

```text
.agents/
└── skills/
    ├── bootstrap-project/
    ├── orchestrator/
    ├── ub-mode/
    ├── grill-me/
    ├── grilling/
    ├── domain-modeling/
    ├── to-tickets/
    ├── resolving-merge-conflicts/
    ├── create-intent/
    ├── create-prd/
    ├── impact-analysis/
    ├── architecture-review/
    ├── business-review/
    ├── security-review/
    ├── observability-review/
    ├── generate-tests/
    ├── implementation-review/
    ├── validate-delivery/
    └── reintegrar-main/

.ai/
├── templates/
│   ├── intent_template.md
│   ├── prd_template.md
│   ├── impact_analysis_template.md
│   ├── test_plan_template.md
│   ├── validation_report_template.md
│   └── adr_template.md
│
└── context/
    ├── project-status.md
    ├── business.md
    ├── architecture.md
    ├── coding-standards.md
    └── testing-standards.md

intent/
└── <slug>.md, <slug>_prd.md, <slug>_impact.md, <slug>_test_plan.md, <slug>_*-review.md, <slug>_validation_report.md

docs/
└── adr/
    ├── README.md
    └── ADR-XXXX-<slug>.md
```

---

## Fluxo Obrigatório

Toda solicitação de desenvolvimento segue obrigatoriamente (coordenado por `$orchestrator`):

```text
IDEIA
  ↓
ENTENDIMENTO ($grilling / $grill-me)
  ↓
INTENT ($create-intent)
  ↓
PRD ($create-prd)
  ↓
IMPACT ANALYSIS ($impact-analysis)
  ↓
ARCHITECTURE REVIEW ($architecture-review)
  ↓
BUSINESS REVIEW ($business-review)
  ↓
TICKETS, quando a entrega exigir mais de uma integração segura na main ($to-tickets)
  ↓
IMPLEMENTAÇÃO ($ub-mode)
  ↓
TESTES ($generate-tests)
  ↓
IMPLEMENTATION REVIEW ($implementation-review)
  ↓
SECURITY REVIEW ($security-review)
  ↓
OBSERVABILITY REVIEW ($observability-review)
  ↓
REINTEGRAÇÃO NA MAIN ($reintegrar-main)
  ↓
VALIDAÇÃO PRD × ENTREGA ($validate-delivery)
  ↓
ENTREGA
```

Para bugs pequenos e correções operacionais de baixo risco, `$orchestrator` define uma Matriz de Decisão com um caminho simplificado — o rigor é proporcional ao risco, não burocracia por burocracia.

---

## Estratégia Obrigatória de Execução

### Isolamento de Contexto

Toda solicitação que gere Intent deve ser tratada como uma frente isolada.

* Não misturar duas Intents na mesma entrega.
* Não reaproveitar PRD de outra demanda para justificar implementação atual.
* Não alterar arquivos fora do escopo da Intent/PRD, salvo correção indispensável documentada no Impact Analysis.
* Se a ferramenta permitir criar/usar thread ou sessão separada, cada Intent deve rodar na sua própria.
* Se não permitir, manter o slug da Intent como fronteira rígida de contexto e registrar qualquer desvio no Validation Report.

### Entendimento Obrigatório

Antes de criar uma Intent, toda solicitação passa por uma entrevista de entendimento (`$grilling`, ou `$grill-me` para pedidos não técnicos). Fatos verificáveis no repositório/ferramentas devem ser investigados pelo agente; o usuário só decide o que depende de preferência, prioridade, negócio ou design. Não criar Intent, PRD, Impact Analysis, ADR ou implementação enquanto houver decisão aberta ou sem confirmação de entendimento compartilhado.

Sempre que a conversa tocar em vocabulário de domínio (termos ambíguos, glossário do projeto, `CONTEXT.md`) ou em uma decisão candidata a ADR leve, usar `$domain-modeling` para manter o glossário e as decisões registradas no momento em que se cristalizam — em paralelo às demais etapas, não como substituto delas.

### Tickets para Entregas Grandes

Após PRD, Impact Analysis e Architecture Review, executar `$to-tickets` quando a mudança exigir mais de uma integração segura na `main`. Cada ticket deve ser uma fatia vertical verificável, com bloqueios explícitos e escopo próprio.

### Paralelização Obrigatória de Análise

Quando houver mais de uma fonte independente para ler ou inspecionar, paralelizar a coleta de contexto sempre que a ferramenta permitir (ex.: ler `AGENTS.md`, a skill aplicável e `.ai/context/*` em paralelo; buscar referências em múltiplos módulos em paralelo). É proibido fazer longas explorações sequenciais quando houver ferramenta de paralelização disponível.

### Ordem Mínima Antes de Codar

Antes de qualquer edição de código, o agente deve ter: lido este `AGENTS.md`, identificado o módulo/projeto correto, criado/atualizado Intent, PRD e Impact Analysis, criado ADR quando houver mudança arquitetural, executado Architecture Review. Se qualquer item obrigatório não existir, a implementação deve ser bloqueada.

### Sincronização Obrigatória Antes de Implementar

Antes de iniciar código, migration, teste ou alteração de configuração em qualquer repositório/módulo envolvido:

1. identificar todos os repositórios Git e módulos envolvidos;
2. executar `git fetch --prune origin` em cada um;
3. verificar se a branch de trabalho contém a `origin/main` atual; se não, integrá-la antes da implementação;
4. registrar qualquer mudança local preexistente e preservá-la, sem usar comandos destrutivos;
5. bloquear a implementação se a sincronização não puder ser concluída com segurança.

A sincronização inicial não substitui a reintegração final (`$reintegrar-main`). Pendências externas à Intent atual não bloqueiam a entrega, mas devem ser preservadas, excluídas do commit e listadas na Validation Report.

---

<!-- BOOTSTRAP:FLOW-CONFIG -->
## Configuração do Fluxo

*(preenchido pelo `$bootstrap-project`: modo padrão — fluxo completo vs. simplificado por tipo de mudança —, rastreador de tickets configurado para `$to-tickets` (arquivos locais ou tracker real), convenção de branch/merge na main, e qualquer regra específica sobre versionamento de credenciais.)*
<!-- /BOOTSTRAP:FLOW-CONFIG -->

---

## Regra de Alteração de Credenciais

Credenciais existentes são configuração operacional do projeto. O agente nunca pode removê-las, substituí-las, rotacioná-las, mascará-las ou movê-las por conta própria.

É proibido remover qualquer chave, token, senha, certificado, placeholder de configuração ou linha de credencial de qualquer arquivo sob a suposição de que o valor estará disponível no ambiente, em secret manager, em variável de ambiente ou em outro arquivo. A ausência de valor no ambiente nunca autoriza alterar, limpar ou excluir a configuração existente.

Ao identificar um risco de exposição, o agente deve reportar o risco sem imprimir o valor e preservar o conteúdo existente.

---

## Testes Obrigatórios

Ver `.ai/context/testing-standards.md` para a configuração específica deste projeto (frameworks, comando de build, ambiente local, banco de testes autorizado).

Regra para agentes: não afirmar que algo funciona sem executar o teste correspondente. Proibido: "deve funcionar", "provavelmente funciona", "parece correto". Aceitável: "validado via teste", "testes executados com sucesso" — sempre com a evidência anexada.

---

## Multi-Tenancy (quando aplicável)

Se `.ai/context/architecture.md` indicar que este projeto é multi-tenant, toda consulta e operação deve respeitar o identificador de isolamento definido lá. Nenhum dado pode atravessar tenants. Toda implementação deve ser revisada sob a ótica de isolamento (`$security-review`).

---

## Banco de Dados

Toda alteração estrutural deve possuir migration versionada (ferramenta definida em `.ai/context/coding-standards.md`). Nunca alterar schema manualmente em produção. Toda migration deve possuir rollback documentado ou ser reversível.

---

## Revisão de Implementação

Toda entrega passa pelas skills `$implementation-review`, `$security-review` e `$observability-review`, validando respectivamente: qualidade técnica/aderência arquitetural; segurança e isolamento; e capacidade de diagnóstico em produção.

### Padrões de Escrita de Código

Acionar `$ub-mode` antes e durante a escrita ou alteração de código, seguindo `.ai/context/coding-standards.md` e `.ai/context/testing-standards.md`. A skill orienta implementação, testes de comportamento e refatoração dentro da Intent/PRD. Ela complementa a governança; não substitui o bootstrap, as reviews ou a hierarquia de documentos.

`$implementation-review` verifica a aplicação desses padrões e as evidências dos gates configurados. Gate obrigatório não executado ou falhando bloqueia a entrega, salvo exceção expressamente aprovada e registrada. Ferramentas não configuradas ou não aplicáveis devem ter justificativa e limitações registradas; nunca são declaradas aprovadas sem execução.

---

## Validação Final

Toda entrega gera `intent/<slug>_validation_report.md`, usando `.ai/templates/validation_report_template.md`, via `$validate-delivery`. A validação confronta PRD × Código Implementado, item por item.

---

## Auditoria de Governança

O repositório possui um script de checagem automática das regras estruturais deste documento:

```bash
scripts/governance-audit.sh
```

Para manutenção do template genérico expressamente autorizada pelo solicitante, mantendo `bootstrap: pending`, usar `scripts/governance-audit.sh --template` e registrar a autorização no Validation Report. Esse modo valida a estrutura do harness; não libera desenvolvimento de aplicação antes do bootstrap. O modo padrão continua exigindo `bootstrap: done`.

Ele valida: números de ADR duplicados em `docs/adr/`, ADRs ausentes do índice `docs/adr/README.md`, sufixos de arquivo divergentes em `intent/`, e skills existentes em `.agents/skills/` que não estão listadas neste `AGENTS.md`.

O agente deve executar esse script como parte da skill `$validate-delivery` sempre que a entrega tiver criado ou renomeado Intent, PRD, ADR ou skill. Falha no script bloqueia a aprovação da Validation Report até a correção.

---

## Regra Suprema

A verdade do sistema é: Intent → PRD → Código. O código nunca prevalece sobre o PRD.

Toda Intent deve rodar em thread/sessão separada, quando a ferramenta permitir, para evitar perda de contexto.

---

## Critério de Conclusão

Nenhuma entrega é considerada concluída sem:

* Intent criada
* PRD criado
* Impact Analysis criado
* Código implementado
* Testes implementados e executados
* Reviews aprovadas (implementação, segurança, observabilidade)
* Validation Report aprovado
* Quando uma branch tiver sido criada para a entrega, seu conteúdo final mesclado na `main` antes da conclusão
* A `main` resultante enviada ao repositório remoto com `git push origin main`

Após a conclusão de qualquer entrega, o agente sempre realiza o push das alterações para o branch remoto correspondente, salvo pedido explícito em contrário.

### Reintegração Obrigatória de Código

Ao final de qualquer trabalho que tenha alterado código ou artefato de governança, o agente deve garantir, antes de considerar a entrega concluída (ver `$reintegrar-main`):

1. buscar a `origin/main` atual;
2. integrar a `origin/main` na branch de entrega e resolver eventuais conflitos (`$resolving-merge-conflicts`);
3. executar novamente as validações proporcionais quando a integração alterar arquivos da entrega;
4. commitar e enviar a branch de entrega ao remoto;
5. trocar para a `main`, mesclar a branch de entrega (fast-forward quando possível) e resolver conflitos, se houver;
6. executar novamente as validações proporcionais se o merge introduzir resolução de conflitos;
7. enviar a `main` resultante para `origin/main` com `git push origin main`;
8. registrar no Validation Report a branch de origem, o SHA final da `main`, o tipo de merge e a evidência do push.

Alterações externas à entrega atual não impedem essa reintegração. Elas ficam fora do staging/commit e são listadas na Validation Report como pendências.

Esta regra só pode ser dispensada quando o solicitante pedir expressamente para não reintegrar, não commitar ou não fazer push.

O agente sempre lista quais arquivos/classes foram alterados, para conferência visual do solicitante e para facilitar rollback.
