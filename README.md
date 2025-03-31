# Projeto Pensamento Computacional
Entrega de atividades

 *Análise crítica* 
 
É entendido por nós (Integrantes do grupo) que ética na programação vai muito além de bons modos em códigos, a ética nesse meio reflete diretamente na nossa vida cotidiana. Como mostrado no filme Hacker – Todo Crime Tem um Início (Anonymous, 2016) que suas escolhas no meio digital refletem em consequências diretas na sua vida. Ética é entendido por ser justo e honesto através de boas práticas, escolhas individuais podem afetar a sociedade em geral. 
No mundo real, a programação é uma ferramenta poderosa para solucionar problemas, seja na segurança digital, no desenvolvimento de softwares financeiros ou na automação de tarefas. No entanto, como mostra o filme, o mesmo conhecimento pode ser usado para fraudes, invasões e crimes digitais.

 *Análise do filme Hacker*

O filme retrata a vida de um jovem chamado Alex que em meio as dificuldades financeiras encontram saídas para ganhar dinheiro através de seu computador. No início são coisas simples e consideradas legais, até que ao surgir uma dificuldade financeira maior recorre a um meio ilegal para ganhar dinheiro, a dark web.
Ao decorrer do filme outros personagens aparecem e se juntam a Alex, o trio usa seus conhecimentos programação para fraudes e roubos bancários, levando uma vida regada a alguns luxos. A cada golpe o nível sobe, sempre desejam aumentar patamar de suas ações.
Alguns dos problemas apresentados no filme são a fragilidade dos bancos, atualmente poderiam usar a IA como o uma diferente abordagem tecnológica, mantendo como detector de possíveis fraudes.
Impactos sérios foram mostrados ao decorrer do filme, como mortes e perseguições. Através de suas escolhas o melhor amigo de Alex teve sua vida ceifada. Isso reflete na ética da programação, talvez se eles tivessem escolhido boas práticas na programação e tivessem levado uma vida correta não teriam mortes e prisões.

------------------------------------------------------------------------------------------------------------------------------------------

                                   Resolução de Problemas com Linguagem de Programação
                                   
Alessandro, o Estudante de Programação
Alessandro está aprendendo sobre segurança digital e percebeu que sempre usava senhas fracas para acessar suas contas em sites de cursos e ferramentas online. Um dia, ele recebeu um alerta de que uma de suas senhas vazou em uma violação de dados. Para evitar problemas futuros, ele começou a usar um gerador de senhas seguras, criando combinações fortes e diferentes para cada conta, que ele salva em um gerenciador de senhas. Isso lhe deu mais tranquilidade e proteção contra ataques.


*Possivel solução aplicavel:*

    import random
import string

def gerar_senha(tamanho=12, maiusculas=True, numeros=True, simbolos=True):
    """Gera uma senha segura com base nas opções do usuário."""
    caracteres = string.ascii_lowercase  # Inclui letras minúsculas
    
    # Adiciona mais complexidade à senha conforme as escolhas do usuário
    if maiusculas:
        caracteres += string.ascii_uppercase  # Adiciona letras maiúsculas
    if numeros:
        caracteres += string.digits  # Adiciona números
    if simbolos:
        caracteres += string.punctuation  # Adiciona símbolos especiais
    
    # Gera a senha escolhendo caracteres aleatórios da lista
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

    # 📌 Lucas agora interage com o programa:
print("🔐 Gerador de Senhas Seguras")

# Pede o tamanho da senha e garante um mínimo de 8 caracteres
tamanho = max(int(input("Tamanho da senha (mínimo 8): ")), 8)

# Pergunta se o usuário deseja incluir certos tipos de caracteres
maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().lower() == 's'
numeros = input("Incluir números? (S/N): ").strip().lower() == 's'
simbolos = input("Incluir símbolos? (S/N): ").strip().lower() == 's'

# Gera e exibe a senha segura
print(f"\n🔑 Senha Gerada: {gerar_senha(tamanho, maiusculas, numeros, simbolos)}")
                                   
*Esssa solução gera senhas seguras*


------------------------------------------------------------------------------------------------------------------------------------------



*Indicação de Problemas para Resolução e Pontuação*

*Desenvolver um programa que simula um sistema de login*

Clara é dona de um pequeno e-commerce. Cansada de senhas fracas e inseguras, ela decidiu implementar um sistema de login para garantir que apenas usuários autorizados acessem seu sistema.
Após pesquisar um pouco, Clara criou este código simples e eficiente para controlar acessos.

Codigo:

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


Esse codigo simula um sistema de login.

------------------------------------------------------------------------------------------------------------------------------------------

*Criar uma solução para identificar ataques a uma rede fictícia.*

Ricardo é responsável pela segurança da rede de uma pequena empresa. Ele percebeu que alguns IPs estavam tentando acessos suspeitos repetidamente e decidiu criar um sistema simples para detectar possíveis ataques e bloquear acessos indevidos automaticamente.
Após pesquisar sobre monitoramento de rede, Ricardo criou este código eficiente.

Codigo:

   import random
import time

# Lista de IPs monitorados
ips = ["192.168.1.10", "192.168.1.15", "192.168.1.20", "200.150.10.5"]

# Dicionário para contar tentativas por IP
tentativas = {}

# Limite de tentativas antes de gerar alerta
limite = 5

print("Monitorando tráfego de rede...\n")

while True:
    # Escolhe um IP aleatoriamente para simular um acesso
    ip = random.choice(ips)
    
    # Registra a tentativa no dicionário, iniciando com 0 se o IP for novo
    tentativas[ip] = tentativas.get(ip, 0) + 1
    
    print(f"Tentativa de acesso do IP {ip} - Total: {tentativas[ip]}")
    
    # Se o IP ultrapassar o limite, alerta e encerra o monitoramento
    if tentativas[ip] > limite:
        print(f"ALERTA: Atividade suspeita detectada do IP {ip}. Encerrando o monitoramento.")
        break  # Sai do loop imediatamente
    
    time.sleep(1)  # Aguarda 1 segundo para simular o tempo real

 Esse sistema simula ataques de ip e gera um alerta.
 
------------------------------------------------------------------------------------------------------------------------------------------

 ALUNOS: Jonathan Alves de Menezes, Alessandro Rodrigues Justino Junior, Kleber Galvão.


 *Referencias:*


 Hacker: Todo Crime Tem um Início. Direção de Michael Spierig e Peter Spierig. Produção: Germany, Estados Unidos, 2015. 1h 58min.
 OPENAI. ChatGPT. Utilizado para auxílio na correção de códigos. Acesso em: 21 mar. 2025. Disponível em: https://chat.openai.com/

 _

