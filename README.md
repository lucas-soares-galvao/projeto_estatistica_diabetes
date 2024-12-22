# Análise Estatística de Base de Dados de Diabetes

Diabetes é uma doença crônica grave na qual os indivíduos perdem a capacidade de regular efetivamente os níveis de glicose no sangue, o que pode levar a uma redução na qualidade de vida e na expectativa de vida.

Este projeto tem como objetivo realizar uma análise estatística detalhada de um conjunto de dados relacionado a diabetes, utilizando técnicas de visualização de dados e análise exploratória para identificar padrões e insights relevantes.

## Fonte dos Dados

O Sistema de Vigilância de Fatores de Risco Comportamentais (BRFSS) é uma pesquisa telefônica relacionada à saúde, coletada anualmente pelo CDC (Centro de Controle e Prevenção de Doenças dos Estados Unidos). A cada ano, a pesquisa coleta respostas de milhares de americanos sobre comportamentos de risco relacionados à saúde, condições crônicas de saúde e o uso de serviços preventivos. Para este projeto, foi utilizado o conjunto de dados disponível no Kaggle para o ano de 2015.

[Link para o conjunto de dados no Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

![imagem](imagens/diabetes.jpg)

## Organização do Projeto

```
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto (MIT)
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── notebooks          <- Jupyter Notebooks.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── estatística.py  <- Funções criadas especificamente para este projeto
|
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
├── imagens         <- Imagens utilizada no projeto
```


## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/projeto_estatistica_diabetes.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd projeto_estatistica_diabetes
    ```

3. Crie o ambiente Conda a partir do arquivo [ambiente.yml](http://_vscodecontentref_/2):
    ```bash
    conda env create -f ambiente.yml
    ```

4. Ative o ambiente:
    ```bash
    conda activate projeto_diabetes
    ```

## Objetivos do Projeto

- Realizar uma análise exploratória dos dados (EDA) para entender a distribuição e as relações entre as variáveis.
- Visualizar os dados utilizando bibliotecas como Matplotlib e Seaborn.
- Identificar padrões e insights relevantes que possam ajudar na compreensão dos fatores de risco associados ao diabetes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](http://_vscodecontentref_/3) para mais detalhes.
