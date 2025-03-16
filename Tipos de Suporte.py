
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
    if resposta == ' Workshops de familiarização com plataformas': click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  #  Workshops de familiarização com plataformas
    elif resposta == 'Suporte técnico online': click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span')  # Suporte técnico online
    elif resposta == 'Tutoriais em vídeo': click_button( '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[3]/label/div/div[2]/div/span')  # Tutoriais em vídeo



    # Enviar o formulário
    submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    # Aguardar o envio do formulário e limpar o formulário para o próximo preenchimento
    time.sleep(2)

    # Recarregar a página para zerar o formulário
    web.get('https://forms.gle/gErbQGmHY1MfbRSR7')


# Repetir as respostas conforme as quantidades solicitadas
for _ in range(40):  #  Workshops de familiarização com plataformas (40 vezes)
    preencher_formulario(' Workshops de familiarização com plataformas')
for _ in range(32):  # Suporte técnico online (32 vezes)
    preencher_formulario('Suporte técnico online')
for _ in range(25):  # Tutoriais em vídeo (25 vezes)
    preencher_formulario('Tutoriais em vídeo')

# Fechar o navegador
web.quit()
