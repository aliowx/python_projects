
from tkinter import *
from tkinter import ttk
from tkinter import Tk, filedialog, messagebox, PhotoImage
import time

list_person_2 = []
list_person_1 = []
def relation_ship():
    """ This function is just about the to finde the relationships between two peopel ! """
    current_time = time.localtime()
    rank = 0
    if (list_person_2[0] or list_person_2[0]) == "":
        rank += 10
    if list_person_1[1]  and list_person_2[1] in range(80,100):
        rank += 10
    elif list_person_1[1]  and list_person_2[1] in range(40,60):
        rank += 5
    elif list_person_1[1]  and list_person_2[1] =="":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[2]  and list_person_2[2] in range(180,190):
        rank += 10
    elif list_person_1[2]  and list_person_2[2] in range(160,180):
        rank += 5
    elif list_person_1[2]  and list_person_2[2] =="":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[3]  and list_person_2[3] == "Blue " or "Red":
        rank += 10
    elif list_person_1[3]  and list_person_2[3] == "Black" or "White":
        rank += 5
    elif list_person_1[3]  and list_person_2[3] == "" :
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[4]  and list_person_2[4] == "Persian" or "English":
        rank += 10
    elif list_person_1[4]  and list_person_2[4] == "German" or "French":
        rank += 5
    elif list_person_1[4]  and list_person_2[4] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[5]  and list_person_2[5] == "Programmer" or "Engineer":
        rank += 10
    elif list_person_1[5]  and list_person_2[5] == "Doctor" or "Nurse":
        rank += 5
    elif list_person_1[5]  and list_person_2[5] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[6]  and list_person_2[6] == "Shiraz" or "Tehran":
        rank += 10
    elif list_person_1[6]  and list_person_2[6] == "Tabriz" or "Isfahan":
        rank += 5
    elif list_person_1[6]  and list_person_2[6] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[7]  and list_person_2[7] == "One Word Titles" or "Tehran":
        rank += 10
    elif list_person_1[7]  and list_person_2[7] == "Swans" or "Sophia":
        rank += 5
    elif list_person_1[7]  and list_person_2[7] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0
    if list_person_1[8]  and list_person_2[8] in range(1000,2000):
        rank += 10
    elif list_person_1[8]  and list_person_2[8] in range(10,1000):
        rank += 5
    elif list_person_1[8]  and list_person_2[8] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0        
    if list_person_1[9]  and list_person_2[9] == "Chelo Kebab" or "Tahchin":
        rank += 10
    elif list_person_1[9]  and list_person_2[9] == "Ghormeh Sabzi" or "Ash Reshteh":
        rank += 5
    elif list_person_1[9]  and list_person_2[9] == "":
        messagebox.showerror("erro","your input is unvalid")
        rank += 0        
                  
    window = Tk()
    window.geometry("300x300")
    label = Label(window,text =f"your rank of the relationship between you and firends is %{rank}in the{ time.strftime ("%Y-%m-%d %H:%M:%S", current_time)}")
    label.place(x="25",y="70")
    window.mainloop()
    #rint(f"your rank of the relationship between you and firends is %{rank}")
    
def create_person_page2():
    """ _summary_
    This is about the secend person as food, city, salary ect... 
    
    """
    
    def relation_ship2():
        result = messagebox.askyesno("Yes No"," Are sure about it !", default = messagebox.YES)
        if result == True: 
            value_name = name_entry.get()#0
            value_wight = weight_entry.get()#1
            valu_height = height_entry.get()#2
            value_color= favorite_color_menu.get()#3
            value_language = language_menu.get()#4
            value_job = job_menu.get()#5
            value_city = city_menu.get()#6
            value_book = book_menu.get()#7
            value_salary = salary_menu.get()##8
            value_food = food_menu .get()##9
            list_person_2.append(value_name)
            list_person_2.append(value_wight)
            list_person_2.append(valu_height)
            list_person_2.append(value_color)
            list_person_2.append(value_language)
            list_person_2.append(value_job)
            list_person_2.append(value_city)
            list_person_2.append(value_book)
            list_person_2.append(value_salary)
            list_person_2.append(value_food)
            print(list_person_2)

    person_page = Tk()
    person_page.geometry("600x420")
    person_page.title("person2")
    person_page.config()
    #___________
    scrollbar = Scrollbar(person_page , orient=VERTICAL,)
    scrollbar.pack(side=RIGHT , fill=Y )
    #___________
    
    file_path = filedialog.askopenfilename(title="Select an image")
    if file_path == "":
        messagebox.showerror("Error", "No file selected")
    else:
        img = PhotoImage(master = person_page , file = file_path)
        canvas = Canvas(person_page, width = img.width(), height = img.height())
        canvas.pack()


        canvas.create_image(0, 0, anchor = "nw" , image = img)


    gender_label = ttk.Label(person_page, text="Gender:")
    gender_label.pack()
    gender_var = StringVar()
    gender_var.set("Male")
    gender_radiobutton1 = ttk.Radiobutton(person_page, text="Male", variable=gender_var, value="Male")
    gender_radiobutton1.pack()
    gender_radiobutton2 = ttk.Radiobutton(person_page, text="Female", variable=gender_var, value="Female")
    gender_radiobutton2.pack()

    name_label = Label(person_page, text="Name:")
    name_label.pack()
    name_entry = Entry(person_page)
    name_entry.pack()
        #list_person_2.append(name2)

    var_weight = IntVar()
    weight_label = ttk.Label(person_page, text="Weight:")
    weight_label.pack()
    weight_entry = ttk.Entry(person_page,textvariable = var_weight)
    weight_entry.pack()

    height_label = ttk.Label(person_page, text="Height (cm):")
    height_label.pack()
    height_entry = ttk.Entry(person_page)
    height_entry.pack()
    

    favorite_color_label = ttk.Label(person_page, text="Favorite Color:")
    favorite_color_label.pack()
    favorite_color_menu = ttk.Combobox(person_page, values=["Red", "Blue", "Green", "Yellow" ,
                                                                "Orange" , "Purple" , "Black" , "White","..."])
    favorite_color_menu.pack()

    language_label = ttk.Label(person_page, text="Language:")
    language_label.pack()
    language_menu = ttk.Combobox(person_page, values= ["Persian","German" , "English", "Spanish",
                                                        "French", "Turkish","..."])
    language_menu.pack()

    job_label = ttk.Label(person_page, text="Job:")
    job_label.pack()
    job_menu = ttk.Combobox(person_page, values=["Programmer" , "Engineer", "Doctor", 
                                                    "Teacher", "Artist" , "Nurse","..."])
    job_menu.pack()

    city_label = ttk.Label(person_page, text="City:")
    city_label.pack()
    city_menu = ttk.Combobox(person_page, values=["Tehran", "Shiraz", "Tabriz", "Isfahan" , "Bushehr"
                                                    ,"..."])
    city_menu.pack()
    
    book_label = ttk.Label(person_page, text="Book:")
    book_label.pack()
    book_menu = ttk.Combobox(person_page, values=["One Word Titles", "Swans", "Elizabeth", "Anna" , "Sophia"
                                                    ,"..."])
    book_menu.pack()
    
    food_label = ttk.Label(person_page, text="Food:")
    food_label.pack()
    food_menu = ttk.Combobox(person_page, values=["Chelo Kebab", "Tahchin", "Ghormeh Sabzi", "Ash Reshteh" , "Tahchin"
                                                    ,"..."])
    food_menu.pack()
    
    salary_label = ttk.Label(person_page, text="salary:")
    salary_label.pack()
    salary_menu = ttk.Spinbox(person_page,from_ = 0 ,to=10000 , format="%.2f" ,increment=0.50 )
    salary_menu.pack()
    

    calculate_button = ttk.Button(person_page, text="Submit!", command=relation_ship2)
    calculate_button.pack()
    # person_page.mainloop()
    #person_page.config(yscrollcommand = scrollbar.set)
    person_page.mainloop()
    
#______________________________________________________________________________________________________    
    
def create_person_page1():
    """_summary_
    This is about the firest person as food, city, salary ect... 
    
    """
    
    def relation_ship1():
        result = messagebox.askyesno("Yes No"," Are sure about it !", default = messagebox.YES)
        if result == True: 
            value_name = name_entry.get()#0
            value_wight = weight_entry.get()#1
            valu_height = height_entry.get()#2
            value_color= favorite_color_menu.get()#3
            value_language = language_menu.get()#4
            value_job = job_menu.get()#5
            value_city = city_menu.get()#6
            value_book = book_menu.get()#7
            value_salary = salary_menu.get()##8
            value_food = food_menu .get()##9
            list_person_1.append(value_name)
            list_person_1.append(value_wight)
            list_person_1.append(valu_height)
            list_person_1.append(value_color)
            list_person_1.append(value_language)
            list_person_1.append(value_job)
            list_person_1.append(value_city)
            list_person_1.append(value_book)
            list_person_1.append(value_salary)
            list_person_1.append(value_food)
            print(list_person_2)

    person_page = Tk()
    person_page.geometry("600x420")
    person_page.title("person2")
    person_page.config()
    #___________
    scrollbar = Scrollbar(person_page , orient=VERTICAL,)
    scrollbar.pack(side=RIGHT , fill=Y )
    #___________
    
    file_path = filedialog.askopenfilename(title="Select an image")
    if file_path == "":
        messagebox.showerror("Error", "No file selected")
    else:
        img = PhotoImage(master = person_page , file = file_path)
        canvas = Canvas(person_page, width = img.width(), height = img.height())
        canvas.pack()


        canvas.create_image(0, 0, anchor = "nw" , image = img)


    gender_label = ttk.Label(person_page, text="Gender:")
    gender_label.pack()
    gender_var = StringVar()
    gender_var.set("Male")
    gender_radiobutton1 = ttk.Radiobutton(person_page, text="Male", variable=gender_var, value="Male")
    gender_radiobutton1.pack()
    gender_radiobutton2 = ttk.Radiobutton(person_page, text="Female", variable=gender_var, value="Female")
    gender_radiobutton2.pack()

    name_label = Label(person_page, text="Name:")
    name_label.pack()
    name_entry = Entry(person_page)
    name_entry.pack()
        #list_person_2.append(name2)

    var_weight = IntVar()
    weight_label = ttk.Label(person_page, text="Weight:")
    weight_label.pack()
    weight_entry = ttk.Entry(person_page,textvariable = var_weight)
    weight_entry.pack()

    height_label = ttk.Label(person_page, text="Height (cm):")
    height_label.pack()
    height_entry = ttk.Entry(person_page)
    height_entry.pack()
    

    favorite_color_label = ttk.Label(person_page, text="Favorite Color:")
    favorite_color_label.pack()
    favorite_color_menu = ttk.Combobox(person_page, values=["Red", "Blue", "Green", "Yellow" ,
                                                                "Orange" , "Purple" , "Black" , "White","..."])
    favorite_color_menu.pack()

    language_label = ttk.Label(person_page, text="Language:")
    language_label.pack()
    language_menu = ttk.Combobox(person_page, values= ["Persian","German" , "English", "Spanish",
                                                        "French", "Turkish","..."])
    language_menu.pack()

    job_label = ttk.Label(person_page, text="Job:")
    job_label.pack()
    job_menu = ttk.Combobox(person_page, values=["Programmer" , "Engineer", "Doctor", 
                                                    "Teacher", "Artist" , "Nurse","..."])
    job_menu.pack()

    city_label = ttk.Label(person_page, text="City:")
    city_label.pack()
    city_menu = ttk.Combobox(person_page, values=["Tehran", "Shiraz", "Tabriz", "Isfahan" , "Bushehr"
                                                    ,"..."])
    city_menu.pack()
    
    book_label = ttk.Label(person_page, text="Book:")
    book_label.pack()
    book_menu = ttk.Combobox(person_page, values=["One Word Titles", "Swans", "Elizabeth", "Anna" , "Sophia"
                                                    ,"..."])
    book_menu.pack()
    
    food_label = ttk.Label(person_page, text="Food:")
    food_label.pack()
    food_menu = ttk.Combobox(person_page, values=["Chelo Kebab", "Tahchin", "Ghormeh Sabzi", "Ash Reshteh" , "Tahchin"
                                                    ,"..."])
    food_menu.pack()
    
    salary_label = ttk.Label(person_page, text="salary:")
    salary_label.pack()
    salary_menu = ttk.Spinbox(person_page,from_ = 0 ,to=10000 , format="%.2f" ,increment=0.50 )
    salary_menu.pack()
    

    calculate_button = ttk.Button(person_page, text="Submit!", command=relation_ship1)
    calculate_button.pack()
    # person_page.mainloop()
    #person_page.config(yscrollcommand = scrollbar.set)
    person_page.mainloop()


root = Tk()
root.geometry("360x300")
root.resizable(0,0)
root.title("Friend's Rank")
root.config( bg="black")

person1_button = ttk.Button(root, text="Person 1", command=create_person_page1)
person1_button.pack()

person2_button = ttk.Button(root, text="Person 2", command=create_person_page2)
person2_button.pack()
person3_button = ttk.Button(root, text="To find Ranke", command=relation_ship)
person3_button.pack()
root.mainloop()