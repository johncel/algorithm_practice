from os import listdir
from os.path import isfile, isdir, join


def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    list_paths = listdir(sPath)
    onlyfiles = [f for f in list_paths if isfile(join(sPath, f))]
    onlydirs = [f for f in list_paths if isdir(join(sPath, f))]
    for dir_path in onlydirs:
        print_directory_contents(join(sPath, dir_path))

    for file in onlyfiles:
        print(f'{join(sPath, file)}')


print_directory_contents('.')
