from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Importando a classe Service

class Bot:
    def __init__(self):
        # Criando um objeto Service com o caminho do chromedriver
        service = Service(r'C:\Python\Bot\chromedriver.exe')
        
        # Inicializando o WebDriver com o Service
        self.driver = webdriver.Chrome(service=service)

        def preencherForms(self):
            drive = self.drive
            drive.get('https://docs.google.com/forms/d/1ic3PVomvWXLMlx7'
            'f5YC0MmHwNviMsfvY7o34m_ZHS8o/edit?pli=1')

# Criando a instância do bot
bot = Bot()
bot.preencherForms()