import PySimpleGUI as sg

# funções só pro arquivo de texto
def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close
    except:
        print("Erro na criação do arquivo")
    else:
        print("Arquivo {} criado com sucesso." .format(nomeArquivo))
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo , 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def EscreveArquivo(nomeArquivo, dados):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print("Erro ao abrir o arquivo")
    else:
        a.write("{}\n" .format(dados))
        a.close()
def LeituraArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print("Erro na leitura.")
    else:
        return a.readlines()
    finally:
        a.close()
# funções gerais

def CadastraItems(arr, nome, valor, qtd):
    dados = {'Nome': values[0],
     'Valor': float(values[1]),
     'Quantidade': int(values[2])}
    arr.append(dados)
    window["items"].Update(values=arr)
    EscreveArquivo(ArquivoEstoque, dados)

#Criação do arquivo de texto e verificação

ArquivoEstoque = 'ArquivoEstoque.txt'
if existeArquivo(ArquivoEstoque):
    print("Arquivo Localizado no Computador")
    Estoque = LeituraArquivo(ArquivoEstoque)
else:
    Estoque = []
    print("Arquivo inexistente")
    criaArquivo(ArquivoEstoque)

# PYSIMPLE GUI COISAS

sg.theme('DarkAmber')

layout = [[sg.Text('Insira os dados necessários:')],
          [sg.Text('Nome do produto:'), sg.InputText()],
          [sg.Text('Valor:'), sg.InputText()],
          [sg.Text('Quantidade:'), sg.InputText()],
          [sg.Button('Cadastrar'), sg.Button('Fechar')],
          [sg.Listbox(values=Estoque, size=(50, 30), key="items")]]

window = sg.Window('Gerenciador de Estoque', layout)

#Loop pra rodar o programa
while True:
    event, values = window.read()
    # Fechar tela
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    elif event == 'Cadastrar':
        CadastraItems(Estoque, values[0], values[1], values[2])

window.close()