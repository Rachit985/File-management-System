import os
class move:
    def __init__(self,filepath):
        self.filepath=filepath
    files = [f for f in os.listdir(.filepath) if os.path.isfile(os.path.join(filepath,f))]
 
    print(os.path.join(filepath,"pdf","fe.txt"))
    def pdf(file):
        x = list(locals().keys())
        print(x[0])