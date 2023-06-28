#!/usr/bin/python3
# /opt/borg/api/rsahelper.py
# Código do projeto BORG


#RSA

import base64, os
from Crypto import Cipher;
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
#Algoritmos do RSA

from Crypto.Cipher import PKCS1_OAEP;
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RsaHelper():
    def __init__(self, path_to_pem=None, name_file_pem="bot.pem", create_private=False):
        if path_to_pem == None:
            path_to_pem = os.path.expanduser("~");
        
        if not os.path.exists(path_to_pem):
            os.makedirs(path_to_pem);
        
        if not os.path.exists(path_to_pem + "/.ssh"):
            os.makedirs(path_to_pem + "/.ssh");

        self.path_to_private = path_to_pem + "/.ssh/private_" + name_file_pem;
        self.key_pub = None; self.key_priv = None;
        if not os.path.exists(self.path_to_private) and create_private == True:
            self.key_priv = RSA.generate(1024);
            self.key_pub = self.key_priv.publickey();
            if not os.path.exists(self.path_to_private):
                with open (self.path_to_private, "bw") as prv_file:
                    prv_file.write(self.key_priv.exportKey());
            if not os.path.exists(self.path_to_public):
                with open (self.path_to_public, "bw") as pub_file:
                    pub_file.write(self.key_pub.exportKey());
        else:
            if os.path.exists(self.path_to_public):
                with open(self.path_to_public, "rb") as k:
                    self.key_pub = RSA.importKey(k.read());
            if os.path.exists(self.path_to_private):
                with open(self.path_to_private, "rb") as k:
                    self.key_priv = RSA.importKey(k.read());
    def encrypt(self, data):
        cipher = Cipher_PKCS1_v1_5.new(self.key_pub);
        cipher = PKCS1_OAEP.new(self.key_pub);
        return base64.b64encode( cipher.encrypt(data.encode()) ).decode();
    def encryptAll(self, data):
        cipher = Cipher_PKCS1_v1_5.new(self.key_pub);
        cipher = PKCS1_OAEP.new(self.key_pub);
        count_cript = 0;
        result = [];
        while count_cript + 100 < len(data):
            result.append(base64.b64encode( cipher.encrypt(data[count_cript:count_cript + 100].encode()) ).decode());
            count_cript += 100;
        return result;
    def decrypt(self, data):
        decipher = Cipher_PKCS1_v1_5.new(self.key_priv);
        decipher = PKCS1_OAEP.new(self.key_priv);
        return decipher.decrypt(    base64.b64decode( data.encode()   ) , None).decode();
    def decryptArray(self, array):
        decipher = Cipher_PKCS1_v1_5.new(self.key_priv);
        decipher = PKCS1_OAEP.new(self.key_priv);
        result = "";
        for item in array:
            result += decipher.decrypt(    base64.b64decode( item.encode()   ) , None).decode();
        return result;

r = RsaHelper(path_to_pem="/tmp/" ,name_file_pem="botafogodotextor.pem", create_private=True);
texto = "Botafogo campeão, será!!!! Deus salve Textor";

criptografado = r.encrypt(texto);

descriptografado = r.decrypt(criptografado);

print(texto);
print(criptografado);
print(descriptografado);

#O código fornecido implementa uma classe chamada RsaHelper que ajuda a criptografar e descriptografar dados usando o algoritmo RSA. 
# Vou explicar brevemente o que cada método faz:
#__init__: O construtor da classe que inicializa os caminhos para os arquivos de chave pública e privada. 
# Se create_private for definido como True e a chave privada não existir, uma nova chave privada será gerada e 
# salva em um arquivo.
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

