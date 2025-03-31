import random
import string


def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """Gera uma senha segura com base nas opções do usuário."""
    caracteres = string.ascii_lowercase  # Letras minúsculas
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase  # Adiciona letras maiúsculas
    if incluir_numeros:
        caracteres += string.digits  # Adiciona números (0-9)
    if incluir_simbolos:
        caracteres += string.punctuation  # Adiciona caracteres especiais

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha

# Configuração do usuário
print("Gerador de Senhas Seguras 🔒")
tamanho = int(input("Digite o tamanho da senha (mínimo 8 caracteres): "))
if tamanho < 8:
    print("Tamanho muito pequeno! Ajustado para 8 caracteres.")
    tamanho = 8

maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
simbolos = input("Incluir símbolos? (S/N): ").strip().lower() == 's'

# Gerando senha segura
senha_segura = gerar_senha(tamanho, maiusculas, numeros, simbolos)

# Exibindo senha e copiando para área de transferência
print(f"\n Senha Gerada: {senha_segura}")



