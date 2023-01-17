import os
from getpass import getpass
from utils import print_logo, print_version, print_author, print_footer
from app.models import Server
from db import DatabaseManager
from app.utils import Utils

def get_ssh(ip, username, password):

    os.system(f'sshpass -p {password} ssh {username}@{ip}')


def remove_server():
    pass

def new_server_register():
    
    ip = input('Digite o endereço do servidor: \n')
    username = input('Digite o usuario do servidor: \n')
    password = getpass('Digite a senha do servidor: \n')

    response = DatabaseManager.save_server(ip, username, password)

    if response:

        print('Servidor cadastrado com sucesso!')
    
    else:
        print('Falha ao cadastrar o servidor!')



def get_connection(machine, server_password):

    machine_user_selected = Server.objects.filter(ip=machine)

    if machine_user_selected.count() == 0:
        
        print('Não foi encontrado registros para realizar a conexão!')
    
    else:

        hashed_password = machine_user_selected.first().password
        username = machine_user_selected.first().username

        if not Utils.check_password(server_password, machine_user_selected):
            print('Credencial inválida!')
        else:
            get_ssh(machine, username, server_password)

def connect_server():
    
    machines = Server.objects.all().values('ip')
    user_option = 1

    for machine in machines:

        print(f'[{user_option}] - {machine}')
        user_option += 1

    user_option_selected = input('Selecione qual máquina deseja conectar\n')
    server_password = getpass('Digite a senha de usuário\n')

    response = get_connection(machines[user_option_selected-1], server_password)

    #if response:

    
def process_user_option(captured_user_option):
    
    try:
        captured_user_option = int(captured_user_option)

        if captured_user_option == 1:

            new_server_register()
    
        elif captured_user_option == 2:

            remove_server()

        elif captured_user_option == 3:

            connect_server()
            
        else:

            print('Opção digitada não existe!')
            exit(0)
    
    except Exception:
        print('Opção digitada não existe!')
        exit(0)

def main():

    print_logo()
    print_version()
    print_author()
    print_footer()

    print('[1] - Adicionar um servidor')
    print('[2] - Remover um servidor')
    print('[3] - Conectar em um servidor')

    captured_user_option = input()

    process_user_option(captured_user_option)

if __name__ == '__main__':
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ssh.settings')
    main()
