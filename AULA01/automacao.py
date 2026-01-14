#imporatações necessárias
import pyautogui
import time 
import pandas as pd

#Lê a base de dados CSV com a lib pandas
tabela = pd.read_csv("AULA01/produtos.csv")

#Intervalo de tempo (s) para executar cada comando do pyautogui
pyautogui.PAUSE = 1

#Abrindo o sistema através do chrome
pyautogui.press("win")  
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Espera o sistema carregar
time.sleep(5)

#Fazer login no sistema
pyautogui.click(x=753, y=503)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaTeste123")
pyautogui.click(x=956, y=711)

#Percorrer as linhas da tabela adicionando os produtos

for linha in tabela.index:
    pyautogui.click(x=605, y=368)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")
    pyautogui.scroll(5000)
