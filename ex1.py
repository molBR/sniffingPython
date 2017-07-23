# encoding: utf-8
import socket
import os
import sys

#ip do host
#host = "192.168.1.6"
host = socket.getfqdn()
#para windows 
if os.name =="nt":


	socket_protocol = socket.IPPROTO_IP
else:
	#linux
	socket_protocol = socket.IPPROTO_IPO_ICMP
#IPPROTO_IP = Pegar pacotes IP direto;
	#existem sockets para a camada de transporte TCP e UDP.

#AF_INET = Familia de endreços, nesse caso: IPv4. Para IPv6 usa-se: AF_INET6
#SOCKET_RAW = Pula a camada de transporte, normalemnte as aplicações de socket que usam o portocolo de internet
	#seguem o protocolo TCP/IP, isso é, são encapsulados pela camada de transporte para chegar à camada de aplicação
	#sock_raw, pula a camada de transporte, pegando as informações da camada de rede direto para a camada de aplicação

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host,0))

#inclui o cabeçalho de IP
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
#seta a placa para modo promiscuo
print sniffer.recvfrom(65565)

if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
#limpa a promiscuidade da placa