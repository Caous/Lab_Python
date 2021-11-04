from PySimpleGUI import PySimpleGUI as sg


# layout
sg.theme('Reddit')

inputs = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(40, 1))],
    [sg.Text('Senha'), sg.Input(key='password',
                                password_char='*', size=(40, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# janela
janela = sg.Window('Tela de Login', inputs)
# ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == "admin" and valores['password'] == "123":
            print("Bem-vindo")
