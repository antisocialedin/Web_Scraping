import requests

def ppc():
    file_url = "https://bri.ifsp.edu.br/phocadownload/2016/Eng_Computacao/PPC-%20Engenharia%20de%20Computao%20Birigui%2028-06-16.pdf"

    r = requests.get(file_url, stream = True)

    with open("PPC_Engenharia.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)


def ativi_compl():
    file_url = "https://drive.ifsp.edu.br/s/1D3UQBS8bp78r1M#pdfviewer"

    r = requests.get(file_url, stream = True)

    with open("Validacao_Atividades_Complementares.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)


def plano_gestao():
    file_url = "https://drive.ifsp.edu.br/s/sPCpJQltZEkMjC2#pdfviewer"

    r = requests.get(file_url, stream = True)

    with open("Plano_Gestao-EngComp.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)


def tcc():
    file_url = "https://drive.ifsp.edu.br/s/RocUdpHFpNWp2FS#pdfviewer"
    r = requests.get(file_url, stream = True)
    with open("Regulamento_TCC-EngComp.pdf","wb") as pdf:
         for chunk in r.iter_content(chunk_size=1024):
                   '''
                   writing one chunk at a time to pdf file
                   '''
                   if chunk:
                       pdf.write(chunk)


opc = 0
while opc != 99:
    print('''
    Engenharia da Computação  
    [1]Baixar PPC 
    [2]Baixar Regulamento para alidação de Atividades Complementares
    [3]Plano de Gestão do Curso
    [4]Regulamento TCC 
    [99]Sair ''')

    opc = int(input('Digite a opção desejada?'))
    if opc == 1: 
        ppc()
        print('Download Concluido!')
    elif opc == 2: 
        ativi_compl()
        print('Download Concluido!')
    elif opc == 3: 
        plano_gestao()
        print('Download Concluido!')
    elif opc == 4: 
        tcc()
        print('Download Concluido!')
    else:
        print('Opção Inválida!!')
    print('=-=' * 10)


print('Fim do Programa!!')

