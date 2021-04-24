class Read:
    portals = []

    def __init__(self,file):
        self.file=file
        self.portals=[]
        self.citeste()

    def citeste(self):
        f = open("layouts/"+self.file+".lay","r")
        Lines = f.readlines()
        k=0
        nr_linii=0
        for line in Lines:
            nr_linii+=1
        # print nr_linii
       
        for line in Lines:
            for i in line:
                if i == 's':
                    self.portals.append((nr_linii-1-Lines.index(line),line.index(i)))
        
        
        