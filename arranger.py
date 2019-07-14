import os
import getpass

files = os.listdir()
extension = []
user = getpass.getuser()

for x in range(len(files)):
    if files[x]=="arranger.py":
            pass
    else:
        if "." in files[x]:
            filename, file_extension = files[x].split(".")
        else:
            pass
    if file_extension in extension:
        pass
    else:
        extension.append(file_extension)

for x in range(len(extension)):
    ex = extension[x]
    fname = '"'+user +' '+ ex +' files"'
    cmd = "mkdir "+fname
    print(cmd)
    os.system(cmd)

files = os.listdir()
for x in range(len(files)):
    if files[x]=="arranger.py":
            pass
    else:
        if "." in files[x]:
            filename, file_extension = files[x].split(".")
            fname = '"'+user +' '+ file_extension +' files"'
            os.system("move "+ '"' +files[x]+'" '+fname)
        else:
            pass


