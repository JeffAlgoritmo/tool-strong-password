"""
Projeto: Senha Forte - CLI
Autor: JeffAlgoritmo
Data de Finalização: 23/05/2025
Data da Última Atualização: 23/05/2025

Propósito do projeto: O intuito inicial do projeto é auxiliar o usuário na criação de uma senha forte que pode ser usada em diversos sites e programas
"""
import random

flag_of_open_program = True
print("#######################################")
print("Desenvolvidor por: JeffAlgoritmo")
print("#######################################")
print("\nBem-vindo ao programa GERADOR DE SENHA FORTE\n")
words = []
set_numbers_letters = [("a","A","4"), ("i","I","1"),("e","E","3"),("s","S","5"),("t","T","7")]
set_letters_choiced = []
set_letters_modified = []
set_special_chars = ["!","@","#","%","&","_","$"]

def separateSetLetters(set_words):
    words_count = 0
    if len(set_words) == 4:
        while words_count <= 3:
            for word in set_words:
                set_letters_choiced.append(words[words_count][0:2])
                words_count += 1
    elif len(set_words) == 3:
        while words_count <= 2:
            for word in set_words:
                set_letters_choiced.append(words[words_count][0:2])
                words_count += 1

def changeLetterToNumber(set_letters):
    # Uma condicional verifica se qualquer um dos caracteres alvos é detectado. Se sim, será efetuada a troca por número
    for setLetter in set_letters:
        if 'a' or 'A' or 'e' or 'E' or 't' or 'T' or 'o' or 'O' or 'i' or 'I' or 's' or 'S' in setLetter:
            setModified = setLetter.replace('a','4').replace('A','4').replace('e','3').replace('E','3').replace('t','7').replace('T','7').replace('o','0').replace('O','0').replace('i','1').replace('I','1').replace('s','5').replace('S','5')   
            set_letters_modified.append(setModified)

def includeSpecialChar(set_modified):
    # Faz a inclusão no inicio e no fim de caracter especial aleatório
    set_modified.insert(0,set_special_chars[random.randint(0, 6)])
    set_modified.insert(6,set_special_chars[random.randint(0, 6)])

    # Faz a inclusão de um caracter especial entre os pares de caracetes
    if len(set_modified) == 6:
        set_modified.insert(2,set_special_chars[random.randint(0, 6)])
        set_modified.insert(4,set_special_chars[random.randint(0, 6)])
        set_modified.insert(6,set_special_chars[random.randint(0, 6)])
    elif len(set_modified) == 5:
        set_modified.insert(2,set_special_chars[random.randint(0, 6)])
        set_modified.insert(4,set_special_chars[random.randint(0, 6)])

def showTheCodifiedPass(set_pass_codified):
    # Mostra a senha codificada
    print("\nAqui está a senha codificada: ", end="")
    for letter in set_letters_modified:
        print(letter,end="")
    print("\n")

def showTableLetterToNumber(set_to_show):
    # Tornando acessível a flag que mantém o programa aberto para finalizar o programa
    global flag_of_open_program 
    
    print("Aqui está a tabela de referência para ajudar a traduzir letras para números e vice-versa usadas nesse programa: ")
    print("--------------------")
    print("| Letra ||  Número |")
    count = 0
    # Algoritmo para gerar a tabela de forma que fique alinhada
    for set in set_to_show:
        print(f"|  {set[0]},{set[1]}",end="")
        print(f"  ||    {set[2]}    |")
        count +=1
    print("--------------------")
    flag_of_open_program = False

if __name__ == '__main__':
    while flag_of_open_program:
        
        print("Escolha o TAMANHO da SENHA CODIFICADA que você deseja ou Digite 1 para SAIR do Programa.\n#=> Digite 10 para 10 caracteres \n#=> Digite 13 para 13 caracteres")

        # Verifica o input e impede que seja passado valor diferente de inteiro       
        try:
            
            option_passLength = int(input("Resposta: "))
            if option_passLength == 1:
                print("\nO programa será encerrado!\n".upper())
                flag_of_open_program = False
                continue 
            # Limita o programa a apenas duas opções 10 ou 13 como resposta pro input             
            elif option_passLength != 10 and option_passLength != 13:
                print("\nNão existe essa opção!\n".upper())
                continue    
        except ValueError:
            print("\nNão é permitido valores diferentes de números\n".upper())        
            continue                      

        print("\nDigite as PALAVRAS que deseja USAR na CODIFICAÇÃO da SENHA e digite-as NA ORDEM que seja MAIS FÁCIL LEMBRAR posteriormente\n OBSERVAÇÃO: É necessário 3 PALAVRAS para 10 caracteres e 4 PALAVRAS para 13 caracteres")
        word = ""

        # Remoção de espaços em branco na direita e esquerda e tratamento para barrar se for número no input
        if option_passLength == 13:
            while len(words) <= 3:
                word = str.rstrip(str.lstrip(input("Resposta: ")))
                if word.isdecimal():
                    print("\nSó é POSSÍVEL enviar VALORES NÃO NÚMERICOS.\n")
                else: 
                    words.append(word)
        elif option_passLength == 10:
            while len(words) <= 2:
                word = str.rstrip(str.lstrip(input("Resposta: ")))
                if word.isdecimal():
                    print("\nSó é POSSÍVEL enviar VALORES NÃO NÚMERICOS.\n")
                else: 
                    words.append(word)
                
        # Função para separar em conjunto de duas letras                   
        separateSetLetters(words)   
        # Parte 1 do processo de codificação. Transformando letra para número
        changeLetterToNumber(set_letters_choiced)
        # Parte 2 do processo de codificação. Incluindo caracteres especiais aleatórios em pontos especificos da senha
        includeSpecialChar(set_letters_modified)
        
        # Análise da estrutura da senha:
        # 4 palavras + 2 caracteres padrões = 13 caracteres máximo no final será gerado (incluindo já os aleatórios)
        # 3 palavras + 2 caracteres padrões = 10 caracteres máximo no final será gerado (incluindo já os aleatórios)
        
        # Mostra a senha codificada
        showTheCodifiedPass(set_letters_modified)
        # Mostra a tabela para consulta
        showTableLetterToNumber(set_numbers_letters)
        
    
    



            