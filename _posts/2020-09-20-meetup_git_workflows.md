# Meetup Git Workflows

* TOC
{:toc}

## Branching

| ![](/images/series-commits.png) |
| :-------------------------------: |
|         **Branch e head**         |

* **Branching** é a duplicação de um objeto sob controle de versão (como um arquivo de código-fonte ou uma árvore de diretório)
* Nesse contexto os objetos são chamados de **branches**
* Cada branch pode ser modificado separadamente em paralelo de forma que os branches se tornam diferentes
* O branch de origem é chamada de *branch pai* ou *branch upstream*
* Um branch sem pai é chamada de *tronco* ou *branch principal*
* O branching implica na capacidade de posteriormente *mergear* ou *integrar* as mudanças para o branch pai
* **Conflito textual** × **conflito semântico**

| ![](/images/split-and-merge.png) |
| :--------------------------------: |
|        **Branch e merge**        |

### Vantagens de Branching

* Permite que partes do software sejam desenvolvidas em paralelo
* Facilita a manter vários releases em produção
* Permite que os desenvolvedores isolem as mudanças sem desestabilizar a base de código: novos features, correções para bugs, integração de versões

### Desvantagens de Branching

* Menor interação entre os membros do time
* Branchear é fácil, mergear é difícil
* Não há como criar um algoritmo para resolver conflitos automaticamente
* Muitos times gastam uma quantidade excessiva de tempo lidando com seu emaranhado de branches

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
*  No Git-flow, o branch principal é denominado `origin/develop`

| ![](/images/main-branch.png) |
| :----------------------------: |
|      **Branch principal**      |

### Branching por Feature

* **Um branch separado para cada feature**
* Tem origem no `develop`
* Pode ter qualquer nome que não comece com `release` ou `hotfix`
* Se estiver trabalhando nisso por um tempo: **mergeie o develop para o branch do feature**
* Continuar trabalhando nesse branch até **terminar o feature**
* **Integrar com o `develop`**
* Incompatível com integração contínua

| ![](/images/feature_integration.png) |
| :------------------------------------: |
|         **Branch de feature**          |

### Branches de Release

* Para estabilizar uma versão do produto pronto para produção
* Branches de release são cortados de um commit específico no `develop`
* Convenção de nomenclatura `release-v<n>.<m>`
* Apenas aceita commits de correções
* **Essas correções** devem ser **integradas ao `develop`**
* É muito comum negligenciar a integração das correções para o `develop`

| ![](/images/release-branch.png) |
| :-------------------------------: |
|       **Branch de release**       |

* Algumas pessoas preferem a criação dessas correções no `develop` ([como Google](/assets/2854146.pdf))
* Depois os **cherry-pickar** no branch de release
* Muitos times acham difícil fazer isso
* Pode ser necessário retrabalhar as correções cherry-pickadas no branch de release

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
* Os **features** são **integrados [squashados](https://softwareengineering.stackexchange.com/questions/263164/why-squash-git-commits-for-pull-requests) diretamente no `master`**  de forma a manter um **histórico linear**
* Os releases e hotfixes são feitos de forma semelhante ao Git-flow

### Vantagens de Oneflow

* O histórico do Git será mais limpo, menos confuso, mais legível
* O histórico de commits é a **história de como o projeto foi feito**
* O **branch de feature** é **passado a limpo** e **integrado diretamente no `master`**

### Desvantagens de Oneflow

* Usa comandos avançados para rescrita do histórico
* Inadequado para projetos que usam integração continua

## GitHub Flow

Criado por [Scott Chacon em 2011](http://scottchacon.com/2011/08/31/github-flow.html).

* Única versão em produção
* **Branch principal pronto para release**
* Branches de releases não são necessários
* Branches de hotfix não são necessários
* **Branches de feature de vida curta (máximo 2 semanas)**
* GitHub flow chama seu branch principal `origin/master`

### Branch Principal Pronto para Release

* Manter o  **branch `master`** suficientemente **saudável** para que o head do `master` possa sempre ser colocado diretamente em produção
* **Delivery contínuo** × **Deploymento contínuo**   

|   ![](/images/mainline-release.png)    |
| :--------------------------------------: |
| **Branch principal pronto para release** |

### Branches de Feature de Vida Curta (máximo duas semanas)

* O estudo do [Relatório State Of DevOps](/assets/2016-State-of-DevOps-Report.pdf) indicou que as equipes de desenvolvimento de elite integram com mais frequência do que as de baixo desempenho
* Aumenta a frequência de merges, mas reduz sua complexidade e risco
* Alerta as equipes sobre conflitos com muito mais rapidez
* Aumenta a interação entre os membros do time

### Integração Contínua

* Os desenvolvedores fazem a integração do branch principal assim que têm um **commit saudável**
* **Não há expectativa de** que o **feature** esteja **completo**
* **O branch deve durar no máximo dois dias**
* O time deve ficar adepta com as técnicas **branch por abstração** para mudanças mais longas e usar **feature flags** no desenvolvimento do dia a dia para permitir a proteção do escopo dos releases

| ![](/images/continuous_integration.png) |
| :---------------------------------------: |
|     **Continuous Delivery em GitHub**     |

#### Branching por Feature × Integração Contínua

#### Branching por Feature

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
* O [Google faz o desenvolvimento Trunk-Based](/assets/2854146.pdf) e tem 35.000 desenvolvedores em um único branch principal monorepo.
* As pessoas que praticam o GitHub flow sentirão que isso é bastante semelhante.
* As pessoas que praticam o Git-flow acharão isso **muito diferente**.
