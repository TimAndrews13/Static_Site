import os
import shutil


def copy_directory(source_dir, target_dir):
    #Set File Paths
    original_cwd = os.getcwd()
    target_path = os.path.join(original_cwd, target_dir)
    source_path = os.path.join(original_cwd, source_dir)

    #Remove public File Directory
    if os.path.exists(target_path):
        print(f"Removing File Directory: {target_path}")
        shutil.rmtree(target_path)

    #Make Removed Directory that is Empty
    os.mkdir(target_path)

    #Recursive Function that Copies all the Contents from Source Directory to Target Directory
    #set contents of Source Directory
    contents = os.listdir(source_path)
    #Loop through contents of Source Directory
    for content in contents:
        content_source_path = os.path.join(source_path, content)
        content_target_path = os.path.join(target_path, content)
        #Check if new content path contains a file:
        if os.path.isfile(content_source_path):
            #If path is file, copy to Target Directory
            print(f"Copying {content_source_path} to {content_target_path}")
            try:
                shutil.copy(content_source_path, content_target_path)
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except PermissionError:
                print("Permission denied")
            except:
                print("Error occured while copying file.")
        #If another directory, recursively call copy_directory
        else:
            print(f"Directory Found: {content_source_path}\nLooping Through Directory for Copy")
            copy_directory(content_source_path, content_target_path)