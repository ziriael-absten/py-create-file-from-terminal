# write your code here
import sys
import os
from datetime import datetime


def create_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{now}\n")
        line_number = 1
        while True:
            line = input(f"Enter content line {line_number}: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
            path = os.path.join(*dirs)
            create_directories(path)
            file_path = os.path.join(path, file_name)
            create_file(file_path)
        else:
            dirs = args[d_index + 1:]
            path = os.path.join(*dirs)
            create_directories(path)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)


if __name__ == "__main__":
    main()
