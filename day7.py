 #operator perbandingan
pagi = input('Apakah sekarang waktu pagi? y/t : ')
if pagi == 'y' :
    pagi = True
    print('Selamat Pagi')
else:
    print('Selamat Malam')   

#operator logika
name = input('Masukkan nama kamu : ')
if len(name) >= 6 :
    print(f'Selamat Datang {name}')
else:    
    print('Nama kamu Terlalu pendek')