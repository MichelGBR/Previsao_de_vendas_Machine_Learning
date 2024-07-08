<img width=100% bottom=50px src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/7d82cf60-19b9-46b7-a92c-ca5eaf9e16e1"/>
<br>
<br> 

# Sobre o projeto :

Este projeto tem como objetivo principal explorar os diversos processos da Data Science, com foco em análise, limpeza e visualização de dados, aplicação de estatística descritiva e implementação de técnicas de Machine Learning para previsão de valores.

<div align="left" > 

# Contexto :

### ⚠️​ ​Problema:

Um dono de mercado deseja estimar o potencial de vendas em função do investimento em estratégias de marketing. Através da análise de dados, buscamos prever o impacto das ações de marketing sobre as vendas e identificar oportunidades de otimização.

### ​🧩​ Objetivo:

Desenvolver um modelo preditivo: Construir um modelo de Machine Learning para estimar as vendas em diferentes cenários de investimento em marketing.
Quantificar o retorno do investimento: Analisar o retorno sobre investimento (ROI) das estratégias de marketing para auxiliar na tomada de decisões estratégicas.
Otimizar a alocação de recursos: Identificar os níveis de investimento em marketing que maximizam o lucro ou outros indicadores de negócio relevantes.
Metodologia:

• Análise Exploratória de Dados: Explorar e compreender o conjunto de dados, identificando padrões, tendências e relações entre as variáveis.

• Pré-processamento de Dados: Limpar e preparar os dados para a modelagem, tratando dados ausentes, inconsistentes e outliers.

• Desenvolvimento do Modelo: Treinar e avaliar diferentes modelos de Machine Learning para estimar as vendas.

• Seleção do Melhor Modelo: Selecionar o modelo com o melhor desempenho em termos de precisão e generalização.

• Interpretação e Validação do Modelo: Analisar os resultados do modelo, interpretando os coeficientes e validando a sua precisão em um conjunto de dados de teste.

• Previsão de Vendas: Utilizar o modelo final para estimar as vendas em diferentes cenários de investimento em marketing.

### ​​✅​ Resultados Esperados:

Modelo preditivo preciso: Um modelo de Machine Learning capaz de estimar as vendas com alta confiabilidade.
Insights acionáveis: Informações valiosas sobre o impacto das estratégias de marketing nas vendas.
Recomendações otimizadas: Recomendações sobre os níveis de investimento em marketing que maximizam o lucro ou outros indicadores de negócio relevantes.



# Habilidades utilizadas  :

<img align="left" height="90" width="80" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/af05ac55-bf57-4bd0-8435-55c9a02dcc95">

<img align="left"  height="80" width="80" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/bf54642d-44a1-4f8a-946c-1bc939033b01">

<img align="left"  height="120" width="120" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/b6bcbd47-226d-4b3a-ad09-dc60ed316cdf">

<img align="left"  height="80" width="80" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/0de88fa5-9696-4012-bc9c-22a7e60bd0bd">

<br>
<br> 
<br>
<br> 



### Python:

O Python desempenhou um papel crucial em todas as etapas deste projeto (será explicado o passo a passo), desde a limpeza de dados até a construção e avaliação do modelo de Machine Learning.


• Limpeza de Dados:

Foi utilizado para manipular e pré-processar os dados, garantindo sua qualidade e consistência para a modelagem.
Tarefas como tratamento de dados faltantes, outliers e inconsistências foram realizadas com eficiência utilizando bibliotecas como Pandas e NumPy.
A exploração e visualização dos dados também foram feitas com ferramentas em Python, permitindo um melhor entendimento das características e relações entre as variáveis.

• Construção do Modelo de Machine Learning:

Ele também foi a linguagem de escolha para o desenvolvimento e implementação do modelo de Machine Learning.
Biblioteca como a scikit-learn forneceu uma ferramenta robusta e flexível para construir, treinar e avaliar o meu modelo de aprendizado.

• Visualização de Dados:

Além de bibliotecas para tratamento de dados, também utilizamos a Matplotilib e Seaborn para reprodução de gráficos essenciais.

### MySQL e Big Query:

O MySQL foi essencial para a consulta de nossos dados, gerando respostas para as "perguntas de negócio" e insights valiosos para a tomada de decisões.
Além disso, é importante destacar a funcionalidade do BigQuery, oferecida pelo Google, que demonstra minhas habilidades em nuvem. 

### Power BI: 

O Power BI se consolidou como uma ferramenta indispensável neste projeto, transformando dados em conhecimento e conhecimento em ação. Sua capacidade de visualizar dados de forma clara, comunicar insights de maneira eficaz e embasar decisões estratégicas foi crucial para o sucesso da equipe de marketing.

<img align="center"  height="600" width="1000" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/12a6c061-f88e-49ec-880b-8023a4ce8119">


### Link: https://app.powerbi.com/reportEmbed?reportId=47e2c18d-484c-4544-8c08-658e12114599&autoAuth=true&ctid=7c2e74a5-a214-4066-ae86-eac16c2f75dd

<div align="left" > 

# Etapas do Python no projeto:

• Resolvi fazer este tópico para melhor entendimento do que fiz nos códigos.

### 1 - Tradução:

Achei necessário fazer esse processo pois permitia melhor compreensão daquele que está visualizando o código. Desse modo, usei a função "replace" para substituir as palavras nas linhas e a "rename" foi responsável por traduzir palavras das colunas.

<img align="center"  height="450" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/e41eb121-5abc-42ae-8471-75228ad843b2">

### Dados traduzidos :

<img align="center"  height="350" width="1000" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/802a1174-96e7-4941-a1b4-26a5d9c3ddab">

### 2 - Verificando se há valores NaN :

<img align="center"  height="350" width="500" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/7581d8aa-2dda-449d-b71f-546dfcce68c9">

### 3 - Ajustando as datas :

As datas estavam definidas como "object", é melhor transformar ela para "date_time" e assim ter melhor entendimento.

<img align="center"  height="350" width="700" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/b57b6896-87c9-47a2-9cc0-05f2e1e40b64">

### 4 - Box-plot


Verificando a quantidade de outliers para melhorar a taxa de acertividade de nosso Machine Learning.

<img align="center"  height="800" width="2700" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/5bbb7e90-32f0-4c50-938d-237eb8f25f92">

<br>
Processo de limpeza dos box-plots "vendas" e "lucros", após verificar os valores abaixo da linha de outliers:

<img align="center"  height="1050" width="900" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/92bb3629-9413-49b0-86f2-1c6feafbaac8">


### Box-plot de "investimento em marketing" limpo:

<img align="center"  height="750" width="700" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/87fdb650-3480-4c88-b7ef-2376b8085a18">

### 5 - Correlação das colunas:

Analisando o quanto as variáveis tem significado entre elas, no qual vemos que o investimento em mkt e vendas andam bem alinhadas (perto do 1), um fator positico para nosso futuro modelo ter maior acertividade.

<img align="center"  height="550" width="900" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/2bd31e0c-7c58-478d-80e5-29b0450ddf3f">

### Correlação por meio de um mapa de calor:

<img align="center"  height="700" width="600" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/bd218035-4239-4621-834e-b6a7d1b89701">

# 6 - Início envolvendo Machine Learning:

Etapa inicial para definir quem será o meu x (investimento em mkt) e y (vendas), temos que fazer alguns ajustes com o Numpy (np) e reshape, pois o modelo espera recebe-los dessa forma. 

<img align="center"  height="350" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/0cb64434-215d-4f2f-839f-f5b302a2e514">

### Gráfico de dispersão:

Importante ver o quanto essas duas caminham e se sua direção é positiva ou negativa.

<img align="center"  height="850" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/512542a0-4c2b-4ca7-969a-7a931f4d53f4">

### Utilizando a regressão linear para nos mostrar o desfecho positivo ou negativo após fazermos um treinamento:

Foi observado que é positivo, então temos um modelo com uma taxa de acertividade boa e que a tendência é se manter positiva sempre aumentando o seu valor pela variável x, quanto maior ela, maior o y.

<img align="center"  height="950" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/a6c9dc1d-18e2-424a-9df4-5b4b2e7f47ad">

# 7 - Modelo de previsão de Machine Learning:

Depois de todo o processo já feito, é o momento de botarmos o modelo em prática para obter respostas. A nossa pergunta será: "Se eu investir x em marketing, o quanto de vendas eu terei?"
OBS: A moeda pode ser considerada dólar.

<img align="center"  height="250" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/ac29f810-7f99-4454-a7ab-b6fcfb6d3a54">

### Outros exemplos:

<img align="center"  height="950" width="800" src="https://github.com/MichelGBR/Previsao_de_vendas_Machine_Learning/assets/169415705/2be681a8-935e-48d3-a12d-eba09bc9cb7b">







