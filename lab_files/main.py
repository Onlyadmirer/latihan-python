# id = input("masukkan id : ")
# nama = input("masukkan nama :")
# posisi = input("masukkan  posisi : ")
# gaji = input("masukkan  gaji : ")


# try :
#     with open("example.txt", "x") as p:
#         p.write(f"ID : {id}\n")
#         p.write(f"NAMA :  {nama}\n")
#         p.write(f"POSISI : {posisi}\n")
#         p.write(f"Gaji : {gaji}\n")
#         p.close()
# except:
#     with open("example.txt", "a") as p:
#         p.write(f"ID : {id}\n")
#         p.write(f"NAMA :  {nama}\n")
#         p.write(f"POSISI : {posisi}\n")
#         p.write(f"Gaji : {gaji}\n")
#         p.close()


# membuat file
import os

folder = "../D:\latihan python\latihan-python\lab_files" 
file_baru = input("masukkan nama file: ")
files = os.path.join(folder, "file_baru")
# with open(files, "w") as f:
#     f.write("file.txt")  # write some content to the file
print("sudah")
