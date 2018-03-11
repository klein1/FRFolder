
Type = ['origin','highscore','normal']

class Folder:

    def __init__(self, index, path, length, size):
        self.type = Type[index]
        self.path = path
        self.buff_length = length
        self.batch_size = size

    def getBuffLength(self):
        return self.buff_length

    def getBatchSize(self):
        return self.batch_size