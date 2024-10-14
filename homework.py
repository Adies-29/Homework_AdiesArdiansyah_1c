nama = input('Masukan Nama : ')
umur = int(input('Masukan Umur : '))

if umur >= 17:
    sim = input('Apakah anda punya SIM (YA/TIDAK) : ').upper()

    if sim == "YA":
        jenis_sim = input('''Jenis SIM anda : (A/C)
:''').upper()
        
        if jenis_sim not in ["C", "A"]:
            print("Data yang anda masukan salah!")
        else:    
            jenis_kendaraan = input('''Kendaraan apa yang ingin anda kendarai ? :
MOBIL/MOTOR
:''').upper()

            if jenis_kendaraan not in ["MOBIL", "MOTOR"]:
                    print("Data yang anda masukan salah!")           
            else: 
                tahun_sim = int(input("Masukan tahun pembuatan SIM anda : "))
                tahun_ini = 2024
                masaberlaku = tahun_ini - tahun_sim 

                if (jenis_sim == "C" and jenis_kendaraan == "MOTOR") or (jenis_sim == "A" and jenis_kendaraan == "MOBIL"):
                        if masaberlaku >= 5:
                            print("SIM anda sudah kadaluarsa, mohon perpanjang.")
                        else:
                            print(f"Selamat, anda layak dan masa berlaku SIM anda sisa {5 - masaberlaku} tahun.")
                else:
                    print("Jenis kendaraan anda tidak cocok.")
    else:
        print("Anda tidak layak karena tidak memilliki SIM.")
else:
    print("Anda belom cukup umur untuk mengendarai kendaraan bermotor.")

    
