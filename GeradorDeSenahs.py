import random
import string
#chama bibliotecas PY
def gerar_senha(tamanho=12, maiusculas=True, numeros=True, simbolos=True):
    """Gera uma senha segura com base nas opções do usuário."""
    caracteres = string.ascii_lowercase 
    # Inclui letras minúsculas
    
    # Adiciona mais complexidade à senha conforme as escolhas do usuário
    if maiusculas:
        caracteres += string.ascii_uppercase  # Adiciona letras maiúsculas
    if numeros:
        caracteres += string.digits  # Adiciona números
    if simbolos:
        caracteres += string.punctuation  # Adiciona símbolos especiais
    
    # Gera a senha escolhendo caracteres aleatórios da lista
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

#  Lucas agora interage com o programa:
print(" Gerador de Senhas Seguras")

# Pede o tamanho da senha e garante um mínimo de 8 caracteres
tamanho = max(int(input("Tamanho da senha (mínimo 8): ")), 8)

# Pergunta se o usuário deseja incluir certos tipos de caracteres, esperando eles como inputs.
maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
simbolos = input("Incluir símbolos? (S/N): ").strip().lower() == 's'

# Gera e exibe a senha segura no onsole de execução
print(f"\n Senha Gerada: {gerar_senha(tamanho, maiusculas, numeros, simbolos)}")
