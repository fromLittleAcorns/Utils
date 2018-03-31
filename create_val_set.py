'''
Simple utility script to split a training set catagorised by folder into a smaller training
set and a validation set.

Modify the val-perc variable to be the percentage of images in each folder that are moved to the
validation directory
Setup the PATH variable so that it points to the level above the folder containing the training
images

sub_path should then be the name of the training folder
target path should be the name of the parent folder for the validaion images

'''

import os
from os.path import isfile, isdir, join
import shutil
import numpy as np


val_perc = 20
PATH="../../../datasets/imagenet/"
sub_path="train/"
target_path="valid/"

os.chdir(PATH)
cwd=os.getcwd()

# Create validation path
try:
    os.listdir(target_path)
except:
    os.mkdir(target_path)

# Get directory names
dirnames=[f for f in os.listdir(sub_path) if isdir(join(sub_path,f))]

# Note - will create parallel folders in a subdirectory called valid

for dirname in dirnames:
    # get list of filenames
    full_path=join(cwd, sub_path)
    full_path=join(full_path, dirname)

    fnames=[f for f in os.listdir(full_path) if isfile(join(full_path, f))]
    no_files=len(fnames)

    # create index numbers to keep and those to move
    idxs = np.random.permutation(no_files)
    val_files = int(no_files*val_perc/100.0)

    # create target directory
    target_dir=join(cwd, target_path)
    target_dir=join(target_dir, dirname)
    try:
        os.mkdir(target_dir)
    except:
        print('Directory already exists')

    # Move relevant files
    for i in range(val_files):
        file = fnames[i]
        shutil.move(join(full_path,file), target_dir)

