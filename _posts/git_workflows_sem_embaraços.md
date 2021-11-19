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

Este fluxo(flow) de trabalho no Git for originalmente proposto por [Adam Ruka](https://www.endoflineblog.com/about) nos artigos:  
1. [GitFlow considered harmful(Março de 2015)](https://www.endoflineblog.com/gitflow-considered-harmful)
1. [Follow-up to 'GitFlow considered harmful'(Junho de 2015)](https://www.endoflineblog.com/follow-up-to-gitflow-considered-harmful)
1. [OneFlow – a Git branching model and workflow(Abril de 2017)](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow)

Há ainda outro artigo escrito pelo autor sobre a aplicação do fluxo nos serviços GitHub, BitBucket & GitLab, mas este escapa ao presente escopo.

| ![](/images/antigitflow-order.png) |
| :----------------------------------: |
|        **Modelo de OneFlow**         |

Um dos aspectos definidores do OneFlow é o uso de um branch único como principal(único "perene") de `master`. Isso é conseguido via eliminação do branch de produção, tal como no Git-Flow, sendo esse substituído por um esquema de tagueamento -- o que é suficiente para manter a informação das versões, originalmente no branch de produção.
Os outros branches "clássicos"(feature, release, hotfix) são temporários, e são usados principalmente como uma conveniência para compartilhar código com outros desenvolvedores e como uma medida de backup. Destarte, os **features** são **integrados diretamente** (rebase) no `master`,  de forma a manter um **histórico linear**; já os releases e hotfixes são feitos de forma semelhante ao Git-flow.

### Características(Vantagens e Desvantagens) do Oneflow

#### Vantagens

A vantagem mais óbvia, do ponto de vista do usuário do git, é a facilidade em se localizar no histórico do Git, dada a linearidade obtida com a manutenção rígida do branch principal único; assim, a sequencia dos commits corresponde rigorosamente à cronologia do projeto. Dentro do contexto mais amplo do presente artigo, a facilidade(e conveniência) estimulada pelo branch principal único no desenvolvimento favorecerá de sobremaneira a abordagem aqui estimulada, no caso, o menor tempo possível de vida das diversas branches, sejam feature, release ou hotfix.

#### Desvantagens

Entre as desvantagens do presente fluxo a mais evidente e óbiva é a inadequação para projetos em que coexistem versões não compatíveis em produção, pelo mero uso do branch principal único. Superado esse aspecto, outra problema é a dificuldade sentida por alguns times em usar os comandos necessários para reescrita do histórico.
Cabe ainda salientar que também não é adequado para o Delivery Contínuo(Continuous Delivery), dada a permissibilidade de branches de feature de longa duração, além do que a branch principal não é, por definição, pronta para o release. Nesse ponto, embora tenha sido apontada anteriormente uma conveniência ao princípio de encurtamento das branches, há oportunidade em se violar o princípio pois não há, por outro lado, uma restrição à duração da branch *per se*.


### Quando Usar o OneFlow
* Por ser uma "reação" ao GitFlow, é um substituto imediato para qualquer projeto que o use;
* Nos projetos onde qualquer versão é necessariamente baseada na anterior, o que casa com a metodologia do OneFlow;
* Na esmagadora maioria dos projetos Web;
* Em grande parte dos projetos Open-Source que seguem o versionamento linear.


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

