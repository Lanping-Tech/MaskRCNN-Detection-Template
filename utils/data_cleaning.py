import os
import random
import shutil

image_suffix = 'jpg'

source_data_path = 'datasets/temp'

target_root_path = 'datasets/ToothData'

os.makedirs(target_root_path)
target_train_path = os.path.join(target_root_path, 'train')
os.makedirs(target_train_path)
os.makedirs(os.path.join(target_train_path, 'PNGImages'))
os.makedirs(os.path.join(target_train_path, 'JSONFiles'))

target_test_path = os.path.join(target_root_path, 'test')
os.makedirs(target_test_path)
os.makedirs(os.path.join(target_test_path, 'PNGImages'))
os.makedirs(os.path.join(target_test_path, 'JSONFiles'))

image_files = set()
json_files = set()

for file_name in os.listdir(source_data_path):
    name = file_name.split('.')[0]
    type = file_name.split('.')[1]
    if type == 'json':
        json_files.add(name)
    elif type == image_suffix:
        image_files.add(name)
    else:
        continue

intersection = list(image_files & json_files)

total_size = len(intersection)
print(total_size)
train_size = int(total_size * 0.9)

train_name = random.sample(intersection, train_size)

for name in intersection:
    image_path = os.path.join(source_data_path, name+'.'+image_suffix)
    json_path = os.path.join(source_data_path, name+'.json')

    if name in train_name:
        shutil.copy(image_path, os.path.join(target_train_path, 'PNGImages', name+'.'+image_suffix))
        shutil.copy(json_path, os.path.join(target_train_path, 'JSONFiles', name+'.json'))
    else:
        shutil.copy(image_path, os.path.join(target_test_path, 'PNGImages', name+'.'+image_suffix))
        shutil.copy(json_path, os.path.join(target_test_path, 'JSONFiles', name+'.json'))

