# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument(
        "-i",
        "--ignore-case",
        action="store_true",
        help="ignore case when searching",
    )

    args = parser.parse_args()

    pattern = args.pattern.lower() if args.ignore_case else args.pattern
    with open(args.filename, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, start=1):
            line_content = line.rstrip("\n")
            search_line = (
                line_content.lower() if args.ignore_case else line_content
            )
            if pattern in search_line:
                print(f"{line_num}: {line_content}")


if __name__ == "__main__":
    main()
