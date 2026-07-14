from datetime import datetime

def komut_calistir(komut):
    komut = komut.lower().strip()

    if komut == "merhaba":
        return "Merhaba. Sana nasıl yardımcı olabilirim?"

    elif komut == "yardım":
        return (
            "Kullanabileceğin komutlar:\n"
            "- merhaba\n"
            "- yardım\n"
            "- saat\n"
            "- tarih"
        )

    elif komut == "saat":
        return datetime.now().strftime("%H:%M:%S")

    elif komut == "tarih":
        return datetime.now().strftime("%d.%m.%Y")

    return None