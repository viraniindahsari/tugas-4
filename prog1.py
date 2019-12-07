data=[]
while(True):
    nama= input("masukan nama :  ")
    nim= input("masukan nim: ")
    tugas= int(input("masukan tugas: "))
    uts= int(input("masukin uts: "))
    uas= int(input("masukan uas: "))
    akhir = (30 * tugas / 100) + (35 * uts / 100) + (35 * uas / 100)
    data.append([nama, nim, tugas, uts, uas, akhir])
    ulangi=input("tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;


print("\nDaftar nama\n")
print("======================================================================================")
print("|    nama    |     nim     |    tugas     |     uts     |    uas      |    akhir     |")
print("======================================================================================")
for x in data:
    print("|{0:10} | {1:10} | {2:10} | {3:10} | {4:10} | {5:10} |".format(x[0], x[1], x[2], x[3], x[4],x[5]))
print("======================================================================================")

