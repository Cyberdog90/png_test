import analyzer

SIGNATURE = "89504e470d0a1a0a"


def main():
    with open("test2_(chunk_deleted).png", "rb") as f:
        data = f.read().hex()

    if data[0:16] == SIGNATURE:
        analyzer.chunk(data)
        print(data)
    else:
        print("no png")
        exit(-1)


if __name__ == "__main__":
    main()
