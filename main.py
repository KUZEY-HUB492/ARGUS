from core.commands import komut_calistir
from core.parser import komutlari_ayir
from modules.learning import komut_getir


print(r"""
=========================================

        █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗
       ██╔══██╗██╔══██╗██╔════╝ ██║   ██║██╔════╝
       ███████║██████╔╝██║  ███╗██║   ██║███████╗
       ██╔══██║██╔══██╗██║   ██║██║   ██║╚════██║
       ██║  ██║██║  ██║╚██████╔╝╚██████╔╝███████║
       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝


              A R G U S  v1.1.0

        Advanced Response & Guidance
             Utility System

=========================================

Sistem hazır.
""")

print("========== ARGUS v1.1.0 ==========")
print("Yazılı mod aktif.")
print("Çıkmak için 'çık' yaz.\n")

while True:

    komut = input("Sen > ").strip()

    if not komut:
        continue

    if komut.lower() == "çık":
        print("ARGUS > Görüşmek üzere.")
        break

    # Öğrenilmiş komut kontrolü
    ogrenilen = komut_getir(komut)

    if ogrenilen:
        komut = ogrenilen

    if komut.startswith("öğren:"):
        cevap = komut_calistir(komut)
        print(f"ARGUS > {cevap}")
        continue

    # Parser
    komutlar = komutlari_ayir(komut)

    # Çalıştır
    for k in komutlar:

        cevap = komut_calistir(k)

        if cevap:
            print(f"ARGUS > {cevap}")

        else:
            print(f"ARGUS > '{k}' komutunu anlayamadım.")