# IMPORTANDO TODAS AS BIBLIOTECAS NECESSARIAS PARA MANIPULAÇÃO DOS DADOS WEB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge import options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
# IMPORTANDO TODAS AS BIBLIOTECAS PARA CONTROLA O TEMPO DE EXECUÇÃO DO CÓDIGO
from time import sleep

# Realizado a instalação do Gerenciamento do EDGE DRIVER para não ter preocupação com a versão do EDGE instalada atual
service = Service(EdgeChromiumDriverManager().install())

# Configurar as opções do Edge
options = webdriver.EdgeOptions()
options.add_experimental_option("prefs", {
    # Manipulando o local que vai ser armazenado o local de dowloads
    "download.default_directory": r'C:\Users\ezequ\OneDrive\Documentos\PROJETOS_POWER_BI_P\DADOS_COVID_BRASIL',
    # Desativar a opção de confirmação de Dowload para realizar o download sem solicitar confirmação
    "download.prompt_for_download": False,
    # Desativado atualizações para evitar erros de versões divergentes
    "download.directory_upgrade": True,
    # Ativando proteção de navegação para evitar pup's indesejados
    "safebrowsing.enabled": True})
    # Realizado leitura de forma visual para executar de forma invisivel trocar para "--headless" 
options.add_argument("--incognito")

# Iniciar o navegador Chrome
print("Abrindo Navegador")
navegador = webdriver.Edge(service=service, options=options)

# Entrando no site da GOV com os dados do Covid para extrair dados 
navegador.get("https://infoms.saude.gov.br/extensions/covid-19_html/covid-19_html.html")
# Maximizado o Navegador para melhor gerenciamento
navegador.maximize_window()
sleep(10)

# Clicando no botão de painel de todos para extrair todas as informações"
navegador.find_element(By.ID, "btTodos").click()
# Atrasar o códgio em 1 segundos para da tempo dos recursos abrir
sleep(1)

# Clicando no Botão para exportar os dados desejados !!!
navegador.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div[3]/div/div/div[7]/div/article/div[1]/div/div/div/div/div").click()
# Atrasar o códgio em 5 segundos para da tempo da pagina carregar
sleep(10)

# Finalizando a conexão com site
navegador.quit()