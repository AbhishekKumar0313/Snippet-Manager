import getpass
import json
import os
from passlib.context import CryptContext
import sys
from fpdf import FPDF

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def check_password(stored_hash, password):
    return pwd_context.verify(password, stored_hash)

class CodeSnippetPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Code Snippets Collection', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_snippet(self, title, code):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font('Courier', '', 10)
        self.multi_cell(0, 10, code)
        self.ln(5)

# Function to create and save the PDF
def create_pdf(snippets, filename='snippets.pdf'):
    pdf = CodeSnippetPDF()
    pdf.add_page()

    for title, code in snippets:
        pdf.add_snippet(title, code)
    
    pdf.output(filename)
    print(f"PDF '{filename}' has been created and saved.")


class Snippet:
    id=0
    def __init__(self,lang,code,description):
        self.__language = lang
        self.__code = code
        self.__description = description
        Snippet.id+=1
        
    def get_language(self):
        return self.__language
    def get_code(self):
        return self.__code
    def get_description(self):
        return self.__description
    

class SnippetManager_Authentication():
    def __init__(self,name=None,email=None,password=None):
        self.__email=email
        self.__password=password
        self.__name=name
        self.first_menu()
        
    def set_email(self,email):
        self.__email=email
        
    def get_email(self):
        return self.__email 
        
    def set_password(self,password):
        self.__password=password
        
    def get_password(self):
        return self.__password
        
    def set_name(self,name):
        self.__name=name    
        
    def get_name(self):
        return self.__name
    
        

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    def first_menu(self):
        print("🙏 Welcome to Snippet Manager 🧑‍💻, Made with 💓",sep="\n")
        print("1.Login\n2.SignUp\n3.Reset Password\n4.Exit")
        choice = int(input("Enter your choice 🫡 "))
        if choice == 1:
            self.user_login()
        elif choice == 2:
            self.user_signup()
        elif choice == 3:
            self.reset()
        elif choice==4:
            print("👋 Budyy!! See you soon 🥲")
            exit()
        else:
            print("Invalid choice 🤭")
            self.first_menu()
    
    def reset(self):
        print("Enter your email 📧 ",end='')
        email=input()
        print("Enter your nickname 😎 ",end='')
        nickname=input()
        with open("User_details.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("Not Registered yet")
                    self.user_signup()
                else:
                    data=json.loads(content)
                if email not in data:
                    self.clear_screen()
                    print("Not Registered yet 😏")
                    self.user_signup()
                else:
                    if data[email][2]==nickname:
                        password = getpass.getpass("Enter your new password #️⃣ ")
                        confirm_password = getpass.getpass("Confirm your new password #️⃣ ")
                        if password != confirm_password:
                            self.clear_screen()
                            print("Password does not match 🤭")
                            self.first_menu()
                        try:
                            with open("User_details.json","w") as y:
                                data=json.loads(content)       
                                data[email][1]=hash_password(password)
                                json.dump(data,y,indent=4)

                        except FileNotFoundError:    
                                 print("File not found , if check your directory 🗃️")
                        
                        
                    
            
            
    def user_login(self):
        print("Login Here 🧑‍💻","-"*30,sep="\n")
        email = input("Enter your email 📧 ")
        if not self.Validate_email(email):
            self.clear_screen()
            print("Invalid email 🤭")
            self.user_login()
        password = getpass.getpass("Enter your password #️⃣  ")
        try:
            with open("User_details.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("Not Registered yet 😏")
                    self.user_signup()
                else:
                    data=json.loads(content)
                if email not in data:
                    self.clear_screen()
                    print("Not Registered yet 😏")
                    self.user_signup()
                else:
                    if check_password(data[email][1] , password):
                        self.set_email(email)
                        self.set_password(password)
                        self.set_name(data[email][0])
                        self.clear_screen()
                        print("Login successful 🥳")
                        SnippetManager(self)
                        
                        
                    else:
                        self.clear_screen()
                        print("Incorrect password 🤭")
                        self.first_menu()
        except FileNotFoundError:
            self.clear_screen()
            print("File not found , if check your directory 🗃️")
            
    def user_signup(self):
        print("🙏 SignUp Here 🧑‍💻",sep="\n")
        name = input("Create your username 👤 ")
        email = input("Enter your email 📧 ")
        
        if not self.Validate_email(email):
            self.clear_screen()
            print("Invalid email 🤭")
            self.user_signup()
        password = getpass.getpass("Enter your password #️⃣ ")
        confirm_password = getpass.getpass("Confirm your password #️⃣ ")
        if password != confirm_password:
            self.clear_screen()
            print("Password does not match 🤭")
            self.user_signup()
        security_question=input("Enter your nickname 😎")
        try:
            with open("User_details.json","r") as f:
                content=f.read().strip()
                data=None
                if content == "":
                    data={}
                else:
                    data=json.loads(content)       
                if email in data:
                    self.clear_screen()
                    print("Email already exists 🙀")
                    self.first_menu()
                if email not in data:
                    data[email]=[name,hash_password(password),security_question]
                    with open("User_details.json","w") as f:
                        json.dump(data,f,indent=4)
                    self.set_email(email)
                    self.set_password(password)
                    self.set_name(name)
                    self.clear_screen()
                    print("SignUp successful 🥳")
                    self.user_login()

        except FileNotFoundError:    
            print("File not found , if check your directory 🗃️")
        
    def Validate_email(self,email):
        if "@" in email and email.endswith(".com"):
            return True
        else:
            return False
            


class SnippetManager(SnippetManager_Authentication):
    def __init__(self,obj):
        self.obj=obj
        self.snippet_menu()
        
    def snippet_menu(self):
        print("What you want to do ? 😅 ",sep="\n")
        print("1.Create Snippet\n2.Read Snippet\n3.Update Snippet\n4.Delete Snippet\n5.Search Snippet\n6.Download Snippet\n7.Exit")
        choice=int(input("Enter your choice 🙂 "))
        if choice == 1:
            self.create_snippet()
        elif choice == 2:
            self.read_snippet()
        elif choice == 3:
            self.update_snippet()
        elif choice == 4:
            self.delete_snippet()
        elif choice == 5:
            self.search_snippet()
        elif choice==6:
            self.save_snippet()
        elif choice == 7:
            self.obj.first_menu()
        else:
            print("Invalid choice 🤭")
            self.snippet_menu()
            
    def save_snippet(self):
        snippet=[]
        try:
            with open("Snippets.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                else:
                    data=json.loads(content)
                if self.obj.get_email() not in data:
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                else:
                    for i in data[self.obj.get_email()]:
                        snippet.append((f'Snippet {i["id"]} : {i["Description"]}',i["Code"]))
                    create_pdf(snippet,f"{self.obj.get_name()}.pdf")
        except FileNotFoundError:
            print("File not found, please check your directory 🗃️")
            
            
    def get_code_input(self):
        print("Code : ", end="",flush=True)  # First, print the prompt
        code = sys.stdin.read()  # Then, read the full input
        return code
    
    def add_snippet(self,obj,snippet_obj):
        with open("Snippets.json",'r') as f:
            content=f.read().strip()
            data=None
            if content=="":
                data={}
            else:
                data=json.loads(content)
            with open("Snippets.json","w") as y:
                if obj.get_email() not in data:
                    data[obj.get_email()]=[{"id":Snippet.id,"Language":snippet_obj.get_language(),"Description":snippet_obj.get_description(),"Code":snippet_obj.get_code()}]
                    json.dump(data,y,indent=4)
                else:
                    curr_id=data[obj.get_email()][-1]["id"]
                    data[obj.get_email()].append({"id":curr_id+1,"Language":snippet_obj.get_language(),"Description":snippet_obj.get_description(),"Code":snippet_obj.get_code()})
                    json.dump(data,y,indent=4)
        self.snippet_menu()
    
    def read_snippet(self):
        try:
            with open("Snippets.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                else:
                    data=json.loads(content)
                if self.obj.get_email() not in data:
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                else:
                    snippet_list=data[self.obj.get_email()]
                    print("🫡  Here is your stored sippets 😎 ")
                    for i in snippet_list:
                        print(f'# Snippet {i["id"]} ')
                        for k,v in i.items():
                            if k=="Code":
                                print(f"{k} :\n{v}")
                            else:
                                print(f"{k} : {v}")
                    self.snippet_menu()
                        
        except FileNotFoundError:
            print("File not found, check your directory 🗃️")                
                
                
    def update_snippet(self):
        try:
            with open("Snippets.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 😎")
                    self.snippet_menu()
                else:
                    data=json.loads(content)
                if self.obj.get_email() not in data:
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 😎")
                    self.snippet_menu()
                else:
                    try:
                        with open("Snippets.json","r") as f:
                            content=f.read().strip()
                            data=None
                            if content=="":
                                self.clear_screen()
                                print("No any spinnet exist with your id, please create new 🥲")
                                self.snippet_menu()
                            else:
                                data=json.loads(content)
                            if self.obj.get_email() not in data:
                                self.clear_screen()
                                print("No any spinnet exist with your id, please create new 🥲")
                                self.snippet_menu()
                            else:
                                snippet_list=data[self.obj.get_email()]
                                print("🫡  Here is your stored sippets 😎 ")
                                for i in snippet_list:
                                    print(f'# Snippet {i["id"]} ')
                                    for k,v in i.items():
                                        if k=="Code":
                                            print(f"{k} :\n{v}")
                                        else:
                                            print(f"{k} : {v}")
                    except FileNotFoundError:
                        print("File not found, check your directory 🗃️")   
                    print("Enter you snippet id number 🙂")
                    my_id=input()
                    print("Language : ",end='')
                    language=input().strip()
                    code=self.get_code_input()
                    print("Description : ",end='')
                    description=input().strip()
                    with open("Snippets.json", 'w') as y:
                        flag = False  
                        for email, codelist in data.items():
                            if email == self.obj.get_email():
                                for item in codelist:
                                    if item["id"] == int(my_id):
                                        item["Language"] = language
                                        item["Code"] = code
                                        item["Description"] = description
                                        flag = True  # Set flag to True once the update is successful
                                        break  # Exit the inner loop as we found the matching ID
                            if flag:
                                break  # Exit the outer loop if the flag is True (update was successful)
                        json.dump(data, y, indent=4)  # Save the updated data to the file
                    self.snippet_menu()
        except FileNotFoundError:
            print("File not found, check your directory 🗃️")                
                
    
    def delete_snippet(self):
        try:
            with open("Snippets.json","r") as f:
                content=f.read().strip()
                data=None
                if content=="":
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🗃️")
                    self.snippet_menu()
                else:
                    data=json.loads(content)
                if self.obj.get_email() not in data:
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🗃️")
                    self.snippet_menu()
                else:
                    print("🫡  Here is your stored sippets 😎 ")
                    self.read_snippet()
                    print("Enter you snippet id number 🙂")
                    my_id=input()
                    with open("Snippets.json", 'w') as y:
                        flag = False  
                        for email, codelist in data.items():
                            if email == self.obj.get_email():
                                for item in codelist:
                                    if item["id"] == int(my_id):
                                        codelist.remove(item)
                                        flag = True  # Set flag to True once the update is successful
                                        break  # Exit the inner loop as we found the matching ID
                            if flag:
                                break  # Exit the outer loop if the flag is True (update was successful)
                        json.dump(data, y, indent=4)  # Save the updated data to the file
                        self.snippet_menu()
                   
        except FileNotFoundError:
            print("File not found, check your directory 🗃️")    
            
    def search_snippet(self):
        print("🔍 enter keyword to search in all your snippets and 'exit' to exit 🔍")
        while True:
            keyword=input().lower()
            if keyword=='exit':
                print("👋 Budyy!! See you soon 🥲")
                self.snippet_menu()
                return
            with open('Snippets.json','r') as f:
                content=f.read()
                result=[]
                if content=="":
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                    return
                else:
                    data=json.loads(content)
                if self.obj.get_email() not in data:
                    self.clear_screen()
                    print("No any spinnet exist with your id, please create new 🥲")
                    self.snippet_menu()
                    return
                else:
                    Snippet_list=data[self.obj.get_email()]
                    for i in Snippet_list:
                        if keyword in str(i["id"]).lower() or keyword in i["Code"].lower() or keyword in i["Language"].lower() or keyword in i["Description"].lower():
                            result.append(i)
                    print("🫡  Here is your sippets 😎 ")
                    for i in result:
                        print(f"# Snippet {i["id"]} ")
                        for k,v in i.items():
                            if k=="Code":
                                print(f"{k} :\n{v}")
                            else:
                                print(f"{k} : {v}")
                        
       
    def create_snippet(self):
        print(" 😎  Create Your Snippet",sep="\n" )
        print("Email : ",self.obj.get_email())
        print("Username : ",self.obj.get_name())
        print("Language : ",end='')
        language=input().strip()
        code=self.get_code_input()
        print("Description : ",end='')
        description=input().strip()
        snippet_obj=Snippet(language,code,description)
        self.add_snippet(self.obj,snippet_obj)
        self.snippet_menu()
        

obj = SnippetManager_Authentication()