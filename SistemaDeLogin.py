# Dicionário contendo usuários e senhas
usuarios = {"admin": "senha123", "usuario1": "segura456"}

# Número máximo de tentativas antes de bloquear o login
tentativas = 3  

while tentativas > 0:
    # Solicita nome de usuário e senha
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se as credenciais estão corretas
    if usuarios.get(usuario) == senha:
        print(f"Login bem-sucedido! Bem-vindo, {usuario}")
        break  # Sai do loop após login bem-sucedido
    
    # Se as credenciais estiverem erradas, reduz uma tentativa
    tentativas -= 1
    print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

# Se todas as tentativas forem usadas, a conta é bloqueada
if tentativas == 0:
    print("Conta bloqueada devido a muitas tentativas erradas.")
