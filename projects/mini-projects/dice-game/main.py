import os

def getfile():
    return input("\n📁 Enter file name:")
    
def getdata():
    return input("📝 Enter data:")

def checkfile(filename):
    if os.path.exists(filename):
        return True
    else:
        print("\n❌ File doesn't exist!\n")

def confirm(msg):
    ch=input(f"\n⚠️ {msg} (y/n):").lower()
    if ch not in ['y','n']:
        print("\n❌ Invalid Choice (X)\n")
        return confirm(msg)
    elif ch=='n':
        print("\n🚫 Cancelled!\n")
    else:
        return True

def create(filename):
    if os.path.exists(filename):
        print("\n⚠️ File already exists\n")
    else:
        with open(filename,'w') as f:
            print("\n✅ File created successfully!\n")
    
def read(filename):
    if checkfile(filename):
        with open (filename,'r') as f:
            content=f.read()
            if content=='':
                print("\n📭 File is Empty!\n") 
            else:
                print("\n📄 "+content+"\n")

def write(filename):
    if checkfile(filename):
        with open (filename) as f:
            content=f.read()
        if content == "":
            with open (filename,'w') as f2:
                f2.write(getdata())
                print("\n✅ Data written successfully!\n")
        else:
            if confirm("File contains data! Want to overwite?"):
                with open (filename,'w') as f3:
                    f3.write(getdata())
                    print("\n✍️ File overwritten successfully!\n")

def append(filename):
        print("""1. ➕ Append at line
2. 🔢 Append at index
3. 🚫 Cancel""")
        ch=input("👉 Enter your choice:")
        if ch=='1':
            with open (filename) as f:
                content=f.readlines()
            line=int(input("\n📌 Enter line number:"))
            if line<1 or line>len(content)+1:
                    print("\n❌ Invalid line number (X)\n")
                    append(filename)
            else:
                with open (filename,'w') as f2:
                    text=getdata()
                    if confirm("Confirm appending line?"):
                        content.insert(line-1,text + '\n')
                        f2.writelines(content)
                        print("\n✅ Data appended in file!\n")
        elif ch=='2':
                with open(filename,'r+') as f:
                    content=f.read()
                    index=int(input("🔢 Enter index:"))
                    if index<0 or index>len(content):
                        print("\n❌ Invalid index (X)\n")
                    else:
                        text=getdata()
                        if confirm("Confirm appending at index?"):
                            content=content[:index]+text+content[index:]
                            f.seek(0)
                            f.write(content)
                            print("\n✅ Data append successfully!\n")
        elif ch=='3':
            return
        else:
            print("\n❌ Invalid Choice (X)\n")
            append(filename)

def delete(filename):
    if checkfile(filename):
        os.remove(filename)
        print("\n🗑️ File deleted seccessfully\n")

def menu():
    while True:
        print("""========== 📂 Menu ==========
Press 1. 📄 Create a file
Press 2. 👀 Read file
Press 3. ✍️ Write in a file
Press 4. ➕ Append a file
Press 5. 🗑️ Delete a file
Press 6. 🚪 Exit
========================""")
        ch=input("👉 Enter your choice:")
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
            print("\n👋 Exited...\n")
            break
        else:
            print("\n❌ Invalid Choice (X)\n")

menu()
