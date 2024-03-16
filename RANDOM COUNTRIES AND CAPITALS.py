from tkinter import *
import random
root=Tk()
root.title("Country Capital")
root.geometry("500x500")
Input_Country=Entry(root)
Input_Capital=Entry(root)
country_list_label=Label(root)
capital_list_label=Label(root)
country_random=Label(root)
capital_random=Label(root)
country_list=[]
capital_list=[]
def add():
    country_list.append(Input_Country.get())
    capital_list.append(Input_Capital.get())
    country_list_label["text"]="Country Name :"+str(country_list)
    capital_list_label["text"]="City Name :"+str(capital_list)
    capital_list_label.place(relx=0.5,rely=0.5,anchor=CENTER)
    country_list_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    btn_display_rand=Button(root,text="Display Country And City Name Randomly",bg="teal",fg="white",command=rand)
    btn_display_rand.place(relx=0.5,rely=0.6,anchor=CENTER)
def rand():
    random_1=random.randint(0, len(country_list)-1)
    random_2=random.randint(0, len(country_list)-1)
    country_random["text"]="Random Country : "+country_list[random_1]
    capital_random["text"]="Random City : "+capital_list[random_2]
    country_random.place(relx=0.5,rely=0.7,anchor=CENTER)
    capital_random.place(relx=0.5,rely=0.8,anchor=CENTER)
btn_display=Button(root,text="Display Country And City Name",bg="teal",fg="white",command=add)
btn_display.place(relx=0.5,rely=0.3,anchor=CENTER)
Input_Country.place(relx=0.5,rely=0.1,anchor=CENTER)
Input_Capital.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()
