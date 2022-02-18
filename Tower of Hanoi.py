def movedisk(n,fromtower,totower,auxtower):
    if(n==1):
        print("Move disk",n,"from",fromtower,"to",totower)
    else:
        movedisk(n-1,fromtower,auxtower,totower)
        print("Move disk",n,"from",fromtower,"to",totower)
        movedisk(n-1,auxtower,totower,fromtower)
print("TOWER OF HANOI USING RECURSION")
num=int(input("How many disks:"))
print("The moves are:")
movedisk(num,'S','D','I')
print("Note:\n S-Source\n D-Destination\n I-Intermediate")