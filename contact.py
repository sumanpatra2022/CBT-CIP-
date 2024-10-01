contacts={}
while True:  
    print('\nCONTACTMASTER')
    print('1.Add new contact')
    print('2.Delete contact')
    print('3.Search contact')
    print('4.Display contact')
    print('5.Exit contact')
    
    choice=input("Enter your choice:=")
    if choice=='1':
        name=input("Enter your name:")
        if name in contacts:
            print(f"Contact {name} name already exists")
        else:
            email=input("Enter your email:")
            mobile=input("Enter mobile number:")
            contacts[name]={
                "Email":email,"Mobile":mobile
            }
            print(f"Contact  {name} name has been created succesfully")
  
    elif choice=='2':
        name=input("Enter contact name to delete:")
        if name in contacts:
            del contacts[name]
            print(f"Contact  {name} name deleted succesfully")
        else:
            print("Contact not found")
    elif choice=='3':
        search_name=input("Enter contact name to search:")
        found=False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found-Name:{name},Email:{email},Mobile:{mobile}')
                found=True
        if not found:
            print("No contact found with that name")
    elif choice=='4':
        name=input("Enter contact name to view=")
        if name in contacts:
            contact=contacts[name]
            print(f'Name:{name},Email:{email},Mobile no:{mobile}')
        else:
            print("Contact not found")            
    elif choice=='5':
        print("Closed the contactmaster")
        break
    else:
        print("Invalid input")                


#OUTPUT:
"""
  CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=1
Enter your name:SUMAN
Enter your email:SUMAN@123
Enter mobile number:1234567892
Contact  SUMAN name has been created succesfully

CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=1
Enter your name:PATRA
Enter your email:PATRA@456
Enter mobile number:7896956256
Contact  PATRA name has been created succesfully

CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=3
Enter contact name to search:SUMAN
Found-Name:SUMAN,Email:PATRA@456,Mobile:7896956256

CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=4
Enter contact name to view=SUMAN
Name:SUMAN,Email:PATRA@456,Mobile no:7896956256

CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=2
Enter contact name to delete:SUMAN
Contact  SUMAN name deleted succesfully

CONTACTMASTER
1.Add new contact
2.Delete contact
3.Search contact
4.Display contact
5.Exit contact
Enter your choice:=5
Closed the contactmaster         
"""