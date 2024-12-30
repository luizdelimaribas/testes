import pyodbc
#definindo as informaçoes da conexao
dados_conexao=(
    "Driver={SQL Server};"
    "Server=DESKTOP-3R513B3\SQLEXPRESS;"
    "Database=biblioteca;"
    )

#conectando ao banco de dados
conex=pyodbc.connect(dados_conexao)

#para fericar se foi feita a conexao
print("conexao feita")

#cursor= e aquilo que executa os comando no sql
cursor=conex.cursor()

#para uma consulta
cursor.execute('select* from Autor')

rows=cursor.fetchall()

for row in rows:
    print(row)
