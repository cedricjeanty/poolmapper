# Import the os module, for the os.walk function
import os
import re
from shutil import copyfile

regex = re.compile(r"\((\d*)\)\.jpeg")

# Set the directory you want to start from
root_dir = '/Volumes/My Passport/Uploads/mapdata/TrainingData'
training_data_dir =  "training_data"
for dirName, subdirList, fileList in os.walk(root_dir):
    idx = 0
    for fname in fileList:
        result = regex.search(fname)
        if result:
            category = result.groups()[0]
            if category:
                folder = os.path.join(training_data_dir, str(category) + "_pools")
                if not os.path.isdir(folder):
                    os.mkdir(folder)
                new_name = fname.replace("(" + category + ")", "")
                dst = ''.join([folder, "/", new_name])
                # print(dst)
                copyfile(dirName + "/" + fname, dst)
                idx += 1