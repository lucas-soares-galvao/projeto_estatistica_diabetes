# Análise estatística de base de dados de diabetes

Diabetes é uma doença crônica grave na qual os indivíduos perdem a capacidade de regular efetivamente os níveis de glicose no sangue e pode levar a uma redução na qualidade de vida e na expectativa de vida.

O Sistema de Vigilância de Fatores de Risco Comportamentais (BRFSS) é uma pesquisa telefônica relacionada à saúde que é coletada anualmente pelo CDC (Centro de Controle e Prevenção de Doenças dos Estados Unidos). A cada ano, a pesquisa coleta respostas de milhares de americanos sobre comportamentos de risco relacionados à saúde, condições crônicas de saúde e o uso de serviços preventivos. Para este projeto, foi utilizado conjunto de dados disponível no Kaggle para o ano de 2015. 

https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

![imagem](imagens/diabetes.jpg)

## Organização do projeto

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

## Configuração do ambiente

1. Faça o clone do repositório.

    ```bash
    git clone git@github.com:lucas-soares-galvao/projeto_estatistica_diabetes.git
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o `conda`.

    ```bash
    conda env create -f ambiente.yml --name estatistica
    ```

## Um pouco mais sobre a base

[Clique aqui](referencias/01_dicionario_de_dados.md) para ver o dicionário de dados da base utilizada.
