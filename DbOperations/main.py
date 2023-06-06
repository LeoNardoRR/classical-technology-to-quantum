import mysql.connector
import bcrypt

# Estabelece a conexão com o banco de dados MySQL
con = mysql.connector.connect(
    host='localhost',
    database='md5',
    user='root',
    password='123456'
)

# Crie um cursor
cursor = con.cursor()

# Solicitar que a pessoa digite seu usuário
login = input("Digite seu login: ")

# Verificar se o usuário existe no banco de dados
query = "SELECT * FROM ic WHERE login = %s"
cursor.execute(query, (login,))

# Recupere todos os registros retornados pela consulta
rows = cursor.fetchall()

# Verificar se algum registro foi encontrado
if len(rows) > 0:
    # Percorra os registros e imprima os resultados
    for row in rows:
        print(row)
else:
    print("Login não encontrado.")

# Inserir um novo campo criptografado
alter_query = "ALTER TABLE ic ADD COLUMN campo_criptografado VARCHAR(255)"
con.commit()

# Solicitar que a pessoa digite o login novamente
login = input("Digite seu login novamente: ")

# Valor original
login_original = login

# Criptografar o valor
login_criptografado = bcrypt.hashpw(login_original.encode('utf-8'), bcrypt.gensalt())

# Inserir o valor criptografado na tabela
update_query = "UPDATE ic SET campo_criptografado = %s WHERE login = %s"
cursor.execute(update_query, (login_criptografado, login))
con.commit()

# Verificar a alteração no banco de dados
select_query = "SELECT * FROM ic WHERE login = %s"
cursor.execute(select_query, (login,))
updated_rows = cursor.fetchall()

# Imprimir os resultados
if len(updated_rows) > 0:
    for row in updated_rows:
        print(row)
else:
    print("Não foi possível encontrar o login atualizado.")

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
con.close()

# 3. Verificar se foi bem sucedido e também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
# (e tentar distinguir a diferença de velocidade)
