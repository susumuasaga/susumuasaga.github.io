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

1. O **conflito semântico estático**  ocorre quando as falhas aparecem na análise do programa estática, por exemplo na compilação. Isso acontece, por exemplo, quando há um conflito associado ao nome de uma função;

1. O **conflito semântico dinâmico** é o mais insidioso e dificultoso, ocorre quando as falhas aparecem somente em tempo execução. Este tipo de conflito é detectado por um teste que reproduza as condições da falha.

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
1. [Follow-up to 'GitFlow considered harmful' (Junho de 2015)](https://www.endoflineblog.com/follow-up-to-gitflow-considered-harmful)
1. [OneFlow – a Git branching model and workflow (Abril de 2017)](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)

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

### Características

### Branch Principal Pronto para o Release

### Feature Branching de Duração Limitada

### Revisão Pré-integração no Modo de Pull Request

## Desenvolvimento Baseado no Tronco

### Características

### Integração Contínua

### Feature Branching × Integração Contínua

## Conclusão

