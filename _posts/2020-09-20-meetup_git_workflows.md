# Meetup Git Workflows

* TOC
{:toc}

## Branching

| ![](/images/series-commits.png) |
| :-------------------------------: |
|         **Branch e head**         |

* **Branching** é a duplicação de um branch
  * Depois do branching, cada branch pode ser modificado separadamente em paralelo
* O branching implica na capacidade de posteriormente **mergear** ou **integrar** as mudanças
* Poderá haver algum esforço para resolver  **conflitos de merge**:
  * **Conflito textual** × **conflito semântico**
  * [Principais fatores que influenciam o esforço na resolução de conflitos](/assets/paper15.pdf):
    * **Complexidade** das linhas de código em conflito
    * **Modularidade**: acoplamento × coesão
    * **Tamanho dos branches**: número de linhas de código modificadas ou adicionadas depois do branching
  * Via de regra, quando dobramos o tamanho dos branches:
    * O valor esperado e a incerteza do esforço na resolução de conflitos quadruplica

| ![](/images/split-and-merge.png) |
| :--------------------------------: |
|        **Branching e merge**        |

### Vantagens e Desvantagens de Branching

#### Vantagens

* Permite que partes do software sejam desenvolvidas em paralelo
* Permite que os desenvolvedores isolem as mudanças numa base de código estável
* Facilita a manter várias versões em produção

#### Desvantagens

* Menor interação entre os membros do time
* Branchear é fácil, mergear é difícil
* Não há como criar um algoritmo para resolver conflitos automaticamente
* Muitos times gastam uma quantidade excessiva de tempo lidando com seu emaranhado de branches

|               ![](/images/leroy-branch.jpg)                |
| :----------------------------------------------------------: |
| **[Falha apontada por LeRoy](https://twitter.com/jahnnie/status/937917022247120898) em como as pessoas desenham os diagramas de branches** |

## Git-flow

Criado por [Vincent Driessen em 2010](https://nvie.com/posts/a-successful-git-branching-model/). 

| ![](/images/gitflow.png) |
| :-----------------------------: |
|     **Modelo de Git-flow**      |

### Branch Principal ou Tronco

*  No Git-flow, o branch principal é chamado `develop`

### Feature Branching

* **Um branch separado para cada feature**
* Tem origem no `develop`
* Pode ter qualquer nome que não comece com `release` ou `hotfix`
* O escopo do branch deve ser definido precisamente na sua criação
  * **Nunca** realizar tarefas **fora do escopo** pré-definido na branch
* Quando houver novos commits no `develop`:
  * **Mergeie o `develop` para o branch do feature**
* Quando **terminar o feature**:
  * **Integrar com o `develop`**

| ![](/images/feature_integration.png) |
| :------------------------------------: |
|         **Branch de feature**          |

### Branches de Release

* Branches de release são cortados de um commit específico no `develop`
* Convenção de nomenclatura `release-v<n>.<m>`
* Não permite que novos features sejam adicionados ao release
* Os desenvolvedores que trabalham no release se concentram exclusivamente em remover quaisquer defeitos que impeçam o release de estar pronto para produção
* Se não há mais falhas para lidar: 
  * O branch está pronto para release em produção
* **Essas correções** devem ser **mergeadas ao `develop`**
* Conforme mais commits modificam o branch principal: 
  * Fica cada vez mais difícil mergear o branch de release no branch principal
* É muito comum negligenciar a integração das correções

| ![](/images/release-branch.png) |
| :-------------------------------: |
|       **Branch de release**       |

* Algumas pessoas preferem a criação dessas correções no `develop`, ([como Google](/assets/why_google_store_billions_of_locs_in_a_single_repository.pdf))
* Quando estiverem funcionando: 
  * **Cherry-pická-los** no branch de release
* Desvantagens:
  * Muitos times acham difícil fazer isso
  * Pode ser necessário retrabalhar as correções no branch de release

| ![](/images/apply_to_mainline.png) |
| :----------------------------------: |
|   **Aplicar correções no branch principal**    |

* Os branches de release são necessários para projetos em que existem várias versões em produção

|         ![](/images/multi_release_branches.png)         |
| :-------------------------------------------------------: |
| **Branches de release com múltiplas versões em produção** |

### Branches de Hotfix

* Branch para capturar trabalho para corrigir um defeito de produção urgente
* Abrir o branch na última versão de release
* Quando o **hotfix** for **concluído**:
  * O hotfix deve ser **mergeado ao `develop`**
* Se houver um branch de release aberto para a próxima versão:
  * O hotfix precisará ir para lá também

| ![](/images/hotfix-branch.png) |
| :----------------------------: |
|      **Branch de hotfix**      |

* O trabalho de hotfix pode ser feito no branch de release
* É possível fazer os hotfixes no branch principal, cherry-pická-los para o branch de release

|  ![](/images/hotfix-rb.png)  |
| :--------------------------------: |
| **Hotfix em um branch de release** |

### Branch de Produção

* Branch que rastreia as versões entregues para produção
* Para preparar um release para produção:
  * Abrir um branch de release para estabilizar o produto  
  * Quando estiver pronta: copiá-lo para um branch de produção de longa duração
* No Git-flow, o branch de produção é chamado de **`master`**
* Uma alternativa ao uso de branch de produção é aplicar um **esquema de tagueamento**

| ![](/images/production-branch.png) |
| :----------------------------------: |
|        **Branch de produção**        |

### Vantagens e Desvantagens de Git-flow

#### Vantagens

* O histórico de commits do repositório mostra um **registro detalhado do que realmente aconteceu**
* É adequado para projetos em que existem várias versões em produção

#### Desvantagens

* O histórico de Git se torna ilegível, cheia de uma série confusa de commits de merge
* O branch de produção é desnecessário
* Com 5 tipos de branches, o Git-flow é desnecessariamente complicado 
* [Não adequado para Delivery Contínuo](https://nvie.com/posts/a-successful-git-branching-model/)
  * Permite branches de feature de longa duração
  * Branch principal não pronto para o realease


## OneFlow

Proposta no artigo [Git-flow considered harmful por Adam Ruka em 2015](https://www.endoflineblog.com/gitflow-considered-harmful).

| ![](/images/antigitflow-order.png) |
| :----------------------------------: |
|        **Modelo de OneFlow**         |

* OneFlow chama seu branch principal de `master`
* O branch de produção é substituído por um esquema de tagueamento
* Todos os outros branches (feature, release, hotfix) são temporários, usados apenas como uma conveniência para compartilhar código com outros desenvolvedores e como uma medida de backup
* Os **features** são **integrados diretamente** (rebase) no `master`,  de forma a manter um **histórico linear**
* Os releases e hotfixes são feitos de forma semelhante ao Git-flow

### Vantagens e Desvantagens de Oneflow

#### Vantagens

* O histórico do Git será mais limpo, menos confuso, mais legível
* O histórico de commits mostra a **história de como o projeto foi feito**
* O histórico do Git é **passado a limpo**
* É adequado para projetos em que existem várias versões em produção

#### Desvantagens

* Alguns times têm dificuldade de usar comandos para rescrita do histórico
* Não adequado para o Delivery Contínuo
  * Permite branches de feature de longa duração
  * Branch principal não pronto para o release

## GitHub Flow

Criado por [Scott Chacon em 2011](http://scottchacon.com/2011/08/31/github-flow.html).

* GitHub flow chama o branch principal de `master`
* Única versão em produção
* **Branch principal pronto para release**
* Branches de releases não são necessários
* Problemas de produção são corrigidos da mesma maneira que features regulares, assim não há necessidade de branches de hotfix
* **Feature branching de duração limitada**
* **Revisão pré-integração usando Pull-Request**

### Branch Principal Pronto para Release

* Manter o  **branch `master`** suficientemente **saudável** para que o head do `master` possa sempre ser colocado diretamente em produção
* Para manter o branch saldável é essencial escrever **código de autoteste**:
  * **Conjunto abrangente de testes automatizados**, para que possamos ter confiança de que, se esses testes passarem, o código de produção **não conterá bugs**
  * **Executados rapidamente**, geralmente **não mais do que dez minutos**
  * **Toma mais tempo do que** o desenvolvimento do **código de produção**
* Precisamos manter **qualidade interna do código** alta usando práticas como:
  * Análise de programa estática
  * **Revisão pré-integração**
* Se o time usa feature branching de longa duração (> 2 semanas):
  * O branch principal pronto para o release pode ser uma barreira para sua melhoria
* Vantagens:
  * Juntamente com a **integração contínua** como parte do **delivery contínuo**, [um branch principal pronto para release é uma característica de times de elite](/assets/2016-State-of-DevOps-Report.pdf)
  * Simplicidade
  * Garante que os problemas não entrem gradualmente no sistema, seja como bugs ou como problemas de processo que retardam o ciclo do produto

|   ![](/images/mainline-release.png)    |
| :--------------------------------------: |
| **Branch principal pronto para release** |

### Feature Branching de Duração Limitada

* No GitHub flow, os branches de feature são pushados regularmente para o repositório `origin`
* Não há integração com o `master`até o feature seja concluído
* O GitHub flow recomenda **branches de feature** de duração limitada entre  **dez minutos a duas semanas** incluindo a revisão pré-integração
* O estudo do [Relatório State Of DevOps](/assets/2016-State-of-DevOps-Report.pdf) indicou que as equipes de desenvolvimento de elite integram com mais frequência do que as de baixo desempenho
  * Aumenta a frequência de merges, mas reduz sua complexidade e risco
  * Alerta as equipes sobre conflitos com muito mais rapidez
  * Aumenta a interação entre os membros do time

### Revisão Pré-integração no Modo de Pull Request

* O modelo **Pull Request** (PR) foi introduzido pelo GitHub, em 2008
* [Google pratica modelo semelhante](https://youtu.be/sMql3Di4Kgc) desde 2005
* Todo o código é revisado antes de ser integrado
* O tempo da revisão deve ser aproximadamente metade do tempo de desenvolvimento do código sendo integrado
* Alguns desenvolvedores squasham (rebase) as mudanças em um único commit antes de iniciar um pull request

|    ![](/images/pull-request-1.png)    |
| :-------------------------------------: |
| **Josh pede ajuda para Brian<br />Brian responde com alguns conselhos** |


|      ![](/images/pull-request-2.png)       |
| :------------------------------------------: |
| **Josh reconhece os comentários de Brian<br />Pusha mais códigos para os atender** |

## Desenvolvimento Baseado no Tronco

Paul Hammand escreveu [um site detalhado](https://trunkbaseddevelopment.com/) para explicar essa abordagem.

* O **Desenvolvimento Baseado no Tronco** se concentra em fazer todo trabalho no branch principal (chamado de “tronco”), evitando assim qualquer tipo de branch de longa duração
* **Integração contínua**
* Times podem usar:
  * Branch de release (“branch para release”)
  * Branch principal pronto para release (“release a partir do tronco”)
* [Google pratica Desenvolvimento Baseado no Tronco](/assets/why_google_store_billions_of_locs_in_a_single_repository.pdf): 
  * **2+ bilhões de linhas de código**
  * Tronco **monorepo** único
  * **Checkout esparso**

|                 ![](/images/trunk1b.png)                 |
| :------------------------------------------------------: |
| **Desenvolvimento baseado no Tronco para times menores** |

|        ![](/images/trunk1c.png)         |
| :---------------------------------------: |
| **Desenvolvimento Baseado no Tronco para times maiores** |

### Integração Contínua

* **Integração contínua**:
  * **Nunca** deve ter **mais de um dia de trabalho não integrado** no repositório local de ninguém
  * Toda integração é buildada e testada com **código de autoteste**
* **Não** é **necessário** de que o **feature** esteja **completo**
* O time deve conhecer técnicas para ocultar features parciais como:
  * **Branch por abstração** para mudanças mais longas
  * **Feature flags** no desenvolvimento do dia a dia
* Pode integrar **diretamente no `master`** ou usar **branches de feature de curta duração**

#### Confusão com Ferramentas de CI

* Uma ferramenta de CI é um serviço que builda automaticamente o produto de software antes de cada delivery (como Jenkins, Team City, Travis CI, Circle CI, Bamboo)
* As organizações que usam essas ferramentas as usa para buildar automaticamente **branches de feature de duração maior que um dia não** estão praticando **integração contínua**
* Um melhor nome para essas ferramentas seria ferramentas de Build Contínuo

#### Feature Branching × Integração Contínua

Conforme [Martin Fowler](https://martinfowler.com/articles/branching-patterns.html#ComparingFeatureBranchingAndContinuousIntegration):

| **Feature Branching**                                        | **Integração Contínua**                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ❌ Merges menos frequentes<br /> ✔ Todo o código em um feature pode ser avaliado quanto à qualidade como uma unidade<br /> ✔ O código do feature só é adicionado ao produto quando o feature estiver completo<br /> | ✔ Merges menores<br /> ✔ Tempo reduzido para encontrar conflitos<br /> ✔ Encoraja a refatoração<br /> ✔ Apoia integração em período menor do que o tamanho do feature<br /> ❌ Requer compromisso com branches saudáveis (e, portanto, código de autoteste)<br /> ✔ [Evidência científica](/assets/2016-State-of-DevOps-Report.pdf) de que contribui para um maior desempenho de entrega de software |

## Recomendações
* Sempre que estiver pensando em usar um branch, procure entender as consequências no merge
* Certifique-se de entender as alternativas ao Git-flow, como o GitHub flow e o Desenvolvimento Baseado no Tronco, que são geralmente superiores
* Pratique revisão pré-integração com duração de aproximadamente metade do tempo de desenvolvimento do código
* Tente duplicar sua frequência de integração
* Quando a duração dos branches de feature não for maior do que 1 semana:
  * Pratique o branch principal pronto para o release 

