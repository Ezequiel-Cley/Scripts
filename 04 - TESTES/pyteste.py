import mysql.connector

conexao = mysql.connector.connect(
  host='localhost',
  user='BD_LOCAL',
  password='1234',
  database='world'
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM city")

resultados = cursor.fetchall()

print(res ultados)