from func import *
from collections import deque
Type = ['origin','highscore','normal']

class Folder:
    dirs = ['JPEGImages','Annotations','ImageSets']

    def __init__(self, index, path, length, size):
        self.type = Type[index]
        self.path = path
        self.buff_length = length
        self.batch_size = size
        self.img_list = deque()
        self.mkdir()

    def getBuffLength(self):
        return self.buff_length

    def getBatchSize(self):
        return self.batch_size

    def getPath(self):
        return self.path

    def mkdir(self):
        for dir in self.dirs:
            path = os.path.join(self.path,dir)
            if not os.path.exists(path):
                os.makedirs(path)
            else:
                print('{0}文件夹中已存在{1}目录'.format(self.path,dir))
                filelist = os.listdir(path)
                if(len(filelist) > 0):
                    del_file(path)
                    os.makedirs(path)
                    print('创建新目录 {0}'.format(path))

    def addImg(self,img):
        self.img_path = self.path + jpg_directory + img.getImgName() + ".jpg"
        self.xml_path = self.path + xml_directory + img.getImgName() + ".xml"
        self.set_path = self.path + set_directory
        writeInJpg(self,img)
        writeInXml(self,img)
        writeInSet(self,img)

        self.img_list.append(img)
        if(len(self.img_list) > self.buff_length):
            del_data(self.path, self.img_list[0].getImgName())
            self.img_list.popleft()

    def getImgPath(self):
        return self.img_path

    def getXmlPath(self):
        return self.xml_path

    def getSetPath(self):
        return self.set_path

    def getImgList(self):
        return self.img_list

