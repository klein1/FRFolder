from PIL import Image

class ImgFile:

    def __init__(self, name, path, bbox_all):
        self.name = name
        self.bbox_all = bbox_all
        try:
            self.img = Image.open(path)
        except Exception as e:
            print('错误：{0}'.format(e))

    def showImg(self):
        self.img.show()

    def getImgSize(self):
        return self.img.size

    def getImgName(self):
        return self.name

    def getBbox(self):
        return self.bbox_all

    def save(self,path):
        self.img.save(path)

    # def saveImg(self):
    #     self.img = self.img.resize((1080, 2160))
    #     self.img.save(self.img_path)
