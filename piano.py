#https://gameforge.com/en-US/littlegames/magic-piano-tiles/#
import webbrowser
import pyautogui
import keyboard
from time import sleep
import win32api #cliques mais rápidos que o próprio pyautogui
import win32con

webbrowser.open("https://gameforge.com/en-US/littlegames/magic-piano-tiles/#")
sleep(6)
#aceitar termos e seguir:
pyautogui.click(934,419)
sleep(3)
# iniciar o jogo
pyautogui.click(777,640,duration=1)
sleep(7)
#fechar adsense
pyautogui.click(832,650)
sleep(3)
#esperar anúncio
sleep(65)
pyautogui.click(757,592)
sleep(2)


def click(x,y):
    win32api.SetCursorPos((x,y))#onde o mouse deve estar posicionado
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #vai pressionar o mouse , basicamente clica com o botão esquerdo
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #vai soltar o mouse, dá o segundo clique de soltar no botão esquerdo

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(720,501,(0,0,0)):
        click(720,501)
    if pyautogui.pixelMatchesColor(879,445,(0,0,0)):
        click(879,445)
    if pyautogui.pixelMatchesColor(966,484,(0,0,0)):
        click(966,484)
    if pyautogui.pixelMatchesColor(662,475,(0,0,0)):
        click(662,475)