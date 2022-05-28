import os
from encodings import utf_8
import re
from subprocess import *
from sys import *
from os import path, makedirs, listdir
from shutil import *
import time


def create_folds():
    if not os.path.exists('Ознакомительная папка'):
        os.mkdir('Ознакомительная папка')
    if not os.path.exists('Ознакомительная папка\тема A'):
        os.makedirs("Ознакомительная папка\тема A")
    if not os.path.exists('Ознакомительная папка\тема B'):
        os. makedirs("Ознакомительная папка\тема B")


def move_folds():
    main_folder = os.listdir()
    print(main_folder)
    for file in main_folder:
        string = re.search(r"[AB]", file)
        if string!=None:
            string = string.group()
            if os.path.exists('Ознакомительная папка\тема '+string):
                move(file,'Ознакомительная папка\тема '+string)
    if os.path.exists('wiki.txt'):
        move('wiki.txt', 'Ознакомительная папка\тема B')


def run_tasks(main_folder):
    folders = listdir(main_folder)
    for folder in folders:
        print('folder "', folder, '":', sep="")
        files = listdir(path.join(main_folder, folder))
        for file in files:
            string = re.search(r"[AB]", file)
            if string != None:
                print('>>> script "', file, '"', sep="")
                start = time.time()
                res = run([executable, path.join(main_folder, folder, file)], stdout=PIPE, encoding="utf_8")
                all_time = time.time() - start
                task = open('/'.join([main_folder, folder, file]), "r")
                for line in task.readlines():
                    if re.search(r"def ", line) != None:
                        line = line[4:(len(line) - 2)]
                        print('>>> >>> function "', line, '"', sep="")
                        break
                task.close()
                out = re.sub(r"\n", "", res.stdout)
                print('>>> >>> output "', out, '"', '\n', ">>> >>> time %s sec" % ('%.3f' % all_time), sep="")


if __name__=='__main__':
    print(os.getcwd())
    create_folds()
    move_folds()
    run_tasks('Ознакомительная папка')