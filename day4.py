# buat kalkulator
from subprocess import call


name =input("Masukkan Nama Anda : ")

print("Selamat Datang " + name)

print('=' * 25)
print(' 1. tambah    \t   [+]')
print(' 2. kurang   \t   [-]')
print(' 3. kali     \t   [*]')
print(' 4. bagi    \t   [/]')
print('=' * 25)

operasi = input('Pilih operasi 1/2/3/4 : ')
bilangan_1 = eval(input('Masukkan Nilai ke 1 : '))
bilangan_2 = eval(input('Masukkan Nilai ke 2 : '))

print('=' * 25)
if operasi == '1':
 print('User memilih penjumlahan')
elif operasi == '2':
    print('user memilih pengurangan')
elif operasi == '3':
    print('user menilih perkalian')    
elif operasi == '4':
    print('user memilih pembagian')  
else:
    print('tidak valid')

print('=' * 25)
if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'Hasil dari operasi {bilangan_1} + {bilangan_2} = {hasil} ')
elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'Hasil dari operasi {bilangan_1} - {bilangan_2} = {hasil} ') 
elif operasi == '3':
    hasil = bilangan_1 * bilangan_2 
    print(f'Hasil dari operasi {bilangan_1} * {bilangan_2} = {hasil} ')
elif operasi == '4':
    hasil = bilangan_1 / bilangan_2 
    print(f'Hasil dari operasi {bilangan_1} / {bilangan_2} = {hasil} ')   
else:
    print("Tidak Valid")    