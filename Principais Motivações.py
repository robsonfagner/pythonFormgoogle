

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
    if resposta == 'Conciliação com trabalho ou responsabilidades familiares':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Conciliação com trabalho ou responsabilidades familiares
    elif resposta == 'Flexibilidade de horário':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Flexibilidade de horário
    if resposta == 'Localização geográfica':
        click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[4]/label/div/div[2]/div/span')  # Localização geográfica

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
for _ in range(55):  # Conciliação com trabalho ou responsabilidades familiares (55 vezes)
    preencher_formulario('Conciliação com trabalho ou responsabilidades familiares')
for _ in range(27):  # Flexibilidade de horário (27 vezes)
    preencher_formulario('Flexibilidade de horário')
for _ in range(15):  # Localização geográfica (15 vezes)
    preencher_formulario('Localização geográfica')

# Fechar o navegador
web.quit()



