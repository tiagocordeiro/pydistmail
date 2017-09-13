#!/usr/bin/python
# coding: utf-8

import email
import csv


# Simula a captura de mensagem do stdin via pipe
emailmock = open("mailmock.txt", "r").read()

msg = email.message_from_string(emailmock)

# lista com vendedores ou emails para distribuição
vendedores = [('Vendedor 01', 'vendas01@dominio.com.br'),
              ('Vendedor 02', 'vendas02@dominio.com.br')]

# Verifica o tamanho da lista de vendedores
totalVendedores = len(vendedores)

# Pega o ultimo vendedor que recebeu email
ultimovendedor = open('ultimovendedor-test.txt', 'r').read()


if int(ultimovendedor) == totalVendedores - 1:
    proximovendedor = 0
else:
    proximovendedor = int(ultimovendedor) + 1

davez = str(proximovendedor)


fvend = open('ultimovendedor-test.txt', 'w')
fvend.write(davez)
fvend.close()


with open('emails-test.csv', 'a') as fcsv:
    mailwriter = csv.writer(fcsv, delimiter=';')
    mailwriter.writerow(
        [msg['date'], msg['from'], msg['subject'],
         vendedores[proximovendedor][0]])


# Simula Encaminhamento do e-mail para o vendedor da vez.
def envio():
    return 'Enviando o email para o vendedor ' + vendedores[proximovendedor][1]

def test_envio():
    assert envio() == str('Enviando o email para o vendedor ' + vendedores[proximovendedor][1])