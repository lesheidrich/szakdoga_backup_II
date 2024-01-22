import os
from pylint import lint


def list_files_recursively(folder_path: str) -> [str]:
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if "venv" not in d]
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))
    return file_list


def run_linter(path: str, exceptions: list) -> None:
    files = list_files_recursively(path)

    if not os.getcwd().endswith("linter"):
        os.chdir(os.path.join(path, "test", "linter"))

    files[:] = [f for f in files if not any(module in f for module in exceptions)]

    [lint.Run([f], exit=False) for f in files]

    # for f in files:
    # THRESHOLD = 10
    # run = lint.Run([f], exit=False)
    # score = run.linter.stats.global_note

    #     if score < THRESHOLD:
    #         print(f"Linter failed, Score:{score} < threshold value: {THRESHOLD}")
    #         exit_code = 1
    # sys.exit(exit_code)
