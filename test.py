import re

myfile = open('test.txt','r')
lines = myfile.readlines()
myfile.close()

matchstring = re.compile("src=[\"|'|a-zA-Z](\w+[/|\w+])+.\w+[\"|'|\s]",re.IGNORECASE)

for line in lines :
    imagepath = matchstring.search(line,1)
    if imagepath :
        print imagepath.group(0)
