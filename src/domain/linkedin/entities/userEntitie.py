

class User:
    """Classe com objetivo para carregar os filtros para pesquisa"""

    def __init__(self: object, email: str, senha: str, filtroCargo: str, filtroRegiao: str, tipoBusca: int):
        self._email = email
        self._senha = senha
        self._filtroCargo = filtroCargo
        self._filtroRegiao = filtroRegiao
        self._typeSearch = tipoBusca

    @property
    def email(self) -> str:
        return self._email

    @property
    def senha(self) -> str:
        return self._senha

    @property
    def filtroCargo(self) -> str:
        return self._filtroCargo

    @property
    def filtroRegiao(self) -> str:
        return self._filtroRegiao

    @property
    def typeSearch(self) -> int:
        return self._typeSearch
