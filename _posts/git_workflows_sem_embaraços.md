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

Este fluxo (flow) de trabalho no Git for originalmente proposto por [Adam Ruka](https://www.endoflineblog.com/about) nos artigos:  
1. [GitFlow considered harmful (Março de 2015)](https://www.endoflineblog.com/gitflow-considered-harmful)
2. [Follow-up to 'GitFlow considered harmful' (Junho de 2015)](https://www.endoflineblog.com/follow-up-to-gitflow-considered-harmful)
3. [OneFlow – a Git branching model and workflow (Abril de 2017)](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)

Há ainda outro artigo escrito pelo autor sobre a aplicação do fluxo nas plataformas de Git: GitHub, Bitbucket e GitLab, que escapa ao presente escopo.

Um dos aspectos definidores do OneFlow é o uso de um branch único como principal (único "perene"), chamado aqui de `master`, correspondente ao branch `develop` de Git-flow. Isso é conseguido via eliminação do branch de produção, chamado de `master` no Git-flow, sendo esse substituído por um esquema de tagueamento -- o que é suficiente para manter a informação das versões, originalmente rastreados no branch de produção.

Os outros branches "clássicos" (feature, release, hotfix) são temporários, e são usados principalmente como uma conveniência para compartilhar código com outros desenvolvedores e como uma medida de backup. Destarte, os **features** são **integrados diretamente** (via `rebase`) no `master`,  de forma a manter um **histórico linear**; já os releases e hotfixes são feitos de forma semelhante ao Git-flow. Na figura abaixo, mostramos como ficaria o diagrama de branch usando OneFlow no projeto exemplo, onde podemos verificar notável simplificação em relação ao Git-flow.

| ![](../images/antigitflow-order.png) |
| :----------------------------------: |
|        **Modelo de OneFlow**         |

### Vantagens do Oneflow

A vantagem mais óbvia, do ponto de vista do usuário do Git, é a facilidade de compreensão do histórico do Git, dada a linearidade obtida com a manutenção rígida do branch principal único; assim, a sequência dos commits é a **narrativa de como o projeto foi feito**. Você não publicaria o primeiro rascunho de um livro, então por que mostrar seu trabalho bagunçado? Quando está trabalhando em um projeto, pode precisar de um registro de todas suas tentativas e erros, mas, quando for a hora de mostrar seu trabalho para o mundo, pode querer contar uma narrativa direta de como sair de A para B. As pessoas neste campo usam comandos como `rebase` e `filter-branch` para rescrever seus commits antes de serem mergeados ao branch principal, de forma a contar a narrativa da maneira que for mais compreensível para futuros leitores. Esses comandos são considerados "avançados", assim alguns times podem ter certa dificuldade em usá-los.

Dentro do contexto mais amplo do presente artigo, a facilidade (e conveniência) estimulada pelo branch principal único no desenvolvimento favorecerá de sobremaneira a abordagem aqui estimulada, no caso, o menor tempo possível de vida das diversas branches, sejam feature, release ou hotfix.

### Quando Usar o OneFlow

OneFlow se destina a ser um substituto imediato para Git-flow, o que significa que é adequado em todas as situações em que o Git-flow é. De fato, é fácil migrar um projeto que esteja usando Git-flow para OneFlow.

Na forma padrão, como foi proposta no artigo original, da mesma forma que o Git-flow, o Oneflow não pode ser usado em projetos em que têm mais do que uma versão em produção. Mas essa deficiência pode ser sanada se mantendo vários branches de release ativos, um para cada versão em produção, como mostramos na seção anterior sobre o Git-flow.

### Quando Não Usar o OneFlow

Como o autor enfatiza em seu artigo, assim como o Git-flow, o OneFlow não é adequado para projetos que usam Integração Contínua (Continuous Integration), dada a probabilidade de branches de feature que duram vários dias, além do que o branch principal não é, por definição, pronto para o release. Talvez partes da metodologia possam ainda ser úteis, mas outros elementos (como o processos de integração e release) teriam que ser fortemente modificados para fazer sentido ao fazer integração em uma cadência tão frequente (diária). 

## GitHub Flow

O fluxo de GitHub é um fluxo de trabalho leve e baseado no branch criado por [Scott Chacon em 2011](http://scottchacon.com/2011/08/31/github-flow.html). Scott  em seu artigo explica que um dos aspectos visados na criação do GitHub Flow é que o GitHub implanta o tempo todo,  as implantações acontecem diariamente ou mesmo várias vezes ao dia, então GitHub Flow veio com uma proposta muito clara, a facilidade e agilidade de implantar, digamos, menos burocrático como Git Flow, que é o sistema que Scott em seu artigo faz um comparativo com o GitHub Flow.

Hoje o GitHub chama sua branch principal de main (antigamente master), possui uma única versão em produção, a branch principal pronto para release, branches de releases não são necessárias, problemas de produção são corrigidos da mesma maneira que features regulares, assim não há necessidade de branches de hotfix e a revisão e pré-integração acontece usando Pull-Request.

A branch principal, por sofrer atualizações em um curto prazo, Scott vê vantagem no aspecto de minimizar às introduções de grandes bugs e em contra-ponto na introduções de pequenos bugs que venham acontecer na branch principal é possível rapidamente corrigir e reimplantar, como já mencionado acima, a branch principal está sempre pronta para release.

O GitHub Flow possui uma proposta menos burocratica e ágil, comumente se comporta muito bem em uma metologia ágil, porém para o GitHub Flow atender sprints de até 2 semanas, ou 1 semana ou implantações diárias é necessário que a equipe tenha uma certa maturidade, tendo e respeitando boas práticas e padrões de desenvolvimento utilizado pela comunidade, e, não menos importantes desenvolvimentos de testes (unitários, integrados e automatizado). Utilizar o TDD (Test Driven Development) como padrão de desenvolvimento de software é uma boa para manter a branch principal saudável.

Se o time usa feature branching de longa duração (> 2 semanas) , a branch principal pronto para o release pode ser uma barreira para sua melhoria, por isso é um ponto importante entender como será o prazo das entregas na utilização do GitHub Flow, porém muito mais enter os prazos das entregas e é isso que veremos no próximo tópico.

### Branch Principal Pronto para Release

Para termos um branch pronto para release é essencial manter o  **branch master** suficientemente **saudável**. Assim o head do `master` possa sempre estar pronto para ser colocado diretamente em produção. Para conseguirmos esse feito de manter a branch sempre saúdavel é recomendado que a equipe trabalhe com código de autoteste como um conjunto abrangente de testes automatizados, para que possamos ter confiança de que, se esses testes passarem, o código de produção **não conterá bugs**.  **Executados rapidamente**, geralmente **não mais do que dez minutos****. **Toma mais tempo do que** o desenvolvimento do **código de produção** . E náo menos importante manter a **qualidade interna do código**, como: Análise de programa estática e **Revisão pré-integração**(mais a frente teremos um parágrafo exclusivo falando sobre)

Como citado, manter uma branch saúdavel precisamos de teste, como testes unitários, integrados e automatizados, por isso é fortemente recomendado que equipe trabalhe com uma linguagem mais madura que possua alguns frameworks que possam te auxiliar nesse aspecto, como JUnit do Java, JUnit permite facilmente com anotaçoes criar testes unitários que lhe informaram de forma muito simples quando teste passou e quando não. Uma linguagem madura, um framework para teste e tão importante quanto, uma IDEA, como eclipse e/ou Intellij que lhe permitirá que você execute e automatize testes facilmente e possa ter code coverage (cobertura de código) e teste coverage (test).

E falando de framework de teste, hoje já não podemos deixar de citar um framework que alguns anos já é muito utilizado por desenvolvedores no mundo, o framework mockito. Mockito nos auxiliar na criação de mocks, isso, ele nos auxilia a criar respostas fakes de recursos do sistema que porventura nossos testes utilizam, assim possamos contonar quando parte do nosso sistema precise acessam outros recursos externos. Lembresse, conforme citado mais acima, a execução de todos os testes devem ser rápidos, geralmente não mais que dez minutos, e que o fazemos quando, por exemplo, um código nosso precisa acessar um outro microservices para tendo informações fazer um deteminado tipo de cálculo e salvar em um banco de dados? Isso é custoso, acessos a recursos externos podem ser demorados ou mesmo estarem indisponíveis no momento, e então nossos testes vão demorar ou mesmo falhar, e isso vai contra a ideia do teste unitários, nesse caso podemos utilizar o framework para nos auxiliar nisso.

OBS: Master é o nome antigo utilizado pelo GitHub Flow para sua branch principal, hoje chamada de main.

| ![img](https://susumuasaga.github.io/images/mainline-release.png) |
| ---------------------------------------- |
| **Branch principal pronto para release** |

### Revisão Pré-integração no Modo de Pull Request

Esse é um ponto de muita relevância, pois esse modo nos da uma visibilidade do código interno para nossa própria revisão, mas também serve para outros revisarem, podendendo indicar suas preocupações para que quem irá revisar se atente com mais cuidado certas linhas de código, além de pedir para mesclar as branch. O tempo da revisão deve ser aproximadamente metade do tempo de desenvolvimento do código sendo integrado.

Scott em seu artigo cita que solicitação de Pull Request é utililizada por eles do GitHub muito antes  de realmente de quererem mesclar no master para implantação, isso como próprio Scott apresenta, é uma fase que integrantes da equipe conseguem fazer revisão, trocar algumas mensagens sobre o código que está na solicitação, seja para solicitar um simples conselho ou mesmo para solicitar ajuda por estar travado no progresso do seu recurso.

E assim que estiver tranquilo e confiante você pode seguir para próxima fase. 

### Merge ao contrário:

Merge ao contrário nada mais é do que você estando na sua feature branch fazer um git merge na branch principal (main/master), assim você manterá seu repositório sempre com as atualições mais recente em conjunto com que você vem desenvolvendo. Com isso quando a etapa de fazer merge com a branch principal você evitará possíveis grandes conflitos, pois sua branch está próxima da versão da master.

### Minimizando conflitos de merge:

O conflito de merge se dá exatamente quando o Git identifica para nós que existe duas ou mais alterações em um mesmo local de um determinado arquivo e que o Git precisa que nós para resolvemos. O conflito de merge que comumente e naturalmente aconteça pode ser algo estressante e ter impacto no processo de entrega, a não ser que práticas sejam adotadas para minimizar esses conflitos.

**Ramificações do Git**: Se pretende utilizar o GitHub Flow que propõe feature com limite de dez minutos a 2 semanas, a metódologia Ágil é boa escolha e assim tendo as ramificações do recurso que será desenvolvido é possível encaixar o Git.

**Macro Solução**: Tendo uma macro solução fica fácil visualizar o fluxo completo do processo assim podendo estabelecer uma melhor divisão e distribuição das tarefas para equipe evitando que a equipe trabalhe de forma aleatória podendo ter recursos desenvolvidos por mais de um colaborardevido que partes diferentes do sistema comumente utilizaram. 

**Testes unitários, integrados e automátizados**: Testes são fundamentais para que mesmo que possa resolver diariamente **conflito textual** e **conflito semântico estático** a cada git pull diário e também no merge final, a equipe tenha a confiança que **conflito semântico dinâmico** não serão visto em ambiente de produção ou mesmo que seja descoberto antes, talvez seja descoberto em cima do prazo da entrega gerando transtorno. (antes de pull request ser aprovados - commit test (não é um teste de aceitação e sim de commit próximo de um teste unitário - verificando se o que está sendo entrega está trazendo bugs na base de código que está na main.

**Git fetch, GitMerge and Git Commit daily na main (nessa ordem)**:  A equipe deve diariamente atualizar seu respositório local e efetuar commits de suas alterações diariamente também assim manterá toda a equipe com as alterações mais recentes constantemente, isso minizará grandes ou até mesmo imensos merges e seus conflitos a pequenos conflitos em partes pontuais e mais criticas do sistema e que comumente são aguardadas no merge. Assim também deve diariamente fazer merge  com a branch principal a main para a feature branch, e em seguinda **Revisão de pull request revisão de pré integração**.

**Merge ao contrário da main para feature** : git merge main (estando na sua feature branch) para que você tenha um repositório mais próximo da main, assim evitando que no momento de mesclar sua versão com a main tenham muito diferenças e/ou conflitos de merge a serem revisados e mesclado. 

**Cada branch deve ter um escopo definido:** Não fazer nada além do que foi definido no escopo.

**Padrões de desenvolvimento**: padrões são essenciais para que possamos minimizar conflitos de merge, pois tendo padrões (code standard) seja convencionais ou não farão com que a equipe respeite eles e as alterações não serão feitas de qualquer jeito, um exemplo, atualizações diárias e antes de commit.

## Desenvolvimento Baseado no Tronco

### Características

### Integração Contínua

### Feature Branching × Integração Contínua

## Conclusão

