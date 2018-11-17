import time
import string
import random
from os import system,name
#import getpass

def clear():
    if name=='nt':
        _=system('cls')
    else:
        _=system('clear')

def randomChar(digit,voucher):
    voucherCreate=''.join(random.choice(string.ascii_letters)for x in range(digit))
    voucher=voucherCreate.upper()
    return voucher

class dagangan():
    hargaTotal=0
    hargaBarang=[]
    jumlahBarang=0
    #Variabel Makanan
    jumlahMakanan=[]
    makananDipesan=[]
    hargaMakanan=[]
    #Variabel Minuman
    jumlahMinuman=[]
    minumanDipesan=[]
    hargaMinuman=[]
    def __init__(self):
        print('-----------------------')

    def jumlahHarga(self):
        for x in range(0,len(dagangan.hargaBarang)):
            dagangan.hargaTotal=dagangan.hargaTotal+dagangan.hargaBarang[x]
        
class makanan(dagangan):
    def __init__(self):
        print('-----------------------')
    def menuMakanan(self):
        a=True
        harga=0
        c=''
        while a is True:
            print('~DAFTAR MENU MAKANAN~\n')
            print('1. Sop Iga     Rp.25000\n'
                  '2. Sate Ayam   Rp.15000\n'
                  '3. Soto Ayam   Rp.13000\n'
                  '4. Nasi Goreng Rp.10000\n'
                  '5. Gado gado   Rp.10000\n'
                  '6. Ketoprak    Rp.10000\n'
                  '7. Nasi Pecel  Rp.7000\n'
                  '8. Nasi        Rp.4000\n'
                  '0. KEMBALI')
            print('-----------------------')
            try:
                pilihMakanan=int(input('\nPilih Nomor Makanan: '))
                if pilihMakanan==1:
                    harga=25000
                    c='Sop Iga'
                elif pilihMakanan==2:
                    harga=15000
                    c='Sate Ayam'
                elif pilihMakanan==3:
                    harga=13000
                    c='Soto Ayam'
                elif pilihMakanan==4:
                    harga=10000
                    c='Nasi Goreng'
                elif pilihMakanan==5:
                    harga=10000
                    c='Gado gado'
                elif pilihMakanan==6:
                    harga=10000
                    c='Ketoprak'
                elif pilihMakanan==7:
                    harga=7000
                    c='Nasi Pecel'
                elif pilihMakanan==8:
                    harga=4000
                    c='Nasi'
                elif pilihMakanan==0:
                    a=False
                else:
                    print('Pilih dari 0-8')

                try:
                    if a==True:
                        dagangan.jumlahBarang=int(input('Jumlah[0 Untuk Batal]: '))
                        if dagangan.jumlahBarang==0:
                            print('Pesanan {} dibatalkan\n'.format(c))
                        else:
                            dagangan.hargaBarang.append(harga*dagangan.jumlahBarang)
                            dagangan.jumlahMakanan.append(dagangan.jumlahBarang)
                            dagangan.makananDipesan.append(c)
                            dagangan.hargaMakanan.append(harga)
                    
                except ValueError:
                        print('Masukan Jumlah Yang Dipesan !!!')
            except ValueError:
                print('Pilih dari 0-8 !!!')
            clear()
            print('Pesanan anda saat ini: ')
            self.listPesananMak()
            print('\n')
            
    def listPesananMak(self):
        for x in range(0,len(dagangan.makananDipesan)):
            print('- {} @{} x {}(qty)'.format(dagangan.makananDipesan[x],dagangan.hargaMakanan[x],dagangan.jumlahMakanan[x]))

class minuman(dagangan):
    def __init__(self):
        print('')
    def menuMinuman(self):
        a=True
        harga=0
        c=''
        while a is True:
            print('~DAFTAR MENU MINUMAN~\n')
            print('1. Sop Buah    Rp.15000\n'
                  '2. Sari Kurma  Rp.15000\n'
                  '3. Es Teler    Rp.13000\n'
                  '4. Jus Alpukat Rp.8000\n'
                  '5. Es Jeruk    Rp.7000\n'
                  '6. Es Teh      Rp.5000\n'
                  '7. Air Mineral Rp.4000\n'
                  '8. Ale ale     Rp.2000\n'
                  '0. KEMBALI')
            print('-----------------------')
            try:
                pilihMakanan=int(input('\nPilih Nomor Minuman: '))
                if pilihMakanan==1:
                    harga=15000
                    c='Sop Buah'
                elif pilihMakanan==2:
                    harga=15000
                    c='Sari Kurma'
                elif pilihMakanan==3:
                    harga=13000
                    c='Es Teler'
                elif pilihMakanan==4:
                    harga=8000
                    c='Jus Alpukat'
                elif pilihMakanan==5:
                    harga=7000
                    c='Es Jeruk'
                elif pilihMakanan==6:
                    harga=5000
                    c='Es Teh'
                elif pilihMakanan==7:
                    harga=4000
                    c='Air Mineral'
                elif pilihMakanan==8:
                    harga=2000
                    c='Ale ale'
                elif pilihMakanan==0:
                    a=False
                else:
                    print('Pilih dari 0-8')

                try:
                    if a==True:
                        dagangan.jumlahBarang=int(input('Jumlah[0 Untuk Batal]: '))
                        if dagangan.jumlahBarang==0:
                            print('Pesanan {} dibatalkan\n'.format(c))
                        else:
                            dagangan.hargaBarang.append(harga*dagangan.jumlahBarang)
                            dagangan.jumlahMinuman.append(dagangan.jumlahBarang)
                            dagangan.minumanDipesan.append(c)
                            dagangan.hargaMinuman.append(harga)
                except ValueError:
                        print('Masukan Jumlah Yang Dipesan !!!')
            except ValueError:
                print('Pilih dari 0-8 !!!')
            clear()
            print('Pesanan anda saat ini: ')
            self.listPesananMin()
            print('\n')
    def listPesananMin(self):
        for x in range(0,len(dagangan.minumanDipesan)):
            print('- {} @{} x {}(qty)'.format(dagangan.minumanDipesan[x],dagangan.hargaMinuman[x],dagangan.jumlahMinuman[x]))
voucherNew=''
voucherNew=randomChar(6,voucherNew)
v=True
bayar=''
bayarUang=int
punya=''
kembali=int
voucher=[]
while v==True:
    clear()
    pilihan=''
    print('~SELAMAT DATANG DI KANTIN WWE~\n'
          '-----------------------\n'
          'Pilih apa yang mau dipesan:\na. Makanan   |   b. Minuman   |   c.SELSAI   |   d.BATAL')
    pilihan=str(input('Pilihan anda: '))
    if pilihan=='a':
        pembeli=makanan()
        pembeli.menuMakanan()
    elif pilihan=='b':
        pembeli=minuman()
        pembeli.menuMinuman()
    elif pilihan=='c':
        pembeli=makanan()
        pembeli.listPesananMak()
        pembeli=minuman()
        pembeli.listPesananMin()
        pembeli.jumlahHarga()
        print('Total Pembelian anda adalah Rp.{}'.format(pembeli.hargaTotal))
        bayar=input('Lanjutkan Pembayaran [y] ?: ')
        if bayar=='y':
            bayar=int(input('Masukan uang: '))
            #voucherLoad(voucher)
            file_pocer=open('pocer.txt','r')
            for x in file_pocer.readlines():
                a=0
                if len(x)>6:
                    y=x.strip('\n')
                    voucher.append(y)
                else:
                    voucher.append(x)
                a+=1
            punya=input('Masukan kode voucher/[n]: ')
            clear()
            print('Mengecek database...')
            time.sleep(1)
            kembali=bayar-pembeli.hargaTotal
            if punya=='n':
                print('Kembali:'
                      '{}-{}=Rp.{}'.format(bayar,pembeli.hargaTotal,kembali))
            elif punya in voucher:
                print('Selamat Voucher anda berhasil')
                print('Kembali:'
                      '{}+20000(potongan)-{}=Rp.{}'.format(bayar,pembeli.hargaTotal,kembali))
                kembali=bayar+20000-pembeli.hargaTotal
            else:
                print('Kode Voucher Salah')
        if pembeli.hargaTotal >=200000:
            print('Selamat anda mendapat voucher cashback Rp.20000 dangan kode {}'.format(voucherNew))
        v=False
    elif pilihan=='d':
        v=False
    else:
        print('Mohon masukan a/b/c')
