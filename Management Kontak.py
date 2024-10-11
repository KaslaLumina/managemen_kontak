#Projek Management kontak

def melihat_kontak():
    #Lihat Semua Kontak
    if kontak :
        for num, item in enumerate(kontak, start=1):
                print(f'{num}. {item['nama']} ({item["HP"]}, {item["email"]})')
                
    else:
        print('Tidak Ada Kontak!')
        input()
        return 1

def menambah_kontak():
    #Buat Kontak Baru
    nama = input('Masukkan nama kontak baru: ')
    hp = input('Masukkan nomor Hp Kontak baru: ')
    email = input('Masukan Email kontak baru: ')

    kontak_baru = {'nama': nama, 'HP': hp, 'email': email}
    kontak.append(kontak_baru)
    print('Kontak Berhasil Dibuat!')
    input()

def menghapus_kontak():
 #Hapus Kontak
    if melihat_kontak() == 1 :
        return
              
    try:
        i_hapus = int(input('Masukan Nomor kontak yang akan dihapus: '))
        del kontak[i_hapus-1]
        print(f'Kontak {i_hapus} berhasil dihapus!')
        input()
    except ValueError:
        print("Key yang anda masukkan salah!")
        input()
    except IndexError:
        print("Kontak yang dimaksud tidak ada!")
        input()

kontak1 = {'nama' : "Kasla", 'HP' : '083806266493', 'email' : 'kasla@gmail.com'}
kontak = [kontak1]
while True:
    print("\n Pilihan Menu Kontak: ")
    print('1. Lihat Semua Kontak')
    print('2. Buat Kontak Baru')
    print('3. Hapus Kontak')
    print('4. Keluar Aplikasi Kontak')

    pilihan = input("\nPilih Menu Kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        melihat_kontak()
        input()
            
    elif pilihan == '2':
        menambah_kontak()
        
    elif pilihan == '3':
       menghapus_kontak()

    elif pilihan == '4':
        #Keluar Kontak
        break
    else:
        print('Pilihan tidak tersedia!')
        input()
        