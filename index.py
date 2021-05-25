#!/usr/bin/python

import sys


"""Divide a lista em pedaços de tamanho n"""
def generate_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

"""Inicio da Execução do Programa """
if len(sys.argv) < 2:
    print("Utilização: python .\\index.py {File Name}")
    quit

"""Leitura dos bytes do arquivo """
file = open(sys.argv[1], "rb")
content = file.read()
file.close()

chunks = generate_chunks(content, 1024)

for x in reversed(list(chunks)):
    print(x)