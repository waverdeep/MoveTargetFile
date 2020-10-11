import FileOI
import multiprocessing

input_dir = './sample_dataset'
target_dir = './new_dataset'
file_extension = 'pcm'
filelist = FileOI.get_all_file_path(input_dir, file_extension=file_extension)
FileOI.parallel_preprocess(filelist, target_dir, multiprocessing.cpu_count())

