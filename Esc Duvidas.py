

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
    if resposta == 'Participando de fóruns online':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Participando de fóruns online
    elif resposta == 'Enviando e-mails para professores':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Enviando e-mails para professores
    if resposta == 'Sala de Tutoria':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')  # Sala de Tutoria
    elif resposta == 'Participando de sessões de chat ao vivo':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Participando de sessões de chat ao vivo

    # Esperar o formulário ser marcado antes de enviar
    time.sleep(1)  # Uma pequena pausa para garantir a marcação

    # Enviar o formulário
    submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
    time.sleep(2)

    # Recarregar a página para zerar o formulário
    web.get('https://forms.gle/gErbQGmHY1MfbRSR7')

# Repetir as respostas conforme as quantidades solicitadas
for _ in range(29):  # Participando de fóruns online (29 vezes)
    preencher_formulario('Participando de fóruns online')
for _ in range(24):  # Sala de Tutoria (24 vezes)
    preencher_formulario('Sala de Tutoria')
for _ in range(29):  # Enviando e-mails para professores (29 vezes)
    preencher_formulario('Enviando e-mails para professores')
for _ in range(15):  # Participando de sessões de chat ao vivo (15 vezes)
    preencher_formulario('Participando de sessões de chat ao vivo')

# Fechar o navegador
web.quit()



