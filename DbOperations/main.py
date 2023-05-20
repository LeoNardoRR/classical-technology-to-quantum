import qsharp
from DbOperations import SayHello

print(SayHello.simulate(name="Leonardo Ribeiro"))

# 1. Trazer os usuários (SELECT)
# 2. Pegar para cada um desses um usuários e tentar realizar a descriptografia da sua senha
# usando o código quantico que vai ser criado no Q# (DbOperations.BreakPassword('123456'))
# 3. Verificar se foi bem sucedido e também quanto tempo levou
# 4. Trocar a senha por um algortimo ruim (MD5) e depois tentar usar uma senha boa (RSA)
# (e tentar distinguir a diferença de velocidade)
