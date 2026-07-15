"""
1.Create list
2.duplicate remove
3.read .csv/.json
4.Freeze the set as tuple[immutable]
5.Find pending files
"""
files = ['file1.csv','file2.json','file3.txt','file4.csv','file5.exe','file1.csv']
print(files)
ids = [101, 102, 101, 103, 102, 104]
def removeDuplicate(files:list)->set:
    return set(files)

print(removeDuplicate(files))
print(removeDuplicate(ids))

def readFiles(files1: list) -> set:
    return [f for f in files1 if f.endswith('.csv')]
print(readFiles(files))

def convertTuple(file1:list) ->tuple:
    return tuple(file1)
print("this is my tupele...",convertTuple([12,34,"345","abcd"]))

all_files = {"users.csv", "products.csv", "sales.csv"}
processed = {"users.csv"}

def findNotProcessed(inputFiles: list,proccesFiles:list)->list:
    return all_files-processed

print(findNotProcessed(all_files,processed))



