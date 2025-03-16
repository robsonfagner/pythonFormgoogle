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

# Qual a sua faixa etária?
    # Menos de 20 anos
sel_button_1 = web.find_element((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/label/div/div[2]/div/span'))

# Quais são suas principais motivações para escolher a educação a distância (EAD)?
    # Flexibilidade de horário
sel_button_2 = web.find_element((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'))

# Qual é a sua ocupação profissional principal?
    #Trabalho em periodo integral
sel_button_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

# Você tem compromissos familiares que influenciam sua escolha pela EAD?
    #Sim
sel_button_4 = wait.until(EC.element_to_be_clickable(('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Qual é a sua área geográfica de origem?
    #Área urbana
sel_button_5 = wait.until(EC.element_to_be_clickable(('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Como você busca esclarecer suas dúvidas acadêmicas em cursos EAD?
    #Participando de Foruns On Line
sel_button_6 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Quais das seguintes dificuldades você enfrenta frequentemente em cursos EAD?
    #Autodisciplina
sel_button_7 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Quais são as principais dificuldades que você enfrenta ao participar de cursos EAD durante a graduação?
    #Autodisciplina também
sel_button_8 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Quais são os principais desafios relacionados à autodisciplina e à organização do tempo para você em cursos EAD?
   #Manter a disciplina
sel_button_9 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Como as dificuldades tecnológicas, como problemas de conectividade ou familiaridade com as plataformas, impactam sua experiência em cursos EAD?
    #Causam frustração
sel_button_10 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Como a ausência de interação social afeta seu sentimento de pertencimento e motivação em cursos EAD? Isso impacta seu bem-estar emocional e acadêmico?
    #Afeta negativamente
sel_button_10 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Quais estratégias você considera úteis para melhorar sua autodisciplina e organização do tempo em estudos EAD?
    #Definir metas regulares
sel_button_11 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Como você acha que poderiam ser promovidas interações mais significativas entre alunos e professores em ambientes virtuais de aprendizagem?
    #Sessões de chat ao vivo
sel_button_12 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Que tipos de suporte tecnológico ou treinamento poderiam ser implementados para minimizar as dificuldades tecnológicas enfrentadas por alunos EAD?
    #Workshops de familiarização com plataformas
sel_button_13 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Quais abordagens você acredita que poderiam criar um senso de comunidade e pertencimento entre alunos EAD, apesar da falta de encontros presenciais?
    #Grupos de estudo online
sel_button_14 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))

#Qual é sua opinião sobre a possibilidade de integração de elementos presenciais opcionais em cursos EAD, como workshops ou encontros ocasionais?
    #Seria benéfico para interação

sel_button_15 = wait.until(EC.element_to_be_clickable(('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span')))


# Clicar nos dois botões
sel_button_1.click()
sel_button_2.click()
sel_button_3.click()
sel_button_4.click()
sel_button_5.click()
sel_button_6.click()
sel_button_7.click()
sel_button_8.click()
sel_button_9.click()
sel_button_10.click()
sel_button_11.click()
sel_button_12.click()
sel_button_14.click()
sel_button_15.click()



submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
submit.click()
# Aguardar um pouco para ver o resultado
time.sleep(2)

# Fechar o navegador
web.quit()


