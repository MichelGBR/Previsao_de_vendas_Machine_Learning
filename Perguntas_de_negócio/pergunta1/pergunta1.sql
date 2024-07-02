# 6 - Quantos mercados estão abaixo da média de vendas por localidade? 
SELECT localidade, ROUND (SUM(vendas),2) AS qtd_total_de_vendas
FROM newdf
GROUP BY localidade
ORDER BY qtd_total_de_vendas DESC
LIMIT 1000;