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
web.get('https://docs.google.com/forms/d/e/1FAIpQLSeFVpqyDiL55qNbB01Iu690YhZAFYrmTQvihDmcFqWssuZeIw/viewform?usp=header')

# Espera até que o primeiro botão esteja visível e clicável (aguarda por até 10 segundos)
wait = WebDriverWait(web, 15)  # Espera de até 15 segundos

# Função para clicar no botão
def click_button(xpath):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    web.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)  # Rolar até o botão
    button.click()

# Preenchendo os campos de resposta (botões de seleção)
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Menos de 20 anos
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Flexibilidade de horário
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Trabalho em periodo integral
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Sim (compromissos familiares)
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Área urbana
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Participando de Foruns On Line
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Autodisciplina
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Autodisciplina também
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Manter a disciplina
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Causam frustração
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Afeta negativamente
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Definir metas regulares
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Sessões de chat ao vivo
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Workshops de familiarização com plataformas
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Grupos de estudo online
click_button('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')  # Seria benéfico para interação

# Enviar o formulário
submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
submit.click()

# Aguardar um pouco para ver o resultado
time.sleep(2)

# Fechar o navegador
web.quit()
