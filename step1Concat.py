import os
import shutil

dirs = "C:\\Users\\your dir\\Downloads\\VM202101\\dt=2021-01-04"

dirPaths = []
destFilenames = []
for dir in next(os.walk(dirs))[1]:
    dirPath = dirs + "\\" + dir 
    destFilename = "results\\vm20210104" + dir[-5:] + ".gz"
    print('destFilename',destFilename)
    print('dirPath',dirPath)

    with open(destFilename, 'wb') as destFile:
        for root, subdirectories, files in os.walk(dirPath):
            # for subdirectory in subdirectories:
            #     print(os.path.join(root, subdirectory))
            for file in files:
                if file.endswith('.gz'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'rb') as sourceFile:
                        shutil.copyfileobj(sourceFile, destFile)

