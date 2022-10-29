print('=' * 50)
print(' 1. Biaya parkir mobil perjam \t : 20000 ')
print(' 2. Biaya parkir motor perjam \t : 30000 ')
print('=' * 50)

mobil = 30000
motor = 20000
perjam = input('Berapa jam anda parkir? :')
perjam = int(perjam)
jenis_kendaraan = input('Jenis kendaraan anda? : ')
if jenis_kendaraan == 'mobil' :
    total = perjam * mobil
    print(f'Karcis sebesar 30000/jam anda parkir selama : {perjam}jam = {total}')
elif jenis_kendaraan == 'motor':
    total = perjam * motor
    print(f'karcis seharga 20000/jam anda parkir selama : {perjam}jam = {perjam} * {motor} = {total}') 
else:
    print('tidak valid')    


