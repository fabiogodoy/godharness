# Coding Standards

> Este arquivo tem uma base genérica (Clean Code) válida para qualquer stack. A seção "Convenções Específicas do Projeto", no final, é preenchida/expandida pelo `$bootstrap-project` e por ADRs posteriores com as regras concretas da stack escolhida (nomenclatura, camadas, frameworks).

## Objetivo

Definir os padrões obrigatórios de desenvolvimento para este projeto.

O objetivo não é produzir código acadêmico. O objetivo é produzir código:

* Legível
* Seguro
* Testável
* Manutenível
* Consistente
* Compatível com a arquitetura existente

---

## Filosofia

Sempre priorizar, nesta ordem:

1. Clareza
2. Simplicidade
3. Manutenção
4. Segurança
5. Performance

Código é lido muito mais vezes do que é escrito.

---

## Regra Principal

Todo código deve ser compreensível por outro desenvolvedor (ou outro agente) em poucos minutos.

Se precisar de muita explicação, provavelmente o código está complexo demais.

---

## Nomes

Nomes devem explicar intenção.

Ruim: `x`, `data`, `process()`, `handleStuff()`

Bom: `totalActiveUsers`, `calculateInvoiceTotal()`, `notifyCustomer()`

---

## Métodos e Funções

Devem fazer apenas uma coisa. Responsabilidades separadas ficam em funções separadas.

Tamanho preferencial: até ~30 linhas. Acima disso, avaliar extração — mas legibilidade importa mais do que seguir esse número cegamente.

Evitar aninhamento profundo (`if` dentro de `if` dentro de `if`); preferir guard clauses.

---

## Classes e Módulos

Devem ter responsabilidade clara. Sinal de alerta: mais de ~1000 linhas ou dezenas de responsabilidades misturadas.

---

## Comentários

Primeiro melhore o código. Depois adicione comentários quando necessário.

Aceitável comentar: regras de negócio complexas, integrações externas, motivações históricas/decisões não óbvias (considere um ADR em vez disso quando a decisão for importante — ver `$domain-modeling`).

---

## Duplicação

Antes de criar código novo, pesquisar implementações semelhantes já existentes no projeto. Reutilização tem prioridade sobre criação.

---

## Tratamento de Erros

Nunca ignorar exceções silenciosamente (`catch { }` vazio é proibido). Sempre registrar (log) ou propagar de forma explícita.

---

## Logging

Logs devem ajudar suporte e diagnóstico (ver `$observability-review`). Nunca registrar senhas, tokens ou dados sensíveis.

---

## Segurança

Toda entrada externa é não confiável. Sempre validar permissões, identidade do usuário/tenant e dados recebidos no servidor — nunca confiar apenas em validação de frontend.

---

## Multi-Tenancy (quando aplicável)

Se o projeto for multi-tenant, toda consulta/operação deve respeitar o isolamento entre tenants (ex.: `owner_id`, `tenant_id`, `organization_id` — o nome exato é definido no bootstrap). Nenhum dado pode atravessar tenants. Isso deve ser tratado como regra absoluta, não como boa prática.

---

## Migrations de Banco de Dados (quando aplicável)

Toda alteração estrutural de banco deve possuir migration versionada (a ferramenta específica — Liquibase, Flyway, Prisma Migrate, Alembic, etc. — é definida no bootstrap). Nunca alterar schema manualmente em produção. Toda migration deve ter rollback documentado ou ser reversível.

---

## Testes

Toda funcionalidade nova deve possuir testes (ver `.ai/context/testing-standards.md`).

## Aplicação do ub-mode

Usar `$ub-mode` na escrita e alteração de código e verificar seus resultados em `$implementation-review`. A definição operacional está em `.agents/skills/ub-mode/SKILL.md`; este documento continua sendo a base oficial de padrões do projeto.

Planejar testes significativos antes de alterar comportamento; registrar no Test Plan uma alternativa quando não houver teste executável honesto. Os gates, comandos e exceções pertencem a `.ai/context/testing-standards.md`; métricas não substituem requisitos, segurança ou legibilidade. Refatorações permanecem limitadas ao escopo da Intent/PRD.

---

## Refatoração

Ao tocar um código, aplicar a Boy Scout Rule: "deixe o código melhor do que encontrou." Pequenas melhorias são incentivadas; grandes refatorações exigem Intent/ADR próprios.

---

## Performance

Antes de otimizar, medir. Não criar complexidade para resolver problemas hipotéticos.

---

## Dependências

Antes de adicionar uma biblioteca nova, perguntar:

1. O problema já pode ser resolvido com o que existe?
2. O ganho compensa o custo (peso, manutenção, superfície de ataque)?
3. O time/projeto conseguirá manter isso a longo prazo?

---

## Checklist Obrigatório Antes de Finalizar Qualquer Implementação

* [ ] Código compila/roda sem erros
* [ ] Testes passam
* [ ] `$ub-mode` aplicado; evidências e limitações dos gates registradas na review
* [ ] Sem código duplicado desnecessário
* [ ] Sem warnings relevantes
* [ ] Sem logs de debug esquecidos
* [ ] Isolamento multi-tenant validado (quando aplicável)
* [ ] Segurança validada
* [ ] Padrões do projeto (seção abaixo) respeitados

---

## Regra Suprema

Sempre preferir código simples funcionando a código sofisticado difícil de manter. O sistema existe para atender usuários reais, não para demonstrar conhecimento técnico.

---

## Convenções Específicas do Projeto

> Preenchido pelo `$bootstrap-project` na primeira execução e evoluído por ADRs. Enquanto estiver vazio, o bootstrap ainda não rodou ou ainda não coletou esta parte.

*(vazio — aguardando bootstrap)*
