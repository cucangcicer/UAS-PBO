import time
import datetime
import string
import random
from os import system,name

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
    trxFile=[]
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
        t=['Sop Iga','Sate Ayam','Soto Ayam','Nasi Goreng','Gado gado','Ketoprak','Nasi Pecel','Nasi']
        y=[25000,15000,13000,10000,10000,10000,7000,4000]
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
                c=t[pilihMakanan-1]
                harga=y[pilihMakanan-1]
                if pilihMakanan==0:
                    a=False
                elif pilihMakanan not in range(0,len(t)+1):
                    print('pilih dari 0-8')
                    
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
                            dagangan.trxFile.append('- {} @{} x {}(qty)'.format(c,harga,dagangan.jumlahBarang))
                                        
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
        t=['Sop Buah','Sari Kurma','Es Teler','Jus Alpukat','Es Jeruk','Es Teh','Air Mineral','Ale ale']
        y=[15000,15000,13000,8000,7000,5000,4000,2000]
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
                pilihMinuman=int(input('\nPilih Nomor Minuman: '))
                c=t[pilihMinuman-1]
                harga=y[pilihMinuman-1]
                if pilihMinuman==0:
                    a=False
                elif pilihMinuman not in range(0,len(t)+1):
                    print('pilih dari 0-8')
                    
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
                            dagangan.trxFile.append('- {} @{} x {}(qty)'.format(c,harga,dagangan.jumlahBarang))
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
            file_pocer.close()
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
                kembali=bayar+20000-pembeli.hargaTotal
                print('Kembali:'
                      '{}+20000(potongan)-{}=Rp.{}'.format(bayar,pembeli.hargaTotal,kembali))
            else:
                print('Kode Voucher Salah')
                v=False
        if pembeli.hargaTotal>=200000 & v==True:
            print('Selamat anda mendapat voucher potongan Rp.20000 dangan kode {}'.format(voucherNew))
            file_pocer=open('pocer.txt','a')
            file_pocer.write('\n{}'.format(voucherNew))
            file_pocer.close()
        if v==True:
            dt=(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
            file_transaksi=open('transaksi.txt','a')
            file_transaksi.write('{}'.format(dt))
            for x in range(0,len(pembeli.trxFile)):
                trx='\n'+dagangan.trxFile[x]
                file_transaksi.write('{}'.format(trx))
            file_transaksi.write('\nTotal Pembelian Rp.{}\n'.format(pembeli.hargaTotal))
            file_transaksi.close()
        v=False
    elif pilihan=='d':
        v=False
    else:
        print('Mohon masukan a/b/c')
