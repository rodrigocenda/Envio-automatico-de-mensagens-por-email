import pyautogui as pg
import time
import datetime as dt

data=str(dt.datetime.now())

email=input("Para qual e-mail deseja enviar esta mensagem? \n")        #coleta as credenciais para o envio do email
assunto=input("Qual será o assunto do email? \n ")
mensagem=input("Qual mensagem deseja enviar? Por favor não inclua acentuação no texto \n")
tempo=5
time.sleep(.5)


while tempo!=0:
    print("O programa começará em: ",tempo)
    tempo-=1
    time.sleep(1)
pg.hotkey("win","printscreen")

pg.press("winleft")                                                     #abre o chrome e o gmail
time.sleep(2.5)
pg.write("chrome")
time.sleep(2.5)
pg.press("enter")
time.sleep(5)
pg.write("mail.google.com")
pg.press("enter")
time.sleep(7.5)
pg.click(36,171)
time.sleep(4)
pg.write(email)                                                         #digita o endereço de email
time.sleep(1)
pg.press("tab")
pg.press("tab")
pg.write(assunto)                                                       #digita o assunto do email
time.sleep(0.5)
pg.press("tab")
pg.write(mensagem)                                                      #digita o corpo do email
pg.press("enter")
pg.press("enter")
pg.write("Email enviado em: ")
pg.write(data)
time.sleep(.5)
pg.hotkey("ctrl","v")                                                   #adiciona as datas e o printscreen

time.sleep(5)
pg.click(204,700)                                                       #envia o email