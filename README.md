# BugClassifier AI

**Projeto de Machine Learning desenvolvido para classificar automaticamente descrições de bugs de software em três categorias: Autenticação, Interface e Pagamento.**

---

## Objetivo

Desenvolver um classificador de texto capaz de identificar a categoria mais provável de um problema relatado por um usuário e indicar quando a previsão deve passar por análise humana.

## Categorias

- **Autenticacao:** problemas relacionados a login, acesso, senha e autenticação.
- **Interface:** problemas visuais, layout, botões e navegação.
- **Pagamento:** problemas com cobranças, cartões, Pix, estornos e transações.

## Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Matplotlib
- Joblib

## Metodologia

O projeto utiliza um pipeline de Machine Learning composto por:

- **TF-IDF** para transformação das descrições em representações numéricas.
- **Logistic Regression** para classificação dos textos.
- Divisão dos dados em treinamento (80%) e teste (20%).
- Avaliação por acurácia, precision, recall, F1-score e matriz de confusão.

## Dataset

O conjunto de dados contém **150 descrições sintéticas**, distribuídas igualmente entre as três categorias.

Os exemplos foram elaborados manualmente para fins de estudo e desenvolvimento do projeto.

## Funcionalidade adicional

O classificador utiliza um limite de probabilidade definido em **70%** para indicar:

- Classificação automática.
- Necessidade de análise humana.

Esse limite é uma regra de encaminhamento definida no projeto, não uma garantia de confiança calibrada.

## Estrutura do projeto

- `BugClassifier_AI.ipynb`: notebook com desenvolvimento, treinamento e avaliação.
- `inference.py`: código para carregar e utilizar o modelo.
- `bug_classifier.joblib`: modelo treinado.
- `requirements.txt`: dependências do projeto.
- `README.md`: documentação.

## Limitações

O dataset é pequeno e sintético. Portanto, os resultados são experimentais e não representam necessariamente o desempenho em sistemas reais.

## Melhorias futuras

- Ampliar o dataset com descrições mais diversificadas.
- Trabalhar com dados reais anonimizados.
- Avaliar outros algoritmos de classificação.
- Melhorar o tratamento de descrições ambíguas.
- Desenvolver uma interface para utilização do classificador.

## Autora

**Projeto desenvolvido como parte dos estudos em Machine Learning e Inteligência Artificial.**
