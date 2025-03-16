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
web.get(
    'https://docs.google.com/forms/d/e/1FAIpQLSeFVpqyDiL55qNbB01Iu690YhZAFYrmTQvihDmcFqWssuZeIw/viewform?usp=header')

# Espera até que o primeiro botão esteja visível e clicável (aguarda por até 5 segundos)
wait = WebDriverWait(web, 5)  # Tempo de espera mais curto


# Função para clicar em um botão
def click_button(xpath):
    try:
        button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        web.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)  # Rolar até o botão
        button.click()
    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


# Função para preencher o formulário e enviar
def preencher_formulario():
    # Preenchendo os campos de resposta (botões de seleção)
    for i in range(1, 19):
        click_button(
            f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i}]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')

    # Rolar até o botão de envio (submit) e enviar o formulário
    try:
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')))
        web.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)  # Rolar até o botão submit
        submit_button.click()  # Clicar no botão de envio
        print("Formulário enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar o formulário: {e}")

    # Aguardar até que a página de confirmação seja carregada
    try:
        confirmation = WebDriverWait(web, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span'))
        )
        print("Página de confirmação carregada.")
    except:
        print("Erro: Página de confirmação não carregada.")

    # Espera antes de preencher novamente
    time.sleep(1)  # Ajuste para permitir que o formulário seja processado corretamente

    # Redirecionar para o formulário novamente
    web.get(
        'https://docs.google.com/forms/d/e/1FAIpQLSeFVpqyDiL55qNbB01Iu690YhZAFYrmTQvihDmcFqWssuZeIw/viewform?usp=header')


# Repetir o preenchimento e envio 20 vezes
for i in range(20):
    print(f"Preenchendo e enviando o formulário pela {i + 1}ª vez...")
    preencher_formulario()

# Fechar o navegador
web.quit()




