""" abrindo arquivos do excel"""

import pandas as pd
dados = pd.read_csv('C:/Users/marce/ansel/Desktop/cod/athlete_events.csv') 
"""quando for excel = pd.read_excel
quando csv = pd.read_csv"""

print(dados.head(40))

 