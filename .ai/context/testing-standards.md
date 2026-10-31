# Testing Standards

> Base genérica válida para qualquer stack. A seção "Configuração Específica do Projeto", no final, é preenchida pelo `$bootstrap-project` com as ferramentas, comandos e ambiente reais (framework de teste, comando de build, como subir o ambiente local, banco de testes autorizado, etc.).

## Objetivo

Garantir que toda alteração seja validada antes da entrega. A implementação não é considerada concluída até que os testes definidos neste documento sejam executados com sucesso.

---

## Filosofia

Confiamos em evidências. Não confiamos apenas em: compilação, revisão visual, suposição do desenvolvedor ou suposição do agente.

Toda funcionalidade deve ser validada através de testes reais, executados.

---

## Pirâmide de Testes

Ordem de prioridade:

1. Testes unitários
2. Testes de integração
3. Testes end-to-end (E2E)

---

## Regra Obrigatória

Toda funcionalidade nova deve possuir pelo menos: testes unitários das regras que introduziu e validação funcional do fluxo principal.

---

## Tipos de Teste

### Testes Unitários

Validam regras isoladas. Obrigatório para: regras de negócio, funções puras, utilitários.

### Testes de Integração

Validam integração entre componentes (ex.: camada de serviço + persistência, endpoint + regra de negócio).

Se o projeto acessar banco de dados em testes de integração, o banco autorizado e as regras de proteção contra ambientes de produção/homologação são definidos na seção "Configuração Específica do Projeto" abaixo — e são absolutas: nenhum teste pode rodar contra um banco fora do configurado ali.

### Testes End-to-End (E2E)

Validam o comportamento real do usuário, do início ao fim. A ferramenta oficial (Playwright, Cypress, etc.) é definida no bootstrap.

---

## Processo Obrigatório Antes de Executar E2E

1. Executar o build do projeto afetado (comando definido na seção específica abaixo).
2. Se o build falhar: **interromper a execução**. Não seguir para E2E com build quebrado.
3. Subir o ambiente local necessário (comando/procedimento definidos na seção específica abaixo).
4. Validar que a aplicação está disponível e sem erros críticos nos logs.
5. Após a conclusão, encerrar o ambiente, se aplicável.

---

## Regra para Agentes

O agente não pode afirmar que algo funciona sem executar os testes correspondentes.

Expressões proibidas: "deve funcionar", "provavelmente funciona", "parece correto".

Expressões aceitáveis: "validado via teste", "validado via execução E2E", "testes executados com sucesso" — sempre com a evidência anexada (log, saída do comando, screenshot).

---

## Cenários Obrigatórios

Toda funcionalidade nova ou alterada deve possuir, no mínimo:

* **Cenário feliz** — o fluxo esperado.
* **Cenário de erro** — entrada ou estado inválido.
* **Cenário de regressão** — garantir que funcionalidades existentes relacionadas continuam funcionando.

---

## Evidências

Toda execução de teste relevante (especialmente E2E) deve produzir evidências: saída de comando, screenshots, vídeos ou logs, conforme o que a stack do projeto permitir.

## Testes de Comportamento e Gates do ub-mode

O Test Plan deve antecipar o comportamento verificável e, quando aplicável, o ciclo de teste falhando pela causa esperada antes da correção e passando depois dela. Refatorações exigem regressão proporcional ao trecho afetado. Documentação sem comportamento executável recebe revisão e verificação adequada ao artefato, sem testes artificiais.

Seguir `.agents/skills/ub-mode/SKILL.md` para os estados dos gates. Cada projeto deve preencher na seção específica abaixo: ferramenta ou equivalente, versão, linguagem/escopo suportado, comando reproduzível, limiar, obrigatoriedade, exclusões justificadas e local da evidência para complexidade/cobertura (CRAP), duplicação e testes de mutação. Os limiares de referência upstream são CRAP por função `< 10` e similaridade de duplicação `< 0.8`; alterações precisam de justificativa. A configuração de mutação deve definir o critério de aprovação e como analisar sobreviventes/equivalentes.

Enquanto não configurado, registrar esse estado, motivo, limitação e próxima ação no Test Plan/Validation Report. Nunca converter indisponibilidade em aprovação. Gate obrigatório ausente ou falhando bloqueia a entrega, salvo exceção expressamente aprovada e registrada; não aplicabilidade precisa de justificativa. O harness genérico não fornece comandos fictícios nem instala Crapper, Dryer ou Mutator.

---

## Processo de Entrega

Nenhuma entrega é considerada concluída sem:

* Build executado quando houver alvo executável ou impacto em seu comportamento/configuração
* Testes unitários executados quando aplicáveis ao comportamento alterado
* Testes E2E executados quando aplicável
* Para alterações exclusivamente documentais sem impacto executável: não aplicabilidades justificadas no Test Plan/Validation Report e verificações dos artefatos executadas; gates obrigatórios pertinentes permanecem exigidos
* Evidências geradas
* Validation Report aprovado (`$validate-delivery`)

---

## Regra Suprema

Código sem teste é hipótese. Código validado por testes é evidência. Somente evidências podem ser utilizadas para aprovar uma entrega.

---

## Configuração Específica do Projeto

> Preenchido pelo `$bootstrap-project` na primeira execução. Deve conter, no mínimo:
>
> * Framework(s) de teste unitário/integração usados
> * Framework de E2E (se houver) e como rodá-lo
> * Comando de build (ex.: `npm run build`, `./gradlew build`, `cargo build`)
> * Como subir o ambiente local para testes manuais/E2E
> * Banco de dados autorizado para testes de integração, se aplicável, e a regra de que nenhum teste pode rodar contra produção/homologação/qualquer outro banco
> * Cobertura mínima esperada, se o time definir uma
> * Gates do `$ub-mode`: ferramenta/versão, compatibilidade/escopo, comando, limiar, obrigatoriedade, exclusões e evidências; ou justificativa explícita de não configuração/não aplicabilidade

*(vazio — aguardando bootstrap)*
