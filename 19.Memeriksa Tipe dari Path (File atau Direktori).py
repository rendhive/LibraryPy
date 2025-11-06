import os

path = 'file_sample.txt'
if os.path.isfile(path):
    print(f"'{path}' adalah file.")
elif os.path.isdir(path):
    print(f"'{path}' adalah direktori.")
else:
    print(f"'{path}' tidak ditemukan.")

#Memeriksa apakah path tersebut adalah file atau direktori.