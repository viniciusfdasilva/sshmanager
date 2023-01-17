import os
from getpass import getpass
from utils import print_logo, print_version, print_author, print_footer

def get_ssh(hostname, username, password):

    os.system(f'sshpass -p {password} ssh {username}@{hostname}')


def remove_server():
    pass

def new_server_register():
    
    hostname = input('Digite o endereço do servidor: \n')
    username = input('Digite o usuario do servidor: \n')
    password = getpass('Digite a senha do servidor: \n')



def connect_server():
    pass

def process_user_option(captured_user_option):
    
    try:
        captured_user_option = int(captured_user_option)

        if captured_user_option == 1:

            print('Opção 1')
            new_server_register()
    
        elif captured_user_option == 2:

            print('Opção 2')
            remove_server()

        elif captured_user_option == 3:

            print('Opção 3')
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
    
    main()
