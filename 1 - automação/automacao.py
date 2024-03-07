import pyautogui
import pandas as pd
import time

#Parametro de pausa pra cada comando
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")
time.sleep(3)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
#pausa a parte
time.sleep(2)

pyautogui.click(x=488, y=367)
pyautogui.write("email@empresa.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")
#print(tabela)

pyautogui.PAUSE = 0.05
for linha in tabela.index:
    pyautogui.click(x=519, y=268)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")