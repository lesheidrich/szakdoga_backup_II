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

# TODO: path to setup.py instead of hardcoded
# TODO: cleanup and make into unittestable class

def run_linter() -> None:
    # path = os.path.dirname(os.path.dirname(os.getcwd()))
    # PROJECT_FOLDER = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MonteCarloSim_gwjz4t'
    path = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MonteCarloSim_gwjz4t'
    files = list_files_recursively(path)

    files[:] = [f for f in files if not any(y in f for y in ["linter.py", "regression.py", "main.py"])]

    [lint.Run([f], exit=False) for f in files]

    # for f in files:
        # THRESHOLD = 10
        # run = lint.Run([f], exit=False)
        # score = run.linter.stats.global_note

    #     if score < THRESHOLD:
    #         print(f"Linter failed, Score:{score} < threshold value: {THRESHOLD}")
    #         exit_code = 1
    # sys.exit(exit_code)


if __name__ == '__main__':
    run_linter()
