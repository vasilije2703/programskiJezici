import os
import shutil

if not os.path.exists('test_prep'):
    os.mkdir('test_prep')


for broj in ['1' , '2', '3']:
    folder_path = os.path.join('test_prep' , broj)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

os.chdir('test')

for fajl in os.listdir():
    index_crte = fajl.index('_')
    test_str = fajl[index_crte + 1:]
    if test_str[0] == '1':
       destination = os.path.join('../test_prep' , '1')
       shutil.copy(fajl, destination)
    elif test_str[0] == '2':
       destination = os.path.join('../test_prep' , '2')
       shutil.copy(fajl, destination)
    else:
       destination = os.path.join('../test_prep' , '3')
       shutil.copy(fajl, destination)
