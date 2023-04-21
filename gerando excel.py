import pandas as pd

#criando tabela
animais = {'Animais':['Rato','gato','cavalo'],
           'Grupo':['Roedor','Felino','Ungulado'],
           'Tamanho':['Pequeno','Médio','Grande'],}

#criando arquivo xlxs
dataframe = pd.DataFrame(animais)
dataframe.to_excel('./animais.xlsx')