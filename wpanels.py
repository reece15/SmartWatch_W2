# coding:utf-8

from PIL import Image
import struct
from WpanelObject import WpanelObject
import config
import os


success_msg = u"""
转换完成!
完成后当前目录下生成的.ob文件为你要的文件
复制到wpanel目录下替换即可，

想恢复的话 从 base目录下复制同名的文件到wpanel下替换
"""
def loads(ob_file):

    wpanel = None
    with open(ob_file, "rb") as f:
        buf = f.read()

        data_len = len(buf)-0x38

        width, height = struct.unpack_from("II", buf, config.POINT_XY1)
        width2, height2 = struct.unpack_from("II", buf, config.POINT_XY2)

        fmt = "{}B".format(width*height*3)

        #assert width == width2
        #assert height == height2
        data = struct.unpack_from(fmt, buf, config.POINT_DATA)

        wpanel = WpanelObject(val="", width=width, height=height, data=data, file=ob_file, data_len=data_len, header=buf[:0x38])
    print(u"加载默认表盘%s" % wpanel)
    return wpanel


def trans(base, ob, file, A=False):

    if not os.path.exists(file):
        return None, "文件 {} 不存在".format(file)

    if not os.path.isfile(file):
        return None, "{} 不是文件".format(file)

    im = Image.open(file)


    w,h = im.size
    if h != ob.height:
        return None, u"图片高度不一致! 需要高度{m}, 待转换图片{n}".format(m=ob.height,n=h)

    if w != ob.width:
        msg = u"图片宽度不一致! 需要宽度{m}, 待转换图片{n}".format(m=ob.width,n=w)
        return None, msg


    with open(base, "wb") as f:

        f.write(ob.header)
        # f.write(struct.pack('{}B'.format(len(ob.header)), *ob.header))

        un_use = []
        for i in range(h):
            for j in range(w):

                pixel = im.getpixel((j, i))
                for k in WpanelObject.rgb888to565(pixel=pixel):
                    f.write(struct.pack('B', k))

                un_use.append(pixel[3])


        f.write(struct.pack('{}B'.format(len(un_use)), *un_use))

    return base, success_msg


def decode_ob(path):
    image = None

    with open(path, "rb") as f:
        buf = f.read()
        width, height = struct.unpack_from("II", buf, config.POINT_XY1)
        width2, height2 = struct.unpack_from("II", buf, config.POINT_XY2)

        print(width, height, width2,height2)

        print(len(buf)-config.POINT_DATA)

        fmt = "{}B".format(width*height*3)

        #assert width == width2
        #assert height == height2

        image = Image.new('RGB', (width, height))
        data = struct.unpack_from(fmt, buf, config.POINT_DATA)

        # f.seek(0x38)
        # image = Image.frombytes("RGB", (width, height), f.read())
        index = 0


        for y in range(height):
            for x in range(width):

                pixel =WpanelObject.rgb565to888(data[index:index+2])
                image.putpixel((x, y), pixel)
                index += 2

    return image


helps = u"""
    错误提示: {err}

    请正确执行：
    时钟的执行: {file} {base_path1}  xxx.bmp
    或者
    数字的执行: {file} {base_path2}  xxx.bmp


    注意: xxx.bmp为你准备的图片
    完成后当前目录下生成的.ob文件为你要的文件
    复制到wpanel目录下替换即可， 想恢复的话 从 base目录下复制同名的文件到wpanel下替换


    """

bases = {
    "a1_1_bg.ob": "base/a1_1_bg.ob",
    "d2.ob": "base/d2.ob",
}

if __name__ == "__main__":

    import sys
    import os

    if len(sys.argv) != 3:
        print(helps.format(file=sys.argv[0], base_path1="a1_1_bg.ob", base_path2="d2.ob", err=u"参数不够！"))
        sys.exit(0)

    base = sys.argv[1]
    file = sys.argv[2]

    p = bases.get(base)
    if p is None:
        print(helps.format(file=sys.argv[0], base_path1="a1_1_bg.ob", base_path2="d2.ob", err=u"第二个参数错误，检查.ob文件是否存在！"))
        sys.exit(0)

    ob = loads(p)
    res, msg = trans(base, ob, file)
    if res:
        decode_ob(res).show()
    else:
        print(msg)