

usuarios = {
    "admin": "senha123",
    "usuario1": "segura456"
}

tentativas = 3  

while tentativas > 0:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Conta bloqueada devido a muitas tentativas erradas.")
