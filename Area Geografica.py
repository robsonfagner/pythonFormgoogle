

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
web.get('https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')

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
    if resposta == 'Área Rural':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Área Rural
    elif resposta == 'Área Suburbana':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Área Suburbana
    elif resposta == 'Área Urbana':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Área Urbana

    # Esperar o formulário ser marcado antes de enviar
    time.sleep(1)  # Uma pequena pausa para garantir a marcação

    # Enviar o formulário
    submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
    time.sleep(2)

    # Recarregar a página para zerar o formulário
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')

# Repetir as respostas conforme as quantidades solicitadas
for _ in range(63):  # Área Rural (63 vezes)
    preencher_formulario('Área Rural')

for _ in range(23):  # Área Suburbana (23 vezes)
    preencher_formulario('Área Suburbana')

for _ in range(11):  # Área Urbana (11 vezes)
    preencher_formulario('Área Urbana')

# Fechar o navegador
web.quit()



