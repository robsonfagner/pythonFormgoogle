#
#
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
# web.get('https://forms.gle/gErbQGmHY1MfbRSR7')
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
#     # Marca a opção com base na resposta
#     if resposta == 'Seria benéfico para interação':
#         click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Seria benéfico para interação
#     elif resposta == 'Seria desnecessário':
#         click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Seria desnecessário
#     if resposta == 'Não tenho certeza':
#         click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Não tenho certeza
#
#     # Esperar o formulário ser marcado antes de enviar
#     time.sleep(1)  # Uma pequena pausa para garantir a marcação
#
#     # Enviar o formulário
#     submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
#     submit.click()
#
#     # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
#     time.sleep(2)
#
#     # Recarregar a página para zerar o formulário
#     web.get('https://forms.gle/gErbQGmHY1MfbRSR7')
#
# # Repetir as respostas conforme as quantidades solicitadas
# for _ in range(79):  # Seria benéfico para interação (79 vezes)
#     preencher_formulario('Seria benéfico para interação familiares')
# for _ in range(9):  # Seria desnecessário (9 vezes)
#     preencher_formulario('Seria desnecessário')
# for _ in range(9):  # Não tenho certeza (9 vezes)
#     preencher_formulario('Não tenho certeza')
#
# # Fechar o navegador
# web.quit()
#
#
#

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
web.get('https://forms.gle/gErbQGmHY1MfbRSR7')

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
    if resposta == 'Seria benéfico para interação familiares':
        click_button(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div')  # Seria benéfico para interação familiares
    elif resposta == 'Seria desnecessário':
        click_button(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div')  # Seria desnecessário
    elif resposta == 'Não tenho certeza':
        click_button(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div')  # Não tenho certeza

    # Esperar um pouco mais para garantir que o clique foi registrado
    time.sleep(1)  # Uma pequena pausa para garantir a marcação

    # Verificar se a opção foi marcada (para garantir que a escolha foi registrada)
    if resposta == 'Seria benéfico para interação familiares':
        selected = web.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div')
        if selected.is_selected():
            print(f"Opção '{resposta}' selecionada com sucesso!")
        else:
            print(f"Erro: A opção '{resposta}' não foi selecionada.")
    elif resposta == 'Seria desnecessário':
        selected = web.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div')
        if selected.is_selected():
            print(f"Opção '{resposta}' selecionada com sucesso!")
        else:
            print(f"Erro: A opção '{resposta}' não foi selecionada.")
    elif resposta == 'Não tenho certeza':
        selected = web.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div')
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
    web.get('https://forms.gle/gErbQGmHY1MfbRSR7')


# Repetir as respostas conforme as quantidades solicitadas
for _ in range(79):  # Seria benéfico para interação familiares (79 vezes)
    preencher_formulario('Seria benéfico para interação familiares')
for _ in range(9):  # Seria desnecessário (9 vezes)
    preencher_formulario('Seria desnecessário')
for _ in range(9):  # Não tenho certeza (9 vezes)
    preencher_formulario('Não tenho certeza')

# Fechar o navegador
web.quit()
