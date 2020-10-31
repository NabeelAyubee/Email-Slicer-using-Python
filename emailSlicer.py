dict={}
while True:
    try:
        mail=input("Enter your email Id:  ")
        mail=mail.strip()
        dict[mail[:mail.index("@")]] = mail[mail.index("@")+1:]
        for keys,values in dict.items():
            print ("Username: ",keys," \nDomain: ",values)
            print(" THANK YOU")
    except:
        print(" enter valid email id")

