import os
import getpass

files = os.listdir()
extension = []
user = getpass.getuser()

for x in range(len(files)):
    if files[x]=="arranger.py": #To ignore this file
            pass
    else:
        if "." in files[x]:
            file_extension = files[x].split(".")[-1] #getting exact extension
        else:
            pass
    if file_extension in extension: #Ignoring multiple extensions
        pass
    else:
        extension.append(file_extension) #getting list of extensions

#Making directories
for x in range(len(extension)):
    ex = extension[x]
    fname = '"'+user +' '+ ex +' files"'
    cmd = "mkdir "+fname
    print(cmd)
    os.system(cmd)

files = os.listdir()

#Moving all files according to extension
for x in range(len(files)):
    if files[x]=="arranger.py":
            pass
    else:
        if "." in files[x]:
            file_extension = files[x].split(".")[-1]
            fname = '"'+user +' '+ file_extension +' files"'
            os.system("move "+ '"' +files[x]+'" '+fname)
        else:
            pass


