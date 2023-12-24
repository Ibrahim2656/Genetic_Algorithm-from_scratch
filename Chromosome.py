import math
from tkinter import filedialog
class Node:
    def __init__(self,id,x,y):
        self.x_axis=float(x)
        self.y_axis=float(y)
        self.id=int(id)
        
#open a file and create adata list using the info in the file 
file_name =""
file_name=filedialog.askopenfilename()
if file_name != " ":
    print("Found file.text",file_name)
dataset=[]

with open(file_name,"r") as data:
    for line in data:
        new_line=line.strip() #remove the spaces at the beginning
        new_line=new_line.split(" ") #split a list into string 
        id,x,y,=new_line[0],new_line[1],new_line[2]
        dataset.append(Node(id=id,x=x,y=y))

N=len(dataset) #total number of unique points, including starting point

# this function will be run once at the beginning of the program to create a distance matrix
def creat_distacne_mtx(node_list):
    #make the matrix zero values
    matrix=[[0 for _ in range(N)] for _ in range(N)]
    
    #calc the distance now 
    for i in range(0,len(matrix)-1):
        for j in range(0,len(matrix[0])-1):
            #calc the euclidean distance (a^2=b^2+c^2)
            matrix[node_list[i].id][node_list[j].id]=math.sqrt(
                pow((node_list[i].x_axis-node_list[j].x_axis),2)+
                    pow((node_list[i].y_axis-node_list[i].y_axis),2))
        
    return matrix
matrix=creat_distacne_mtx(dataset)

class chromosome:
    def __init__(self,node_list):
        self.chromosome=node_list
        chr_represntation=[]
        for i in range(0,len(node_list)):
            chr_represntation.append(self.chromosome[i].id)
        self.chr_represntation=chr_represntation
        
        dist=0
        #get distance from the matirx
        for j in range(1,len(self.chr_represntation)-1):
            dist+=matrix[self.chr_represntation[j]-1][self.chr_represntation[j+1]-1]
        self.cost=dist
        self.fitness=1/self.cost
            
