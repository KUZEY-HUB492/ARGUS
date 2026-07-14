from core.commands import komut_calistir

print("========== ARGUS v0.3 ==========")
print("Yazılı mod aktif.")
print("Çıkmak için 'çık' yaz.\n")

while True:
    komut = input("Sen > ").strip()

    if not komut:
        continue

    if komut.lower() == "çık":
        print("ARGUS > Görüşmek üzere.")
        break

    cevap = komut_calistir(komut)

    if cevap:
        print(f"ARGUS > {cevap}")
    else:
        print("ARGUS > Bu komutu henüz bilmiyorum.")