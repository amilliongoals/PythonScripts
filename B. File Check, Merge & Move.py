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
Coding= 'C:\\Users\\gagni\\Coding'

Folder_list=[Pictures, Videos, Desktop, Documents, Downloads, Music, ThreeD_Objects, Coding]


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

    
        for files in Folder_list[i]:
           if files.endswith('.jpeg', '.jpg', '.png','.gif', '.tiff', '.psd', '.raw', '.bmp', '.hdr',  '.heic', '.img', '.jfif', '.snag', '.svg', '.tif'):
              shutilmove( source , Pictures ) #go to pictures of file type oflder 
        #can change to shutilcopy if I don't want to remove where it is currently. 

         for files in Folder_list[i]:
           if files.endswith('.mov', '.mp4',  '.SC2Replay', '.rofl', '.swf', '.webm', '.zoom'):
              shutilmove( source , Videos )    
           if files.endswith('.exe'):
              shutilmove( source ,Desktop)
           if files.endswith('.csv','.dat','.doc','.docx','.escv','.fits','.pp_','.ppt', '.pptx','.txt','.xls','.xlsm','.xlsx'):
              shutilmove( source ,Documents)
           if files.endswith('.download','.ex_','.gz','.jar','.zip','.msi','.pak'):
              shutilmove( source ,Downloads )
           if files.endswith('.glb','.stl', '.obj', '.x3g', '.3ds', '.3dm', '.dae', '.fbx'):
              shutilmove( source ,ThreeD_Objects )
           if files.endswith('.ahk','.apk','.aia','.appinstaller','.css','.db', '.h','.html','.ino', '.ipynb','.ipynd', '.js','.json','.jsp','.notebook','.py','.pyc'):
              shutilmove( source ,Coding )


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


#now that I know all my file types let me plan where I want specific ones to go
#I'll just ignore the file that are not of use, below is my structure for the files I 
#want ended up in each respective folder 

#Pictures= jpeg jpg png gif tiff psd raw bmp hdr heic img jfif snag svg tif 
#Videos= mov mp4  SC2Replay rofl swf webm zoom 
#Desktop= exe
#Documents=  csv  dat doc docx escv fits pp_ ppt pptx txt xls xlsm xlsx 
#Downloads= download ex_ gz jar zip msi pak 
#Music= mp3 aup3 ogg
#ThreeD_Objects= glb stl 
#Coding =  ahk apk aia appinstaller css db h html ino ipynb ipynd js json jsp notebook py pyc

# create folders for each extension type
for extension in extensions:
    if not os.path.exists(os.path.join(target_folder, extension)):
        os.mkdir(os.path.join(target_folder, extension))

shutil.move(os.path.join(target_folder, item), 
             os.path.join(target_folder, file_extension, item)) 

#move to folder by file type and file name (item)
