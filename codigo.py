# Passo a passo 
# Passo 1 - Entrar no sistema
# Passo 2 - Fazer Login
# Passo 3 - Importar base de dados 
# Passo 4 - Cadastrar produto
# Passo 5 - Repetir até acabar a lista de produtos 

import pyautogui 
import time
import pandas

#pyautogui.click - clicar com o mouse 
#pyautogui.write - escrever um texto 
#pyautogui.press - apertar 1 tecla
#pyautogui.hotkey - combinação de teclas (Ctrl C)
#pyautogui.scroll - rolar a tela para cima ou para baixo

# Passo 1 - Entrar no sistema
pyautogui.PAUSE = 0.5

pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("Enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(3)

# Passo 2 - Fazer Login
pyautogui.click(x=708, y=371)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("salvesalve909090")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3 - Importar base de dados 

tabela = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar produto
# Passo 5 - Repetir até acabar a lista de produtos 
for linha in tabela.index:
    #codigo
    pyautogui.click(x=731, y=260) 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    #tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    #categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    #preço unitario
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    #custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    #obs    
    pyautogui.press("tab")
    observacao = str(tabela.loc[linha, "obs"])
    if observacao != 'nan':
        pyautogui.write(observacao)

    #clicar no botão de enviar  
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) 

