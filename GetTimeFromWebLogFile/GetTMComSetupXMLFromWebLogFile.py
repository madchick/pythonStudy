import re

#resultFile = open('result_tmcomsetupxml.txt','w')

#i = 1
#for i in range(1,28) :

#    if i<10 :
#        myfile = open("ex05090" + str(i) + ".log","r")
#    else :
#        myfile = open("ex0509" + str(i) + ".log","r")
        
#    lines = myfile.readlines()
#    myfile.close()

#    matchstring = re.compile("/tmcomsetup.xml",re.IGNORECASE)

#    for line in lines :
#        times = matchstring.search(line,1)
#        if times :
#            resultFile.writelines(line)

#resultFile.close()



myfile = open('result_tmcomsetupxml.txt','r')
lines = myfile.readlines()
myfile.close()

matchstringTime = re.compile("[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}",re.IGNORECASE)
matchstringDate = re.compile("[0-9]{1,4}-[0-9]{1,2}-[0-9]{1,2}",re.IGNORECASE)
matchstringIP   = re.compile("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",re.IGNORECASE)

myfile     = open('result_tmcomsetupxml.csv','w')

for line in lines :
    times = matchstringTime.search(line,0)
    dates = matchstringDate.search(line,0)
    ips = matchstringIP.search(line,40)
        
    myfile.writelines(dates.group(0)+","+times.group(0)[0:2]+","+ips.group(0)+"\n")

myfile.close()



