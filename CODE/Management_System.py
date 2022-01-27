from kivy.app import App
from kivy.lang import Builder
from kivy.uix.video import Video
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.config import Config 
from kivy.properties import NumericProperty
import threading 
import os
from datetime import datetime
import pandas as pd
import csv
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

class MainWindow(Screen):
    pass

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    def check(self):
        if(self.ids.pid.text != "341267"):
            self.ids.loc.text ="INCORRECT!!!"
            self.ids.grt.text ="Retry."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()
        else:
            self.ids.loc.text =""
            self.ids.grt.text =""

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    Config.set('graphics', 'resizable', True)
    last_name_text_input = ObjectProperty()
    ego = NumericProperty(0)
       
    def search(self):
        if(self.ids.book_name.text != ''):
            #to get the current working directory
            directory = os.getcwd()

            print(directory)
            
            # get fileName from user
            filepath = directory + '\\' + "Search_History.txt"
            pathy = directory + '\\' + "Search_History.txt"

            isFile = os.path.exists(pathy)
            if(isFile == True):
                if((os.stat('Search_History.txt').st_size == 0) == True): 
                    with open("Search_History.txt", "w") as fp:
                        fp.write("Book Name,Date,Time")
                        fp.write("\n")
                        fp.write(self.ids.book_name.text)
                        fp.write(",")
                        fp.write(datetime.now().strftime("%d/%m/%Y"))
                        fp.write(",")
                        fp.write(datetime.now().strftime("%H:%M:%S"))
                        fp.write("\n")
                    # readinag given csv file
                    # and creating dataframe
                    dataframe1 = pd.read_csv("Search_History.txt")
                    
                    # storing this dataframe in a csv file
                    dataframe1.to_csv('Search_History.csv', index = None)
                else:
                    fp = open('Search_History.txt','a')
                    fp.write(self.ids.book_name.text)
                    fp.write(",")
                    fp.write(datetime.now().strftime("%d/%m/%Y"))
                    fp.write(",")
                    fp.write(datetime.now().strftime("%H:%M:%S"))
                    fp.write("\n")
                    fp.close()
                    # readinag given csv file
                    # and creating dataframe
                    dataframe1 = pd.read_csv("Search_History.txt")
                    
                    # storing this dataframe in a csv file
                    dataframe1.to_csv('Search_History.csv', index = None)
            else:
                # Creates a new file
                with open(filepath, 'w+') as fp:
                    fp.write("Book Name,Date,Time")
                    fp.write("\n")
                    fp.write(self.ids.book_name.text)
                    fp.write(",")
                    fp.write(datetime.now().strftime("%d/%m/%Y"))
                    fp.write(",")
                    fp.write(datetime.now().strftime("%H:%M:%S"))
                    fp.write("\n")
                # readinag given csv file
                # and creating dataframe
                dataframe1 = pd.read_csv("Search_History.txt")
                
                # storing this dataframe in a csv file
                dataframe1.to_csv('Search_History.csv', index = None)
            name = self.ids.book_name.text
            ans=''

            df = pd.read_csv("Library_Dataset.csv")

            if (df["Book Name"].loc[df['Book Name'].str.contains(name, case=False)].any() == True):
                ans = df["Position"].loc[df['Book Name'].str.contains(name, case=False)]
                print(ans)
                self.ids.loc.text = ans.tolist()[0]
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text ="LOCATION"
                    self.ids.grt.text =""
                timer = threading.Timer(10.0, gfg)
                timer.start()
            else:
                self.ids.loc.text = "Not Found!!"
                self.ids.grt.text ="Please Enter the correct details."
                def gfg():
                    self.ids.loc.text ="LOCATION"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
                  
        else:
            self.ids.loc.text = "Not Found!!"
            self.ids.grt.text ="Please Enter the correct details."
            def gfg():
                self.ids.loc.text ="LOCATION"
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()

class SixthWindow(Screen):
    def check1(self):
        if(self.ids.cid.text == '' or self.ids.bid.text == '' or self.ids.mid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()
        else:
            df = pd.read_csv("Library_Dataset.csv")
            name = self.ids.bid.text
            z=0
            with open('Library_Dataset.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',') 
                for row in reader:
                    for field in row:
                        if field == name:
                            z=1
                            break
            if(((z == 0) and (len(self.ids.mid.text) == 10))):
                self.ids.loc.text = 'Book Id Not Found!!'
                self.ids.grt.text ="Please Enter the Correct Id."
                def gfg():
                    self.ids.loc.text =""
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif((z == 1) and (len(self.ids.mid.text) != 10)):
                print((self.ids.mid.text).count)
                self.ids.loc.text = 'Incorrect Phone Number!!'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text =""
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif((z == 0) and (len(self.ids.mid.text) != 10)):
                self.ids.loc.text = 'Book Id Not Found and Incorrect Phone Number!!'
                self.ids.grt.text ="Please Enter the Correct Id and Phone Number."
                def gfg():
                    self.ids.loc.text =""
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif((df["Book Id"].loc[df['Book Id'].str.contains(name, case=False)].any() == True) and (len(self.ids.mid.text) == 10)):
                print(df["Book Id"].loc[df['Book Id'].str.contains(name, case=False)])
                #to get the current working directory
                directory = os.getcwd()

                print(directory)
                
                # get fileName from user
                filepath = directory + '\\' + "Issue.txt"
                pathy = directory + '\\' + "Issue.txt"

                isFile = os.path.exists(pathy)
                if(isFile == True):
                    if((os.stat('Issue.txt').st_size == 0) == True): 
                        with open("Issue.txt", "w") as fp:
                            fp.write("Book Id,Customer Name,Phone Number,Date,Time")
                            fp.write("\n")
                            fp.write(self.ids.bid.text)
                            fp.write(",")
                            fp.write(self.ids.cid.text)
                            fp.write(",")
                            fp.write(self.ids.mid.text)
                            fp.write(",")
                            fp.write(datetime.now().strftime("%d/%m/%Y"))
                            fp.write(",")
                            fp.write(datetime.now().strftime("%H:%M:%S"))
                            fp.write("\n")
                        # readinag given csv file
                        # and creating dataframe
                        dataframe1 = pd.read_csv("Issue.txt")
                        
                        # storing this dataframe in a csv file
                        dataframe1.to_csv('Issue.csv', index = None)
                    else:
                        fp = open('Issue.txt','a')
                        fp.write(self.ids.bid.text)
                        fp.write(",")
                        fp.write(self.ids.cid.text)
                        fp.write(",")
                        fp.write(self.ids.mid.text)
                        fp.write(",")
                        fp.write(datetime.now().strftime("%d/%m/%Y"))
                        fp.write(",")
                        fp.write(datetime.now().strftime("%H:%M:%S"))
                        fp.write("\n")
                        fp.close()
                        # readinag given csv file
                        # and creating dataframe
                        dataframe1 = pd.read_csv("Issue.txt")
                        
                        # storing this dataframe in a csv file
                        dataframe1.to_csv('Issue.csv', index = None)
                else:
                    # Creates a new file
                    with open(filepath, 'w+') as fp:
                        fp.write("Book Id,Customer Name,Phone Number,Date,Time")
                        fp.write("\n")
                        fp.write(self.ids.bid.text)
                        fp.write(",")
                        fp.write(self.ids.cid.text)
                        fp.write(",")
                        fp.write(self.ids.mid.text)
                        fp.write(",")
                        fp.write(datetime.now().strftime("%d/%m/%Y"))
                        fp.write(",")
                        fp.write(datetime.now().strftime("%H:%M:%S"))
                        fp.write("\n")
                    # readinag given csv file
                    # and creating dataframe
                    dataframe1 = pd.read_csv("Issue.txt")
                    
                    # storing this dataframe in a csv file
                    dataframe1.to_csv('Issue.csv', index = None)

                self.ids.loc.text = 'Press Issue!!'
                def gfg():
                    self.ids.loc.text =""
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()

    def check2(self):
        if(self.ids.cid.text == '' or self.ids.bid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()

class SeventhWindow(Screen):
    def check1(self):
        if(self.ids.cid.text == '' or self.ids.bid.text == '' or self.ids.mid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()
        else:
            #to get the current working directory
            directory = os.getcwd()

            print(directory)
            
            # get fileName from user
            filepath = directory + '\\' + "Return.txt"
            pathy = directory + '\\' + "Return.txt"

            isFile = os.path.exists(pathy)
            if(isFile == True):
                df = pd.read_csv("Library_Dataset.csv")
                df1 = pd.read_csv("Issue.csv")
                df2 = pd.read_csv("Return.csv")
                name = self.ids.bid.text
                df = pd.read_csv("Library_Dataset.csv")
                z=0
                with open('Library_Dataset.csv', 'rt') as f:
                    reader = csv.reader(f, delimiter=',') 
                    for row in reader:
                        for field in row:
                            if field == name:
                                z=1
                                break
                a=0
                with open('Issue.csv', 'rt') as f:
                    reader = csv.reader(f, delimiter=',') 
                    for row in reader:
                        for field in row:
                            if field == name:
                                a=1
                                break
                if(((z == 0) and (len(self.ids.mid.text) == 10))):
                    self.ids.loc.text = 'Book Id Not Found!!'
                    self.ids.grt.text ="Please Enter the Correct Id."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                elif((z == 1) and (len(self.ids.mid.text) != 10)):
                    print((self.ids.mid.text).count)
                    self.ids.loc.text = 'Incorrect Phone Number!!'
                    self.ids.grt.text =""
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                elif((z == 0) and (len(self.ids.mid.text) != 10)):
                    self.ids.loc.text = 'Book Id Not Found and Incorrect Phone Number!!'
                    self.ids.grt.text ="Please Enter the Correct Id and Phone Number."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()

                elif(a == 0):
                    self.ids.loc.text = 'Book Not Issued, So cannot be returned!!'
                    self.ids.grt.text ="Please Enter the Correct Id."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                else:
                    if((os.stat('Return.txt').st_size == 0) == True): 
                        with open("Return.txt", "w") as fp:
                            fp.write("Book Id,Customer Name,Phone Number,Date,Time")
                            fp.write("\n")
                            fp.write(self.ids.bid.text)
                            fp.write(",")
                            fp.write(self.ids.cid.text)
                            fp.write(",")
                            fp.write(self.ids.mid.text)
                            fp.write(",")
                            fp.write(datetime.now().strftime("%d/%m/%Y"))
                            fp.write(",")
                            fp.write(datetime.now().strftime("%H:%M:%S"))
                            fp.write("\n")
                        # readinag given csv file
                        # and creating dataframe
                        dataframe1 = pd.read_csv("Return.txt")
                        
                        # storing this dataframe in a csv file
                        dataframe1.to_csv('Return.csv', index = None)
                    else:
                        fp = open('Return.txt','a')
                        fp.write(self.ids.bid.text)
                        fp.write(",")
                        fp.write(self.ids.cid.text)
                        fp.write(",")
                        fp.write(self.ids.mid.text)
                        fp.write(",")
                        fp.write(datetime.now().strftime("%d/%m/%Y"))
                        fp.write(",")
                        fp.write(datetime.now().strftime("%H:%M:%S"))
                        fp.write("\n")
                        fp.close()
                        # readinag given csv file
                        # and creating dataframe
                        dataframe1 = pd.read_csv("Return.txt")
                        
                        # storing this dataframe in a csv file
                        dataframe1.to_csv('Return.csv', index = None)

                    self.ids.loc.text = 'Press Return!!'
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
            else:
                df = pd.read_csv("Library_Dataset.csv")
                name = self.ids.bid.text
                z=0
                with open('Library_Dataset.csv', 'rt') as f:
                    reader = csv.reader(f, delimiter=',')
                    for row in reader:
                        for field in row:
                            if field == name:
                                z=1
                                break
                a=0
                with open('Issue.csv', 'rt') as f:
                    reader = csv.reader(f, delimiter=',') 
                    for row in reader:
                        for field in row:
                            if field == name:
                                a=1
                                break
                if(((z == 0) and (len(self.ids.mid.text) == 10))):
                    self.ids.loc.text = 'Book Id Not Found!!'
                    self.ids.grt.text ="Please Enter the Correct Id."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                elif((z == 1) and (len(self.ids.mid.text) != 10)):
                    print((self.ids.mid.text).count)
                    self.ids.loc.text = 'Incorrect Phone Number!!'
                    self.ids.grt.text =""
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                elif((z == 0) and (len(self.ids.mid.text) != 10)):
                    self.ids.loc.text = 'Book Id Not Found and Incorrect Phone Number!!'
                    self.ids.grt.text ="Please Enter the Correct Id and Phone Number."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()

                elif(a == 0):
                    self.ids.loc.text = 'Book Not Issued, So cannot be returned!!'
                    self.ids.grt.text ="Please Enter the Correct Id."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                else:
                    # Creates a new file
                    with open(filepath, 'w+') as fp:
                        fp.write("Book Id,Customer Name,Phone Number,Date,Time")
                        fp.write("\n")
                        fp.write(self.ids.bid.text)
                        fp.write(",")
                        fp.write(self.ids.cid.text)
                        fp.write(",")
                        fp.write(self.ids.mid.text)
                        fp.write(",")
                        fp.write(datetime.now().strftime("%d/%m/%Y"))
                        fp.write(",")
                        fp.write(datetime.now().strftime("%H:%M:%S"))
                        fp.write("\n")
                    dataframe1 = pd.read_csv("Return.txt")
                    dataframe1.to_csv('Return.csv', index = None)

                    self.ids.loc.text = 'Press Return!!'
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()
                    

    def check2(self):
        if(self.ids.cid.text == '' or self.ids.bid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()

class EighthWindow(Screen):
    pass

class NinthWindow(Screen):
    pass

class TenthWindow(Screen):
    def check(self):
        if(self.ids.bid.text == '' or self.ids.bn.text == '' or self.ids.an.text == '' or self.ids.ps.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()

        else:
            List=[self.ids.bid.text,self.ids.bn.text,self.ids.an.text,self.ids.ps.text]
            with open('Library_Dataset.csv', 'a', newline='') as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow(List)
            self.ids.loc.text ="Book Added!!"
            self.ids.grt.text ="Thank You!"
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()

class TwelfthWindow(Screen):
    def check(self):
        if(self.ids.bid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text =""
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()
        else:
            df = pd.read_csv("Library_Dataset.csv")
            name = self.ids.bid.text
            z=0
            with open('Library_Dataset.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    for field in row:
                        if field == name:
                            z=1
                            break
            if(z == 1):
                name = self.ids.bid.text
                df = pd.read_csv("Library_Dataset.csv")
                m = df[df['Book Name'] == name].index.values
                df = df.drop(df.index[int(m)])
                df.to_csv('Library_Dataset.csv', index = None)
                self.ids.loc.text = 'Book Deleted!!'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text =""
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif(z == 0):
                    self.ids.loc.text = 'Book Not Found!!'
                    self.ids.grt.text ="Please Enter the Correct Name."
                    def gfg():
                        self.ids.loc.text =""
                        self.ids.grt.text =""
                    timer = threading.Timer(2.0, gfg)
                    timer.start()

class MWindow(Screen):
    pass

class LastWindow(Screen):
    pass

class ThirteenthWindow(Screen):       
    def search(self):
        if(self.ids.bid.text == ''):
            self.ids.loc.text ="Warning!!"
            self.ids.grt.text ="Please Enter the above details."
            def gfg():
                self.ids.loc.text ="SEARCH"
                self.ids.grt.text =""
            timer = threading.Timer(2.0, gfg)
            timer.start()
        else:
            df = pd.read_csv("Library_Dataset.csv")
            df1 = pd.read_csv("Issue.csv")
            df2 = pd.read_csv("Return.csv")
            name = self.ids.bid.text
            z=0
            with open('Library_Dataset.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    for field in row:
                        if field == name:
                            z=1
                            break
            a=0
            with open('Issue.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    for field in row:
                        if field == name:
                            a=1
                            break
            c=0
            with open('Return.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    for field in row:
                        if field == name:
                            c=1
                            break
            if((a == 1) and (c == 1) and (z == 1)):
                self.ids.loc.text = 'Book Issued and Returned'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text ="SEARCH"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif ((a == 1) and (c == 0) and (z == 1)):
                self.ids.loc.text = 'Book Issued But Not Returned'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text ="SEARCH"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif ((a == 0) and (c == 0) and (z == 1)):
                self.ids.loc.text = 'Book Not Issued'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text ="SEARCH"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            elif((a == 0) and (c == 0) and (z == 0)):
                self.ids.loc.text = 'Book Id Not Found!!'
                self.ids.grt.text =""
                def gfg():
                    self.ids.loc.text ="SEARCH"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()
            else:
                self.ids.grt.text ="Please Enter the correct details."
                def gfg():
                    self.ids.loc.text ="SEARCH"
                    self.ids.grt.text =""
                timer = threading.Timer(2.0, gfg)
                timer.start()

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("management_system.kv")


class Management_SystemApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Management_SystemApp().run()