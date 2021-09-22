# Meetup Git Workflows

* TOC
{:toc}

## Branching

| ![](/images/series-commits.png) |
| :-------------------------------: |
|         **Branch e head**         |

* **Branching** é a duplicação de um objeto sob controle de versão (como um arquivo de código-fonte ou uma árvore de diretório)
* Cada objeto pode, a partir daí, ser modificado separadamente em paralelo de forma que os objetos se tornam diferentes
* Nesse contexto os objetos são chamados de **branches**
* O branching também geralmente implica na capacidade de posteriormente mergear ou integrar as mudanças para o branch pai

| ![](/images/split-and-merge.png) |
| :--------------------------------: |
|        **Branch e merge**        |

### Vantagens de Branching

* Permite que partes do software sejam desenvolvidas em paralelo.
* Facilita a manter vários releases em produção.
* Permite que os desenvolvedores isolem as mudanças sem desestabilizar a base de código, por exemplo, correções para bugs, novos features, integração de versões.

### Desvantagens de Branching

* Branchear é fácil, mergear é difícil.
* **Conflito textual** × **conflito semântico**.
* Não há como criar um algoritmo para resolver conflitos automaticamente.
* Muitos times gastam uma quantidade excessiva de tempo lidando com seu emaranhado de branches.

|               ![](/images/leroy-branch.jpg)                |
| :----------------------------------------------------------: |
| **[Falha apontada por LeRoy](https://twitter.com/jahnnie/status/937917022247120898) em como as pessoas desenham os diagramas de branches** |

## Git-flow

Criado por [Vincent Driessen em 2010](https://nvie.com/posts/a-successful-git-branching-model/). 

| ![](/images/git-model@2x.png) |
| :-----------------------------: |
|     **Modelo de Git-flow**      |

### Branch Principal

*  O **branch principal** é um branch especial no **repositório central** que consideramos ser o estado corrente do código do time
   *  Para iniciar um novo trabalho: branchear do branch principal para um branch de trabalho
   *  Sempre que quiser compartilhar seu trabalho com o resto do time: **mergear seu branch de trabalho para o branch principal** (**integração com o branch principal**)
*  No Git-flow, o branch principal é denominado `origin/develop`

| ![](/images/main-branch.png) |
| :----------------------------: |
|      **Branch principal**      |

### Branches de Feature

* Desenvolvedores abrem uma branch quando começam a trabalhar em um feature:
  * Branchear de develop
  * Se estiver trabalhando nisso por um tempo, manter atualizado **mergeando o develop para o branch do feature**
  * Continuar trabalhando nesse branch até **terminar o feature**
  * **Integrar com o develop**
* Se trabalhar em mais do que um feature: abrir um branch separado para cada
* Incompatível com integração contínua

| ![](/images/feature_integration.png) |
| :------------------------------------: |
|         **Branch de feature**          |

### Branches de Release

* Branches de release são cortados de um commit específico no `develop`
* Convenção de nomenclatura `release-v<n>.<m>`
* Apenas aceita commits de correções
* Para estabilizar uma versão do produto pronto para produção
* **Essas correções** devem ser **mergeadas ao `develop`** 
* É muito comum negligenciar o mergeamento das correções para o `develop`

| ![](/images/release-branch.png) |
| :-------------------------------: |
|       **Branch de release**       |

* Algumas pessoas preferem a criação dessas correções no `develop` ([como Google](/assets/2854146.pdf))
* Depois os cherry-pickar no branch de release
* Desvantagens
  * Muitos times acham difícil fazer isso
  * Consertar de uma maneira na linha principal e ter que retrabalhar no branch de release

| ![](/images/apply_to_mainline.png) |
| :----------------------------------: |
|   **Aplicar correções no branch principal**    |

* Os branches de release são necessários para projetos em que existem várias versões em produção

|         ![](/images/multi_release_branches.png)         |
| :-------------------------------------------------------: |
| **Branches de release com múltiplas versões em produção** |

### Branches de Hotfix

* Branch para capturar trabalho para corrigir um defeito de produção urgente
* Quando o **hotfix** for **concluído**
  * Um novo release é feito
  * O hotfix deve ser **mergeado ao `develop`**
* O trabalho de hotfix pode ser feito no branch de release
  * Que se transforma num branch de hotfix

|  ![](/images/hotfix-branch.png)  |
| :--------------------------------: |
| **Hotfix em um branch de release** |

* É possível fazer os hotfixes no branch principal
* Depois os cherry-pickar para o branch de release
* Menos comum
  * Hotfixes geralmente são feitos sob forte pressão de tempo 

### Branch de Produção

* Quando estamos preparando um release de produção, abrimos um branch de release
* Assim que estiver pronto, mergeamos para um branch de produção
* No Git-flow, o branch de produção é denominado **`origin/master`**

| ![](/images/production-branch.png) |
| :----------------------------------: |
|        **Branch de produção**        |

* Uma alternativa ao uso de branch de produção é aplicar um **esquema de tagueamento**

### Vantagens de Git-flow

* O histórico de commits do repositório é um **registro detalhado do que realmente aconteceu**
* Os nomes dos branches seguem um padrão sistemático tornando mais fácil de compreender
* É adequado para projetos em que existem várias versões em produção

### Desvantagens de Git-flow

* O histórico de Git se torna ilegível, cheia de uma série confusa de commits de merge
* O branch de produção é desnecessário
* Git-flow é desnecessariamente complicado 
  * Um [grande script auxiliar](https://github.com/nvie/gitflow) foi desenvolvido para ajudar a cumprir o procedimento. 
  * Não pode ser aplicado em uma GUI Git, apenas na linha de comando
* Incompatível para projetos que usam integração continua

## OneFlow

Proposta no artigo [Git-flow considered harmful por Adam Ruka em 2015](https://www.endoflineblog.com/gitflow-considered-harmful).

| ![](/images/antigitflow-order.png) |
| :----------------------------------: |
|        **Modelo de OneFlow**         |

* O branch de produção é substituído por um esquema de tagueamento
* OneFlow chama seu branch principal de `origin/master`
* Os features são integrados diretamente no branch principal [squashados](https://softwareengineering.stackexchange.com/questions/263164/why-squash-git-commits-for-pull-requests) de forma a manter um **histórico linear**
  * No OneFlow, a integração é feita por meio de rebase interativo (`git rebase --interactive`) e merge fast-forward (`git merge --ff-only`)
* Os releases e hotfixes são feitos de forma semelhante ao Git-flow

### Vantagens de Oneflow

* O histórico do Git será mais limpo, menos confuso, mais legível
  * O histórico de commits é a **história de como o projeto foi feito**
  * O branch é passado a limpo antes de ser mergeado no branch principal 
  * Conta a história da maneira que for mais compreensível para os leitores

### Desvantagens de Oneflow

* Usa comandos avançados para rescrita do histórico
* Inadequado para projetos que usam integração continua

## GitHub Flow

Criado por [Scott Chacon em 2011](http://scottchacon.com/2011/08/31/github-flow.html).

* O branch de produção é substituído por um esquema de tagueamento
* GitHub flow chama seu branch principal `origin/master`
* Premissas
  * Única versão em produção
  * Branch principal pronto para release
  * Alta-frequência de integração (2 semanas no máximo)

### Única Versão em Produção

* Branches de releases não são necessários
* Os branches de hotfix não são necessários: issues de produção são corrigidos da mesma forma que features comuns
* A estrutura de branching drasticamente simplificada para: um branch principal e branches de features

### Branch Principal Pronto para Release

*  **Branch principal saudável**
   *  Um desenvolvedor deve ser capaz de iniciar um novo trabalho simplesmente brancheando do branch principal, não se enredar em defeitos que atrapalhem seu trabalho
   *  Facilita o caminho para produção
      *  Um novo release de produção pode ser criado a qualquer momento a partir do head do branch principal
   *  Um **código de autoteste** com uma **suíte de commit** que rode em alguns minutos é fundamental
      *  É um investimento significativo: para cada linha de código escrita, os programadores geralmente precisam de 3 a 5 linhas de código de teste
      *  Possibilita fazer mudanças mais rapidamente, refatorar com segurança nosso código para o manter fácil de trabalhar, reduzir drasticamente o tempo de ciclo de um feature desejado para o código rodando em produção

### Frequência de Integração

De acordo com [Martin Fowler](https://martinfowler.com/articles/branching-patterns.html#integration-frequency)

* A frequência com que fazemos a integração tem um efeito extraordinariamente poderoso sobre como uma equipe opera
* A pesquisa do [Relatório State Of DevOps](https://martinfowler.com/bliki/StateOfDevOpsReport.html) indicou que as equipes de desenvolvimento de elite integram notavelmente com mais frequência do que as de baixo desempenho

#### Integração de baixa-frequência

* Nossas duas heroínas, Scarlett e Violet, começam brancheando o branch principal em seus branches, então fazendo alguns commits locais que não querem integrar ainda.
* Enquanto trabalham, outra pessoa coloca um commit no branch principal.
* Esta equipe trabalha mantendo um branch saudável, mergeando do branch principal após cada commit. Scarlett não tinha nada para mergear com seus dois primeiros commits já que o branch principal estava inalterada, mas agora precisa mergear M1.
* Logo Violet precisa fazer a mesma coisa.
* Scarlett faz mais alguns commits locais, então está pronta para fazer a integração ao branch principal. Este é um merge fácil para ela, já que margeou M1 antes.
* Violet tem um exercício mais complicado. Quando ela faz a integração ao branch principal, ela agora precisa integrar S1..5 com V1..6.

| ![](/images/low-freq-V-push.png) |
| :--------------------------------: |
| **Baixa frequência de integração** |

#### Integração de alta-frequência

* A primeira mudança é aparente com o primeiro commit de Violet, já que ela integra imediatamente. Uma vez que o branch principal não mudou, este é um merge sem conflitos.
* O primeiro commit de Scarlett também tem integração com o branch principal, mas como Violet chegou lá primeiro, pode haver conflitos. Mas, como ela está mergeando apenas V1 com S1, o esforço é pequeno.
* A próxima integração de Scarlett é um merge sem conflitos, o que significa que o próximo commit de Violet também exigirá um merge com os dois últimos commits de Scarlett. No entanto, ainda é um merge bem pequeno, uma de Violet e duas de Scarlett.
* Quando o push externo para o branch principal aparece, ele é captado no ritmo usual das integrações de Scarlett e Violet.
* As desenvolvedoras continuam com o trabalho restante, integrando a cada commit.

|  ![](/images/high-freq-V6.png)  |
| :-------------------------------: |
| **Alta frequência de integração** |

#### Comparando frequências de integração

* A integração frequente aumenta a frequência de merges, mas reduz sua complexidade e risco
* A integração frequente também alerta as equipes sobre conflitos com muito mais rapidez
* Sistema de controle de versão é uma ferramenta de comunicação

|      ![](/images/low-freq-conflict.png)       |
| :---------------------------------------------: |
| **Conflito com baixa frequência de integração** |

|     ![](/images/high-freq-conflict.png)      |
| :--------------------------------------------: |
| **Conflito com alta frequência de integração** |

### Integração Contínua

* Os desenvolvedores fazem a integração do branch principal assim que têm um commit saudável que podem compartilhar
* **Nunca deve ter mais do que um dia de trabalho não integrado em seu repositório local**
* Acostumar com a ideia de alcançar pontos de integração frequentes com **features parcialmente construídos**

| ![](/images/continuous_integration.png) |
| :---------------------------------------: |
|     **Continuous Delivery em GitHub**     |

#### Integração por Feature × Integração Contínua

#### Integração por Feature

* Todo o código em um feature pode ser avaliado quanto à qualidade como uma unidade ✔
* O código do feature só é adicionado ao produto quando o feature estiver completo ✔
* Merges menos frequentes ❌

#### Integração Contínua

* Apoia integração em período menor do que o tamanho do feature ✔
* Tempo reduzido para encontrar conflitos ✔
* Merges menores ✔
* Encoraja a refatoração ✔
* Evidência científica de que contribui para um maior desempenho de entrega de software ✔
* Requer compromisso com branches saudáveis (e, portanto, código autoteste) ❌

### Pull Request como Ferramenta de Conversação do Branch

* No GitHub flow, o **pull request** é usado mais como como uma ferramenta de conversação do branch do que propriamente uma solicitação de integração

|    ![](/images/pull-request-1.png)    |
| :-------------------------------------: |
| **Início de discussão de pull request** |

|      ![](/images/pull-request-2.png)       |
| :------------------------------------------: |
| **Continuação de discussão em pull request** |

| ![](/images/rebase_feature.png) |
| :-------------------------------: |
|     **Atualizando um branch**     |

### Revisão Pré-integração com Pull Request

* No GitHub flow, cada commit para o branch principal é revisado por pares, no pull-request, antes de o commit ser aceito
* Antes de submeter, a branch deve:
  * estar saldável
  * ser passada a limpo 
  * ter conflitos existentes com o branch principal resolvidos
* Difícil de ser usado com integração contínua, mas é possível ([Google usa esta abordagem](/assets/2854146.pdf))

| ![](/images/pull-request-3.png) |
| :-------------------------------: |
|   **Aprovação de pull request**   |

### Vantagens de GitHub Flow

* Amigável à integração contínua
* Alternativa mais simples para Git-flow
* Ideal quando precisa manter uma versão única em produção

### Desvantagens de GitHub Flow

* Requer compromisso com branches saudáveis
* Não recomendado quando várias versões em produção são necessárias

## Desenvolvimento Trunk-Based

* **Branch principal**:
  * Usuários de Subversion o chamam de “trunk”
  * Usuários de Git o chamam de “master”

|             ![](/images/trunk1b.png)             |
| :------------------------------------------------: |
| **Desenvolvimento Trunk-Based para times menores** |

|        ![](/images/trunk1c.png)         |
| :---------------------------------------: |
| **Desenvolvimento Trunk-Based em escala** |

**Regras**

* Você deve fazer o Desenvolvimento Trunk-Based em vez de Git-Flow e outros modelos de branching que apresentam várias ramificações de longa duração.
* Você pode fazer um commit / push direto para o master (em times pequenos) ou um workflow Pull-Request, desde que esses branches de feature tenham vida curta e sejam o produto de uma única pessoa.

**Ressalvas**

* Dependendo do tamanho do time e da frequência de commits, **branches de feature de curta duração** são usados para revisão de código e verificação de build (CI), mas não para a criação ou publicação de artefatos, para acontecer antes que os commits sejam integrados ao master para outros desenvolvedores os consumirem. Esses branches permitem que os desenvolvedores se envolvam em uma **revisão de código ágil e contínua** de contribuições antes que seu código seja integrado ao master. Equipes muito pequenas podem **cometer diretamente para o master**.
* Dependendo da frequência de release pretendida, pode haver **branches de release** que são brancheados do master em uma base just-in-time, são estabilizados antes de um release (sem que isso seja uma atividade de equipe), e **esses branches são deletados** algum tempo após o release. Como alternativa, também pode não haver ramos de lançamento se a equipe usando **branch principal pronto para release** e escolhendo uma estratégia de “correção futura” para correções de bugs. O branch principal pronto para release também é para equipes de alto rendimento.
* Os times devem se tornar adeptas da técnica de **branch por abstração** para mudanças mais longas e usar **feature flags** no desenvolvimento do dia a dia para permitir a proteção na ordem dos releases.
* O [Google faz o desenvolvimento Trunk-Based](/assets/2854146.pdf) e tem 35.000 desenvolvedores em um único branch principal monorepo.
* As pessoas que praticam o GitHub flow sentirão que isso é bastante semelhante.
* As pessoas que praticam o Git-flow acharão isso **muito diferente**.
