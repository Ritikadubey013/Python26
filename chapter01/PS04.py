import os

# specifying the directory you want to list 
directory_path='chapter01' 
#basically in this we can find out the details of folder 


# list all the files and directories in specified path 
contents= os.listdir(directory_path)

#print each file and directory name 
for item in contents:
    print(item)