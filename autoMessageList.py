import time
import keyboard
import webbrowser as web
import pyautogui as pg
from pywhatkit.core import core, log

pg.FAILSAFE = False

try:
    core.check_connection()
    print("✅ İnternet bağlantısı başarılı.\n")
except Exception as e:
    print(f"❌ İnternet bağlantısı hatası: {e}")
    exit()


def wait_for_whatsapp():
    print("📌 Lütfen WhatsApp Web'in açılmasını bekleyin ve QR kodunu taratın.")
    input("➡ QR kod tarandıysa ve WhatsApp açıldıysa Enter'a basın...")


def close_current_tab():
    keyboard.press_and_release("ctrl+w")
    time.sleep(1)


def send_auto_msg(phone_no: str, message: str, wait_time: int = 15):
    try:
        close_current_tab()
        web.open(f"https://web.whatsapp.com/send?phone={phone_no}")
        print(f"📨 {phone_no} numarasına mesaj gönderiliyor...")

        for _ in range(wait_time):
            if pg.locateOnScreen("whatsapp_message_box.png", confidence=0.99):
                break
            time.sleep(1)

        pg.click(pg.size().width // 2, pg.size().height // 2)
        time.sleep(3)

        keyboard.write(message)
        keyboard.press("enter")
        log.log_message(_time=time.localtime(), receiver=phone_no, message=message)

        print(f"✅ {phone_no} numarasına mesaj başarıyla gönderildi.")

        time.sleep(3)

    except Exception as e:
        print(f"❌ Hata oluştu ({phone_no}): {e}")


print("📌 WHATSAPP OTOMATİK MESAJ BOTU\n")
print("⚠️ DİKKAT: BOT ÇALIŞIRKEN BİLGİSAYARINIZI KULLANMAYINIZ!\n")

phone_numbers = [
   "+905345820441"
]


message = (
    "Tekrardan merhaba, bildiğiniz gibi GameNight etkinliğimizde asıl kontenjana dahilsiniz!🥳 "
    "Etkinliğimize kesin katılım sağlayacaksanız en geç 23 Mayıs Cuma günü 18.00'e kadar haber vermenizi rica ediyoruz, "
    "aksi takdirde hakkınız yedek kontenjana devredilecektir.🌼\n\n"
    "Dipnot: Etkinliğimizin kurallarını hatırlamak için aşağıdaki bağlantıyı kullanabilirsiniz:\n"
    "https://drive.google.com/file/d/1Ns8gKqt4si_Htu3kk5X4Yh-Fqsy8c-mn/view?usp=sharing"
)


wait_for_whatsapp()

for phone_num in phone_numbers:
    send_auto_msg(phone_num, message)
    time.sleep(2)

print("🎉 Tüm mesajlar başarıyla gönderildi!")
