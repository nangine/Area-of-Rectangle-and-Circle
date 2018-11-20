print ()
yes=True
while yes:
    print ("Choose shapes below :")
    print ("    1. Rectangle")
    print ("    2. Circle")
    print ()
    Choice = input ("Your choice? [1/2] ")
    if Choice == "1":
        print ()
        print ()
        length = float(input ("Insert length = "))
        width = float(input ("Insert width = "))
        arearec = length*width
        print ()
        print ("Area of Rectangle = ")
        print (round(arearec,2))
        print ()
        opt = input ("Continue ? y/t -> ")
        print ()
        if opt == "y":
            yes=True
        else :
            print ("***Done***")
            break
    else :
        print ()
        rad = float(input ("Insert radius = "))
        pi=22/7
        areacir = pi*rad*rad
        print ()
        print ("Area of Circle = ")
        print (round(luasl,2))
        print ()
        opt = input ("Continue ? y/t -> ")
        print ()
        if opt == "y":
            yes=True
        else :
            print ("***Done***")
            break
