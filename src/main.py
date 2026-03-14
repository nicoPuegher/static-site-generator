from textnode import TextNode


def main():
    node = TextNode("This is some anchor text", "LINK", "www.google.com")
    print(node)


def copy_recursive(src, dest):
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dest_path}")
            shutil.copy(src_path, dest_path)

        else:
            print(f"Creating directory: {dest_path}")
            os.mkdir(dest_path)
            copy_recursive(src_path, dest_path)


if __name__ == "__main__":
    main()
