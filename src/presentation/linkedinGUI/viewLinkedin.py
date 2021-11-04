from PySimpleGUI import PySimpleGUI as sg
from src.domain.linkedin.entities.userEntitie import User
from src.domain.linkedin.repository.linkedinRepository import LinkedinRepository

# layout
sg.theme('DarkBlue2')

layout = [

    [sg.Text('E-mail'), sg.Input(key='email',
                                 size=(40, 1))],
    [sg.Text('Senha'), sg.Input(key='password',
                                password_char='*', size=(40, 1))],
    [sg.Text('Cargo'), sg.Input(key='filtroCargo', size=(40, 1))],
    [sg.Text('Região'), sg.Input(key='filtroRegiao', size=(40, 1))],

    [sg.Button('Pesquisar Avulso', button_color=(
        'white', 'green'), key='btnPesquisaAvulso'), sg.Button('Pesquisar Filtro', button_color=(
            'white', 'blue'), key='btnPesquisaFiltro')]

]
# janela
janela = sg.Window('Tela de Login', layout)

# ler eventos
while True:

    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break

    linkRepo = LinkedinRepository()

    if eventos == 'btnPesquisaAvulso':
        usuario = User(valores['email'], valores['password'],
                       valores['filtroCargo'], valores['filtroRegiao'], 1)

    if eventos == 'btnPesquisaFiltro':
        usuario = User(valores['email'], valores['password'],
                       valores['filtroCargo'], valores['filtroRegiao'], 2)

    linkRepo.start(usuario)
