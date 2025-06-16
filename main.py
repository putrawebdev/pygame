import random

nama = "WELCOME THE PYGAME"

print(f'''==========================
=== {nama} ===
==========================
''')

namasaya = input("halo nama kamu siapa: ")

print(f'hai {namasaya} selamat datang di pygame')

print('''
{_} {_} {_} {_}
''')
jawabanasli = 1
jawabanuser = input("coba lihat kolom diatas, menurutmu di kolom berapa py berada? (1/2/3/4)= ")
lanjutga = input("apakah kamu yakin? (y/n) = ")
match jawabanasli : 
    case 1:
        if jawabanuser == "1" and lanjutga == "y":
            print('''
            {🙆‍♂️} {_} {_} {_}
            ''')
            print(f'WAWWW KAMU BENAR PY ADA DI NOMER {jawabanasli}, KAMU MENANG')
        else:
            print(f'yahh kamu kalahhh PY ada di nomer {jawabanasli}')
    case 2:
        if jawabanuser == "2" and lanjutga == "y":
            print('''
            {_} {🙆‍♂️} {_} {_}
            ''')
            print(f'WAWWW KAMU BENAR PY ADA DI NOMER {jawabanasli}, KAMU MENANG')
        else:
            print(f'yahh kamu kalahhh PY ada di nomer {jawabanasli}')
    case 3:
        if jawabanuser == "3" and lanjutga == "y":
            print('''
            {_} {_} {🙆‍♂️} {_}
            ''')
            print(f'WAWWW KAMU BENAR PY ADA DI NOMER {jawabanasli}, KAMU MENANG')
        else:
            print(f'yahh kamu kalahhh PY ada di nomer {jawabanasli}')
    case 4:
        if jawabanuser == "4" and lanjutga == "y":
            print('''
            {_} {_} {_} {🙆‍♂️}
            ''')
            print(f'WAWWW KAMU BENAR PY ADA DI NOMER {jawabanasli}, KAMU MENANG')
        else:
            print(f'yahh kamu kalahhh PY ada di nomer {jawabanasli}')

