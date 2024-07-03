# 6 - Quantos mercados estão abaixo da média de vendas por localidade? 

SELECT localidade, COUNT (vendas) AS qtd_abaixo_da_media
FROM newdf
WHERE vendas <124
GROUP BY localidade
ORDER BY qtd_abaixo_da_media DESC
LIMIT 1000;