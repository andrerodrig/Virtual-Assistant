import speech_recognition as sr
import pyttsx3
from random import choice
import config as cfg
import re
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicia o módulo de voz
engine = pyttsx3.init()



# voz fala o texto passado como parâmetro
def talk(response: str) -> None:
    engine.say(response)
    engine.runAndWait()



def assistant():
#--------------------------------------------------------------------------------
    print('Oi, qual é o seu nome?')
    talk('Oi, qual é o seu nome?')

    while True:
        random_err_response = choice(cfg.errors_list)
        rec = sr.Recognizer()

        mic = sr.Microphone()

        with mic as source:
            rec.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = rec.listen(source)
                    input_data = rec.recognize_google(audio, language='pt-br')
                    user_name = cfg.verify_name(input_data)

                    cfg.open_names_list()
                    presentation = f'{cfg.verify_exists_name(user_name)}'
                    print(presentation)
                    talk(presentation)

                    user_name = user_name.split(' ')[0]
                    break
                except sr.UnknownValueError:
                    talk(random_err_response)
        break
    #--------------------------------------------------------------------------------
    print('=' * len(presentation))
    print("Ouvindo")

    while True:
        random_err_response = choice(cfg.errors_list)
        rec = sr.Recognizer()

        mic = sr.Microphone()

        with mic as source:
            rec.adjust_for_ambient_noise(source)

            while True:
                try:

                    audio = rec.listen(source)
                    input_data = rec.recognize_google(audio, language='pt-br')
                    print(f"{user_name}: {input_data}")
                    
                    if 'Abrir Google' in input_data:
                        reg_ex = re.search('abrir google (.*)', input_data)
                        url = 'https://www.google.com/'
                        if reg_ex:
                            subgoogle = reg_ex.group(1)
                            url = url + 'r/' + subgoogle
                        webbrowser.open(url)
                        print('Ok!')
                    

                    if 'Abrir Google e pesquisar' in input_data:
                        reg_ex = re.search('abrir google e pesquisar (.*)', input_data)
                        search_for = input_data.split('pesquisar',1)[1]
                        print(search_for)
                        url = 'https://www.google.com/'
                        if reg_ex:
                            subgoogle = reg_ex.group(1)
                            url = url + 'r/' + subgoogle
                        talk('Ok!')
                        driver = webdriver.Firefox(executable_path='C:\\Users\\andre\\Documents\\computer_engineering\\python\\virtual-assistant\geckodriver')
                        driver.get('https://www.google.com')
                        search = driver.find_element_by_name('q')
                        search.send_keys(str(search_for))
                        search.send_keys(Keys.RETURN)



                    else:
                        talk_response = cfg.talk_responses[input_data]
                        print(f'Assistente: {talk_response}')
                        talk(f'{talk_response}')

                except sr.UnknownValueError:
                    talk(random_err_response)
            

if __name__ == '__main__':
    cfg.intro()
    talk('Iniciando')
    assistant()