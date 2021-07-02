password = "Hi";

pas = input("Give me your password: ")

if pas == password:
    print("Welcome Back\nSelect Option:\na)View All Passwords\nb)Select Password\nc)Add Password")
    sel = ""
    while sel.upper()!="A" and sel.upper()!="B" and sel.upper()!="C":
        sel = input("Select: ")
    print("")
    if sel.upper()=='A':
        file = open("passwords.txt",'r')
        lines = file.readlines()
        vals = []
        for n in lines:
            vals.append(n.split(","))
        for i in range(len(vals)):
            print("{}: {}".format(vals[i][0].upper(),vals[i][1][:-1]))
        file.close()
    elif sel.upper()=='B':
        file = open("passwords.txt",'r')
        lines = file.readlines()
        vals = []
        for n in lines:
            vals.append(n.split(","))
        search = input("What Password you search?: ")
        found = False
        for i in range(len(vals)):
            if search.upper()==vals[i][0].upper():
                print(vals[i][0]+": "+vals[i][1][:-1])
                found = True
        if not(found):
            print("No password found")
        file.close()
    elif sel.upper()=='C':
        name = input("New Site Password: ")
        pw = input("New Password: ")
        file = open("passwords.txt",'a')
        file.write(name.upper()+","+pw+"\n")
        file.close()
else:
    print("Incorrect, Good Bye :)")
print("")