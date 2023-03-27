import time
import keyboard
import webbrowser as web
import pyautogui as pg
from pywhatkit.core import core, exceptions, log

pg.FAILSAFE = False

core.check_connection()

def sendautomsg(
    phone_no: str,
    message: str,
    message_piece: int,
    wait_time: int = 9,
    tab_close: bool = False,
    close_time: int = 3,):

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
    
    time.sleep(wait_time)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time-8)
    for i in range(message_piece):
        keyboard.write(message)
        keyboard.press("enter")
        time.sleep(2)
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)

print("WHATSAPP OTOMATİK MESAJ BOTUNA HOŞ GELDİNİZ\n")
print("DİKKAT: BOT ÇALIŞIRKEN BİLGİSAYARINIZI KULLANMAYINIZ!\n")
phoneNum = input("Mesaj göndermek istediğiniz numarayı başında 0 olmadan yazınız: ")
messageParam = input("Mesajınızı yazınız: ")
messagePiece = int(input("Göndermek istediğiniz mesaj adedini giriniz: "))

sendautomsg("+90"+phoneNum,messageParam,messagePiece)



