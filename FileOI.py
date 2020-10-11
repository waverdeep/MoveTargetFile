import errno
import os
import glob
import shutil
import multiprocessing
import functools
from tqdm import tqdm


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def copy_all_file_to_target_directory(data, target_directory):
    shutil.copy(data, target_directory)
    return 0


def move_all_file_to_target_directory(data, target_directory):
    shutil.move(data, target_directory)
    return 0


def parallel_preprocess(filelist, target_directory, type='copy', parallel=None):

    try:
        if not (os.path.isdir(target_directory)):
            os.makedirs(os.path.join(target_directory))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise
    with multiprocessing.Pool(parallel) as p:
        if type == 'copy':
            func = functools.partial(copy_all_file_to_target_directory, target_directory=target_directory)
            output = list(tqdm(p.imap(func, filelist), total=len(filelist)))
        elif type == 'move':
            func = functools.partial(move_all_file_to_target_directory, target_directory=target_directory)
            output = list(tqdm(p.imap(func, filelist), total=len(filelist)))
