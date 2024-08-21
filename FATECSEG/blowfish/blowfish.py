import mysql.connector
import bcrypt
import time
import hashlib


#O bcrypt é uma função de hash e algoritmo de criptografia usado para armazenar senhas de forma segura. 
#Ele foi projetado para ser lento e resistente a ataques de força bruta, o que o torna uma escolha popular para o armazenamento 
#seguro de senhas.

# Estabelece a conexão com o banco de dados MySQL
con = mysql.connector.connect(
    host='localhost',
    database='md5',
    user='root',
    password='123456',
    Teste = '0192'
)

# Crie um cursor
cursor = con.cursor()

def tela():
    # Limpa a tela

    print("=== Computação quantica ===")
    print("----------------\n")
    
    # Desenha o titulo
    print("   AQUI TEREMOS UM TESTE DE CRIPTOGRAFIA \n")


    print("----------------\n")

# Chamada da função para exibir a tela
tela()

# Solicitar que o usuário digite seu nome, idade, login e senha
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))  # Converter para inteiro
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# Excluir a tabela 'usuarios' se ela existir
cursor.execute("DROP TABLE IF EXISTS usuarios")

# Definir o comando SQL para criar a tabela
comando_sql = '''CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                idade INT,
                login VARCHAR(50) NOT NULL,
                senha VARCHAR(50) NOT NULL,
                senha_criptografado VARCHAR(255) DEFAULT ''
                )'''

cursor.execute(comando_sql)

# Definir o comando SQL para inserir o usuário e senha na tabela
comando_sql = "INSERT INTO usuarios (nome, idade, login, senha) VALUES (%s, %s, %s, %s)"
valores = (nome, idade, login, senha)

try:
    # Executar o comando SQL para inserir os valores na tabela
    cursor.execute(comando_sql, valores)

    # Verificar se o registro foi inserido com sucesso
    if cursor.lastrowid > 0:
        print("Registro inserido com sucesso.")
    else:
        print("Falha ao inserir o registro.")

    # Salvar as alterações no banco de dados
    con.commit()

    print("----------------\n")
    
    # Desenha a área do jogo
    print("   AQUI INSERIMOS O NOVO CAMPO COM A SENHA CRIPTOGRAFADA: \n")


    print("----------------\n")

except mysql.connector.Error as erro:
    print("Erro ao inserir o registro:", erro)

# Verificar se o usuário existe no banco de dados
query = "SELECT * FROM usuarios WHERE senha = %s"
cursor.execute(query, (senha,))

# Recupere o registro retornado pela consulta
row = cursor.fetchone()

#O método fetchone() é usado em programação para recuperar a próxima linha de um conjunto de resultados de uma consulta SQL. 
#Geralmente, é usado em conjunto com uma instrução de consulta executada em um banco de dados.

# Inserir um novo campo criptografado
comando_sql = "ALTER TABLE usuarios ADD campo_criptografado VARCHAR(255)"

# Solicitar que a pessoa digite o senha novamente
senha = input("Digite sua senha novamente: ")

# Criptografar o valor
senha_criptografado = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

# Inserir o valor criptografado na tabela
update_query = "UPDATE usuarios SET senha_criptografado = %s WHERE senha = %s"
cursor.execute(update_query, (senha_criptografado, senha))
con.commit()

# Verificar a alteração no banco de dados
select_query = "SELECT * FROM usuarios WHERE senha = %s"
cursor.execute(select_query, (senha,))
updated_rows = cursor.fetchall()

#O método fetchall() é usado em programação para recuperar todas as linhas restantes de um conjunto de resultados de uma consulta SQL. 
# Ele é frequentemente utilizado em conjunto com uma instrução de consulta executada em um banco de dados.

# Imprimir os resultados
if len(updated_rows) > 0:
    for alter in updated_rows:
        print(alter)
else:
    print("Não foi possível encontrar o senha atualizado.")
    exit()
print("----------------\n")
    
    # Desenha a área do jogo
print("   AQUI SUA SENHA CRIPTOGRAFADA FOI GERADA! \n")


print("----------------\n")

senha_hash_bd = row[5]  # Assumindo que a coluna 'senha_criptografado' está na posição 5 do resultado da consulta

# Registrar o tempo de início
inicio = time.time()

# Exibir o hash gerado
print("senha_criptografado:", senha_criptografado.decode())

# Converter senha_criptografado para string
senha_criptografado_str = senha_criptografado.decode('utf-8')

# Hash 1
senha_criptografado = hashlib.sha256(b"senha123").hexdigest()

# Hash 2
senha_criptografado = hashlib.sha256(b"senha456").hexdigest()

# Comparar os hashes
if senha_criptografado != senha_hash_bd:
    print("Os hashes são iguais, a senha esta correta!.")
else:
    print("Os hashes são diferentes, a senha esta incorreta.")

#Calcular tempo de execução do comando
#def calcular_tempo_execucao(checkpw):
#    inicio = time.time()
    # Executar o comando
#    exec(checkpw)
#    fim = time.time()
#    tempo_execucao = fim - inicio
#    return tempo_execucao

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
con.close()

# Registrar o tempo de término
fim = time.time()

# Calcular o tempo de execução
tempo_execucao = fim - inicio

print("Tempo de execução:", tempo_execucao, "segundos")

# 3. Verificar se foi bem sucedido 
#E também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
#MD5

# POR ULTIMO ---- (e tentar distinguir a diferença de velocidade)
