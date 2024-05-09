import sys

#===============================
# Para converter facil os Dumps 
#===============================

#Desenvolvido por: ScaryHollow

#===============================

print("Digite o nome do arquivo: (O nome deve ser exato e o arquivo deve estar no mesmo diretorio deste programa!)")
filename = input()

try:
   with open(filename, 'r') as arquivobin: #leitura de BIN
    countline = 0
    pularlinhas = 0

    for linha in arquivobin: #percorre as linhas
     #print(linha)
     count = 0
     caracterant = None
     pointer = None

     if countline % 5 == 0: #quebra a linha para evitar contar o Sector: 0,1,2...
        print(linha, end="")
        countline += 1
        
        
     else:
        
        countline += 1
        countpoint = 0
     
        for caractere in linha: #percorre os caracteres
            #print(caractere, end="")
            count += 1

            if caracterant is not None: #Inverter os valores HEX
               pointer = caracterant + caractere
               #print(pointer, end=" ")               
               if countpoint == 0:
                  pointer1 = pointer
               elif countpoint == 1:
                  pointer2 = pointer
               elif countpoint == 2:
                  pointer3 = pointer
               elif countpoint == 3:
                  pointer4 = pointer
                  print("Hex:", pointer4, pointer3, pointer2, pointer1, end=" Dec:", sep="") #imprime em HEX
                  hexfull = pointer4 + pointer3 + pointer2 + pointer1                 
                  decimal = int(hexfull, 16) #conversão para decimal
                  print(decimal, end="")
                  pularlinhas += 1
                  
               countpoint += 1

               #caracterant = None
               #time.sleep(1)
            caracterant = caractere
            

            if count % 8 == 0 and count != 0: #Coloca um separador a cada 8 caracteres         
                print(" | ", end="")
                countpoint = 0
                count == 0
            
            if pularlinhas % 4 == 0 and pularlinhas != 0: #pra quebrar a linha a cada 4 hex
               print("")
               pularlinhas = 0

            if count % 2 == 0 and count != 0: #reseta o caracter anterior a cada 2 lidos
                #print(" ", end="")
                caracterant = None

except FileNotFoundError:
   print("Arquivo não encontrado!!")
   sys.exit()

arquivobin.close