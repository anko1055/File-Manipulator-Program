
contents=""
def reverse(inputpath,outputpath):
    with open(inputpath) as f:
        contents=f.read()
    with open(outputpath,'w') as f:
        f.write(contents[::-1])

def copy(inputpath,outputpath):
    with open(inputpath) as f:
        contents=f.read()
    with open(outputpath,'w') as f:
        f.write(contents)

def duplicate_contents(inputpath,n):
    with open(inputpath) as f:
        contents=f.read()
    i=0
    duplicated=""
    while i<int(n):
        duplicated+=contents
        i+=1
    with open(inputpath,'w') as f:
        f.write(duplicated)

def replace_string(inputpath,needle,newstring):
    with open(inputpath) as f:
        contents=f.read()
        replaced=contents.replace(needle,newstring)
    with open(inputpath,'w') as f:
        f.write(replaced)

def main():
    print("Choice manipulator")
    print("1. Revese contents")
    print("2. Copy contents")
    print("3. Repeat contents as many times as you like")
    print("4. Contents replace")
    choice=input("choice number")
    inputpath=input("inputpath:")
    
    if choice=="1":
        outputpath=input("outputpath:")
        reverse(inputpath,outputpath)

    elif choice=="2":
        outputpath=input("outputpath:")
        copy(inputpath,outputpath)
    
    elif choice=="3":
        n=input("What times you are repeat?")
        duplicate_contents(inputpath,n)    
    elif choice=="4":
        needle=input("What is the word before change?")
        newstring=input("What is the word after change?")
        replace_string(inputpath,needle,newstring)

if __name__ == "__main__":
    main()



