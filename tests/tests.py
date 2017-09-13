import email
import smtplib
import sys
import csv

emailmock = open("mailmock.txt", "r").read()

msg = email.message_from_string(emailmock)

vendedores = [("Vendedor 01", "vendas01@dominio.com"),("Vendedor 02", "vendas02@domini0.com")]


