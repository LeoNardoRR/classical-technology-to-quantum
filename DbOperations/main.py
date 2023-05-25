#import qsharp
import mysql.connector
#from DbOperations import SayHello

#print(SayHello.simulate(name="Leonardo Ribeiro"))

# 1. Trazer os usuários (SELECT)
# Estabelece a conexão com o banco de dados MySQL
con = mysql.connector.connect(
    host='localhost',
    database='aes',
    user='root',
    password='123456'
)

if con.is_connected():
    cursor = con.cursor()
    
    # Executa a consulta SELECT
    cursor.execute("SELECT * FROM ic WHERE ano=1994")
    
    # Obtém todos os registros da consulta
    rows = cursor.fetchall()
    
    # Itera sobre os registros e exibe os resultados
    for row in rows:
        print(row)
    
    cursor.close()
    con.close()

# 2. Pegar para cada um desses um usuários e tentar realizar a descriptografia da sua senha
# usando o código quantico que vai ser criado no Q# (DbOperations.BreakPassword('123456'))
# 3. Verificar se foi bem sucedido e também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
# (e tentar distinguir a diferença de velocidade)
