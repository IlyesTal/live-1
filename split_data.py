# Imports des modules utiles
import glob
import random
import os
import shutil

# On récupère le chemin vers le dataset (images+txt)
PATH = './'
img_paths = glob.glob(PATH+'*.jpg')
txt_paths = glob.glob(PATH+'*.txt')

# Nombres de fichiers pour l'entraînement, le test et la validation
data_size = len(img_paths)
r_train = 0.7
r_test = 0.2
r_valid = 0.1
train_size = int(data_size * r_train)
test_size = int(data_size * r_test)
valid_size = int(data_size * r_valid)

# On mélange aléatoirement les fichiers
img_txt = list(zip(img_paths, txt_paths))
random.seed(43)
random.shuffle(img_txt)
img_paths, txt_paths = zip(*img_txt)

# On split en respectant les proportions
train_img_paths = img_paths[:train_size]
train_txt_paths = txt_paths[:train_size]

test_img_paths = img_paths[train_size:train_size + test_size]
test_txt_paths = txt_paths[train_size:train_size + test_size]

valid_img_paths = img_paths[train_size + test_size:]
valid_txt_paths = txt_paths[train_size + test_size:]

# Enfin, on renvoi chaque fichier dans le bon dossier :
train_folder = PATH + 'train/'
test_folder = PATH + 'test/'
valid_folder = PATH + 'valid/'
os.mkdir(train_folder)
os.mkdir(test_folder)
os.mkdir(valid_folder)


def move(paths, folder):
    for p in paths:
        shutil.move(p, folder)


move(train_img_paths, train_folder)
move(train_txt_paths, train_folder)
move(test_img_paths, test_folder)
move(test_txt_paths, test_folder)
move(valid_img_paths, valid_folder)
move(valid_txt_paths, valid_folder)
