#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

src = "/data/prod/"
dest = "/data/prod_backup/"
src = os.path.expanduser('~' + src)
dest = os.path.expanduser('~' + dest)

#os.chdir("~")
#for root, dirs, files in os.walk(".", topdown = False):
#   for name in files:
#      print(os.path.join(root, name))
#   for name in dirs:
#      print(os.path.join(root, name))

def run(task):
  # Do something with task here
    print("Handling {}".format(task))
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3', 'task4']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
