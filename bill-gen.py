from tkinter import*

den=Tk()
den.geometry('1400x1400')


def show():
    f1=Frame()
    f1.place(x=0,y=0,width=1400,height=1400)
    f1.config(bg='maroon')
    m1=Label(f1,text="Wellcome To Grace Food Court",font=('algerian',20),bg='yellow',fg='black').place(x=300,y=50,height=50,width=500)
    m2=Label(f1,text="Press Next To Brows Menu",font=('Arial Black',18),background='grey',fg="black").place(x=350,y=300,height=50,width=400)
    n1=Button(f1,text='NEXT>>',command=main,font=('arial black',18),fg='black',bg='white').place(x=600,y=600,height=50,width=150)

def main():
    f2=Frame()
    f2.place(x=0,y=0,height=1400,width=1400)
    f2.config(bg='pink')
   

    def calculate():
        print("wellcome")
        a=e1_value.get()*60
        b=e2_value.get()*50
        c=e3_value.get()*40
        d=e4_value.get()*70
        e=e5_value.get()*100
        f=i1_value.get()*40
        g=i2_value.get()*60
        h=i3_value.get()*60
        i=i4_value.get()*40
        j=i5_value.get()*30
        value=a+b+c+d+e+f+g+h+i+j
        t1.delete(0,END)
        t1.insert(END,value)



    lh=Label(den,text="Grace Food Court",font=('ALGERIAN',25,'bold'),bg="red")
    lh.place(x=400,y=50,width=450,height=50)
    bill=Label(den,text="bill no.:",font=('comocs sans MS',14),bg='grey').place(x=900,y=50,width=120,height=50)
    be_value=IntVar()
    be=Entry(den,textvariable=be_value,font=('comocs sans MS',18),bg='grey').place(x=1100,y=50,width=80,height=40)

    lh2=Label(den,text="Menu :",font=('Arial black',20,'bold'),bg="green")
    lh2.place(x=400,y=150,width=120,height=50)

    lh3=Label(den,text="Fast Food :", font=('arial black',20,'bold'),bg="maroon",fg="white")
    lh3.place(x=50,y=230,width=170,height=50)
    #label 1
    l1=Label(den,text="Sandwich :60",font=('copper black',14),bg="white")
    l1.place(x=50,y=300,width=200,height=50)
    #entry 1
    e1_value=IntVar()
    e1=Entry(den,textvariable=e1_value,font=('comics sans MS',18))
    e1.place(x=300,y=300,width=150,height=50)
    # label 2
    l2=Label(den,text="Bread Omlet :50",font=('copper black',14),bg="white")
    l2.place(x=50,y=370,width=200,height=50)

    #entry 2
    e2_value=IntVar()
    e2=Entry(den,textvariable=e2_value,font=('comics sans MS',18))
    e2.place(x=300,y=370,width=150,height=50)
    #label 3
    l3=Label(den,text="Cheese Bread :40",font=('copper black',14),bg="white")
    l3.place(x=50,y=440,width=200,height=50)
    #entry 3
    e3_value=IntVar()
    e3=Entry(den,textvariable=e3_value,font=('comics sans MS',18))
    e3.place(x=300,y=440,width=150,height=50)

    l4=Label(den,text="Chicken Sandwich :70",font=('copper black',14),bg="white")
    l4.place(x=50,y=520,width=200,height=50)
    e4_value=IntVar()
    e4=Entry(den,textvariable=e4_value,font=('comics sans MS',18))
    e4.place(x=300,y=520,width=150,height=50)

    l5=Label(den,text="Garlic Bread :100",font=('copper black',14),bg="white")
    l5.place(x=50,y=600,width=200,height=50)
    e5_value=IntVar()
    e5=Entry(den,textvariable=e5_value,font=('comics sans MS',18))
    e5.place(x=300,y=600,width=150,height=50)

    # Drinks

    lh4=Label(den,text="Drinks :",font=('Arial black',20,'bold'),bg='maroon',fg='white')
    lh4.place(x=700,y=230,width=150,height=50)

    d1=Label(den,text="coke :40",font=('copper black',14),bg='white')
    d1.place(x=600,y=300,width=200,height=50)
    i1_value=IntVar()
    i1=Entry(den,textvariable=i1_value,font=('comics sans MS',18),bg='white')
    i1.place(x=850,y=300,width=150,height=50)

    d2=Label(den,text="Vergin Mojito :60",font=('copper black',14),bg='white')
    d2.place(x=600,y=370,width=200,height=50)
    i2_value=IntVar()
    i2=Entry(den,textvariable=i2_value,font=('comics sans MS',18),bg='white')
    i2.place(x=850,y=370,width=150,height=50)

    d3=Label(den,text="Espresso Cof. :60",font=('copper black',14),bg='white')
    d3.place(x=600,y=440,width=200,height=50)
    i3_value=IntVar()
    i3=Entry(den,textvariable=i3_value,font=('comics sans MS',18),bg='white')
    i3.place(x=850,y=440,width=150,height=50)

    d4=Label(den,text="Pepsi :40",font=('copper black',14),bg='white')
    d4.place(x=600,y=520,width=200,height=50)
    i4_value=IntVar()
    i4=Entry(den,textvariable=i4_value,font=('comics sans MS',18),bg='white')
    i4.place(x=850,y=520,width=150,height=50)

    d5=Label(den,text="Lemonade :30",font=('copper black',14),bg='white')
    d5.place(x=600,y=600,width=200,height=50)
    i5_value=IntVar()
    i5=Entry(den,textvariable=i5_value,font=('comics sans MS',18),bg='white')
    i5.place(x=850,y=600,width=150,height=50)

    # place order button
    b1=Button(den,command=calculate,text="Place Order",font=('Arial black',20),bg="maroon",fg="white")
    b1.place(x=500,y=700,width=200,height=50)

    lh6=Label(den,text="Total Amount:",font=('copper black',19),bg='yellow')
    lh6.place(x=1100,y=200,width=200,height=50)

    t1=Entry(den,font=('comics sans MS',20),bg='white')
    t1.place(x=1100,y=350,width=200,height=50)
    b2=Button(f2,text="<<BACK",command=show,font=('arial ',15),bg='white').place(x=1050,y=650,height=50,width=150)
    b3=Button(f2,text='NEXT>>',command=end,font=('arial ',15),bg='white').place(x=1050,y=700,height=50,width=150)
def end():
    f3=Frame()
    f3.place(x=0,y=0,height=1300,width=1300)
    f3.config(bg='maroon')
    m3=Label(f3,text='Thanks For Shopping',font=('algerian',20),fg='black').place(x=200,y=50,height=50,width=500)

    
# b2=Button(den,command=delet,text="RESET",font=('algerian',18)).place(x=1100,y=450,width=100,height=50)
show() #1st gui will come

den.mainloop()