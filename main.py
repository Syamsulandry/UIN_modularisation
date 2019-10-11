def hitung_tekanan_fluida(massa_jenis, percepatan_gravitas, ketinggian_fluida):
    tekanan_fluida = massa_jenis * percepatan_gravitas * ketinggian_fluida
    print(f'Tekanan Fluida = {tekanan_fluida} Pascal')

tekanan_fluida = hitung_tekanan_fluida(1, 10, 90)
