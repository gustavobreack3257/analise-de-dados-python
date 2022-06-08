import pandas
import pandas as pd

dados = {
'nome' : 'Howard Ian Peter Jonah Kellie'.split(),
'cpf' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
'email' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
'idade' : [32, 22, 25, 29, 38]
}
df_dados = pd.DataFrame(dados)
df_uma_coluna = df_dados['idade']
print(type(df_uma_coluna))

print("média de idades:", df_uma_coluna.mean())

print(df_uma_coluna)

colunas = ['nome', 'cpf']
df_duas_coluna = df_dados[colunas]
print(type(df_duas_coluna))

print(df_duas_coluna)
