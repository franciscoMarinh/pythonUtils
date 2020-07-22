import os

def getDirectoryfilesByCreationDate(dirpath):
    a = [s for s in os.listdir(dirpath)
        if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a

def getDirectoryFiles(dirpath):
    path = os.path.join(dirpath)
    files = os.listdir(path)
    return files

def renameLastFileInFolder(folderPath, renamedFile, renamedExt):
    files = getfiles(folderPath)
    lastFile = files[-1]
    os.rename(folderPath + files[-1], folderPath + renamedFile + renamedExt)
