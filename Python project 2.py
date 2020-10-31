from tkinter import *
root = Tk()
root.title("Welcome to Multibank Acoount BOOK  --(MAINPAGE)")

frame  = LabelFrame(root  , padx = 70 , pady = 70)
frame.grid(padx =30 , pady = 70)
# Entry widget
e1 = Entry(frame ).grid(row=1 , column = 1)
e2 = Entry(frame).grid(row= 2 , column = 1)
e3 = Entry(frame).grid(row= 3 , column = 1)

# Creating a Label widget
mylabel1 = Label(frame , pady = 8 ,text = " User Name " , bg ="grey")
mylabel2 = Label(frame , pady = 8 , text = "Aadhar Number " , bg ="grey")
mylabel3 = Label(frame , pady = 8, text = "Phone_No " , bg ="grey")

mylabel1.grid(row= 1 , column =  0, padx = 3 , pady = 5)
mylabel2.grid(row= 2 , column =  0, padx = 3 , pady = 5)
mylabel3.grid(row= 3 , column =  0, padx = 3 , pady = 5)

# Entry widget
def NextPage():
    tops = Toplevel()
    tops.title(" Second Page of MULTIBANK ACCOUNT BOOK  (ACCOUNT PAGE) ")
    import mysql.connector
    mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "password" , database = "User_Bank_Details")
    mycursor = mydb.cursor()
    mycursor .execute("Create table Bank_details(Bank_Name varchar(200) , AccountNo int(30) , IFSC_Code  varchar(20) , Balance int(50))")
    mycursor.close()
    mydb.commit()
    mydb.close()

    #Creating Method for Putting Data in database:

    def put():
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "password" , database = "User_Bank_Details")
        mycursor = mydb.cursor()
        sql_insert = "Insert into Bank_details(Bank_Name , AccountNo , IFSC_Code , Balance )  values (%s , %s , %s , %s)"
        Bank_Details =[ (Bank.get() , A_no.get() , ifsc.get()  , Balance.get()) ]
        mycursor.executemany(sql_insert , Bank_Details )

        mycursor.close()
        mydb.commit()
        mydb.close()
        status.set(' DATA ADDED SUCCESSFULLY ')

    # Creating Variables for Accessing Entry Boxes and Labels :
    Bank = StringVar();
    A_no = IntVar();
    ifsc = StringVar();
    Balance = IntVar();
    status = StringVar();


    frame = LabelFrame(tops, padx = 100 , pady = 100)
    frame.grid(padx =30 , pady = 70)
    #root.title("Welcome to Multibank Acoount BOOK  --")

    # Creating a Label widget
    mylabel4 = Label(frame , pady = 8 ,text = "Bank Name " , bg ="grey")
    mylabel5 = Label(frame , pady = 8 , text = "Account Number " , bg ="grey")
    mylabel6 = Label(frame , pady = 8 , text = "IFSC CODE " , bg ="grey")
    mylabel7 = Label(frame , pady = 8 , text = "Balance " , bg ="grey")
    mylabel8 = Label(frame , text = ' ' , textvariable = status )

    mylabel4.grid(row= 1 , column =   0 , padx = 3 , pady = 5)
    mylabel5.grid(row= 2 , column =  0 , padx = 3 , pady = 5)
    mylabel6.grid(row= 3 , column =  0 , padx = 3 , pady = 5)
    mylabel7.grid(row= 4 , column =   0 , padx = 3 , pady = 5)
    mylabel8.grid(row= 7 ,columnspan = 2 , padx = 3 , pady = 5)


    # Entry widget
    Entry(frame , textvariable = Bank).grid(row=1 , column = 1 , padx = 3 , pady = 5)
    Entry(frame , textvariable = A_no).grid(row=2 , column = 1 , padx = 3 , pady = 5)
    Entry(frame , textvariable = ifsc).grid(row=3 , column = 1 , padx = 3 , pady = 5)
    Entry(frame , textvariable = Balance).grid(row=4 , column = 1 , padx = 3 , pady = 5)

    # SUBMIT Button of NextPage
    myButton = Button(frame , text = " SUBMIT "  , command = put )
    myButton.grid(row  = 5, column = 1 , padx = 2 , pady = 4 )

    def ThirdPage():
        top = Toplevel()
        top.title(" Third Page of MULTIBANK ACCOUNT BOOK  (SHOW PAGE) ")
        import mysql.connector
        mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "password" , database = "User_Bank_Details")
        mycursor = mydb.cursor()
        mycursor.close()
        mydb.commit()
        mydb.close()

        def show():
            import mysql.connector
            mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "password" , database = "User_Bank_Details")
            mycursor = mydb.cursor()
            sql_search =  "select * from Bank_Details where AccountNo = '%s'  "%AccountNo.get()
            mycursor.execute(sql_search  )
            myresult =  mycursor.fetchall()
            print(myresult)
            # This code is for printing the output from console to GUI interface
            status.set("-------------------------------------------------------------------------------------")
            print_results = ' '
            for i in myresult:
                print_results += str(i) +"  "
            Label(frame ,text = print_results).grid(row= 8 , column =   0)
            mycursor.close()
            mydb.commit()
            mydb.close()

        Bank_Name = StringVar();
        AccountNo = IntVar();
        status = StringVar();

        frame = LabelFrame(top, padx = 100 , pady = 100)
        frame.grid(padx =30 , pady = 70)


        mylabel9 = Label(frame , pady = 8 ,text = "Bank Name " , bg = "grey")
        mylabel10 = Label(frame , pady = 8 , text = "Account Number ", bg = "grey")
        mylabel11 = Label(frame  , textvariable = status)

        mylabel9.grid(row= 1 , column =   0, padx = 3 , pady = 5)
        mylabel10.grid(row= 2 , column =  0, padx = 3 , pady = 5)
        mylabel11.grid(row= 7 ,columnspan = 2)



        # Entry widget
        Entry(frame , textvariable = Bank_Name).grid(row=1 , column = 1, padx = 3 , pady = 5)
        Entry(frame , textvariable = AccountNo).grid(row=2 , column = 1, padx = 3 , pady = 5)

        # SUBMIT Button of SecondPage
        myButton = Button(frame  , text = " SUBMIT "  , command = show )
        myButton.grid(row  = 5, column = 1  )

        # SUBMIT Button of ThirdPage
    myButton = Button(frame , text = " NEXT "  , command = ThirdPage )
    myButton.grid(row  = 7, column = 3  )
    tops.mainloop()


 # ======================================================== #
# SUBMIT Button of Mainpage
myButton = Button(frame , text = " Login "  , command = NextPage )
myButton.grid(row  = 8, column = 1  )
root.mainloop()
