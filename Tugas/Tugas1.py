print(10*'=', 'PROGRAM MENGHITUNG NILAI AKHIR', 10* '=')

nama = input("Masukan Nama : ")
nim = int(input("Masukan NIM : "))
semester = input("Masukan Semester : ")
mata_kuliah = input("Masukan Mata kuliah : ")
nilai_kehadiran = float(input("Masukan nilai kehadiran : "))
nilai_tugas = float(input("Masukan Nilai Tugas : "))
nilai_uts = float(input("Masukan Nilai UTS : "))
nilai_uas = float(input('Masukan Nilai UAS : '))

nilai_akhir = (0.1 * nilai_kehadiran) + (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas)

print(10*'=', 'HASIL PERHITUNGAN' ,10*'=')
print(f'''NAMA        : {nama}
NIM         : {nim}
SEMESTER    : {semester}
MATA KULIAH : {mata_kuliah}
NILAI AKHIR : {nilai_akhir}''')

if nilai_akhir >= 82:
    print('GRADE       : A')
elif nilai_akhir >= 72:
    print('GRADE       : B')
elif nilai_akhir <= 71:
    print('GRADE       : C')
elif nilai_akhir <= 61:
    print('GRADE       : D') 

print('=' * 40)