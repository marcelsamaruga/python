fname = "romeo.txt"

fh = open(fname,'r')
lst = list()

for line in fh:

    words = line.rstrip().split()
    
    for word in words:
        if not word in lst:
            lst.append(word)
        
lst.sort()
print lst

