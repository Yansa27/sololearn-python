name =input('masukkan nama anda : ')
perintah = ''
while perintah != 'exit' :
    perintah = input('masukkan perintah : ')

    if perintah == 'yes' :
        print(f'selamat datang yansa')
        array = [2 , 4 , 5 , 6 , 7 , 3, 2 , 4]

        for item in array :
            if item % 2  == 0 :
                print(f'{item} bilangan genap')
            else :
                print(f'{item} bilangan ganjil')    
                break


    else :
        print('oke')
        break

