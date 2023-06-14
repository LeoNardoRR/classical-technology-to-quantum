import mysql.connector
import bcrypt
#import base64, os
#from Crypto import Cipher;
#from Crypto.PublicKey import RSA
#from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

#O bcrypt é uma função de hash e algoritmo de criptografia usado para armazenar senhas de forma segura. 
#Ele foi projetado para ser lento e resistente a ataques de força bruta, o que o torna uma escolha popular para o armazenamento 
#seguro de senhas.

# Estabelece a conexão com o banco de dados MySQL
con = mysql.connector.connect(
    host='localhost',
    database='md5',
    user='root',
    password='123456'
)

# Crie um cursor
cursor = con.cursor()

def draw_game_screen():
    # Limpa a tela
    # Desenha o título do jogo

    print("=== Computação quantica ===")
    print("----------------\n")
    
    # Desenha a área do jogo
    print("   AQUI TEREMOS UM TESTE DE CRITORGRIFIA USANDO VARIAS LINGUANGES E BIBLIOTECAS \n")


    print("----------------\n")

# Chamada da função para exibir a tela do jogo
draw_game_screen()

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
    print("   AQUI INSERIMOS O NOVO CAMPO COM A SENHA CRIPTOGRADAFA: \n")


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
con.commit()

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

print("----------------\n")
    
    # Desenha a área do jogo
print("   AQUI SUA SENHA CRIPTOGRAFADA FOI GERADA! \n")


print("----------------\n")

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
con.close()

# 3. Verificar se foi bem sucedido 
#E também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
#MD5

#RSA

#import base64, os
#from Crypto import Cipher;
#from Crypto.PublicKey import RSA
#from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
#Algoritmos do RSA

#from Crypto.Cipher import PKCS1_OAEP;
#from Crypto.PublicKey import RSA
#from Crypto.Cipher import PKCS1_OAEP

#class RsaHelper():
#    def __init__(self, path_to_pem=None, name_file_pem="bot.pem", create_private=False):
#        if path_to_pem == None:
#            path_to_pem = os.path.expanduser("~");
        
#        if not os.path.exists(path_to_pem):
#            os.makedirs(path_to_pem);
        
#        if not os.path.exists(path_to_pem + "/.ssh"):
#            os.makedirs(path_to_pem + "/.ssh");

#        self.path_to_private = path_to_pem + "/.ssh/private_" + name_file_pem;
#        self.path_to_public  = path_to_pem + "/.ssh/public_"  + name_file_pem;
#        self.key_pub = None; self.key_priv = None;
#        if not os.path.exists(self.path_to_private) and create_private == True:
#            self.key_priv = RSA.generate(1024);
#            self.key_pub = self.key_priv.publickey();
#            if not os.path.exists(self.path_to_private):
#                with open (self.path_to_private, "bw") as prv_file:
#                    prv_file.write(self.key_priv.exportKey());
#            if not os.path.exists(self.path_to_public):
#                with open (self.path_to_public, "bw") as pub_file:
#                    pub_file.write(self.key_pub.exportKey());
#        else:
#            if os.path.exists(self.path_to_public):
#                with open(self.path_to_public, "rb") as k:
#                    self.key_pub = RSA.importKey(k.read());
#            if os.path.exists(self.path_to_private):
#                with open(self.path_to_private, "rb") as k:
#                    self.key_priv = RSA.importKey(k.read());
#    def encrypt(self, data):
#        cipher = Cipher_PKCS1_v1_5.new(self.key_pub);
        #cipher = PKCS1_OAEP.new(self.key_pub);
#        return base64.b64encode( cipher.encrypt(data.encode()) ).decode();
#    def encryptAll(self, data):
#        cipher = Cipher_PKCS1_v1_5.new(self.key_pub);
        #cipher = PKCS1_OAEP.new(self.key_pub);
#        count_cript = 0;
#        result = [];
#        while count_cript + 100 < len(data):
#            result.append(base64.b64encode( cipher.encrypt(data[count_cript:count_cript + 100].encode()) ).decode());
#            count_cript += 100;
#        return result;
#    def decrypt(self, data):
#        decipher = Cipher_PKCS1_v1_5.new(self.key_priv);
        #decipher = PKCS1_OAEP.new(self.key_priv);
#        return decipher.decrypt(    base64.b64decode( data.encode()   ) , None).decode();
#    def decryptArray(self, array):
#        decipher = Cipher_PKCS1_v1_5.new(self.key_priv);
        #decipher = PKCS1_OAEP.new(self.key_priv);
#        result = "";
#        for item in array:
#            result += decipher.decrypt(    base64.b64decode( item.encode()   ) , None).decode();
#        return result;

#r = RsaHelper(path_to_pem="/tmp/" ,name_file_pem="botafogodotextor.pem", create_private=True);
#texto = "Botafogo campeão, será!!!! Deus salve Textor";
#criptografado = r.encrypt(texto);
#descriptografado = r.decrypt(criptografado);
#print(texto);
#print(criptografado);
#print(descriptografado);

#O código fornecido implementa uma classe chamada RsaHelper que ajuda a criptografar e descriptografar dados usando o algoritmo RSA. 
# Vou explicar brevemente o que cada método faz:
#__init__: O construtor da classe que inicializa os caminhos para os arquivos de chave pública e privada. 
# Se create_private for definido como True e a chave privada não existir, uma nova chave privada será gerada e salva em um arquivo.
# A chave pública correspondente também será salva em um arquivo.
#encrypt: Recebe um dado como entrada e criptografa usando a chave pública. O dado é convertido para bytes, criptografado e, 
#em seguida, retornado como uma string base64 codificada.
#encryptAll: Semelhante ao método encrypt, mas é usado quando o dado é muito longo e precisa ser dividido em blocos menores. 
#O dado é dividido em blocos de 100 caracteres (assumindo que é uma string) e cada bloco é criptografado separadamente. Os blocos criptografados são armazenados em uma lista e retornados.
#decrypt: Recebe um dado criptografado como entrada e descriptografa usando a chave privada correspondente. 
#O dado é decodificado a partir da codificação base64, descriptografado e retornado como uma string.
#decryptArray: Semelhante ao método decrypt, mas é usado quando o dado criptografado foi dividido em blocos menores usando o 
#método encryptAll. Cada bloco é descriptografado individualmente e concatenado para formar o dado original descriptografado.
#Em seguida, o código cria uma instância da classe RsaHelper com um caminho para os arquivos de chave personalizados e define 
#create_private como True. Em seguida, ele criptografa uma mensagem de texto usando o método encrypt, imprime o texto original, 
#o texto criptografado e, em seguida, descriptografa o texto criptografado usando o método decrypt e imprime o resultado descriptografado.
#No final, você terá a saída do texto original, texto criptografado e texto descriptografado.









# POR ULTIMO ---- (e tentar distinguir a diferença de velocidade)
