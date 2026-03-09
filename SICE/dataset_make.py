import glob
import shutil

import os
from pathlib import Path


# for p in Path('Dataset_Part2/').iterdir():
#     for file in p.rglob('*'):
#         index = str(file).split('/')[1]
#         filename = str(file).split('/')[-1].split('.')[0]
#         print(str(file))
#         # print('Dataset_Part1/' + index + '_' + filename + '.jpg')
#         shutil.move(str(file), 'Dataset_Part2/' + index + '_' + filename + '.jpg')

for file in Path('Dataset_Part2/Lowlight_img_Label').glob('*'):
    index = str(file).split('/')[1]
    filename = str(file).split('/')[-1].split('.')[0]
    if str(file)[-3:] == 'JPG':
        print(str(file).replace('JPG', 'jpg'))
        # print('Dataset_Part1/' + index + '_' + filename + '.jpg')
        # shutil.move(str(file), str(file).replace('JPG', 'jpg'))
    if str(file)[-3:] == 'PNG':
        # print(str(file).replace('PNG', 'png'))
        # print(str(file), str(file).replace('PNG', 'png'))
        shutil.move(str(file), str(file).replace('PNG', 'png'))
