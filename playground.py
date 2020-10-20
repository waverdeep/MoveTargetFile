import FileOI
import multiprocessing

input_dir = '/data/Kspon_dataset/original'
target_dir = '/data/Kspon_dataset/wav'
file_extension = 'txt'
# input_dir = './sample_dataset'
# target_dir = './new_dataset'
# file_extension = 'pcm'
# filelist = FileOI.get_all_file_path(input_dir, file_extension=file_extension)
# FileOI.parallel_preprocess(filelist, target_dir, _type='copy', parallel=multiprocessing.cpu_count())
#
wav_list = FileOI.get_all_file_path(target_dir, file_extension='wav')
print(len(wav_list))
txt_list = FileOI.get_all_file_path(input_dir, file_extension='txt')
print(len(txt_list))

# FileOI.wav_text_pair(target_dir)
# FileOI.parallel_preprocess(txt_list, target_dir, _type='remove', parallel=multiprocessing.cpu_count())
#
# print(len(FileOI.get_all_file_path(target_dir, file_extension='wav')))
# print(len(FileOI.get_all_file_path(target_dir, file_extension='txt')))
# #
# for i in range(10):
#     print(FileOI.read_txt_file(txt_list[i], encoding='cp949'))
#     print(txt_list[i])
# #
# FileOI.wav_text_pair(target_dir)

FileOI.parallel_preprocess(txt_list, target_dir, _type='copyto', parallel=multiprocessing.cpu_count())

wav_list = FileOI.get_all_file_path(target_dir, file_extension='wav')
print(len(wav_list))
txt_list = FileOI.get_all_file_path(target_dir, file_extension='txt')
print(len(txt_list))
