# PythonScripts
Scripts to make my life easier 


A) **Clean my X Folder **
Purpose: I have files of every type everywhere in every major folder: Documents, Pictures, Videos, Downloads, Desktop. 
This code is to help first uniformly figure out what is each of those folders and put them in their appropriate buckets in each of those locations 

Modify the file target, and take all of the files in a folder [ignores current folders], and 
  1) Reads all the extensions for 'files' that are in the folder currently
  2) Create a folder for each extension type that is represented in the folder that does not exist already
  3) Place files of each extension into their respective folder


Next step: 

B) Have this script run through multiple folders, then report what extension folders are in each of the 'major areas'. From there, merge folders into the correct locations for them. 
E.g., move all video folders into video, and merge them into a centralized extension folder in those 'major areas' 
Create unique folders [3D Models, Arduino Code, Python Code, etc.] under C\Users\<me>, and organize those files appropriately

C) Create a script that runs daily at a set time, on boot-up, etc., or just in some determined interval, and regularly cleans

D) Create a script to find hidden images (screenshots), audio files, and videos (recordings/playbacks) and report their location and file size [this is most of the 'bloat' on my computer. Then create a method to ignore specific folders they are in (primarily attempting to ignore places where those programs use those images and videos as a core feature focus on the 'bloat', and move all non-ignored folder content into the centralized image, video, etc. folders. 

Think of unique ways to report this in a manageable way - potentially, report out the folder each of these is in (once), and not duplicates, and the file size of the folder that said files can be found in (otherwise won't be very manageable to scan through, ignore, etc.). 

E) Inside each of the extension folders in each of the 'major areas', will create sub-folders for large memory items inside of it, and leave the rest normally inside of the folder to quickly identify storage eating items. 

F) Do this to help find all my hidden coding projects from the past for C++, C#, and Python and throw them on Github while also solving my storage issue on my cpu :) 
