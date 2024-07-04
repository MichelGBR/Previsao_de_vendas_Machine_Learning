# 8 - Quais os estados com mercados "pequenos" têm o investimento maior que a média? 

SELECT estado, COUNT (investimento_em_marketing) AS qntd_maior_que_a_media
FROM newdf
WHERE investimento_em_marketing >16 AND tamanho_do_mercado = "Pequeno"
GROUP BY estado
ORDER BY qntd_maior_que_a_media DESC
LIMIT 1000;