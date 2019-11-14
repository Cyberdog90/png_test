import png_open


def main():
    image = png_open.PngOpen("lenna")
    if image.check_image():
        pass
    else:
        exit(-1)


if __name__ == "__main__":
    main()
