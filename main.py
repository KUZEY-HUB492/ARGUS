from brain import cevap_ver
from commands import komut_calistir
from tts import konus

print("ARGUS başlatılıyor...")

while True:

    komut = input("Sen: ").lower()

    if komut == "çık":
        mesaj = "Görüşmek üzere efendim."
        print("ARGUS:", mesaj)
        konus(mesaj)
        break

    cevap = komut_calistir(komut)

    if cevap:
        print("ARGUS:", cevap)
        konus(cevap)
        continue

    cevap = cevap_ver(komut)
    print("ARGUS:", cevap)
    konus(cevap)