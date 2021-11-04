from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from src.domain.linkedin.entities.userEntitie import User
from selenium.webdriver.chrome.options import Options


class ScrapingLinkedinService:
    def __init__(self, usuario: User) -> None:
        self.usuario = usuario

    def loadDriverBrowser(self) -> None:

        # FireFox - Verificar se o driver está na ultima versão, qualquer coisa rebaixar novamente
        # driver = webdriver.Firefox(
        #     executable_path="C:\\Users\\Public\\Documents\\Python_Estudo\\Lab_Python\\src\\domain\\linkedin\\service\\geckodriver.exe")
        # driver.get('https://www.google.com.br')

        # Google - Verificar se o driver está na ultima versão, qualquer coisa rebaixar novamente
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Public\\Documents\\Python_Estudo\\Lab_Python\\src\\domain\\linkedin\\service\\chromedriver.exe", chrome_options=chrome_options)

    def acessSite(self) -> None:
        driver = self.driver
        driver.get(
            'https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    def login(self) -> None:
        driver = self.driver

        user_element = driver.find_element_by_xpath(
            "//input[@name='session_key']")
        user_element.clear()
        # Preenchendo valor
        # user_element.send_keys('caous.g@gmail.com')
        user_element.send_keys(self.usuario.email)

        # Irá buscar o campo senha para preencher
        pass_element = driver.find_element_by_xpath(
            "//input[@name='session_password']")
        pass_element.clear()

        # pass_element.send_keys('gugusn2000')
        pass_element.send_keys(self.usuario.senha)
        pass_element.send_keys(Keys.RETURN)
        time.sleep(5)

    def redirect(self) -> None:
        driver = self.driver
        driver.get('https://www.linkedin.com/feed/')
        time.sleep(10)

        if self.usuario.typeSearch == 1:
            driver.get('https://www.linkedin.com/jobs/')
            time.sleep(5)
        if self.usuario.typeSearch == 2:
            self.optionSearchJobs()

    def optionSearchJobs(self) -> None:
        driver = self.driver

        driver.get("https://www.linkedin.com/jobs/search/?keywords="
                   + self.usuario.filtroCargo + "&location=" + self.usuario.filtroRegiao)

        # driver.get(
        #     "https://www.linkedin.com/jobs/search/?keywords=Gerente&location=São%20Paulo,%20Brasil")

        time.sleep(5)

        # for i in range(1, 4):
        #     driver.execute_script(
        #         "window.scrollTo(0,document.body.scrollHeight);")
        #     # Para de executar o robô por 2 segundos para carregar as fotos
        #     time.sleep(2)

    def searchVaga(self) -> None:
        driver = self.driver

        # element = driver.find_elements_by_css_selector(
        #     '.jobs-search-results__list-item')

        # for elem in element:
        #     print(elem.text)
        #     filterNameEnterprise = elem.text
        #     enterpriseName = filterNameEnterprise.split("\n")[0]
        #     linkmoment = elem.get_attribute('href')
        #     print(enterpriseName)

        # element = driver.find_element_by_class_name(
        #     'jobs-search-results__list-item')

        # filterNameEnterprise = element.text

        # enterpriseName = filterNameEnterprise.split("\n")[0]

        # links = driver.find_element_by_link_text(enterpriseName)

        elems = driver.find_elements_by_css_selector(
            ".jobs-search-results__list-item [href]")
        links = [elem.get_attribute('href') for elem in elems]

        print(links)

        # testeone = links.get_attribute('innerHTML')

        # print(testeone)
