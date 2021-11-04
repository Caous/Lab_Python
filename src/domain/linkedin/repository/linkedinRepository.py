
from src.domain.linkedin.service.scrapinglinkedinService import ScrapingLinkedinService
from src.domain.linkedin.entities.userEntitie import User


class LinkedinRepository:
    def __init__(self) -> None:
        pass

    def start(self, usuario: User) -> None:

        teste = ScrapingLinkedinService(usuario)
        teste.loadDriverBrowser()
        teste.acessSite()
        teste.login()
        teste.redirect()
