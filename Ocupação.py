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
    if resposta == 'Trabalho em período integral':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Trabalho em período integral
    elif resposta == 'Estudante em período integral':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')  # Estudante em período integral
    elif resposta == 'Trabalho em meio período':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Trabalho meio período
    elif resposta == 'Desempregado':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Desempregado

    # Enviar o formulário
    submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
    time.sleep(2)

    # Recarrega a página para zerar o formulário
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSf15dmpYRr_EQ0qywZJXVX2gAZt8Dj2uzqhqbFAKiAwywYOKw/viewform?usp=dialog')

# Repetir as respostas conforme as quantidades solicitadas
# for _ in range(37):  # Trabalho em período integral (37 vezes)
#     preencher_formulario('Trabalho em período integral')
#
# for _ in range(31):  # Estudante em período integral (31 vezes)
#     preencher_formulario('Estudante em período integral')
#
# for _ in range(17):  # Trabalho em meio período (17 vezes)
#     preencher_formulario('Trabalho em meio período')

for _ in range(11):  # Desempregado (12 vezes)
    preencher_formulario('Desempregado')

# Fechar o navegador
web.quit()


