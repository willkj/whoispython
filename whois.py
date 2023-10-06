#!/usr/share/python
#WHOIS PYTHON

#Modo de USO: python consulta.py [ip]

import socket, sys

s = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
s.connect(("whois.iana.org", 43))
s.send(sys.argv[1]+ "\r\n")
resposta = s.recv(1024)
resposta_split = resposta.split()
print resposta
print resposta_split[19]
