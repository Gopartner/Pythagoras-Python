import math
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def pythagoras():
    # Header program
    print(Fore.CYAN + Style.BRIGHT + "========================================")
    print(Fore.CYAN + Style.BRIGHT + "Menghitung Sisi Miring Segitiga Siku-Siku")
    print(Fore.CYAN + Style.BRIGHT + "========================================\n")

    # Penjelasan rumus
    print(Fore.GREEN + "Rumus Pythagoras:\nUntuk segitiga siku-siku")
    print(Fore.GREEN + "- rumus yang digunakan adalah: a² + b² = c²")
    print(Fore.GREEN + "Di mana:")
    print(Fore.GREEN + "a = panjang sisi pertama (alas)")
    print(Fore.GREEN + "b = panjang sisi kedua (tinggi)")
    print(Fore.GREEN + "c = panjang sisi miring (hipotenusa), yaitu hasil yang dicari.\n")
    
    # Catatan untuk format desimal
    print(Fore.YELLOW + Style.BRIGHT + "Catatan: Gunakan tanda titik (.) untuk angka pecahan.")
    print(Fore.YELLOW + Style.BRIGHT + "Contoh: 60.5 untuk 60,5 cm.\n")

    while True:
        # Pemilihan satuan panjang
        print(Fore.YELLOW + "Pilih satuan panjang:")
        print(Fore.YELLOW + "> 1. Senti meter (CM)")
        print(Fore.YELLOW + "> 2. Meter (M)")
        print(Fore.YELLOW + "> 3. Keluar")
        satuan = input(Fore.YELLOW + "Pilih satuan (1/2/3): ")

        if satuan == "3":
            print(Fore.RED + Style.BRIGHT + "Program selesai.")
            break

        if satuan not in ["1", "2"]:
            print(Fore.RED + "Input tidak valid. Coba lagi.")
            continue

        # Menentukan satuan yang digunakan untuk input
        satuan_text = "CM" if satuan == "1" else "M"

        # Input sisi dengan titik untuk desimal
        try:
            a = float(input(Fore.MAGENTA + f"Masukkan sisi A ({satuan_text}): ").replace(",", "."))
            b = float(input(Fore.MAGENTA + f"Masukkan sisi B ({satuan_text}): ").replace(",", "."))
        except ValueError:
            print(Fore.RED + "Input tidak valid. Harap masukkan angka.")
            continue

        # Menghitung sisi miring (c)
        c = math.sqrt(a ** 2 + b ** 2)

        # Menampilkan hasil sesuai satuan input
        if satuan == "1":  # Input dalam CM
            c_cm = c
            c_m = c / 100
            c_mm = c * 10  # Sesuai skala CM ke MM
            c_km = c / 100000
        elif satuan == "2":  # Input dalam M
            c_m = c
            c_cm = c * 100
            c_mm = c * 1000
            c_km = c / 1000

        print(Fore.CYAN + "\nHasil:")
        print(Fore.CYAN + f"{c_cm:.2f} CM")
        print(Fore.CYAN + f"{c_m:.2f} M")
        print(Fore.CYAN + f"{c_mm:.2f} MM")
        print(Fore.CYAN + f"{c_km:.5f} KM\n")  # Menambah presisi untuk hasil KM agar lebih akurat

        # Validasi input y/n
        while True:
            ulang = input(Fore.GREEN + "Hitung lagi atau keluar (y/n): ").lower()
            if ulang == "y":
                break
            elif ulang == "n":
                print(Fore.RED + Style.BRIGHT + "Program selesai.")
                return
            else:
                print(Fore.RED + "Input tidak valid. Masukkan 'y' untuk mengulang atau 'n' untuk keluar.")

pythagoras()

