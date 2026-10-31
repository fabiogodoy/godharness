# Procedência do ub-mode e manutenção local

- Origem: [unclebob/ub-mode](https://github.com/unclebob/ub-mode).
- Revisão consultada em 2026-10-31: `57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f` (`master`).
- Fontes fixas: [SKILL.md](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/SKILL.md) e [README.md](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/README.md).
- Nessa revisão, a árvore contém apenas esses dois arquivos; não foi identificada declaração de licença. O conteúdo local é uma adaptação própria de práticas de engenharia, sem distribuição de cópia integral ou atribuição de licença MIT ao texto upstream.

## Integração com o harness

| Tema de upstream | Tratamento local |
|---|---|
| Implementação, correção e refatoração | Ciclo de trabalho dentro do PRD, com verificação por fatia e limites de escopo |
| TDD e testes de comportamento | Test Plan com evidências de falha/sucesso quando aplicável; alternativa justificada para trabalho sem comportamento executável |
| Domínio e arquitetura | Padrões oficiais do projeto e `$domain-modeling`; segurança e isolamento continuam obrigatórios |
| Ferramentas de qualidade | Crapper, Dryer e Mutator são referências; comandos dependem da stack e configuração do projeto; equivalentes e exceções são explícitos |
| Registro e contexto | Artefatos existentes de Intent e evidências, sem novo log obrigatório fora da entrega |
| Limpeza, commit e push | Preservação de pendências e permissões; entrega pelo `$reintegrar-main` |

O `uml-viewer` aparece como ferramenta companheira no README upstream; não é requisito nem dependência desta integração. Não foram instaladas ferramentas companheiras ou alteradas skills globais.

## Atualizações futuras

Compare a revisão fixa com a nova fonte antes de mudar a adaptação. Registre novo SHA, diferenças e impacto na governança; valide compatibilidade com AGENTS e padrões, frontmatter da skill, testes da auditoria e cenários da review. Atualizações não são automáticas e não executam scripts de upstream.
