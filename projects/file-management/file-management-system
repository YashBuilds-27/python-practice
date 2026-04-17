import os

def getfile():
    return input("\nEnter file name:")
    
def getdata():
    return input("Enter data:")

def checkfile(filename):
    if os.path.exists(filename):
        return True
    else:
        print("\nFile doesn't exist!\n")

def confirm(msg):
    ch=input(f"\n{msg} (y/n):").lower()
    if ch not in ['y','n']:
        print("\nInvalid Choice (X)\n")
        return confirm(msg)
    elif ch=='n':
        print("\nCancelled!\n")
    else:
        return True

def create(filename):
    if os.path.exists(filename):
        print("\nFile already exists\n")
    else:
        with open(filename,'w') as f:
            print("\nFile created successfully!\n")
    
def read(filename):
    if checkfile(filename):
        with open (filename,'r') as f:
            content=f.read()
            if content=='':
                print("\nFile is Empty!\n") 
            else:
                print("\n"+content+"\n")

def write(filename):
    if checkfile(filename):
        with open (filename) as f:
            content=f.read()
        if content == "":
            with open (filename,'w') as f2:
                f2.write(getdata())
                print("\nData written successfully!\n")
        else:
            if confirm("File contains data! Want to overwite?"):
                with open (filename,'w') as f3:
                    f3.write(getdata())
                    print("\nFile overwritten successfully!\n")

def append(filename):
        print("""1. Append at line
2. Append at index
3. Cancel""")
        ch=input("Enter your choice:")
        if ch=='1':
            with open (filename) as f:
                content=f.readlines()
            line=int(input("\nEnter line number:"))
            if line<1 or line>len(content)+1:
                    print("\nInvalid line number (X)\n")
                    append(filename)
            else:
                with open (filename,'w') as f2:
                    text=getdata()
                    if confirm("Confirm appending line?"):
                        content.insert(line-1,text + '\n')
                        f2.writelines(content)
                        print("\nData appended in file!\n")
        elif ch=='2':
                with open(filename,'r+') as f:
                    content=f.read()
                    index=int(input("Enter index:"))
                    if index<0 or index>len(content):
                        print("\nInvalid index (X)\n")
                    else:
                        text=getdata()
                        if confirm("Confirm appending at index?"):
                            content=content[:index]+text+content[index:]
                            f.seek(0)
                            f.write(content)
                            print("\nData append successfully!\n")
        elif ch=='3':
            return
        else:
            print("\nInvalid Choice (X)\n")
            append(filename)

def delete(filename):
    if checkfile(filename):
        os.remove(filename)
        print("\nFile deleted seccessfully\n")

def menu():
    while True:
        print("""==========Menu==========
Press 1. Create a file
Press 2. Read file
Press 3. Write in a file
Press 4. Append a file
Press 5. Delete a file
Press 6. Exit
========================""")
        ch=input("Enter your choice:")
        if ch=='1':
            create(getfile())
        elif ch=='2':
            read(getfile())
        elif ch=='3':
            write(getfile())
        elif ch=='4':
            append(getfile())
        elif ch=='5':
            delete(getfile())
        elif ch=='6':
            print("\nExited...\n")
            break
        else:
            print("\nInvalid Choice (X)\n")

menu()
