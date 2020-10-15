import FileOI
import multiprocessing

input_dir = '/data/Kspon_dataset/character'
target_dir = '/data/Kspon_dataset/wav'
file_extension = 'txt'
# input_dir = './sample_dataset'
# target_dir = './new_dataset'
# file_extension = 'pcm'
filelist = FileOI.get_all_file_path(input_dir, file_extension=file_extension)
# FileOI.parallel_preprocess(filelist, target_dir, _type='copy', parallel=multiprocessing.cpu_count())
#
print(len(FileOI.get_all_file_path(target_dir, file_extension='wav')))
print(len(FileOI.get_all_file_path(target_dir, file_extension='txt')))

# FileOI.wav_text_pair(target_dir)
FileOI.parallel_preprocess(filelist, target_dir, _type='copy', parallel=multiprocessing.cpu_count())

print(len(FileOI.get_all_file_path(target_dir, file_extension='wav')))
print(len(FileOI.get_all_file_path(target_dir, file_extension='txt')))

FileOI.wav_text_pair(target_dir)