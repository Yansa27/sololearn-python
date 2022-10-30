#tembak angka
trying = 0 
secret_number = 8
limit = 3 

while trying < 3 :
    guest_number = input('Masukkan angkka 1-9 : ')
    guest_number = int(guest_number)

    if guest_number == secret_number :
        print('Selamat kamu benar')
        break
    trying += 1
print('game selesai')    
