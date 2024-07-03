 #7 - Quais os estados que tem mais mercados com investimento em mkt maior que a sua média? 
SELECT estado, COUNT (DISTINCT investimento_em_marketing) AS invest_maior_que_media
FROM newdf 
WHERE investimento_em_marketing >16
GROUP BY estado
ORDER BY invest_maior_que_media DESC
LIMIT 1000