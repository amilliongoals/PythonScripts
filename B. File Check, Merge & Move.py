import os
import shutil

#first parent (overarching user folder that has desktop, images, videos, etc)
parent_folder='C\\Users\\gagni'
#our first target folder Pictures
Pictures= 'C:\\Users\\gagni\\Pictures'
Videos= 'C:\\Users\\gagni\\Videos'
Desktop= 'C:\\Users\\gagni\\Desktop'
Documents= 'C:\\Users\\gagni\\Documents'
Downloads= 'C:\\Users\\gagni\\Downloads'
Music= 'C:\\Users\\gagni\\Music'
ThreeD_Objects= 'C:\\Users\\gagni\\3D_Objects'


Folder_list=[Pictures, Videos, Desktop, Documents, Downloads, Music, ThreeD_Objects]


file_types_available=set()

#this gets the name of the extensions, by looking at the target folder, and looking at the item names, and then splitting the extension name out
#extensions =  {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}  #checks for files not folders
#splits the item file name by the period symbnol, and -1 focuses on text after the . which is file type 
#print(extensions)


i=0
maxelement=len(Folder_list)-1 #number of list elements -1 

while i <len(Folder_list):
    for root, dirs, files in os.walk(Folder_list[i], topdown=True):
        #print(root) #to view root from folder currently being viewed 
        #print(dirs) #to view directory from folder currently being viewed 
        #print(files) #to view files from folder currently being viewed 

        for item in files:
         if "." in item:    #check for files with . in the name (filename)
            extensions =item.split('.')[-1]  #the extension type will be stored as 'extensions'
            file_types_available.add(extensions)  
    i=i+1

#this prints out the extensions from all the items in my list, my list currently includes
# everything in Folder_list,    

#extensiosn are not alphabetical, so I would like to rearrange them to easily find different parts

#file_types_available.sort()         
#error 'set' object has no attribute 'sorted'/'sort' 
#need to convert set objet into a list to sort it 
filetypesort=list(file_types_available) #convert 'set' data into a normal list 

filetypesort.sort() #sort said list now  

print(filetypesort) #moved print outside of loop, so it only prints all of the values
#succesfully printed sorted list of data types of files in each of the folder/sub-folder of interest 



