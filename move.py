import os
class move:
    def __init__(self,filepath): #constructor function
        self.filepath=filepath
    
    def file_names(self):  #getting file names 
        self.filenames=os.listdir(self.filepath)

    sorted_files={'folders':[]}

    def sortfiles(self):  #sorting files by type
        for i in self.filenames:
            if not os.path.isfile(os.path.join(self.filepath,i)):
                self.sorted_files['folders'].append(i)
            else:
                split_up_name = os.path.splitext(i)
                extenstion=split_up_name[1][1:]
                if extenstion in self.sorted_files:
                    self.sorted_files[extenstion].append(i)
                else:
                    self.sorted_files[extenstion]=[]
        print(self.sorted_files)
    

test = move(r"C:\Users\rachi\OneDrive\Desktop")
test.file_names()
test.sortfiles()