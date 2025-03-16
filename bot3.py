import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciando o WebDriver com Service para o caminho do chromedriver
service = Service(r'C:\Python\Bot\chromedriver.exe')  # Caminho do chromedriver
web = webdriver.Chrome(service=service)  # Usando o Service para passar o caminho

# Acessando o formulário
web.get('https://docs.google.com/forms/d/e/1FAIpQLSeFVpqyDiL55qNbB01Iu690YhZAFYrmTQvihDmcFqWssuZeIw/viewform?usp=header')

# Espera até que o primeiro botão esteja visível e clicável (aguarda por até 15 segundos)
wait = WebDriverWait(web, 15)

# Preenchendo os campos de resposta (botões de seleção)
sel_button_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_1.click()

sel_button_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_2.click()

sel_button_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_3.click()

sel_button_4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
web.execute_script("arguments[0].scrollIntoView();", sel_button_4)  # Rolar até o botão 4
sel_button_4.click()

sel_button_5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_5.click()

sel_button_6 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_6.click()

sel_button_7 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_7.click()

sel_button_8 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_8.click()

sel_button_9 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_9.click()

sel_button_10 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_10.click()

sel_button_11 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_11.click()

sel_button_12 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_12.click()

sel_button_13 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_13.click()

sel_button_14 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_14.click()

sel_button_15 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))
sel_button_15.click()

# Rolar até o botão de envio (submit)
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')))
web.execute_script("arguments[0].scrollIntoView();", submit_button)

# Clicar no botão submit (enviar)
submit_button.click()

# Aguardar um pouco para ver o resultado
time.sleep(5)

# Fechar o navegador
web.quit()
