import os


def get_file_extension(file_name):
    _, file_extension = os.path.splitext(file_name)
    if not file_extension:
        raise ValueError("File has no extension.")
    return file_extension


def main():
    try:
        file_name = input("Enter the file name: ")
        extension = get_file_extension(file_name)
        print(f"The file extension is: {extension}")
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
