import pyautogui 
from time import sleep
import pyperclip

# Criar uma funcao para poder copiar e colar uma frase com caracteres
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey("Ctrl","v")
    pyautogui.hotkey("Enter")
                     

pyautogui.click(4106,1014,duration=2)
escrever_frase('Olá, bem vindo ao meu mundo AI!')

