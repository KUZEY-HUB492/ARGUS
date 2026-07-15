import platform
import psutil


def sistem_bilgisi():

    cpu = platform.processor()
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    sistem = platform.system()

    return (
        f"Sistem: {sistem}\n"
        f"İşlemci: {cpu}\n"
        f"RAM: {ram} GB"
    )