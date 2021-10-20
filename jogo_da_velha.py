#manipulando vetores: jogo da velha

tabela = ['_','_','_','_','_','_','_','_','_']

def tabela(vetor_velha):
    jogo = ''
    for i in range(len(vetor_velha)):
        
        if(i == 2 or i == 5 or i == 8):
            jogo += " " + vetor_velha[i] + " \n"
        else:
            jogo += "  " + vetor_velha[i] + " |"
        return jogo

def verifica_tabela(vetor_velha, posicao):
    resultado = False
    if(vetor_velha[posicao] == '_'):
        resultado = True
    return resultado

def verifica_vitoria(vetor_velha, simbolo):
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
