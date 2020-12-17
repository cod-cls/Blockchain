# Criando Blockchain genérico

import datetime  #cada bloco quando for criado vai ser registrado sua data exata
import hashlib  # permite a criação de hash
import json  #codificar os blocos antes e depois de gerar os hashs, leitura e geração de dados em json
from flask import flask, jsonify  #vamos usar função json fy para fazer requesta dos post e exibir resultados, vamos retornar em formato json a mineração


#parte 1, criar um blockchain
# a maneira mais robusta de se fazer um blockchai é através de uma classe

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash ='0') #criação do bloco genesis, função create_block, proof e link com bloco anterior, (a função hash só aceita texto)
        
# alem do bloco genesis, precisa-se criar outros blocos, função create_block, depois de minerar um bloco, presisa-se da solução resolvida(PoW) encontrar o hash para depois criar o bloco.


    def crate_block(self, proof, previous_hash):   #deve ter proof (nounce), a função de mineração vai entregar para esta função, dizendo que foi minerado e o previous_hash, que vai linkalo ao bloco anterior
     
         block = { 'indice': len(self.chain) + 1,              # agora se cria um dicionário, que vai ter 4 chaves: um índice(numero que identifica cardinalmente), o time, o proof, e o previus_hash
                   'timestamp': str(datetime.datetime.now()),
                   'proof': proof,
                   'previous_hash': previous_hash }   
                                        
         self.chain.append(block)  #adicionando o bloco ao chain
         return block
     
    def get_previous_block(self):  #retornar o bloco anterior
        return self.chain[-1]
        
        



        



