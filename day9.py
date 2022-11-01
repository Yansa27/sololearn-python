#50%
nama = input('masukkan nama anda : ')
nim = input('masukkan nim anda : ')
nilai_absensi = eval(input('masukkan nilai absensi anda : '))
nilai_quis = eval(input('masukkan nilai quis anda : '))
nilai_tugas = eval(input('masukkan nilai tugas anda : '))
nilai_mid = eval(input('masukkan nilai mid anda : '))
nilai_uas = eval(input('masukkan nilai uas anda : '))
nilai_huruf = input('masukkan nilai huruf anda : ')
nilai_huruf = int(nilai_huruf)
nilai_akhir = nilai_absensi + nilai_quis + nilai_tugas + nilai_mid + nilai_uas 
nilai_akhir = int(nilai_akhir)
total_nilai = nilai_akhir / 5
print(total_nilai)
if  nilai_huruf >= 90 :
    nilai_huruf = 'A'
elif nilai_huruf >= 80 :
    nilai_huruf = 'B'   
elif nilai_huruf >= 70  :
    nilai_huruf = 'C'
elif nilai_huruf >= 60 :
    nilai_huruf = 'D'  
elif nilai_huruf < 60 :
    nilai_huruf = 'E'      

print(f'{nilai_huruf}')    



