# coding:utf-8

import json

from PIL import Image


class WpanelObject(object):

    def __init__(self, val, width, height, data, file,data_len, header):
        self.val = val
        self.width = width
        self.height = height
        self.data = data
        self.file = file
        self.data_len = data_len
        self.header = header

        self.un_use = data[width * height * 2:]

    def __len__(self):
        return len(self.data)

    def check(self):

        return self.height * self.width * 3 == self.data_len

    def __str__(self):
        return json.dumps({
            "file": self.file,
            "val": self.val,
            "width": self.width,
            "height": self.height,
            "data_len": len(self),
            "header_len": len(self.header),
            "footer_len": len(self.un_use)
        }, indent=4)

    def gen_rgb(self):
        image = Image.new('RGB', (self.width, self.height))
        index = 0
        for y in range(self.height):
            for x in range(self.width):

                image.putpixel((x, y), self.rgb565to888(self.data[index, index+2]))
                index += 2

        return image

    @staticmethod
    def rgb565to888(pixel):
        c = pixel[0] + (pixel[1] << 8)
        r = ((c & 0xf800) >> 11) << 3
        g = ((c & 0x7e0) >> 5) << 2
        b = (c & 0x1f) << 3

        return (r,g,b)

    @staticmethod
    def rgb888to565(pixel):
        r = (pixel[0] << 8) & 0xf800
        g = (pixel[1] << 3)  & 0x7e0
        b = pixel[2] >> 3
        c = r|g|b
        return  c& 0x00ff, c>>8