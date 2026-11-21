class hyundai:
    pass
class mobil:
    pass

hyundai1 = hyundai()
hyundai2 = hyundai()

print(type(hyundai1))
print(type(hyundai2))

mobil1 = mobil()
mobil2 = mobil()

print(type(mobil1))
print(type(mobil2))

class Mahasiswa :
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo nama saya {self.nama}")

    def hello (self, nama):
        print(f"hello {nama},nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "indah"
mahasiswa.perkenalan()
mahasiswa.hello("aliya")


#instance atribute

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 123456
mahasiswa1.nama = "indah"

print(mahasiswa1.nim)
print(mahasiswa1.nama)

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = ("123456")
mahasiswa2.nama = "indah"

print(mahasiswa2.nim)
print(mahasiswa2.nama)


