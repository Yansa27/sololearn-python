


password = input('masukkan pasword anda : ')

while password == 'hallo deck' : 
    print ('password benar')
    perintah = input('lanjut atau udahan y/t : ')
    if perintah != 'y' :
        break
    name = input('masukkan nama anda : ')
    if len(name) <= 6 :
        print('nama anda terlalu pendek')
        continue
    tahun_lahir = input('masukkan tahun lahir anda : ')
    tahun_lahir = int(tahun_lahir)
    tahun_lahir = 2022 - tahun_lahir
    print(f'umur kamu {tahun_lahir}')
     

   

    

