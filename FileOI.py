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


def get_pure_filename(filename):
    temp = filename.split('.')
    del temp[-1]
    temp = ' '.join(temp)
    temp = temp.split('/')
    temp = temp[-1]
    return temp


def copy_all_file_to_target_directory(data, target_directory):
    pure_filename = get_pure_filename(data)
    temp = '{}/{}.txt'.format(target_directory, pure_filename)
    if os.path.isfile(temp):
        pass
    else:
        shutil.copy(data, target_directory)
    return 0


def move_all_file_to_target_directory(data, target_directory):
    shutil.move(data, target_directory)
    return 0


def remove_all_file_to_target_directory(data, target_directory):
    os.remove(data)
    return 0


def parallel_preprocess(filelist, target_directory, _type='copy', parallel=None):

    try:
        if not (os.path.isdir(target_directory)):
            os.makedirs(os.path.join(target_directory))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise
    with multiprocessing.Pool(parallel) as p:
        if _type == 'copy':
            func = functools.partial(copy_all_file_to_target_directory, target_directory=target_directory)
            output = list(tqdm(p.imap(func, filelist), total=len(filelist)))
        elif _type == 'move':
            func = functools.partial(move_all_file_to_target_directory, target_directory=target_directory)
            output = list(tqdm(p.imap(func, filelist), total=len(filelist)))
        elif _type == 'remove':
            func = functools.partial(remove_all_file_to_target_directory, target_directory=target_directory)
            output = list(tqdm(p.imap(func, filelist), total=len(filelist)))


def wav_text_pair(input_dir):
    wav = get_all_file_path(input_dir, file_extension='wav')
    txt = get_all_file_path(input_dir, file_extension='txt')
    # for file in tqdm(wav):
    #     temp = file.replace('.wav', '.txt')
    #     if temp not in txt:
    #         print(file, "not exist")
    for idx, file in enumerate(wav):
        wav[idx] = file.replace('.wav', '')
    for idx, file in enumerate(txt):
        txt[idx] = file.replace('.txt', '')

    wav = set(wav)
    txt = set(txt)
    print(wav.difference(txt))
    print(txt.difference(wav))