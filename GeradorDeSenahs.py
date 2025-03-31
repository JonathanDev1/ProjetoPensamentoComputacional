import random
import string


def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """Gerador de senhas"""
    caracteres = string.ascii_lowercase 
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase 
    if incluir_numeros:
        caracteres += string.digits  
    if incluir_simbolos:
        caracteres += string.punctuation  

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    
    return senha


print("Gerador de Senhas Seguras ")
tamanho = int(input("Digite o tamanho da senha (mínimo 8 caracteres): "))
if tamanho < 8:
    print("Tamanho muito pequeno! Ajustado para 8 caracteres.")
    tamanho = 8

maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
simbolos = input("Incluir símbolos? (S/N): ").strip().lower() == 's'


senha_segura = gerar_senha(tamanho, maiusculas, numeros, simbolos)


print(f"\n Senha Gerada: {senha_segura}")



