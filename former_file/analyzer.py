import inflate
import zlib

IHDR = "0000000d49484452"
IDAT = "49444154"


def chunk(data):
    if data.find(IHDR) == -1:
        exit(-1)
    ihdr(data)
    if data.find(IDAT) == -1:
        exit(-1)
    idat(data)


def ihdr(data):
    print(type(data))
    ihdr_index = data.find(IHDR) + 16
    print(ihdr_index)
    width = data[ihdr_index:ihdr_index + 8]
    ihdr_index += 8
    height = data[ihdr_index:ihdr_index + 8]
    ihdr_index += 8
    bit_depth = data[ihdr_index:ihdr_index + 2]
    ihdr_index += 2
    color_type = data[ihdr_index:ihdr_index + 2]
    ihdr_index += 2
    comp_method = data[ihdr_index:ihdr_index + 2]
    ihdr_index += 2
    filter_method = data[ihdr_index:ihdr_index + 2]
    ihdr_index += 2
    inter_method = data[ihdr_index:ihdr_index + 2]

    print("横幅 : {}".format(width))
    print("縦幅 : {}".format(height))
    print("ビット深度 : {}".format(bit_depth))
    print("カラータイプ : {}".format(color_type))
    print("圧縮手法 : {}".format(comp_method))
    print("フィルター手法 : {}".format(filter_method))
    print("インターレース手法 : {}".format(inter_method))


def idat(data):
    idat_size = int(data[data.find(IDAT) - 8:data.find(IDAT)], 16)
    print("IDATサイズ : {}".format(idat_size))
    idat_chunk = data[data.find(IDAT) - 8:data.find(IDAT) + 8 + idat_size * 2+8]
    print(idat_chunk)
    bytes_chunk = idat_chunk.encode("utf-8")
    print(zlib.decompress(bytes_chunk))
