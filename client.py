import socket
import logo
from termcolor import colored
import driver
import server
client_obj = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 5556
client_obj.connect((ip_address,port))
conn_conf = client_obj.recv(1024)
while conn_conf:
    print(colored((logo.names),"green"))
    user_input = input(colored("Enter your Choice: ","red", attrs=["bold"]))
    if user_input == 'stop':
        break
    client_obj.send(user_input.encode('utf-8'))
    conn_conf = client_obj.recv(1024)
    print_quote = '''\n
        {}\n'''.format(conn_conf.decode('utf-8'))
    print(colored(print_quote,"blue", attrs=['bold']))

    
