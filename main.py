from Folder import *
from Image import *

folder0 = Folder(0,'origin_list',256,32)
folder1 = Folder(1,'highscore_list',256,16)
folder2 = Folder(2,'normal_list',256,8)

bbox = [[1,2,3,4,'rect'],[1,2,3,4,'rect'],[1,2,3,4,'circle']]

img = ImgFile('000001','example.jpg',bbox)
img2 = ImgFile('000003','example.jpg',bbox)

folder0.addImg(img)
folder1.addImg(img2)
