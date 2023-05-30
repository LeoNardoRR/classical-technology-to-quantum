#import qsharp
import mysql.connector
import qsharp

from DbOperations import SayHello
#from DbOperations import QuantumDecrypt
#from DbOperations import register

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

from cryptography.fernet import Fernet

# geração de chave
key = Fernet.generate_key()

# string a chave em um arquivo
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# abrindo a chave
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# usando a chave gerada
fernet = Fernet(key)

# abrindo o arquivo original para criptografar
with open('nba.csv', 'rb') as file:
    original = file.read()

# criptografar o arquivo
encrypted = fernet.encrypt(original)

# abrir o arquivo no modo de gravação e
# gravar os dados criptografados
with open('nba.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# usando a chave
fernet = Fernet(key)

# abrindo o arquivo criptografado
with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()

# descriptografando o arquivo
decrypted = fernet.decrypt(encrypted)

# abrindo o arquivo no modo de gravação e
# gravando os dados descriptografados
with open('nba.csv', 'wb') as dec_file:
    dec_file.write(decrypted)

# 3. Verificar se foi bem sucedido e também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
# (e tentar distinguir a diferença de velocidade)
