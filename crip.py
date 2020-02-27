#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:38:29 2020

@author: steffens
"""

import sys
import binascii


# Bloco Conversao de ASCII para binario e vice versa, retirado de : https://vike.io/pt/534905/


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#FIM bloco Conversao de ASCII para binario e vice versa, retirado de : https://vike.io/pt/534905/


cripto=''
param = sys.argv[1:]  # entrada de parametros

if len(param)==3:  # Testa se a quantidade de parametros é correta
    arqTextoClaro = param[1]
    chave = param[0]
    modo = param[2]
    chave =  text_to_bits(chave)  
    #print(type(chave))
    
    
    if(len(chave)!=64 and len(chave)!=128):
        print('Tamanho da chave invalido!\n Passe a chave de 64 bits ou 128 bits (8 ou 16 caracteres).\n')
        exit()

else:
    print('Quantidade de parametros invalida! \n Passe a chave de 64 bits ou 128 bits (8 ou 16 caracteres).\n O caminho para o arquivo de texto.\n E o modo, C para criptografar D para descriptografar.\n')
    print('Exemplo: $ python crip.py steffens lucas.txt c \n')
    exit()

    

    

 #Abrir o arquivo de texto claro
with open(arqTextoClaro, 'r') as f:
    texto = f.read() # Le arquivo 
lista=[]
vetor =''   
i =0 # Auxilar percorerr o texto a ser cifrado
j=0

if(modo=='c' or modo=='C'):
    while (i < len(texto)-1): # Enquanto o texto nao for todo percorrido
    
        if(len(chave)==64 and j<=8): # se a chave é de 64 bits e nao foi percorrido 8 caracteres
       
            vetor+=texto[i] # Cria uma string com os caracteres
            j=j+1
            if(j==8): # Se j=8 os 8 caracteres foram formados e podem ser adicionados a lista
                #print(vetor)          
                vetor = text_to_bits(vetor) 
                lista.append(vetor)
                vetor=''
                j=0
      
       
       
    
        if(len(chave)==128 and j<=16):
            vetor+=texto[i] # Cria uma string com os caracteres
            j=j+1
            if(j==16): # Se j=16 os 16 caracteres foram formados e podem ser adicionados a lista
               # print(vetor)          
                vetor = text_to_bits(vetor) 
                lista.append(vetor)
                vetor=''
                j=0
    
    
    
    
        i+=1

    if(j>0): # Se percorreu os caracteres e nao formou blocos completos pega oque sobrou e coloca 0 ate bater no numero de bits escolhidos
        #print('j>0')
        #print(vetor)
        vetor = text_to_bits(vetor)
        if(len(chave)==64):
            while len(vetor)<64:
                vetor+='0'
       
            lista.append(vetor) 
        elif(len(chave)==128):
            while len(vetor)<128:
                vetor+='0'
            lista.append(vetor)
##########################################  
if(modo=='d' or modo=='D'):
    while (i < len(texto)):
        if(len(chave)==64 and j<=64):
            vetor+=texto[i] # Cria uma string com os caracteres
            
            j=j+1
            
            if(j==64): # Se j=8 os 8 caracteres foram formados e podem ser adicionados a lista
                #print(vetor)          
                
                lista.append(vetor)
                vetor=''
                j=0
        
        if(len(chave)==128 and j<=128):
            vetor+=texto[i] # Cria uma string com os caracteres
            j=j+1
            if(j==128): # Se j=16 os 16 caracteres foram formados e podem ser adicionados a lista
               # print(vetor)          
                #vetor = text_to_bits(vetor) 
                lista.append(vetor)
                vetor=''
                j=0
    
    
    
    
        i+=1
            
##########################################            
#print(lista)
saida=[]           
p=0

chave1= list(chave)
#print(chave)
#print(chave1)
if(modo=='c' or modo=='C'):
    while (p <= len(lista)-1):
        x= list(lista[p])
        #print(x)  # Aqui percorre cada indice da lista, cada bloco de 64 ou 128 bits
        o = 0
        while(o <= len(x)-1):
            if(chave1[o]==x[o]):
                cripto+='0'
            else:
                cripto+='1'
            
            o+=1
        saida.append(cripto)
        cripto=''
        o=0
        p+=1
    string=''
    string=string.join(saida)
    print(string)
    f = open('criptografado.txt', "w")
    f.write(string)
    print('Confira o arquivo criptografado.txt em seu diretorio \n')

#print('\n')
#print(saida)
#print('\n')





saida2=[]
p=0
if(modo=='d' or modo=='D'):
    while (p <= len(lista)-1):
        x= list(lista[p])
        #print(x)  # Aqui percorre cada indice da lista, cada bloco de 64 ou 128 bits
        o = 0
        while(o <= len(x)-1):
            if(chave1[o]==x[o]):
                cripto+='0'
            else:
                cripto+='1'
            
            o+=1
        saida2.append(cripto)
        cripto=''
        o=0
        p+=1
    #print('\n')
    #print(saida2)
    #print('\n')

#    if(saida2==lista):
#        print('true')
#print(type(saida2))    

    string=''
    string=string.join(saida2)
#print(type(string))
    #print(string)    
# Desconverter    
    print(text_from_bits(string))



