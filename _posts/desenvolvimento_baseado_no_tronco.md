---
marp: true
---

# Desenvolvimento Baseado no Tronco: <br/>Céu, Terra e Purgatório

---
# Branch Develop (Terra)

![h 500](/images/develop.png)

---
# Branch Develop (Terra)

- Branch principal cujo Head sempre reflete um estado com as últimas mudanças de desenvolvimento para a próxima versão
- O desenvolvimento se dá por Feature Branching
  - Todo trabalho para uma feature é colocada numa Feature Branch (Subterrânea)
  - É integrada ao branch Develop quando a Feature estiver **completa**

---
# Branch Master ou Tronco (Céu)

- Branch principal cujo Head sempre pode ser colocado diretamente em produção
- É o Branch dos códigos perfeitos

---

# Padrões para Saúde do Tronco

- Padrão de codificação, como um dos [padrões de codificação do Google](https://google.github.io/styleguide/)
  - Padrão PEP 8
  - Docstrings
  - Anotações de tipos
- Código de auto-teste
- Revisão pré-integração

---
# Pontos Principais do Padrão [PEP 8](https://peps.python.org/pep-0008/)

- Leiaute do código
  - Indentação
  - Comprimento de linha máximo
  - Linhas em branco
  - Importações
- Convenções de nomenclatura

---
# Docstrings

- [Docstrings padrão Google](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings)
  - Podem ser extraídas automaticamente e são usadas por Sphinx <br/>(rodar Sphinx para [ver como ficam](https://spark-tests.readthedocs.io/en/latest/))
- Modules
- Classes
- Funções e métodos <br/>exceto as que atendam cumulativamente:
    - não visível externamente
    - muito curta
    - óbvia

---
# Anotações de Tipos

- Pelo menos anotar as APIs públicas
- Usar julgamento para chegar a um bom equilíbrio entre segurança e clareza por um lado, e flexibilidade por outro
- Anotar código que é propenso a erros relacionados ao tipo 
- Anotar códigos difíceis de entender
- Anotar código a medida que se torna estável do ponto de vista dos tipos

---
# Código de Auto-teste

- A medida que escrevemos o código de produção, também escrevemos um conjunto abrangente de testes automatizados
- São executados em cada Commit
- Para garantir que não tenha defeitos no Tronco
- É normal o código de testes ser maior do que o código de produção

---
# Revisão Pré-integração

- Cada Commit para o tronco é revisado por pares antes que o Commit seja aceito
- Encaixa-se particularmente bem com o mecanismo de Pull Requests
- A prática se espalhou amplamente nas maiores empresas de tecnologia
- É importante desenvolver a disciplina para Revisões Pré-integração no prazo
  - Mesmo quando bem feito, as Revisões Pré-integração sempre introduzem alguma latência no processo de integração
  - Quando usado com Integração Contínua, o prazo para Revisão Pré-integração não pode exceder a **um dia**

---
# Git-flow
![](/images/gitflow.png)

---
# Branch Release (Purgatório)

- Um Branch Release típico copiará do Branch Develop atual, mas não permitirá a adição de novos features
- Os desenvolvedores trabalhando no Branch de Release se concentram apenas em **retrabalhar** o código para remover as imperfeições que impeçam o Merge ao Tronco
- Quaisquer correções a estas imperfeições são criadas no Branch de Release e mergeadas ao Branch Develop
- Quando não houver mais imperfeições a serem retrabalhadas, o Branch estará pronto para o Merge ao Tronco

---
# Fogo do Purgatório

- Os desenvolvedores que fazem o retrabalho na maioria das vezes não são os mesmos que desenvolveram o código
- Algumas vezes o retrabalho é maior do que o trabalho feito no desenvolvimento do código original
- Fica cada vez mais difícil fazer merge de volta ao Branch Develop com o passar do tempo

---
# Desenvolvimento Baseado no Tronco
![](/images/trunk1c.png)

---
# Desenvolvimento Baseado no Tronco
- Desenvolvedores fazem a integração diretamente no Tronco
- O código cometido têm que estar saldáveis
- Branches de Feature de vida curta: 2 dias máximo
- Normas em organizações de alto desempenho, o como o [Google](../assets/why_google_store_billions_of_locs_in_a_single_repository.pdf)
- Implícita pela [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration)
- [Evidência Científica](../assets/2016-State-of-DevOps-Report.pdf) de que contribui para um maior desempenho de entrega de Software

---
# Branches de Release no Desenvolvimento Baseado no Tronco

- Não são para correções
  - As correções são aplicadas diretamente ao Tronco
  - As correções para as features incluídas na Release são copiadas (cherry-picked) do Tronco
- Servem para fixar um conjunto de features para próxima release
- São apagadas algum tempo depois da release

---
# Estratégias de Migração

- Se o time usa feature branching de longa duração, o desenvolvimento baseado no tronco pode ser uma barreira para a melhoria
- A chave para sair da armadilha é aumentar a frequência de integração, enquanto mantém com uso de Branches de Release
  - A integração dos Branches de Release com Tronco não precisa esperar que a Release esteja completa
  - O desenvolvimento dos Branches de Release pode seguir um estilo de desenvolvimento baseado no Tronco