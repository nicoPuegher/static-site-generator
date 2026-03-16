import os
import shutil
import sys

from generate_page import generate_page


def main():
    basepath = "/"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Copying static files...")
    copy_static("static", "docs")

    print("Generating pages...")

    generate_pages_recursive("content", "template.html", "docs", basepath)


def copy_static(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)

    os.mkdir(dest)

    copy_recursive(src, dest)


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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(src_path):

            if src_path.endswith(".md"):
                dest_html = dest_path.replace(".md", ".html")

                generate_page(src_path, template_path, dest_html, basepath)

        else:
            os.makedirs(dest_path, exist_ok=True)

            generate_pages_recursive(src_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
