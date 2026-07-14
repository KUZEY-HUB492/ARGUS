import subprocess
from config import TLAUNCHER_PATH


def uygulama_ac(uygulama):
    uygulama = uygulama.lower()

    uygulamalar = {
        "not defteri": "notepad.exe",
        "hesap makinesi": "calc.exe",
        "cmd": "cmd.exe",
        "paint": "mspaint.exe",
        "brave": "brave.exe",
        "minecraft": TLAUNCHER_PATH,
    }

    if uygulama in uygulamalar:
        try:
            subprocess.Popen(uygulamalar[uygulama])
            return f"{uygulama.title()} açılıyor..."
        except Exception as e:
            return f"Hata oluştu: {e}"

    return "Bu uygulamayı tanımıyorum."