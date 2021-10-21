#manipulando vetores: jogo da velha

tabela = ['_','_','_','_','_','_','_','_','_']

def desenho_tabela(vetor_velha):
    jogo = ''
    for i in range(len(vetor_velha)):
        if(i == 2 or i == 5 or i == 8):
            jogo += " " + vetor_velha[i] + " \n"
        else :
            jogo += " " + vetor_velha[i] + " |"
    return jogo

def verifica_tabela(vetor_velha, posicao):
    resultado = False
    if(vetor_velha[posicao] == '_'):
        resultado = True
    return resultado

def verifica_vitoria(vetor_velha,simbolo):
    resultado = False

# Confere por linha
    if(vetor_velha[0] == simbolo and vetor_velha[1] == simbolo and vetor_velha[2] == simbolo):
        resultado = True
    elif(vetor_velha[3] == simbolo and vetor_velha[4] == simbolo and vetor_velha[5] == simbolo):
        resultado = True
    elif(vetor_velha[6] == simbolo and vetor_velha[7] == simbolo and vetor_velha[8] == simbolo):
        resultado = True

# Confere por coluna
    elif(vetor_velha[0] == simbolo and vetor_velha[3] == simbolo and vetor_velha[6] == simbolo):
        resultado = True
    elif(vetor_velha[1] == simbolo and vetor_velha[4] == simbolo and vetor_velha[7] == simbolo):
        resultado = True
    elif(vetor_velha[2] == simbolo and vetor_velha[5] == simbolo and vetor_velha[8] == simbolo):
        resultado = True

# Confere Verticalmente
    elif(vetor_velha[0] == simbolo and vetor_velha[4] == simbolo and vetor_velha[8] == simbolo):
        resultado = True
    elif(vetor_velha[6] == simbolo and vetor_velha[4] == simbolo and vetor_velha[2] == simbolo):
        resultado = True
    return resultado


# Confere casos de empate
def verificar_empate(vetor_velha):
    resultado = True
    for i in vetor_velha:
        if(i == '_'):
            resultado = False
    return resultado

# Variaveis do jogo

jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0

print("Jogo da Velha")
print("")
print(desenho_tabela(tabela))

while(True):
#jogador 1
    if(jogador == 1):
        jogador_numero_1 = input('Jogador 1 Digite uma posição de 1 a 9 : ')
        if(verifica_tabela(tabela,int(jogador_numero_1)-1)):
            tabela[int(jogador_numero_1)-1] = 'X'
            jogador = 2
            print(desenho_tabela(tabela))
        else :
            print(desenho_tabela(tabela))
            print('Posicao ja ocupada')
    if(verifica_vitoria(tabela,'X')):
        print('Jogador numero 1 ganhou')
        break
    if(verificar_empate(tabela)):
        print('DEU VELHA!')
        break

#jogador 2
    if(jogador == 2):
        jogador_numero_2 = input('Jogador 2 Digite uma posição de 1 a 9 : ')
        if(verifica_tabela(tabela,int(jogador_numero_2)-1)):
            tabela[int(jogador_numero_2)-1] = 'O'
            jogador = 1
            print(desenho_tabela(tabela))
        else :
            print(desenho_tabela(tabela))
            print('Posicao ja ocupada')
    if(verifica_vitoria(tabela,'O')):
        print('Jogador numero 2 ganhou')
        break
    if(verificar_empate(tabela)):
        print('DEU VELHA')
        break