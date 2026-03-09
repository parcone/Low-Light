import glob
import random

image_list_lowlight = glob.glob('Dataset_Part1/Lowlight_img/' + "*.jpg")
print(image_list_lowlight)
train_list = []
val_list = []

for img_path in image_list_lowlight:
    if random.random() > 1:
        print('Lowlight_img/' + img_path.split('/')[-1])
        val_list.append(
            'Lowlight_img/' + img_path.split('/')[-1] + '\tLowlight_img_Label/' +
            img_path.split('/')[-1].split('_')[0] + '.jpg\n')
    else:
        print('Lowlight_img/' + img_path.split('/')[-1])
        train_list.append(
            'Lowlight_img/' + img_path.split('/')[-1] + '\tLowlight_img_Label/' +
            img_path.split('/')[-1].split('_')[0] + '.jpg\n')
# lowlight_images_path = 'Dataset_Part1_official/'
# with open('train_list.txt', 'r+') as file:
#     lines = file.readlines()
#
#     print([lowlight_images_path + item.strip() for item in lines])
with open('train_list.txt', 'w+') as file:
    for f in train_list:
        file.write(f)
with open('val_list.txt', 'w+') as file:
    for f in val_list:
        file.write(f)

