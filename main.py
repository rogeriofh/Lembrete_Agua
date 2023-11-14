import time
import pyautogui
import schedule
# Mensagem a ser enviada
mensagem = 'Seu Marido alerta: Hora de beber agua! 💧'

# Função para enviar mensagem no WhatsApp Desktop
def enviar_mensagem():
    pyautogui.PAUSE = 3
    pyautogui.press('win')
    pyautogui.write('Whatsapp')
    pyautogui.press('enter')
    pyautogui.write('amor')
    pyautogui.click(x=244, y=227) #Point(x=244, y=227)
    pyautogui.write(mensagem)
    pyautogui.press('enter')

schedule.every().hour.do(enviar_mensagem)

#Executar indefinidamente
while True:
    schedule.run_pending()
    time.sleep(1)


