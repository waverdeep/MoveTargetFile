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
        elif _type=='copyto':
            func = functools.partial(copy_to_save_txt, target_directory=target_directory, encoding='cp949')
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
        txt[idx] = txt[idx].replace('KsponScript', 'KsponSpeech')

    wav = set(wav)
    txt = set(txt)
    # print(wav.difference(txt))
    print(txt.difference(wav))
    print(len(wav.difference(txt)))
    print(len(txt.difference(wav)))


def read_txt_file(file_path, encoding='utf8'):
    lines = []
    f = open(file_path, 'r', encoding=encoding, errors='ignore')
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
    f.close()
    return lines


def read_text_file_one_line(file_path, encoding='utf8'):
    f = open(file_path, 'r', encoding=encoding)
    line = f.readline()
    f.close()
    line = line.replace('\n', '')
    return line


def create_file(filepath):
    f = open(filepath, 'w', encoding='utf8')
    return f


def write_txt_file(line, target_filepath):
    file = create_file(target_filepath)
    file.write(line[0])
    file.close()
    return True


def copy_to_save_txt(filepath, target_directory, encoding='utf8'):
    line = read_txt_file(filepath, encoding=encoding)
    pure_filename = get_pure_filename(filepath)
    new_filepath = '{}/{}'.format(target_directory, pure_filename)
    status = write_txt_file(line, new_filepath)

