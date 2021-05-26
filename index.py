#!/usr/bin/python

import sys
from Crypto.Hash import SHA256

"""Divide a lista em pedaços de tamanho n"""
def generate_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

"""Inicio da Execução do Programa """
if len(sys.argv) < 2:
    print("Utilização: python .\\index.py {File Name}")
    quit()

"""Leitura dos bytes do arquivo """
file = open(sys.argv[1], "rb")
content = file.read()
file.close()

""" Chama função para dividir a lista de bytes em tamanhos iguais"""
chunks = generate_chunks(content, 1024)

last_hash = -1
""" Itera pela lista de blocos de byets em ordem reversa iniciando pelos ultimos bytes do arquivo """
for x in reversed(list(chunks)):
    """ Verifica se é a primeira iteração caso seja realiza o hash do bloco b(n-1) e salva para proxima iteração"""
    if last_hash == -1:
        h = SHA256.new(x)
        last_hash = h.digest()
    else:
        """ Caso não seja a primeira iteração adiciona o bloco de bytes para realizar o hash 
        e contatena com o hash do bloco anterior """
        h = SHA256.new(x)
        h.update(last_hash)
        last_hash = h.digest()

""" Após toda iteração do script é retornado o valor encontrado para o hash do bloco b(0) informado como h0 """
print("h0 = " + h.hexdigest())