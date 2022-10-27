#tugas anak si uin rafah palembang
gaji_lembur = 10000
jam_kerja = 8

print('=' * 25)
name = input('masukkan nama anda : ')
jam_pulang = input('Berapa jam anda Bekerja : ')
jam_pulang = int(jam_pulang)
if jam_pulang <= 8 :
    
    print(f'anda tidak mendapatkan uang lembur')
elif jam_pulang >= 8  :
    uang_lembur = jam_pulang * gaji_lembur
    print(f'anda mendapatkan gaji lembur sebesar : {uang_lembur}')  
else:
    print('Tidak valid')    