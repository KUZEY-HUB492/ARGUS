import subprocess
import os

from config import (
    EPIC_PATH,
    STEAM_PATH,
    TLAUNCHER_PATH,
    RIOT_CLIENT_PATH,
    BRAVE_PATH,
    OBS_PATH,
    VSCODE_PATH
)


def uygulama_ac(uygulama):
    uygulama = uygulama.lower()

    uygulamalar = {
        "not defteri": "notepad.exe",
        "hesap makinesi": "calc.exe",
        "cmd": "cmd.exe",
        "paint": "mspaint.exe",

        "brave": BRAVE_PATH,
        "epic games": EPIC_PATH,
        "steam": STEAM_PATH,
        "tlauncher": TLAUNCHER_PATH,
        "riot": RIOT_CLIENT_PATH,
        "obs": OBS_PATH,
        "vs code": VSCODE_PATH,
    }


    if uygulama in uygulamalar:
        try:
            subprocess.Popen(uygulamalar[uygulama])
            return f"{uygulama} açılıyor."

        except Exception as e:
            return f"Açılırken hata oluştu: {e}"

    else:
        return "Bu uygulamayı bilmiyorum."


def uygulama_kapat(uygulama):
    uygulama = uygulama.lower()

    uygulamalar = {
        "brave": "brave.exe",
        "epic games": "EpicGamesLauncher.exe",
        "tlauncher": "TLauncher.exe",
        "riot": "RiotClientServices.exe",
        "cmd": "cmd.exe",
        "not defteri": "notepad.exe",
        "paint": "mspaint.exe"
    }


    if uygulama in uygulamalar:
        try:
            subprocess.run(
                f"taskkill /f /im {uygulamalar[uygulama]}",
                shell=True
            )

            return f"{uygulama} kapatılıyor."

        except Exception as e:
            return f"Kapatılırken hata oluştu: {e}"

    return "Bu uygulamayı kapatmayı bilmiyorum."