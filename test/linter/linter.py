import os
from pylint import lint


def list_files_recursively(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if "venv" not in d]
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))
    return file_list


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(os.getcwd()))
    files = list_files_recursively(path)

    for f in files:
        THRESHOLD = 10

        run = lint.Run([f], exit=False)
        score = run.linter.stats.global_note

        print(f"Score: {score}")
