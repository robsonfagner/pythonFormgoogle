# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By  # Importando o módulo By para localizar os elementos
# from selenium.webdriver.chrome.service import Service  # Importando a classe Service para o caminho do ChromeDriver
# from selenium.webdriver.support.ui import WebDriverWait  # Importando a classe WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC  # Importando expected_conditions
#
# # Iniciando o WebDriver com Service para o caminho do chromedriver
# service = Service(r'C:\Python\Bot\chromedriver.exe')  # Caminho do chromedriver
# web = webdriver.Chrome(service=service)  # Usando o Service para passar o caminho
#
# # Acessando o formulário
# web.get('https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')
#
# # Espera até que o primeiro botão esteja visível e clicável (aguarda por até 15 segundos)
# wait = WebDriverWait(web, 15)  # Espera de até 15 segundos
#
# # Função para clicar no botão
# def click_button(xpath):
#     button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#     web.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)  # Rolar até o botão
#     button.click()
#
# # Função para preencher o formulário e enviar
# def preencher_formulario(resposta):
#     # if resposta == 'Interação social limitada':
#     #     click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Interação social limitada
#     # elif resposta == 'Problemas tecnológicos':
#     #     click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Problemas tecnológicos
#     if resposta == 'Organização do tempo':
#         click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')  # Organização do tempo
#     # if resposta == 'Falta de Autodisciplina':
#     #     click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Falta de Autodisciplina
#
#
#     # Enviar o formulário
#     submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
#     submit.click()
#
#     # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
#     time.sleep(2)
#
#     # Recarrega a página para zerar o formulário
#     web.get('https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')
#
# # Repetir as respostas conforme as quantidades solicitadas
# # for _ in range(34):  # Interação social limitada (34 vezes)
# #     preencher_formulario('Interação social limitada')
# #
# # for _ in range(34):  # Falta de Autodisciplina (34 vezes)
# #     preencher_formulario('Falta de Autodisciplina')
# #
# # for _ in range(15):  # Problemas tecnológicos (15 vezes)
# #     preencher_formulario('Problemas tecnológicos')
#
# for _ in range(1):  #  Organização do tempo (14 vezes)
#     preencher_formulario(' Organização do tempo')
#
# # Fechar o navegador
# web.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importando o módulo By para localizar os elementos
from selenium.webdriver.chrome.service import Service  # Importando a classe Service para o caminho do ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait  # Importando a classe WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Importando expected_conditions

# Iniciando o WebDriver com Service para o caminho do chromedriver
service = Service(r'C:\Python\Bot\chromedriver.exe')  # Caminho do chromedriver
web = webdriver.Chrome(service=service)  # Usando o Service para passar o caminho

# Acessando o formulário
web.get(
    'https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')

# Espera até que o primeiro botão esteja visível e clicável (aguarda por até 15 segundos)
wait = WebDriverWait(web, 15)  # Espera de até 15 segundos


# Função para clicar no botão
def click_button(xpath):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    web.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)  # Rolar até o botão
    button.click()


# Função para preencher o formulário e enviar
def preencher_formulario(resposta):
    # Marca a opção com base na resposta
    if resposta == 'Organização do tempo':
        click_button(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')  # Organização do tempo

    # Esperar um pouco mais para garantir que o clique foi registrado
    time.sleep(1)

    # Verificar se o botão de rádio foi selecionado
    selected = web.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')
    if selected.is_selected():
        print(f"Opção '{resposta}' selecionada com sucesso!")
    else:
        print(f"Erro: A opção '{resposta}' não foi selecionada.")

    # Enviar o formulário
    submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
    time.sleep(2)

    # Recarregar a página para zerar o formulário
    web.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')


# Repetir as respostas conforme as quantidades solicitadas
for _ in range(13):  # Organização do tempo (13 vezes)
    preencher_formulario('Organização do tempo')

# Fechar o navegador
web.quit()
