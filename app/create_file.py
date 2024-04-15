import sys
import os
import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(
            str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")))
        line_number = 1
        while True:
            input_content = input("Enter content line:")
            if input_content == "stop":
                file.write("\n")
                break

            file.write(f"{line_number} {input_content}\n")
            line_number += 1


def main() -> None:
    cmd_text = sys.argv

    if "-d" in cmd_text and "-f" in cmd_text:
        index_d = cmd_text.index("-d")
        index_f = cmd_text.index("-f")

        file_name = cmd_text[index_f + 1]

        correct_path = os.path.join(*cmd_text[index_d + 1: index_f])
        os.makedirs(correct_path, exist_ok=True)
        create_file(os.path.join(correct_path, file_name))
        return

    if "-d" in cmd_text:
        index_d = cmd_text.index("-d")
        correct_path = os.path.join(*cmd_text[index_d + 1:])
        os.makedirs(correct_path, exist_ok=True)
        return

    if "-f" in cmd_text:
        index_f = cmd_text.index("-f")
        create_file(cmd_text[index_f + 1])
        return


if __name__ == "__main__":
    main()
