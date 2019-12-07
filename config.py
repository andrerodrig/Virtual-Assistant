import re
from random import choice

version = '1.4.0'

# Apresenta o assistente virtual
def intro() -> None:
    msg = f"Assistente - version {version} by: André"
    print(f"{'-' * len(msg)} \n{msg}\n {'-' * len(msg)}")


# Lista de respostas de erro
errors_list = [
    "Não entendi nada",
    "Não entendi",
    "Desculpe, não entendi",
    "Repita novamente, por favor",
    "Não entendi nada, por favor, repita novamente",
]


# Lista de saudações
greetings = [
    'Oi, tudo bom?'
    'Olá',
    'Oi, como você está',
    'Olá, tudo bem com você?',
]

# dicionário com respostas para cada comando de voz
talk_responses = {
    'Oi': choice(greetings),
    'Olá': choice(greetings),
    'tudo bem, e com voce': 'Tudo bem por aqui também',
    'que bom': 'Ótimo',
    'estou bem, e você': 'Tambem estou bem, obrigada',
    'sim e você': 'Estou bem, obrigada',
    'Abrir Google': 'Ok',
}

commands = {
    "desligar": "desligando",
    "reiniciar": "reiniciando",
}

# verifica o nome
def verify_name(user_name: str) -> str:
    if user_name.startswith("Meu nome é"):
        user_name = user_name.replace('Meu nome é', '')

    if user_name.startswith("Eu me chamo"):
        user_name = user_name.replace('Eu me chamo', '')
        
    if user_name.startswith("Eu sou o"):
        user_name = user_name.replace('Eu sou o', '')
        
    if user_name.startswith("Eu sou a"):
        user_name = user_name.replace('Eu sou a', '')

    return user_name

# verifica se um nome existe no arquivo e dependendo, o insere
# neste arquivo ou não
def verify_exists_name(name: str) -> str:
    with open('data/names.txt', 'r') as data:
        name_list = data.readlines()
    
    if not name_list:
        name_list.append(f'{name}')
        with open('data/names.txt', 'w') as void_data:
            void_data.writelines(name_list)
        
        return f'Olá {name}, prazer em te conhecer!'
    
    else:
        for line in name_list:
            if line == name:
                return f'Olá {name}, como você está?'
        
        name_list.append(f'\n{name}')
        with open('data/names.txt','w') as nvoid_data:
            nvoid_data.writelines(name_list)
        
        return f'Oi {name}. É a primeira vez que nos falamos.'

# tenta abrir o arquivo data/names.txt
# se não conseguir, o cria
def open_names_list() -> None:
    try:
        names = open('data/names.txt', 'r')
        names.close()

    except FileNotFoundError:
        names = open('data/names.txt', 'w')
        names.close()        
