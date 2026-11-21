class Mahasiswa:
    def __init__(self, nama, jurusan, semester):
        self.nama = nama
        self.jurusan = jurusan
        self.semester = semester

    def perkenalan(self):
        print(f"Halo, nama aku {self.nama}, jurusan {self.jurusan} semester {self.semester}")

    def bicara(self, kalimat):
        print(f"{self.nama}: {kalimat}")


indah = Mahasiswa("Indah", "Sistem Informasi", 3)
aliyah = Mahasiswa("Aliyah", "Ilmu Komputer", 5)

print("=== Berkenalan di Cafe ===")
print("Indah dan Aliyah bertemu di cafe saat sedang mengerjakan tugas.")

indah.bicara("Hai kak, maaf, kursi sebelah kosong gak?")
aliyah.bicara("Kosong kok, silahkan duduk aja")

indah.perkenalan()
aliyah.perkenalan()

indah.bicara("Kakak kuliah di mana?")
aliyah.bicara("Aku di Universitas Bina Bangsa, kamu?")
indah.bicara("Aku juga kak, ternyata satu kampus ya")
aliyah.bicara("Iya nih, salam kenal ya Indah")
indah.bicara("Salam kenal juga kak Aliyah")

indah.bicara("Kak, aku lagi bingung nih sama tugas Python, class dan object")
aliyah.bicara("Gampang kok, class itu cetakan, object itu hasil cetakannya")
indah.bicara("Ooh gitu, aku ngerti sekarang, makasih ya kak")
aliyah.bicara("Sama-sama, kapan-kapan tanya aja")
