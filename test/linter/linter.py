import glob
import os
import sys
from pylint import lint

project_directory = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MonteCarloSim_gwjz4t'

def list_files_recursively(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))
    return file_list


files = list_files_recursively(project_directory)

for f in files:
    THRESHOLD = 10

    run = lint.Run([f], exit=False)
    score = run.linter.stats.global_note

    print(f"Score: {score}")

    # if score < THRESHOLD:
    #     print(f"Linter failed, Score: {score} < threshold: {THRESHOLD}")
    #     sys.exit(1)
    # sys.exit(0)

# THRESHOLD = 10

# run = lint.Run(["../main.py"], exit=False)
# score = run.linter.stats.global_note
#
# print(f"Score: {score}")
#
# if score < THRESHOLD:
#     print(f"Linter failed, Score: {score} < threshold: {THRESHOLD}")
#     sys.exit(1)
# sys.exit(0)


