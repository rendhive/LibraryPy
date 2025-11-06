import os

os.mkdir('folder_kosong')

# Membuat beberapa file contoh
for i in range(5):
    with open(f'folder_kosong/file_{i}.txt', 'w') as f:
        f.write("File ke-" + str(i))

# Menghapus semua file dalam folder
for filename in os.listdir('folder_kosong'):
    file_path = os.path.join('folder_kosong', filename)
    os.remove(file_path)

print("Semua file dalam 'folder_kosong' telah dihapus.")


#Menghapus semua file dalam direktori yang ditentukan.