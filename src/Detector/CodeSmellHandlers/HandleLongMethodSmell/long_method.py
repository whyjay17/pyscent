import shlex
from subprocess import run, PIPE
import os

def output_long_methods(directory):
    cmd = "pylint --disable=E,W,C,F,I " + get_file_list(directory)
    print (cmd)
    result = run(shlex.split(cmd), stdout=PIPE , cwd=directory)
    # out, err = process.communicate()
    # exit_code = process.wait()
    print(result)
    return result

def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_list.append(filename + " ")
    return "".join(file_list)