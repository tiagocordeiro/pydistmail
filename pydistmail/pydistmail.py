#!/usr/bin/python
# coding: utf-8

import csv
import email
import smtplib
import sys

# Captura mensagem do stdin via pipe
msg = email.message_from_file(sys.stdin)

# lista com vendedores ou emails para distribuição
vendedores = [('Vendedor 01', 'vendas01@dominio.com.br'),
              ('Vendedor 02', 'vendas02@dominio.com.br')]

# Verifica o tamanho da lista de vendedores
totalVendedores = len(vendedores)

# Pega o ultimo vendedor que recebeu email
ultimovendedor = open('ultimovendedor.txt', 'r').read()  # use o path completo

# Determina o próximo vendedor que irá receber e-mail
if int(ultimovendedor) == totalVendedores - 1:  # Se o ultimo que recebeu, é o
    proximovendedor = 0  # ultimo da lista, volta para
else:  # o primeiro da lista.
    proximovendedor = int(ultimovendedor) + 1  # Se não, pega o próximo.

davez = str(proximovendedor)

# Salva qual vendedor está recebendo o e-mail atual.
fvend = open('ultimovendedor.txt', 'w')  # use o path completo
fvend.write(davez)
fvend.close()

# Testa se tem um email para resposta.
if not msg['reply-to']:
    emailcontato = msg['from']
else:
    emailcontato = msg['reply-to']

# Salva log de recebimento em csv
with open('emails.csv', 'a') as fcsv:  # use o path completo
    mailwriter = csv.writer(fcsv, delimiter=';')
    mailwriter.writerow(
        [msg['date'], msg['subject'], emailcontato,
         vendedores[proximovendedor][0]])

# Encaminha o e-mail para o vendedor da vez.
s = smtplib.SMTP('localhost')
s.sendmail("vendas@dominio.com.br", vendedores[proximovendedor][1],
           msg.as_string())
s.quit()
