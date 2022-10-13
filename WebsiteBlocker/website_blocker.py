def block(site):
    self.data.append("127.0.0.1\t{}\t#siteblocker\n".format(site))
    with open("C:\Windows\System32\drivers\etc\hosts","w") as wf:
        wf.writelines()
    wf.close()

def unblock(site):
    for i in data: 
        if site in i and "#siteblocker" in i:
            data.remove(i)
            
    with open("C:\Windows\System32\drivers\etc\hosts","w") as wf:
        wf.writelines(data)
    wf.close()

def main():
    print("Welcome to webiste blocker!")
    print("1.Block\n2.Unblock")
    inp = int(input("Choose an option"))
    if inp==1:
        site = input("Enter the website url to block : ")
        if site:
            block(site)
    
    elif inp==2:
        site = input("Enter the website url to unblock : ")
        if site:
            unblock(site)

if __name__ == "__main__":
    with open("C:\Windows\System32\drivers\etc\hosts","r") as rf:
        data =rf.readlines()
    rf.close()

    main()