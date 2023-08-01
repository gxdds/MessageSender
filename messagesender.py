import pyautogui
import emoji
import time

pyautogui.PAUSE = 0.5

i = 0
p = str(input('Digite o nome de quem você deseja mandar mensagem: '))
m = str(input('Digite a mensagem que deseja enviar: '))
v = int(input('Digite quantas vezes deseja enviar essa mensagem: '))
inicio = str(input('Deseja iniciar o envio de mensagens? [S/N]: '))
        
if inicio in'Ss':
#abrir o zap (app da microsoft store)
    pyautogui.press("win")
    pyautogui.write("whatsapp")
    pyautogui.press("enter")

    time.sleep(5)

    #pesquisar a pessoa
    pyautogui.click(x=208, y=195)
    
    #escrever a msg
    pyautogui.write(p)
    time.sleep(2)
    pyautogui.click(x=236, y=263)
    
    for c in range(0, v): #contador de vezes / se quiser infinito só fazer um while
        pyautogui.write(m)
        #mandar
        pyautogui.press("enter")
else:
    print('Ok, envio de mensagens cancelado.')
