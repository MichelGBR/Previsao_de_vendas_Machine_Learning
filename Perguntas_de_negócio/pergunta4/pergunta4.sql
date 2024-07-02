# 4 - Quantos mercados estão abaixo da média em marketing por localidade? 

SELECT localidade, COUNT (investimento_em_marketing) AS qtd_abaixo_da_media
FROM newdf
WHERE investimento_em_marketing <16
GROUP BY localidade
ORDER BY qtd_abaixo_da_media DESC
LIMIT 1000;