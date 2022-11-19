perintah = ''
print('=' * 50)
print('Masukan perintah [+] [-] [*] [/]')
print('untuk memberhentikan program masukan perintah [exit]')
while perintah != 'exit' :
    print('=' * 50)
    perintah = input('masukkan perintah : ')

    if perintah == 'exit':
        break

    if perintah != '+' and perintah != '-' and perintah != '*' and perintah != '/' :
        print('=' * 50)
        print('perintah tidak di ketahui')
        continue 
    a = eval(input('masukkan bilangan pertama : '))
    b = eval(input ('masukkan bilangan kedua : '))
    if perintah == '+' :
        hasil = a + b
        print(f'hasil dari {a} + {b} =')
    elif perintah == '-' :
        hasil = a - b 
        print(f'hasil dari {a} - {b} =')
    elif perintah == '*' :
        hasil = a * b 
        print(f'hasil dari {a} * {b} =')
    elif perintah == '/':
        hasil = a / b 
        print(f'hasil dari {a} / {b} =')
print('=' * 50)        
print('Terimakasih telah memakai program ini')        

