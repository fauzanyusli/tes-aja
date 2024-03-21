import os

class Queue:
    def __init__(self):
        self.item = []

    def isempty(self):
        return len(self.item) == 0

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        if not self.isempty():
            return self.item.pop(0)
        else:
            return "Kosong"

    def display_queue(self):
        os.system("cls")
        print("Isi Antrian:")
        if self.isempty():
            print("Antrian Kosong")
        else:
            for index, item in enumerate(self.item, start=1):
                print(f"{index}. {item}")

    def antrian(self):
        pilih = "y"
        while (pilih != "5"):
            os.system("cls")
            print("=========================================")
            print("|          PEMBUATAN SIM MOTOR          |")
            print("|        POLRES METRO BEKASI KOTA       |")
            print("=========================================")
            print("|1. Daftar Antrian                      |")
            print("|2. Antrian Selesai                     |")
            print("|3. Periksa Antrian                     |")
            print("|4. Tampilkan Isi Antrian               |")
            print("|5. Keluar Program                      |")
            print("=========================================")
            pilihan = str(input(("Silakan masukkan pilihan anda: ")))
            if pilihan == "1":
                os.system("cls")
                print("==== ANDA BERADA DI MENU PENDAFTARAN ====")
                obj = str(input("Masukkan nama anda: "))
                self.enqueue(obj)
                print("Antrian dengan nama "+obj+" telah ditambahkan")
                input("Tekan [ENTER] untuk kembali ke daftar menu ")
            elif pilihan == "2":
                os.system("cls")
                print("==== ANDA BERADA DI MENU ANTRIAN SELESAI")
                datakeluar = self.dequeue()
                if datakeluar == "Kosong":
                    print("Antrian Kosong")
                else:
                    print("Antrian selesai untuk", datakeluar)
                input("Tekan [ENTER] untuk kembali ke daftar menu ")
            elif pilihan == "3":
                os.system("cls")
                print("Panjang Antrian: {}".format(len(self.item)))
                input("Tekan [ENTER] untuk kembali ke daftar menu ")
            elif pilihan == "4":
                self.display_queue()
                input("Tekan [ENTER] untuk kembali ke daftar menu ")
            elif pilihan == "5":
                pilih = "n"
                break

if __name__ == "__main__":
    q = Queue()
    q.antrian()