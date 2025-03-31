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
                                   
*Esssa solução gera senhas seguras*


------------------------------------------------------------------------------------------------------------------------------------------



*Indicação de Problemas para Resolução e Pontuação*

*Desenvolver um programa que simula um sistema de login*

Codigo:

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

Esse codigo simula um sistema de login.

------------------------------------------------------------------------------------------------------------------------------------------

*Criar uma solução para identificar ataques a uma rede fictícia.*

Codigo:

import random
import time


ips_monitorados = ["192.168.1.10", "192.168.1.15", "192.168.1.20", "200.150.10.5"]


tentativas_por_ip = {}


limite_tentativas = 5

print("Monitorando tráfego de rede...\n")

while True:
    
   ip_origem = random.choice(ips_monitorados)
    
   
   tentativas_por_ip[ip_origem] = tentativas_por_ip.get(ip_origem, 0) + 1
    
   print(f"Tentativa de acesso do IP {ip_origem} - Total: {tentativas_por_ip[ip_origem]}")
    
    
   if tentativas_por_ip[ip_origem] > limite_tentativas:
        print(f" *ALERTA*: Atividade suspeita detectada do IP {ip_origem}. Possível ataque em andamento!")
        print("Encerrando o monitoramento...\n")
        break  
    
   
   time.sleep(1)


 Esse sistema simula ataques de ip e gera um alerta.
 
------------------------------------------------------------------------------------------------------------------------------------------

 ALUNOS: Jonathan Alves de Menezes, Alessandro Rodrigues Justino Junior, Kleber Galvão.


 *Menções:*


 Hacker: Todo Crime Tem um Início. Direção de Michael Spierig e Peter Spierig. Produção: Germany, Estados Unidos, 2015. 1h 58min.
 OPENAI. ChatGPT. Utilizado para auxílio na correção de códigos. Acesso em: 21 mar. 2025. Disponível em: https://chat.openai.com/

 _

