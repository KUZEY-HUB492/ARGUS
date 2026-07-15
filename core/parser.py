def komutlari_ayir(komut):
    ayiricilar = [
        " ve ",
        " sonra ",
        " ardından ",
        ","
    ]

    komutlar = [komut]

    for ayirici in ayiricilar:
        yeni = []

        for k in komutlar:
            yeni.extend(k.split(ayirici))

        komutlar = yeni

    return [k.strip() for k in komutlar if k.strip()]