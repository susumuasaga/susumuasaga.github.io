# Workflows de Git Sem Embaraços: Prevenindo a Dificuldade de Conflitos de Merge

Edson Susumu Asaga<br/>
Alex Nascimento<br/>
Gabriel Costa<br/>
Wilson Barros

* TOC
{:toc}

## Resumo

## Introdução

O branching é considerado o feature matador do Git, permitindo que milhares de desenvolvedores trabalhem em paralelo sobre uma mesma base de código. No entanto, apesar do Git facilitar muito, o processo básico continua sendo o mesmo: cada desenvolvedor trabalha em uma cópia privada da base de código. Agora os desenvolvedores podem facilmente trabalhar em seus próprios features, mas surge um problema: como juntar as cópias novamente ao final do trabalho? 

Os desafios com esse processo são os **conflitos de merge**. Estudos mostram que os conflitos de merge são prevalentes: cerca de 20% de todos os merges acabam em um conflito de merge.

| ![](../images/split-and-merge.png) |
| :--------------------------------: |
|       **Branching e merge**        |

Os conflitos de merge podem ser classificados em três tipos conforme a forma de sua detecção, por ordem crescente de dificuldade:

1. O **conflito textual** ocorre quando os desenvolvedores modificam os mesmos arquivos de código em paralelo. Este é o tipo de conflito que é detectado automaticamente pelo Git, mas requer intervenção humana para sua resolução;

2. O **conflito semântico estático**  ocorre quando as falhas aparecem na análise do programa estática, por exemplo na compilação. Isso acontece, por exemplo, quando há um conflito associado ao nome de uma função;

3. O **conflito semântico dinâmico** é o mais insidioso e dificultoso, ocorre quando as falhas aparecem somente em tempo execução. Este tipo de conflito é detectado por um teste que reproduza as condições da falha.

Os conflitos de merge têm impacto na qualidade do código, são perturbadores para o fluxo de trabalho de desenvolvimento. Para resolver um conflito de merge, um desenvolvedor tem que parar o que está fazendo e focar na resolução. Resolver um conflito requer que o desenvolvedor entenda as mudanças conflitantes, crie uma solução de consenso que satisfaça ambos os conjuntos de requisitos que impulsionaram as mudanças. Não há como criar um algoritmo para resolver conflitos automaticamente. Muitos times gastam uma quantidade excessiva de tempo lidando com seu emaranhado de branches.

Esses fatores podem levar os desenvolvedores a adiar a resolução do conflito ou “empurrar o problema com a barriga”, especialmente no caso do conflito semântico dinâmico. De fato, um [estudo de Nelson et al.](../assets/Nelson2019_Article_TheLife-cycleOfMergeConflicts.pdf) descobriu que 56.0% dos desenvolvedores adiaram pelo menos uma vez resolver um conflito de merge. No entanto, quanto mais tarde um conflito for resolvido, mais difícil é recordar a lógica das mudanças, o que [torna o processo de resolução muito mais difícil](https://martinfowler.com/articles/continuousIntegration.html). Como apropriadamente colocado por um participante do estudo de Nelson et al.:

> Adiar um conflito de merge é simplesmente empurrar o problema com a barriga (para um precipício). Geralmente, a resolução do conflito só fica mais difícil com o passar do tempo

[Estudo de Brindescu et al.](../assets/paper15.pdf) descobriu os principais fatores que influenciam a dificuldade dos conflitos de merge:

* **Complexidade** das linhas de código em conflito: quando mais complexo maior a dificuldade dos conflitos de merge;
* **Modularidade**: se um sistema tem bons módulos, então na maioria das vezes os desenvolvedores estarão trabalhando em partes bem separadas da base de código, suas mudanças não causarão conflitos;
* **Tamanho dos branches** paralelos (número de linhas de código modificadas ou adicionadas): via de regra, quando dobramos o tamanho dos branches, o valor esperado e a incerteza da dificuldade dos conflitos de merge (pessoa-horas) quadruplica.

Neste artigo expomos diversos workflows que suportam o desenvolvimento em paralelo propiciado pelo  Git, mas buscando minimizar a dificuldade dos conflitos de merge.

## Git-flow

### Branch Principal ou Tronco

### Feature Branching

### Branches de Release

### Branches de Hotfix

### Branch de Produção

### Quando Usar o Git-flow

## OneFlow

### Características

### Quando Usar o OneFlow

## GitHub Flow

O fluxo de GitHub é um fluxo de trabalho leve e baseado no branch criado por [Scott Chacon em 2011](http://scottchacon.com/2011/08/31/github-flow.html). Scott no eu artigo explica que um dos aspecto visado na criação do GitHub flow é a implantação diaria, ou mesmo várias vezes ao dia, isto é, a branch principal o repositorio de produção sofre atualizações constantemente.

Hoje o GitHub chama sua branch principal de main (antigamente master), possui uma única versão em produção, a branch principal pronto para release, branches de releases não são necessários, problemas de produção são corrigidos da mesma maneira que features regulares, assim não há necessidade de branches de hotfix, feature branching de duração limitada, revisão pré-integração usando Pull-Request.

A branch principal por sofrer atualições em um curto prazo Scott vê vantagem no aspecto de minimizar a introduções de grandes bugs e também em contra pronto na introduções de pequenos bugs na branch principal é possível rapidamente corrigir e reimplantar, como já listado acima, a branch principal está sempre pronta para release.

O GitHub Flow possui uma proposta menos burocratica e agil, comumente se comporta muito bem uma metologia agil, porém para o GitHub Flow atender sprints de até 2 semanas, 1 semanas ou implantações diárias é necessário uma equipe com uma certa maturidade, tendo e respeitando boas práticas de desenvolvimento, padrões desenvolvimento de sofwtare e não menos importante desenvolvimento de testes (unitários, integrados e automatizado), utilizar o TDD (Test Driven Development) como padrão de desenvolvimento de software é uma boa. 

### Branch Principal Pronto para Release

- Manter o  **branch master** suficientemente **saudável** para que o head do `master` possa sempre ser colocado diretamente em produção

- Para manter o branch saldável é essencial escrever 

  código de autoteste:    

  - **Conjunto abrangente de testes automatizados**, para que possamos ter confiança de que, se esses testes passarem, o código de produção **não conterá bugs**.
  - **Executados rapidamente**, geralmente **não mais do que dez minutos**
  - **Toma mais tempo do que** o desenvolvimento do **código de produção**

- Precisamos manter 

  qualidade interna do código

   alta usando práticas como:    

  - Análise de programa estática
  - **Revisão pré-integração**

- Se o time usa feature branching de longa duração (> 2 semanas):    

  - O branch principal pronto para o release pode ser uma barreira para sua melhoria

- Vantagens:    

  - Juntamente com a **integração contínua** como parte do **delivery contínuo**, [um branch principal pronto para release é uma característica de times de elite](https://susumuasaga.github.io/assets/2016-State-of-DevOps-Report.pdf)
  - Simplicidade
  - Garante que os problemas não entrem gradualmente no sistema, seja como bugs ou como problemas de processo que retardam o ciclo do produto

| ![img](https://susumuasaga.github.io/images/mainline-release.png) |
| ---------------------------------------- |
| **Branch principal pronto para release** |

### Feature Branching de Duração Limitada

- No GitHub flow, os branches de feature são pushados regularmente para o repositório `origin`

- Não há integração com o `master`até o feature seja concluído

- O GitHub flow recomenda **branches de feature** de duração limitada entre  **dez minutos a duas semanas** incluindo a revisão pré-integração

- O estudo do 

  Relatório State Of DevOps

   indicou que as equipes de desenvolvimento de elite integram com mais frequência do que as de baixo desempenho    

  - Aumenta a frequência de merges, mas reduz sua complexidade e risco
  - Alerta as equipes sobre conflitos com muito mais rapidez
  - Aumenta a interação entre os membros do time

### Revisão Pré-integração no Modo de Pull Request

- O modelo **Pull Request** (PR) foi introduzido pelo GitHub, em 2008
- [Google pratica modelo semelhante](https://youtu.be/sMql3Di4Kgc) desde 2005
- Todo o código é revisado antes de ser integrado
- O tempo da revisão deve ser aproximadamente metade do tempo de desenvolvimento do código sendo integrado
- Alguns desenvolvedores squasham (rebase) as mudanças em um único commit antes de iniciar um pull request

| ![img](https://susumuasaga.github.io/images/pull-request-1.png) |
| ---------------------------------------- |
| **Josh pede ajuda para BrianBrian responde com alguns conselhos** |

| ![img](https://susumuasaga.github.io/images/pull-request-2.png) |
| ---------------------------------------- |
| **Josh reconhece os comentários de BrianPusha mais códigos para os atender** |

### Minimizando conflitos no merge:

O conflito de merge se dá exatamente quando o Git identifica para nós que existe duas ou mais alterações em um mesmo local de um determinado arquivo e que o Git precisa que nós para resolvemos. O conflito de merge que comumente e naturalmente aconteça pode ser algo estressante e ter impacto no processo de entrega, a não ser que práticas sejam adotadas para minimizar esses conflitos.

**Ramificações do Git**: Se pretende utilizar o GitHub Flow que propõe feature com limite de dez minutos a 2 semanas, a metódologia Ágil é boa escolha e assim tendo as ramificações do recurso que será desenvolvido é possível encaixar o Git.

**Macro Solução** (ver o termo diferente /planejamento): Tendo uma macro solução fica fácil visualizar o fluxo completo do processo assim podendo estabelecer uma melhor divisão e distribuição das tarefas para equipe evitando que a equipe trabalhe de forma aleatória podendo ter recursos desenvolvidos por mais de um colaborardevido que partes diferentes do sistema comumente utilizaram. 

**Git fetch, GitMerge and Git Commit daily na master (nessa ordem)**:  (master para feature branch .....) A equipe deve diariamente atualizar seu respositório local e efetuar commits de suas alterações diariamente também assim manterá toda a equipe com as alterações mais recentes constantemente minizande grandes ou até mesmo imensos merges e seus conflitos a pequenos conflitos em partes pontuais e mais criticas do sistema e que comumente são aguardadas no merge.

**Cada branch deve ter um escopo definido:** Não fazer nada além do que foi definido no escopo.

**Testes unitários, integrados e automátizados**: Testes são fundamentais para que mesmo que possa resolver diariamente **conflito textual** e **conflito semântico estático** a cada git pull diário e também no merge final, a equipe tenha a confiança que **conflito semântico dinâmico** não serão visto em ambiente de produção ou mesmo que seja descoberto antes, talvez seja descoberto em cima do prazo da entrega gerando transtorno. (antes de pull request ser aprovados - commit test (não é um teste de aceitação e sim de commit próximo de um teste unitário - verificando se o que está sendo entrega está trazendo bugs /trazendo problemas na base de código que está na main;;;; Teste de verificação estática - compilador/IDE faz essa verificação;;;;;; Revisão de pull request/revisão de pré integração - Padrão de condificação - code standard))

**Padrões de desenvolvimento**: padrões são essenciais para que possamos minimizar conflitos de merge, pois tendo padrões seja convencionais ou não farão com que a equipe respeite eles e as alterações não serão feitas de qualquer jeito, um exemplo, atualizações diárias e antes de commit.

### Características

### Branch Principal Pronto para o Release

### Feature Branching de Duração Limitada

### Revisão Pré-integração no Modo de Pull Request

## Desenvolvimento Baseado no Tronco

### Características

### Integração Contínua

### Feature Branching × Integração Contínua

## Conclusão

