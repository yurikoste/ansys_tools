""" 
Script removes files listed be re patterns in <PATTERN_TO_DEL> list from the current folder
Can be used to remove unnecessary files from working folder
"""
import os


def getFiles(path: str) -> list:
    """
    Get list of files in directory. 
    """
    import glob 

    files = glob.glob(os.path.join(path,'**'))
    global_path = os.getcwd()
    return [os.path.join(global_path, f) for f in files]
    

def matchFiles(PATTERN_TO_DEL: list, files_in_folder: list) -> list:
    """
    Match files from list of files in folder with pattern to defined which of them
    should be deleted
    """
    import re

    matched_files = []
    for f in files_in_folder:
        for pattern in PATTERN_TO_DEL:
            if re.search(pattern, f):
                matched_files.append(f)
    return matched_files

def delFiles(files_to_del: list) -> None: 
    """
    Delete files from folder according to input list
    """
    num_of_deleted = 0  
    for f in files_to_del: 
        if os.path.isfile(f):
            try:
                os.remove(f)
                num_of_deleted += 1
                # print(f'File {f} was deleted')                
            except OSError as err:
                print(f"Error '{err.strerror}' during attempt to delete file '{err.filename}'")    
    print(f'{num_of_deleted} ANSYS temporary files was/were deleted from the working folder')


PATTERN_TO_DEL = [
        "\.(esav|osav|full|emat|page|DSPsymb)", 
        "run\d{1,3}\.(r001|r002|r003|db|ldhi|rdb|rst)",
        "_+\w\.out$"
        ]
PATH = 'test' 

if __name__ == '__main__':       
    delFiles(matchFiles(PATTERN_TO_DEL, getFiles(PATH)))



