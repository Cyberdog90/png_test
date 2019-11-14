import png_open


def main():
    image = png_open.PngOpen("lenna")
    if image.check_image():
        print("correct")
    else:
        print("wrong")


if __name__ == "__main__":
    main()
