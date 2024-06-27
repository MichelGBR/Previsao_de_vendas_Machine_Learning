# 1 - Qual o número total de vendas por localidade?


SELECT Localidade , ROUND (SUM(Vendas),2) AS soma_de_vendas_por_estado
FROM df
GROUP BY Localidade
ORDER BY soma_de_vendas_por_estado DESC
LIMIT 10;