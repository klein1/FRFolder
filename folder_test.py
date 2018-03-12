from Folder import *
from Image import *
from collections import deque

list = ['highscore_list','normal_list','origin_list']

folder = Folder(0,'highscore_list',256,32)
bbox = [[1,2,3,4,'rect'],[1,2,3,4,'rect'],[1,2,3,4,'circle']]
img = ImgFile('000001','example.jpg',bbox)

bbox2 = [[1,2,3,4,'chess'],[1,2,3,4,'circle']]
img2 = ImgFile('000003','example.jpg',bbox2)

# folder.addImg(img)
# folder.addImg(img2)

for i in range(1,10):
    img = ImgFile('00000{0}'.format(i), 'example.jpg', bbox)
    folder.addImg(img)

# types = []
# for x1, x2, y1, y2, type in bbox:
#     types.append(type)
# if ('circle' in types):
#     print('circle')
# if ('rect' in types):
#      print('rect')
# if ('chess' in types):
#      print('chess')
