from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import os

jpg_directory = "/JPEGImages/"
xml_directory = "/Annotations/"
set_directory = "/ImageSets/"

def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            print('删除文件 {0}'.format(path_file))
            os.remove(path_file)
        else:
            del_file(path_file)
    print('删除目录 {0}'.format(path))
    os.rmdir(path)

def del_data(path, name):
    os.remove(path + jpg_directory + name + ".jpg" )
    os.remove(path + xml_directory + name + ".xml")
    del_set_data(path + set_directory)

def del_set_data(path):
    overwrite(path + 'rect_trainval.txt')
    overwrite(path + 'circle_trainval.txt')
    overwrite(path + 'chess_trainval.txt')

def overwrite(path):
    with open(path, 'r') as r:
        lines = r.readlines()
    with open(path, 'w') as w:
        for l in lines[1:]:
            w.write(l)
    r.close()
    w.close()

def writeInJpg(folder,img):
    img.save(folder.getImgPath())

def writeInSet(folder,img):
    directory = folder.getSetPath()
    types = []
    for x1,x2,y1,y2,type in img.getBbox():
        types.append(type)
    f = open(directory + 'rect_trainval.txt', 'a')
    if ('rect' in types):
        st = img.getImgName() + ' ' + str(1).rjust(2, ' ') + '\n'
    else:
        st = img.getImgName() + ' ' + str(-1).rjust(2, ' ') + '\n'
    f.write(st)
    f = open(directory + 'circle_trainval.txt', 'a')
    if ('circle' in types):
        st = img.getImgName() + ' ' + str(1).rjust(2, ' ') + '\n'
    else:
        st = img.getImgName() + ' ' + str(-1).rjust(2, ' ') + '\n'
    f.write(st)
    f = open(directory + 'chess_trainval.txt', 'a')
    if ('chess' in types):
        st = img.getImgName() + ' ' + str(1).rjust(2, ' ') + '\n'
    else:
        st = img.getImgName() + ' ' + str(-1).rjust(2, ' ') + '\n'
    f.write(st)
    f.close()

def writeInXml(folder,img):
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'JUMP2018'

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = img.getImgName() + '.jpg'

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = "1080"
    node_height = SubElement(node_size, 'height')
    node_height.text = "1920"
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    node_segmented = SubElement(node_root, 'segmented')
    node_segmented.text = '1'

    for board in img.getBbox():
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = board[4]
        node_pose = SubElement(node_object, 'pose')
        node_pose.text = 'Unspecified'
        node_truncated = SubElement(node_object, 'truncated')
        node_truncated.text = '0'
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(int(board[0]))
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(int(board[1]))
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(int(board[2]))
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(int(board[3]))

    xml = tostring(node_root, pretty_print=True)  # 格式化显示，该换行的换行
    dom = parseString(xml)
    # print(xml)

    try:
        with open(folder.getXmlPath(), 'w') as fh:
            # writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
            # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
            dom.writexml(fh, indent='', addindent='\t', newl='', encoding='UTF-8')
    except Exception as err:
        print('错误：{0}'.format(err))
