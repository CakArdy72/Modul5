def read_data():
    try:
        with open("data_mahasiswa.txt", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("File data_mahasiswa.txt tidak ditemukan. Belum ada data mahasiswa.")
        return []

def write_data(lines):
    with open("data_mahasiswa.txt", "w") as file:
        file.writelines(lines)

def tambah_data():
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    mata_kuliah = input("Masukkan Mata Kuliah: ")
    semester = input("Masukkan Semester: ")

    data = f"NIM: {nim}, Nama: {nama}, Mata Kuliah: {mata_kuliah}, Semester: {semester}\n"

    with open("data_mahasiswa.txt", "a") as file:
        file.write(data)

    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_data():
    lines = read_data()
    if lines:
        print("===== Data Mahasiswa =====")
        print(''.join(lines))

def update_data():
    nim_target = input("Masukkan NIM mahasiswa yang akan diperbarui: ")

    lines = read_data()
    updated_lines = []

    for line in lines: 
        data = line.split(", ")
        if len(data) >= 1 and data[0].startswith("NIM: ") and len(data[0].split(": ")) >= 2:
            if data[0].split(": ")[1] == nim_target:
                nama_baru = input("Masukkan Nama baru: ")
                mata_kuliah_baru = input("Masukkan Mata Kuliah baru: ")
                semester_baru = input("Masukkan Semester baru: ")
                line = f"NIM: {nim_target}, Nama: {nama_baru}, Mata Kuliah: {mata_kuliah_baru}, Semester: {semester_baru}\n"
                print("Data mahasiswa berhasil diperbarui.")
            updated_lines.append(line)

    write_data(updated_lines)

def delete_data():
    nim_target = input("Masukkan NIM mahasiswa yang akan dihapus: ")

    lines = read_data()
    updated_lines = []

    for line in lines:
        data = line.split(", ")
        if len(data) >= 1 and data[0].startswith("NIM: ") and len(data[0].split(": ")) >= 2:
            if data[0].split(": ")[1] == nim_target:
                print(f"Data mahasiswa dengan NIM {nim_target} berhasil dihapus.")
            else:
                updated_lines.append(line)
        else:
            print("Invalid data format: unable to process line:", line)

    write_data(updated_lines)

def search_data():
    nim_target = input("Masukkan NIM mahasiswa yang akan dicari: ")

    lines = read_data()

    for line in lines:
        data = line.split(", ")
        if len(data) >= 1 and data[0].startswith("NIM: ") and len(data[0].split(": ")) >= 2:
            if data[0].split(": ")[1] == nim_target:
                print(f"NIM: {data[0].split(': ')[1]}, Nama: {data[1].split(': ')[1]}, Mata Kuliah: {data[2].split(': ')[1]}, Semester: {data[3].split(': ')[1]}")
                return

    print(f"Data mahasiswa dengan NIM {nim_target} tidak ditemukan.")

while True:
    print("\n=====APLIKASI KELOLA DATA MAHASISWA=====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        update_data()
    elif pilihan == "4":
        delete_data()
    elif pilihan == "5":
        search_data()
    elif pilihan == "6":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
