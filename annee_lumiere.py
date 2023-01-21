# coding :utf-8
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
from math import *
import sqlite3

def main():
    root=Tk()
    app= windows1(root)
    root.mainloop()

class windows1:
    def __init__(self, master):
        self.master = master
        self.master.iconbitmap("logo.ico")
        self.master.title("année lumière")  # bad relief "SUNKEN": must be flat, groove, raised, ridge, solid, or sunken
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()
        self.labeltitre = Label(self.frame, text="bienvenue", font=("arial", 40, "bold"), bd=10, relief="sunken")
        self.labeltitre.grid(row=0, column=0, columnspan=2, pady=20,padx=100)
        self.framepr = Frame(self.frame, width=1000, height=300, bg="white")
        self.framepr.grid(row=1, column=0, pady=4, columnspan=4)
        self.framechoix = Frame(self.frame, width=1000, height=300, bd=10, bg="white")
        self.framechoix.grid(row=2, column=0, pady=4,columnspan=4)
        self.labelinfo=Label(self.framepr,text="PRE-DIMMENSIONNEMENT",font=("arial", 20))
        self.labelinfo.grid(row=0, column=0, padx=15, pady=15,columnspan=10)
        self.butnervure = Button(self.framepr, width=8, height=3, text="Nervure", bg="#535c68",font=("arial", 15, "bold"), command=self.Nervure_window)
        self.butnervure.grid(row=1, column=0, padx=15, pady=15)
        self.butPoutreISost = Button(self.framepr, width=8, height=3, text="Poutre ISO", bg="#535c68",font=("arial", 15, "bold"), command=self.poutreISO_window)
        self.butPoutreISost.grid(row=1, column=1, padx=15, pady=15)
        self.butPoutreHYP = Button(self.framepr, width=8, height=3, text="Poutre HYP", bg="#535c68",font=("arial", 15, "bold"), command=self.poutreHYP_window)
        self.butPoutreHYP.grid(row=1, column=2, padx=15, pady=15)
        self.butG = Button(self.framepr, width=8, height=3, text="charge G", bg="#535c68",font=("arial", 15, "bold"), command=self.chargePermanentes_window)
        self.butG.grid(row=1, column=3, padx=15, pady=15)
        self.butELU = Button(self.framechoix,width=8,height=3,text="ELU",bg="#535c68", font=("arial", 15, "bold"),command=self.ELU_window)
        self.butELU.grid(row=0, column=0, padx=15, pady=15)
        self.butELS = Button(self.framechoix, width=8,height=3 ,text="ELS",bg="#535c68", font=("arial", 15, "bold"),command=self.ELS_window)
        self.butELS.grid(row=0, column=1, padx=15, pady=15)
        self.butquit = Button(self.framechoix,width=8,height=3, text="quiter",bg="#535c68", font=("arial", 15, "bold"),command=self.button_quitter)
        self.butquit.grid(row=0, column=4, padx=15, pady=15)

    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("calcul d'une section rectangulaire en flexion simple", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return

    def ELU_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)
    def ELS_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)
    def Nervure_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=windows4(self.newWindow)
    def poutreISO_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)
    def poutreHYP_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows6(self.newWindow)
    def chargePermanentes_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows7(self.newWindow)


#_________________mes class________

class windows2:
    def __init__(self, master):
        self.master = master
        self.master.title("calcul a l'ELU")
        self.master.geometry('1350x750+0+0')
        self.master.iconbitmap("logo.ico")
        # mes variables

        self.nom=StringVar(self.master)
        self.Mu=DoubleVar(self.master)
        self.b=DoubleVar(self.master)
        self.dp=DoubleVar(self.master)
        self.d=DoubleVar(self.master)
        self.fc=IntVar(self.master)
        self.sec=DoubleVar(self.master)
        self.sec2=DoubleVar(self.master)

       # self.frame = Frame(self.master)
       # self.frame.pack()
        self.master.config(background="#2c3e50")
        self.lbltitre = Label(self.master, text="constantes ELU:γb=1,5 ;θ=1 ;fe=400 ;Es=210 000 MPA ;αlim=0,668 ;deformation=1,739 ;µlim=0,391", font=("arial", 21,"bold"), bg="black", fg="white")
        self.lbltitre.place(x=0,y=0,width=1360)
        self.lblnom = Label(self.master, text="nom", font=("calibri", 21, "bold"), bg="dark gray",fg="white")
        self.lblnom.place(x=1, y=40, width=250)
        self.entrynom = Entry(self.master, font=("calibri", 21, "bold"), bg="white",textvariable=self.nom, fg="black")
        self.entrynom.place(x=250, y=40, width=150)
        self.lblmomnent=Label(self.master,text="moment Mu",font=("calibri", 21,"bold"), bg="dark gray", fg="white")
        self.lblmomnent.place(x=1,y=90,width=250)
        self.entrymomnent =Entry(self.master,font=("calibri", 21, "bold"), bg="white",textvariable=self.Mu,fg="black")
        self.entrymomnent.place(x=250, y=90, width=150)
        self.lblbase = Label(self.master, text="base b", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblbase.place(x=1,y=140 , width=250)
        self.entrybase = Entry(self.master, font=("calibri", 21, "bold"), bg="white",textvariable=self.b, fg="black")
        self.entrybase.place(x=250, y=140, width=150)
        self.lbldp = Label(self.master, text="hauteur  d’", font=("calibri", 21, "bold"), bg="dark gray",fg="white")
        self.lbldp.place(x=1,y=190 , width=250)
        self.entrydp = Entry(self.master, font=("calibri", 21, "bold"), bg="white",textvariable=self.dp ,fg="black")
        self.entrydp.place(x=250, y=190, width=150)
        self.lbld = Label(self.master, text="hauteur d", font=("calibri", 21, "bold") ,bg="dark gray", fg="white")
        self.lbld.place(x=1, y=240 , width=200)
        self.entryd = Entry(self.master, font=("calibri",21,"bold"), bg="white",textvariable=self.d, fg="black")
        self.entryd.place(x=250, y=240, width=150)
        self.btver=Button(self.master,text="verifier",command=self.verifier).place(x=200, y=240, width=50,height=40)
        self.lblfc = Label(self.master, text="fc28", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.combofc=ttk.Combobox(self.master, text="fc28",font=("calibri", 21, "bold"),state="readonly",textvariable=self.fc)
        self.combofc['values']=(16,20,25,30)
        self.combofc.place(x=250, y=290, width=150)
        self.lblfc.place(x=1, y=290, width=250)
        self.btSAt = Button(self.master, text="section acier tend ELU",command=self.section ,bg="red",fg="#4f4e4d",font=("yu gothic ui", 12, "bold"))
        self.btSAt .place(x=1, y=340, width=250)
        self.lblSAt =Label(self.master, bg="white",fg="#4f4e4d",font=("yu gothic ui", 15, "bold"),textvariable=self.sec)
        self.lblSAt.place(x=250, y=340, width=150)
        self.btSAc = Button(self.master, text="section acier comp ELU", command=self.section2, bg="red", fg="#4f4e4d",  font=("yu gothic ui", 12, "bold"))
        self.btSAc.place(x=1, y=390, width=250)
        self.lblSAc = Label(self.master, bg="white", fg="#4f4e4d", font=("yu gothic ui", 15, "bold"), textvariable=self.sec2)
        self.lblSAc.place(x=250, y=390, width=150)
        self.lblnote = Label(self.master, text="note", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnote.place(x=1, y=435, width=400)
        self.textnote = Text(self.master, font=("calibri", 21, "bold"), bg="white", fg="black",height=5)
        self.textnote.place(x=1, y=465, width=400)
        #__________________la partie vue______________
        self.tree_frame=Frame(self.master,bg="#ecf0f1")
        self.tree_frame.place(x=400,y=40,width=960,height=700)
        self.tv = ttk.Treeview(self.tree_frame,height=34, column=(1, 2, 3, 4, 5, 6, 7, 8,9))
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=0)
        self.tv.heading("2", text="nom")
        self.tv.column("2", width=1)
        self.tv.heading("3", text="moment flechissant Mu")
        self.tv.column("3", width=2)
        self.tv.heading("4", text="base b")
        self.tv.column("4", width=2)
        self.tv.heading("5", text="hauteur d")
        self.tv.column("5", width=2)
        self.tv.heading("6", text="hauteur d'")
        self.tv.column("6", width=2)
        self.tv.heading("7", text="fc28")
        self.tv.column("7", width=2)
        self.tv.heading("8", text="section d'acier T")
        self.tv.column("8", width=2)
        self.tv.heading("9", text="section d'acier C")
        self.tv.column("9", width=2)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=X)
        #____________________les boutons________________________
        self.btnajt = Button(self.master, text="Enregistre",command=self.enregistre, width=15, font=("calibri", "16"),bg="#16a085", fg="white")
        self.btnajt.place(x=1, y=605, width=200)
        self.btnrange = Button(self.master, text="ranger", width=15, font=("calibri", "16"),bg="#1298b9",command=self.ranger, fg="white")
        self.btnrange.place(x=200, y=605, width=200)
        self.btndesup = Button(self.master, text="Suprimer", width=15,command=self.suprimer, font=("calibri", "16"),bg="#c0392b", fg="white")
        self.btndesup.place(x=1, y=650, width=200)
        self.btnequit = Button(self.master, text="quiter", width=15, font=("calibri", "16"),command=self.button_quitter ,bg="#f39c12",fg="white")
        self.btnequit.place(x=200, y=650, width=200)
        self.btexp=Button(self.master,text="exporter",command=self.exporter ,width=15, font=("calibri", "16"),bg="#91a915", fg="white")
        self.btexp.place(x=1,y=690,width=400)
        #___________________connection a matable___________________________
        self.conn = sqlite3.connect('database1.db')
        self.cur = self.conn.cursor()
        self.select = self.cur.execute('select * from donnees')
        for row in self.select:
            self.tv.insert('', END, value=row)
        self.conn.close()

        #____________les methodes_________________
    def enregistre(self):
        # create connection
        if self.nom.get()=="" or self.Mu.get()=="":
            tkinter.messagebox.showerror("BA ELU" ,"vous devez remplire toute les cases")
        else:

            self.conn = sqlite3.connect('database1.db')
            self.cur = self.conn.cursor()
            self.cur.execute("INSERT INTO donnees('nom','Mu','b','h','d','fc','section','section2') values(?,?,?,?,?,?,?,?)", (self.nom.get(),self.Mu.get(),self.b.get(),self.dp.get(),self.d.get() ,self.fc.get(),self.sec.get(),self.sec2.get()))
            self.conn.commit()
            self.conn.close()
            self.conn = sqlite3.connect('database1.db')
            self.cur = self.conn.cursor()
            self.select = self.cur.execute("SELECT * FROM donnees order by id desc")
            self.select = list(self.select)
            self.tv.insert('', END, value=self.select[0])
            self.conn.close()

    def verifier(self):
        if self.dp.get()<=self.d.get():
            tkinter.messagebox.showerror("BA ELU", "Validé")
        else:
            tkinter.messagebox.showerror("BA ELU", " Non validé")
            self.d.set(0)

    def suprimer(self):
        idslect=self.tv.item(self.tv.selection())['values'][0]
        self.conn=sqlite3.connect("database1.db")
        self.cur=self.conn.cursor()
        self.sup=self.cur.execute("delete from donnees where id={}".format(idslect))
        self.conn.commit()
        self.tv.delete(self.tv.selection())

    def ranger(self):
        for x in self.tv.get_children():
            self.tv.delete(x)
        self.conn = sqlite3.connect("database1.db")
        self.cur = self.conn.cursor()
        self.select = self.cur.execute("select * from donnees order by nom asc")
        self.conn.commit()
        for row in self.select:
            self.tv.insert('', END, values=row)
        self.conn.close()
    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("BA ELU", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return
    def exporter(self):
        exp=filedialog.asksaveasfilename(initialdir="/",title="exporter",defaultextension=".*",filetypes=(("Text File","*.txt"),("base de donnée","*.db"),("All File","*.*")))
        f=open(exp,'w')
        self.conn = sqlite3.connect("database1.db")
        self.cur = self.conn.cursor()
        self.select = self.cur.execute("select * from donnees")
        f.write()
        f.close()
        self.conn.close()

    def section(self):
       fbu=(0.85*self.fc.get())/1.5
       NUu=(self.Mu.get())/(self.b.get()*pow(self.d.get(),2)*fbu)
       if NUu<=0.391:
           alphaU=1.25*(1-sqrt(1-(2*NUu)))
           st=(3.5*(1-alphaU))/alphaU
           if st<=1.739:
               contrainte=200000*st
               Asu=self.Mu.get()/(contrainte*self.d.get()*(1-0.4*alphaU))
           else:
               contrainte=400/1.15
               Asu = self.Mu.get()/(contrainte * self.d.get() * (1 -( 0.4 * alphaU)))
           self.sec.set("{:.4f}".format(Asu))
       else:
         alphaU=self.Mu.get()-(0.391*self.b.get()*pow(self.d.get(),2)*fbu)
         if alphaU>=0.4*self.Mu.get():
             MUcalcul=0.6*NUu
         else:
             MUcalcul=0.391
         alphacalcul=1.25*(1-sqrt(1-(2*MUcalcul)))
         epsiprimSC=3.5*(1-(self.dp.get()/(alphacalcul*self.d.get())))
         epsiST=3.5*((1-alphacalcul)/alphacalcul)
         if epsiprimSC<=1.739:
             contraintreprimSC=200000*epsiprimSC
         else:
             contraintreprimSC=400/1.15
         if epsiST<=1.739:
             contraintST=200000*epsiST
         else:
             contraintST=400/1.15
         AprimSU=(self.Mu.get()-MUcalcul*self.b.get()*pow(-self.d.get(),2)*fbu)/(contraintreprimSC*(self.d.get()-self.dp.get()))
         ASU=((AprimSU*contraintreprimSC)+(0.8*alphacalcul*self.b.get()*self.d.get()*fbu))/contraintST
         self.sec.set("{:.4f}".format(ASU))
    def section2(self):
       fbu=(0.85*self.fc.get())/1.5
       NUu=(self.Mu.get())/(self.b.get()*pow(self.d.get(),2)*fbu)
       if NUu<=0.391:
           alphaU=1.25*(1-sqrt(1-(2*NUu)))
           st=(3.5*(1-alphaU))/alphaU
           if st<=1.739:
               contrainte=200000*st
               Asu=self.Mu.get()/(contrainte*self.d.get()*(1-0.4*alphaU))
           else:
               contrainte=400/1.15
               Asu = self.Mu.get()/(contrainte * self.d.get() * (1 -( 0.4 * alphaU)))
           self.sec2.set(0)
       else:
         alphaU=self.Mu.get()-(0.391*self.b.get()*pow(self.d.get(),2)*fbu)
         if alphaU>=0.4*self.Mu.get():
             MUcalcul=0.6*NUu
         else:
             MUcalcul=0.391
             A=1-(2*MUcalcul)
         alphacalcul=1.25*(1-sqrt(A))
         epsiprimSC=3.5*(1-(self.dp.get()/(alphacalcul*self.d.get())))
         epsiST=3.5*((1-alphacalcul)/alphacalcul)
         if epsiprimSC<=1.739:
             contraintreprimSC=200000*epsiprimSC
         else:
             contraintreprimSC=400/1.15
         if epsiST<=1.739:
             contraintST=200000*epsiST
         else:
             contraintST=400/1.15
         AprimSU=(self.Mu.get()-MUcalcul*self.b.get()*pow(-self.d.get(),2)*fbu)/(contraintreprimSC*(self.d.get()-self.dp.get()))
         self.sec2.set("{:.4f}".format(AprimSU))

class windows3:
    def __init__(self, master):
        self.master = master
        self.master.title("calcul a l'ELS")
        self.master.geometry('1350x750+0+0')
        self.master.iconbitmap("logo.ico")
        #self.frame = Frame(self.master)
       #self.frame.pack()
        self.master.config(background="#2c3e50")
        # mes variables
        self.nom1 = StringVar(self.master)
        self.Mser = DoubleVar(self.master)
        self.b1 = DoubleVar(self.master)
        self.dp1 = DoubleVar(self.master)
        self.d1 = DoubleVar(self.master)
        self.fc1 = IntVar(self.master)
        self.sec1 = DoubleVar(self.master)
        self.sec21=DoubleVar(self.master)

        #self.frame = Frame(self.master)
        #self.frame.pack()
        self.master.config(background="#2c3e50")
        self.lbltitre = Label(self.master, text="constantes ELS:γb=1,5;FP ;θ=1 ;fe=400 ;Es=210 000 MPA ;αlim=0,668 ;deformation=1,739 ;µlim=0,391", font=("arial", 21, "bold"), bg="black", fg="white")
        self.lbltitre.place(x=0, y=0, width=1360)
        self.lblnom = Label(self.master, text="nom", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnom.place(x=1, y=40, width=250)
        self.entrynom = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.nom1, fg="black")
        self.entrynom.place(x=250, y=40, width=150)
        self.lblmomnent = Label(self.master, text="moment Mser", font=("calibri", 21, "bold"), bg="dark gray",  fg="white")
        self.lblmomnent.place(x=1, y=90, width=250)
        self.entrymomnent = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.Mser,  fg="black")
        self.entrymomnent.place(x=250, y=90, width=150)
        self.lblbase = Label(self.master, text="base b", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblbase.place(x=1, y=140, width=250)
        self.entrybase = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.b1, fg="black")
        self.entrybase.place(x=250, y=140, width=150)
        self.lbldp = Label(self.master, text="d'", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbldp.place(x=1, y=190, width=250)
        self.entrydp = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.dp1, fg="black")
        self.entrydp.place(x=250, y=190, width=150)
        self.lbld = Label(self.master, text="hauteur d", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbld.place(x=1, y=240, width=200)
        self.entryd = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.d1, fg="black")
        self.entryd.place(x=250, y=240, width=150)
        self.btver = Button(self.master, text="verifier", command=self.verifier).place(x=200, y=240, width=50, height=40)
        self.lblfc = Label(self.master, text="fc28", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.combofc = ttk.Combobox(self.master, text="fc28", font=("calibri", 21, "bold"), state="readonly",textvariable=self.fc1)
        self.combofc['values'] = (16, 20, 25, 30)
        self.combofc.place(x=250, y=290, width=150)
        self.lblfc.place(x=1, y=290, width=250)
        self.combofc.place(x=250, y=290, width=150)
        self.lblfc.place(x=1, y=290, width=250)
        self.btSAt = Button(self.master, text="section acier tend ELS", command=self.Section1, bg="red", fg="#4f4e4d", font=("yu gothic ui", 12, "bold"))
        self.btSAt.place(x=1, y=340, width=250)
        self.lblSAt = Label(self.master, bg="white", fg="#4f4e4d", font=("yu gothic ui", 15, "bold"), textvariable=self.sec1)
        self.lblSAt.place(x=250, y=340, width=150)
        self.btSAc = Button(self.master, text="section acier comp ELS", bg="red",command=self.Section21, fg="#4f4e4d",font=("yu gothic ui", 12, "bold"))
        self.btSAc.place(x=1, y=390, width=250)
        self.lblSAc = Label(self.master, bg="white", fg="#4f4e4d", font=("yu gothic ui", 15, "bold"),textvariable=self.sec21)
        self.lblSAc.place(x=250, y=390, width=150)
        self.lblnote = Label(self.master, text="note", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnote.place(x=1, y=435, width=400)
        self.textnote = Text(self.master, font=("calibri", 21, "bold"), bg="white", fg="black", height=5)
        self.textnote.place(x=1, y=465, width=400)
        # __________________la partie vue______________
        self.tree_frame = Frame(self.master, bg="#ecf0f1")
        self.tree_frame.place(x=400, y=40, width=960, height=700)
        self.tv = ttk.Treeview(self.tree_frame, height=34, column=(1, 2, 3, 4, 5, 6, 7, 8,9))
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=0)
        self.tv.heading("2", text="nom")
        self.tv.column("2", width=1)
        self.tv.heading("3", text="moment flechissant Mu")
        self.tv.column("3", width=8)
        self.tv.heading("4", text="base b")
        self.tv.column("4", width=2)
        self.tv.heading("5", text="hauteur h")
        self.tv.column("5", width=2)
        self.tv.heading("6", text="hauteur d")
        self.tv.column("6", width=2)
        self.tv.heading("7", text="fc28")
        self.tv.column("7", width=2)
        self.tv.heading("8", text="section d'acier T")
        self.tv.column("8", width=4)
        self.tv.heading("9", text="section d'acier C")
        self.tv.column("9", width=2)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=X)
        # ____________________les boutons________________________
        self.btnajt = Button(self.master, text="Enregistre", command=self.enregistre, width=15, font=("calibri", "16"), bg="#16a085", fg="white")
        self.btnajt.place(x=1, y=565, width=200)
        self.btnrange = Button(self.master, text="ranger", width=15, font=("calibri", "16"), bg="#1298b9", command=self.ranger, fg="white")
        self.btnrange.place(x=200, y=565, width=200)
        self.btndesup = Button(self.master, text="Suprimer", width=15, command=self.suprimer, font=("calibri", "16"), bg="#c0392b", fg="white")
        self.btndesup.place(x=1, y=610, width=200)
        self.btnequit = Button(self.master, text="quiter", width=15, font=("calibri", "16"),command=self.button_quitter, bg="#f39c12", fg="white")
        self.btnequit.place(x=200, y=610, width=200)
        # ___________________connection a ma table___________________________
        self.conn = sqlite3.connect('databasels1.db')
        self.cur = self.conn.cursor()
        self.select = self.cur.execute('select * from donnees')
        for row in self.select:
            self.tv.insert('', END, value=row)
        self.conn.close()

        # ____________les methodes_________________

    def enregistre(self):
        # create connection
        if self.nom1.get() == "" or self.Mser.get() == "":
            tkinter.messagebox.showerror("BA ELS", "vous devez remplire toute les cases")
        else:

            self.conn = sqlite3.connect('databasels1.db')
            self.cur = self.conn.cursor()
            self.cur.execute("INSERT INTO donnees('nom','Mu','b','h','d','fc','section','section2') values(?,?,?,?,?,?,?,?)", (self.nom1.get(),self.Mser.get(),self.b1.get(),self.dp1.get(),self.d1.get() ,self.fc1.get(),self.sec1.get(),self.sec21.get()))
            self.conn.commit()
            self.conn.close()
            self.conn = sqlite3.connect('databasels1.db')
            self.cur = self.conn.cursor()
            self.select = self.cur.execute("SELECT * FROM donnees order by id desc")
            self.select = list(self.select)
            self.tv.insert('', END, value=self.select[0])
            self.conn.close()

    def verifier(self):
        if self.dp1.get() >=self.d1.get():
            tkinter.messagebox.showerror("BA ELS", "mauvais choix de d")
            self.d1.set(0)
        else:
            tkinter.messagebox.showerror("BA ELS", "validé")

    def suprimer(self):
        idslect = self.tv.item(self.tv.selection())['values'][0]
        self.conn = sqlite3.connect("databasels1.db")
        self.cur = self.conn.cursor()
        self.sup = self.cur.execute("delete from donnees where id={}".format(idslect))
        self.conn.commit()
        self.tv.delete(self.tv.selection())

    def ranger(self):
        for x in self.tv.get_children():
            self.tv.delete(x)
        self.conn = sqlite3.connect("databasels1.db")
        self.cur = self.conn.cursor()
        self.select = self.cur.execute("select * from donnees order by nom asc")
        self.conn.commit()
        for row in self.select:
            self.tv.insert('', END, values=row)
        self.conn.close()

    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("BA ELS", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return

    def Section1(self):
        alphaLim=(9*self.fc1.get())/((9*self.fc1.get())+200)
        MlimSER=0.1*self.fc1.get()*self.b1.get()*pow(self.d1.get(),2)*alphaLim*(3-alphaLim)
        if self.Mser.get()<=MlimSER:
            lamda=1+(30*self.Mser.get())/(self.b1.get()*pow(self.d1.get(),2)*200)
            phy=acos(pow(lamda,-(1.5)))*(180/pi)
            alpha=1+(2*sqrt(lamda)*cos(240+phy/3))
            Asser=self.Mser.get()/(200*self.d1.get()*(1-(alpha/3)))
            self.sec1.set("{:.4f}".format(Asser))
        else:
            lamda=self.Mser.get()-MlimSER
            contraintPrimSC=(9*self.fc1.get())*(1-self.dp1.get()/(alphaLim*self.d1.get()))
            AprimSser=lamda/(contraintPrimSC*(self.d1.get()-self.dp1.get()))
            Asser=((AprimSser*contraintPrimSC)+(0.3*alphaLim*self.b1.get()*self.d1.get()*self.fc1.get()))/200
            self.sec1.set("{:.4f}".format(Asser))


    def Section21(self):
        alphaLim = (9 * self.fc1.get()) / ((9 * self.fc1.get()) + 200)
        MlimSER = 0.1 * self.fc1.get() * self.b1.get() * pow(self.d1.get(), 2) * alphaLim * (3 - alphaLim)
        if self.Mser.get() <= MlimSER:
            lamda = 1 + (30 * self.Mser.get()) / (self.b1.get() * pow(self.d1.get(), 2) * 200)
            phy = acos(pow(lamda, -(1.5))) * (180 / pi)
            alpha = 1 + (2 * sqrt(lamda) * cos(240 + phy / 3))
            Asser = self.Mser.get() / (200 * self.d1.get() * (1 - (alpha / 3)))
            self.sec21.set(0)
        else:
            MprimS = self.Mser.get() - MlimSER
            contraintPrimSC = (9 * self.fc1.get()) * (1 - self.dp1.get() / (alphaLim * self.d1.get()))
            AprimSser = MprimS / (contraintPrimSC * (self.d1.get() - self.dp1.get()))
            self.sec21.set("{:.4f}".format(AprimSser))

class windows4:
    def __init__(self,master):
        self.master = master
        self.master.title("Prédim Nervure")
        self.master.geometry('1350x750+0+0')
        self.master.config(background="#2c3e50")
        self.master.iconbitmap("logo.ico")
        self.lblt=Label(self.master,text="Prédimensionnement des Nervures", font=("calibri", 21, "bold"))
        self.lblt.place(x=0,y=0,width=1360)
        #___________________________variables______________
        self.nom2=StringVar(self.master)
        self.long=DoubleVar(self.master)
        self.lonG=DoubleVar(self.master)
        self.haut=DoubleVar(self.master)
        self.larg=DoubleVar(self.master)

        self.lblnom = Label(self.master, text="nom", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnom.place(x=1, y=40, width=250)
        self.entrynom = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.nom2, fg="black")
        self.entrynom.place(x=250, y=40, width=150)
        self.lbllong = Label(self.master, text="longueur", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbllong.place(x=1, y=90, width=250)
        self.entrylong = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.long, fg="black")
        self.entrylong.place(x=250, y=90, width=150)
        self.butlongS225=Button(self.master,text="longueur/22.5",fg="black",bg="#4f1d5e",command=self.div,font=("yu gothic ui", 12, "bold"))
        self.butlongS225.place(x=1, y=140, width=250)
        self.labellongS225 =Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white",textvariable=self.lonG,fg="black")
        self.labellongS225.place(x=250, y=140, width=150)
        self.lblh = Label(self.master, text="hauteur", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblh.place(x=1, y=190, width=250)
        self.entryh = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.haut,fg="black")
        self.entryh.place(x=250, y=190, width=150)
        self.lbllarg = Label(self.master, text="largeur", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbllarg.place(x=1, y=240, width=250)
        self.combolarg = ttk.Combobox(self.master, text="largeur", font=("calibri", 21, "bold"), state="readonly",textvariable=self.larg)
        self.combolarg['values'] = (12,15)
        self.combolarg.place(x=250, y=240, width=150)
        #_________les fonctions____________________

        self.lblnote = Label(self.master, text="note", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnote.place(x=1, y=300, width=400)
        self.textnote = Text(self.master, font=("calibri", 21, "bold"), bg="white", fg="black", height=5)
        self.textnote.place(x=1, y=340, width=400)
        # __________________la partie vue______________
        self.tree_frame = Frame(self.master, bg="#ecf0f1")
        self.tree_frame.place(x=400, y=40, width=960, height=700)
        self.tv = ttk.Treeview(self.tree_frame, height=34, column=(1, 2, 3, 4, 5,6))
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=0)
        self.tv.heading("2", text="nom")
        self.tv.column("2", width=1)
        self.tv.heading("3", text="longeur")
        self.tv.column("3", width=8)
        self.tv.heading("4", text="longeur/22.5")
        self.tv.column("4", width=2)
        self.tv.heading("5", text="hauteur h")
        self.tv.column("5", width=2)
        self.tv.heading("6", text="largeur l")
        self.tv.column("6", width=2)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=X)
        # ____________________les boutons________________________
        self.btnajt = Button(self.master, text="Enregistre", command=self.enregistre, width=15, font=("calibri", "16"),bg="#16a085", fg="white")
        self.btnajt.place(x=1, y=490, width=200)
        self.btnrange = Button(self.master, text="ranger", width=15, font=("calibri", "16"), bg="#1298b9", command=self.ranger, fg="white")
        self.btnrange.place(x=200, y=490, width=200)
        self.btndesup = Button(self.master, text="Suprimer", width=15, command=self.suprimer, font=("calibri", "16"), bg="#c0392b", fg="white")
        self.btndesup.place(x=1, y=530, width=200)
        self.btnequit = Button(self.master, text="quiter", width=15, font=("calibri", "16"), command=self.button_quitter, bg="#f39c12", fg="white")
        self.btnequit.place(x=200, y=530, width=200)

        #_______________connection_________
        self.conn1 = sqlite3.connect('databaseNervure.db')
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute('select * from valeur')
        for row in self.select:
            self.tv.insert('', END, value=row)
        self.conn1.close()
    def enregistre(self):
        # create connection
        if self.nom2.get()=="" or self.long.get()=="":
            tkinter.messagebox.showerror("BA NERVURE" ,"vous devez remplire toute les cases")
        else:

            self.conn1 = sqlite3.connect('databaseNervure.db')
            self.cur1 = self.conn1.cursor()
            self.cur1.execute("INSERT INTO valeur('nom','longueur','longueurp','hauteur','largeur') values(?,?,?,?,?)", (self.nom2.get(),self.long.get(),self.lonG.get(),self.haut.get(), self.larg.get()))
            self.conn1.commit()
            self.cur1 = self.conn1.cursor()
            self.select = self.cur1.execute("SELECT * FROM valeur order by id desc")
            self.select = list(self.select)
            self.tv.insert('', END, value=self.select[0])
            self.conn1.close()
    def suprimer(self):
        idslect = self.tv.item(self.tv.selection())['values'][0]
        self.conn1 = sqlite3.connect("databaseNervure.db")
        self.cur1 = self.conn1.cursor()
        self.sup1 = self.cur1.execute("delete from valeur where id={}".format(idslect))
        self.conn1.commit()
        self.tv.delete(self.tv.selection())

    def ranger(self):
        for x in self.tv.get_children():
            self.tv.delete(x)
        self.conn1 = sqlite3.connect("databaseNervure.db")
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute("select * from valeur order by nom asc")
        self.conn1.commit()
        for row in self.select:
            self.tv.insert('', END, values=row)
        self.conn1.close()

    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("BA NERVURE", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return

    def div(self):
        X=self.long.get()/22.5
        self.lonG.set("{:.4f}".format(X))

class windows5:
    def __init__(self,master):
        self.master = master
        self.master.title("Prédim POUTRE ISOSTATIQUE")
        self.master.geometry('1350x750+0+0')
        self.master.config(background="#2c3e50")
        self.master.iconbitmap("logo.ico")
        self.lblt=Label(self.master,text="Prédimensionnement des poutre isostatiques", font=("calibri", 21, "bold"))
        self.lblt.place(x=0,y=0,width=1360)
        #___________________________variables______________
        self.nom3=StringVar(self.master)
        self.long=DoubleVar(self.master)
        self.long15=DoubleVar(self.master)
        self.long10=DoubleVar(self.master)
        self.h1=DoubleVar(self.master)
        self.hp=DoubleVar(self.master)
        self.hpp=DoubleVar(self.master)
        self.b1=DoubleVar(self.master)

        self.lblnom = Label(self.master, text="nom", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnom.place(x=1, y=40, width=250)
        self.entrynom = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.nom3, fg="black")
        self.entrynom.place(x=250, y=40, width=150)
        self.lbllong = Label(self.master, text="longueur", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbllong.place(x=1, y=90, width=250)
        self.entrylong = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.long, fg="black")
        self.entrylong.place(x=250, y=90, width=150)
        self.butlongS15=Button(self.master,text="longueur/15",fg="black",bg="#4f1d5e",command=self.longA15,font=("yu gothic ui", 12, "bold"))
        self.butlongS15.place(x=1, y=140, width=250)
        self.lbllongS15 = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white",textvariable=self.long15, fg="black")
        self.lbllongS15.place(x=250, y=140, width=150)
        self.butlongS10 = Button(self.master, text="longueur/10", fg="black", bg="#4f1d5e",command=self.longA10,font=("yu gothic ui", 12, "bold"))
        self.butlongS10.place(x=1, y=190, width=250)
        self.lbllongS10 = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.long10,fg="black")
        self.lbllongS10.place(x=250, y=190, width=150)
        self.lblh1 = Label(self.master,text="choix hauteur" ,font=("yu gothic ui", 16, "bold"),bg="dark gray", fg="white")
        self.lblh1.place(x=1, y=240, width=200)
        self.btver = Button(self.master, text="verifier", command=self.verifier).place(x=200, y=240, width=50, height=35)
        self.comboh1 = ttk.Combobox(self.master, font=("yu gothic ui", 16, "bold"), state="readonly",textvariable=self.h1)
        self.comboh1['values'] = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100)
        self.comboh1.place(x=250, y=240, width=150)
        self.buthp = Button(self.master, fg="black",text="0,27h",bg="#4f1d5e",font=("yu gothic ui", 12, "bold"),command=self.hautA27)
        self.buthp.place(x=1, y=290, width=250)
        self.lblhp = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.hp,fg="black")
        self.lblhp.place(x=250, y=290, width=150)
        self.buthpp= Button(self.master, fg="black",text="0,54h", bg="#4f1d5e",font=("yu gothic ui", 12, "bold"),command=self.hautA54)
        self.buthpp.place(x=1, y=340, width=250)
        self.lblhpp = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.hpp,fg="black")
        self.lblhpp.place(x=250, y=340, width=150)
        self.lblh1 = Label(self.master, text="choix base", font=("yu gothic ui", 16, "bold"), bg="dark gray",fg="white")
        self.lblh1.place(x=1, y=390, width=250)
        self.comboh1 = ttk.Combobox(self.master, font=("yu gothic ui", 16, "bold"), state="readonly",textvariable=self.b1)
        self.comboh1['values'] = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100)
        self.comboh1.place(x=250, y=390, width=150)
        self.btver1 = Button(self.master, text="verifier", command=self.verifier2).place(x=200, y=390, width=50,height=35)
        self.lblnote = Label(self.master, text="note", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnote.place(x=1, y=440, width=400)
        self.textnote = Text(self.master, font=("calibri", 21, "bold"), bg="white", fg="black", height=5)
        self.textnote.place(x=1, y=440, width=400)
        # ____________________les boutons________________________
        self.btnajt = Button(self.master, text="Enregistre", command=self.enregistre, width=15, font=("calibri", "16"),bg="#16a085", fg="white")
        self.btnajt.place(x=1, y=610, width=200)
        self.btnrange = Button(self.master, text="ranger", width=15, font=("calibri", "16"), bg="#1298b9",command=self.ranger, fg="white")
        self.btnrange.place(x=200, y=610, width=200)
        self.btndesup = Button(self.master, text="Suprimer", width=15, command=self.suprimer, font=("calibri", "16"),bg="#c0392b", fg="white")
        self.btndesup.place(x=1, y=650, width=200)
        self.btnequit = Button(self.master, text="quiter", width=15, font=("calibri", "16"), command=self.button_quitter, bg="#f39c12", fg="white")
        self.btnequit.place(x=200, y=650, width=200)
        self.tree_frame = Frame(self.master, bg="#ecf0f1")
        self.tree_frame.place(x=400, y=40, width=960, height=700)
        self.tv = ttk.Treeview(self.tree_frame, height=34, column=(1, 2, 3, 4, 5, 6,7,8,9))
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=0)
        self.tv.heading("2", text="nom")
        self.tv.column("2", width=1)
        self.tv.heading("3", text="longeur")
        self.tv.column("3", width=8)
        self.tv.heading("4", text="longeur/15")
        self.tv.column("4", width=8)
        self.tv.heading("5", text="longeur/10")
        self.tv.column("5", width=8)
        self.tv.heading("6", text=" hauteur")
        self.tv.column("6", width=8)
        self.tv.heading("7", text="0,27h")
        self.tv.column("7", width=8)
        self.tv.heading("8", text="0,54h")
        self.tv.column("8", width=2)
        self.tv.heading("9", text="base")
        self.tv.column("9",width=2)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=X)
        # _______________connection_________
        self.conn1 = sqlite3.connect('databasePoutreiso.db')
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute('select * from valeur')
        for row in self.select:
            self.tv.insert('', END, value=row)
        self.conn1.close()


    def enregistre(self):
        # create connection
        if self.nom3.get() == "" or self.long.get() == "":
            tkinter.messagebox.showerror("BA poutre ISO", "vous devez remplire toute les cases")
        else:

            self.conn1 = sqlite3.connect('databasePoutreiso.db')
            self.cur1 = self.conn1.cursor()
            self.cur1.execute("INSERT INTO valeur('nom','longueur','longueur15','longueur10','hauteur','hauteur1','hauteur2','base') values(?,?,?,?,?,?,?,?)",
                              (self.nom3.get(), self.long.get(), self.long15.get(), self.long10.get(), self.h1.get(),self.hp.get(),self.hpp.get(),self.b1.get()))
            self.conn1.commit()
            self.cur1 = self.conn1.cursor()
            self.select = self.cur1.execute("SELECT * FROM valeur order by id desc")
            self.select = list(self.select)
            self.tv.insert('', END, value=self.select[0])
            self.conn1.close()


    def suprimer(self):
        idslect = self.tv.item(self.tv.selection())['values'][0]
        self.conn1 = sqlite3.connect("databasePoutreiso.db")
        self.cur1 = self.conn1.cursor()
        self.sup1 = self.cur1.execute("delete from valeur where id={}".format(idslect))
        self.conn1.commit()
        self.tv.delete(self.tv.selection())


    def ranger(self):
        for x in self.tv.get_children():
            self.tv.delete(x)
        self.conn1 = sqlite3.connect("databasePoutreiso.db")
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute("select * from valeur order by nom asc")
        self.conn1.commit()
        for row in self.select:
            self.tv.insert('', END, values=row)
        self.conn1.close()


    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("BA POUTRE ISO", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return
    def longA15(self):
        A=self.long.get()/15
        self.long15.set("{:.4f}".format(A))
    def longA10(self):
        B=self.long.get()/10
        self.long10.set("{:.4f}".format(B))
    def hautA27(self):
        C=self.h1.get()*0.27
        self.hp.set("{:.4f}".format(C))
    def hautA54(self):
        D=self.h1.get()*0.54
        self.hpp.set("{:.4f}".format(D))
    def verifier(self):
        if self.long15.get()<=self.h1.get() and self.long10.get()>=self.h1.get():
            tkinter.messagebox.showerror("BA POUTRE ISO", "VALIDE")
        else:
            tkinter.messagebox.showerror("BA POUTRE ISO", "NON VALIDE")
            self.h1.set(0)
    def verifier2(self):
        if self.hp.get()<=self.b1.get() and self.hpp.get()>=self.b1.get():
            tkinter.messagebox.showerror("BA POUTRE ISO", "VALIDE")
        else:
            tkinter.messagebox.showerror("BA POUTRE ISO", "NON VALIDE")
            self.b1.set(0)

class windows6:
    def __init__(self,master):
        self.master = master
        self.master.title("Prédim POUTRE HYPERSTATIQUE")
        self.master.geometry('1350x750+0+0')
        self.master.config(background="#2c3e50")
        self.master.iconbitmap("logo.ico")
        self.lblt=Label(self.master,text="Prédimensionnement des poutres hyperstatiques", font=("calibri", 21, "bold"))
        self.lblt.place(x=0,y=0,width=1360)
        #___________________________variables______________
        self.nom4=StringVar(self.master)
        self.long1=DoubleVar(self.master)
        self.long20=DoubleVar(self.master)
        self.long16=DoubleVar(self.master)
        self.h2=DoubleVar(self.master)
        self.hp2=DoubleVar(self.master)
        self.hpp2=DoubleVar(self.master)
        self.b3=DoubleVar(self.master)

        self.lblnom = Label(self.master, text="nom", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnom.place(x=1, y=40, width=250)
        self.entrynom = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.nom4, fg="black")
        self.entrynom.place(x=250, y=40, width=150)
        self.lbllong = Label(self.master, text="longueur", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lbllong.place(x=1, y=90, width=250)
        self.entrylong = Entry(self.master, font=("calibri", 21, "bold"), bg="white", textvariable=self.long1, fg="black")
        self.entrylong.place(x=250, y=90, width=150)
        self.butlongS15=Button(self.master,text="longueur/20",fg="black",bg="#4f1d5e",command=self.longA20,font=("yu gothic ui", 12, "bold"))
        self.butlongS15.place(x=1, y=140, width=250)
        self.lbllongS15 = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white",textvariable=self.long20, fg="black")
        self.lbllongS15.place(x=250, y=140, width=150)
        self.butlongS10 = Button(self.master, text="longueur/16", fg="black", bg="#4f1d5e",command=self.longA16,font=("yu gothic ui", 12, "bold"))
        self.butlongS10.place(x=1, y=190, width=250)
        self.lbllongS10 = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.long16,fg="black")
        self.lbllongS10.place(x=250, y=190, width=150)
        self.lblh1 = Label(self.master,text="choix hauteur" ,font=("yu gothic ui", 16, "bold"),bg="dark gray", fg="white")
        self.lblh1.place(x=1, y=240, width=200)
        self.btver = Button(self.master, text="verifier", command=self.verifier).place(x=200, y=240, width=50, height=35)
        self.comboh1 = ttk.Combobox(self.master, font=("yu gothic ui", 16, "bold"), state="readonly",textvariable=self.h2)
        self.comboh1['values'] = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100)
        self.comboh1.place(x=250, y=240, width=150)
        self.buthp = Button(self.master, fg="black",text="0,27h",bg="#4f1d5e",font=("yu gothic ui", 12, "bold"),command=self.hautA27)
        self.buthp.place(x=1, y=290, width=250)
        self.lblhp = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.hp2,fg="black")
        self.lblhp.place(x=250, y=290, width=150)
        self.buthpp= Button(self.master, fg="black",text="0,54h", bg="#4f1d5e",font=("yu gothic ui", 12, "bold"),command=self.hautA54)
        self.buthpp.place(x=1, y=340, width=250)
        self.lblhpp = Label(self.master, font=("yu gothic ui", 16, "bold"), bg="white", textvariable=self.hpp2,fg="black")
        self.lblhpp.place(x=250, y=340, width=150)
        self.lblh1 = Label(self.master, text="choix base", font=("yu gothic ui", 16, "bold"), bg="dark gray",fg="white")
        self.lblh1.place(x=1, y=390, width=250)
        self.comboh1 = ttk.Combobox(self.master, font=("yu gothic ui", 16, "bold"), state="readonly",textvariable=self.b3)
        self.comboh1['values'] = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100)
        self.comboh1.place(x=250, y=390, width=150)
        self.btver1 = Button(self.master, text="verifier", command=self.verifier2).place(x=200, y=390, width=50,height=35)
        self.lblnote = Label(self.master, text="note", font=("calibri", 21, "bold"), bg="dark gray", fg="white")
        self.lblnote.place(x=1, y=440, width=400)
        self.textnote = Text(self.master, font=("calibri", 21, "bold"), bg="white", fg="black", height=5)
        self.textnote.place(x=1, y=440, width=400)
        # ____________________les boutons________________________
        self.btnajt = Button(self.master, text="Enregistre", command=self.enregistre, width=15, font=("calibri", "16"),bg="#16a085", fg="white")
        self.btnajt.place(x=1, y=610, width=200)
        self.btnrange = Button(self.master, text="ranger", width=15, font=("calibri", "16"), bg="#1298b9",command=self.ranger, fg="white")
        self.btnrange.place(x=200, y=610, width=200)
        self.btndesup = Button(self.master, text="Suprimer", width=15, command=self.suprimer, font=("calibri", "16"),bg="#c0392b", fg="white")
        self.btndesup.place(x=1, y=650, width=200)
        self.btnequit = Button(self.master, text="quiter", width=15, font=("calibri", "16"), command=self.button_quitter, bg="#f39c12", fg="white")
        self.btnequit.place(x=200, y=650, width=200)
        self.tree_frame = Frame(self.master, bg="#ecf0f1")
        self.tree_frame.place(x=400, y=40, width=960, height=700)
        self.tv = ttk.Treeview(self.tree_frame, height=34, column=(1, 2, 3, 4, 5, 6,7,8,9))
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=0)
        self.tv.heading("2", text="nom")
        self.tv.column("2", width=1)
        self.tv.heading("3", text="longeur")
        self.tv.column("3", width=8)
        self.tv.heading("4", text="longeur/20")
        self.tv.column("4", width=8)
        self.tv.heading("5", text="longeur/16")
        self.tv.column("5", width=8)
        self.tv.heading("6", text=" hauteur")
        self.tv.column("6", width=8)
        self.tv.heading("7", text="0,27h")
        self.tv.column("7", width=8)
        self.tv.heading("8", text="0,54h")
        self.tv.column("8", width=2)
        self.tv.heading("9", text="base")
        self.tv.column("9",width=2)
        self.tv['show'] = 'headings'
        self.tv.pack(fill=X)
        # _______________connection_________
        self.conn1 = sqlite3.connect('databasePoutreiso.db')
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute('select * from valeur')
        for row in self.select:
            self.tv.insert('', END, value=row)
        self.conn1.close()


    def enregistre(self):
        # create connection
        if self.nom4.get() == "" or self.long1.get() == "":
            tkinter.messagebox.showerror("BA poutre ISO", "vous devez remplire toute les cases")
        else:

            self.conn1 = sqlite3.connect('databasePoutrehyp.db')
            self.cur1 = self.conn1.cursor()
            self.cur1.execute("INSERT INTO valeur('nom','longueur','longueur20','longueur16','hauteur','hauteur1','hauteur2','base') values(?,?,?,?,?,?,?,?)",
                              (self.nom4.get(), self.long1.get(), self.long20.get(), self.long16.get(), self.h2.get(),self.hp2.get(),self.hpp2.get(),self.b3.get()))
            self.conn1.commit()
            self.cur1 = self.conn1.cursor()
            self.select = self.cur1.execute("SELECT * FROM valeur order by id desc")
            self.select = list(self.select)
            self.tv.insert('', END, value=self.select[0])
            self.conn1.close()


    def suprimer(self):
        idslect = self.tv.item(self.tv.selection())['values'][0]
        self.conn1 = sqlite3.connect("databasePoutrehyp.db")
        self.cur1 = self.conn1.cursor()
        self.sup1 = self.cur1.execute("delete from valeur where id={}".format(idslect))
        self.conn1.commit()
        self.tv.delete(self.tv.selection())


    def ranger(self):
        for x in self.tv.get_children():
            self.tv.delete(x)
        self.conn1 = sqlite3.connect("databasePoutrehyp.db")
        self.cur1 = self.conn1.cursor()
        self.select = self.cur1.execute("select * from valeur order by nom asc")
        self.conn1.commit()
        for row in self.select:
            self.tv.insert('', END, values=row)
        self.conn1.close()


    def button_quitter(self):
        self.button_quitter = tkinter.messagebox.askyesno("BA POUTRE HYP", "voulez vous quitter ?")
        if self.button_quitter > 0:
            self.master.destroy()
            return
    def longA20(self):
        A=self.long1.get()/20
        self.long20.set("{:.4f}".format(A))
    def longA16(self):
        B=self.long1.get()/16
        self.long16.set("{:.4f}".format(B))
    def hautA27(self):
        C=self.h2.get()*0.27
        self.hp2.set("{:.4f}".format(C))
    def hautA54(self):
        D=self.h2.get()*0.54
        self.hpp2.set("{:.4f}".format(D))
    def verifier(self):
        if self.long20.get()<=self.h2.get() and self.long16.get()>=self.h2.get():
            tkinter.messagebox.showerror("BA POUTRE HYP", "VALIDE")
        else:
            tkinter.messagebox.showerror("BA POUTRE HYP", "NON VALIDE")
            self.h2.set(0)
    def verifier2(self):
        if self.hp2.get()<=self.b3.get() and self.hpp2.get()>=self.b3.get():
            tkinter.messagebox.showerror("BA POUTRE HYP", "VALIDE")
        else:
            tkinter.messagebox.showerror("BA POUTRE HYP", "NON VALIDE")
            self.b3.set(0)

class windows7:
    def __init__(self, master):
        self.master = master
        self.master.title("Charges permanantes G")
        self.master.geometry('1350x750+0+0')
        self.master.config(background="#2c3e50")
        self.master.iconbitmap("logo.ico")
        self.lblt = Label(self.master, text="calcul de charge permanentes",font=("calibri", 21, "bold"))
        self.lblt.place(x=0, y=0, width=1360)
        self.framePR=Frame(self.master,width=1350,height=750)
        self.framePR.pack(side=LEFT)
        self.f1=Frame(self.framePR,width=450,height=750,bd=50)
        self.f1.pack(side=LEFT)
        self.f2 = Frame(self.framePR, width=450, height=750,bd=50)
        self.f2.pack(side=LEFT)
        self.f3 = Frame(self.framePR, width=450, height=750,bd=50)
        self.f3.pack(side=RIGHT)

        #____________________mes variables_______________
        self.var1=  IntVar(self.master)
        self.var2 = IntVar(self.master)
        self.var3 = IntVar(self.master)
        self.var4 = IntVar(self.master)
        self.var5 = IntVar(self.master)
        self.var6 = IntVar(self.master)
        self.var7 = IntVar(self.master)
        self.var8 = IntVar(self.master)
        self.var9 = IntVar(self.master)
        self.var10 = DoubleVar(self.master)



        self.var1.set("0")
        self.var2.set("0")
        self.var3.set("0")
        self.var4.set("0")
        self.var5.set("0")
        self.var6.set("0")
        self.var7.set("0")
        self.var8.set("0")
        self.var9.set("0")

        #________________________variable entry________________________
        self.Gceram=DoubleVar(self.master)
        self.Gceram.set("0.5")
        self.Gceramique=DoubleVar(self.master)
        self.Gceramique.set("0.6")
        self.pierre_dure=DoubleVar(self.master)
        self.pierre_dure.set("7.8")
        self.carrelages=DoubleVar(self.master)
        self.carrelages.set("0.2")
        self.chape_ciment=DoubleVar(self.master)
        self.chape_ciment.set("0.2")
        self.Tchape_flo=DoubleVar(self.master)
        self.Tchape_flo.set("0.5")
        self.dalle_flo=DoubleVar(self.master)
        self.dalle_flo.set("0.22")
        self.Paquets=DoubleVar(self.master)
        self.Paquets.set("0.25")
        self.Plastiques=DoubleVar(self.master)
        self.Plastiques.set("0.08")

#____________________________frame 1__________________________________________________________
        lblRE=Label(self.f1,text="revetement planchers KN/m²",font=("arial",18,"bold"),fg="blue",justify="left")
        lblRE.grid(row=0,column=0)
        lblep1 = Label(self.f1, text="G", font=("arial", 18, "bold"),bg="orange",fg="ivory", justify="left")
        lblep1.grid(row=0, column=1)

        Tgres_cerame=Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.Gceram, width=6, justify="left", state=DISABLED)
        Tgres_cerame.grid(row=1, column=1)
        gres_cerame  =Radiobutton(self.f1, text="Grès cérame",value=0.500001, variable=self.var1, font=("arial", 18, "bold"))
        gres_cerame .grid(row=1, column=0, sticky=W)

        Tgres_ceramique = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.Gceramique, width=6, justify="left", state=DISABLED)
        Tgres_ceramique.grid(row=2, column=1)
        gres_ceramique = Radiobutton(self.f1, text="Grès céramique",value=0.6, variable=self.var1, font=("arial", 18, "bold"))
        gres_ceramique.grid(row=2, column=0, sticky=W)

        Tpierre_dure = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.pierre_dure, width=6, justify="left",state=DISABLED)
        Tpierre_dure.grid(row=3, column=1)
        pierre_dure = Radiobutton(self.f1, text="pierre dure",value=0.8, variable=self.var1,font=("arial", 18, "bold"))
        pierre_dure.grid(row=3, column=0, sticky=W)

        Tcarrelages = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.carrelages, width=6, justify="left",state=DISABLED)
        Tcarrelages.grid(row=4, column=1)
        carrelages = Radiobutton(self.f1, text="Carrelages",value=0.200001, variable=self.var1, font=("arial", 18, "bold"))
        carrelages.grid(row=4, column=0, sticky=W)

        Tchape_ciment = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.chape_ciment, width=6, justify="left",state=DISABLED)
        Tchape_ciment.grid(row=5, column=1)
        chape_ciment = Radiobutton(self.f1, text="Chape mortier ciment",value=0.2, variable=self.var1,font=("arial", 18, "bold"))
        chape_ciment.grid(row=5, column=0, sticky=W)

        Tchape_flo = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.Tchape_flo, width=6, justify="left",state=DISABLED)
        Tchape_flo.grid(row=6, column=1)
        chape_flo = Radiobutton(self.f1, text="Chape flottante asphalte",value=0.5, variable=self.var1, font=("arial", 18, "bold"))
        chape_flo.grid(row=6, column=0, sticky=W)

        Tdalle_flo = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.dalle_flo, width=6, justify="left",state=DISABLED)
        Tdalle_flo.grid(row=7, column=1)
        dalle_flo = Radiobutton(self.f1, text="Chape flottante béton",value=0.22, variable=self.var1, font=("arial", 18, "bold"))
        dalle_flo.grid(row=7, column=0, sticky=W)

        TPaquets = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.Paquets, width=6, justify="left",state=DISABLED)
        TPaquets.grid(row=8, column=1)
        Paquets = Radiobutton(self.f1, text="Parquets 23 mm", variable=self.var1,value=0.25, font=("arial", 18, "bold"))
        Paquets.grid(row=8, column=0, sticky=W)

        TPlastiques = Entry(self.f1, font=("arial", 18, "bold"), textvariable=self.Plastiques, width=6, justify="left", state=DISABLED)
        TPlastiques.grid(row=9, column=1)
        Plastiques = Radiobutton(self.f1, text="Plastiques", variable=self.var1,value=0.08,font=("arial", 18, "bold"))
        Plastiques.grid(row=9, column=0, sticky=W)

#____________________________frame 2______________________________________________
        lblRE = Label(self.f2, text="Maconnerie  KN/m²", font=("arial", 16, "bold"), fg="blue",justify="left")
        lblRE.grid(row=0, column=0)
        lblRE = Label(self.f2, text="Briques creuses", font=("arial", 16, "bold"), fg="blue", justify="left")
        lblRE.grid(row=1, column=0)
        lblep1 = Label(self.f2, text="G", font=("arial", 18, "bold"), bg="orange",fg="ivory", justify="left")
        lblep1.grid(row=1, column=1)

        self.BC1=DoubleVar(self.master)
        self.BC1.set("0.45")
        self.BC2=DoubleVar(self.master)
        self.BC2.set("0.9")
        self.BC3=DoubleVar(self.master)
        self.BC3.set("1.3")
        self.BC4 = DoubleVar(self.master)
        self.BC4.set("1.75")
        self.BC5 =DoubleVar(self.master)
        self.BC5.set("2.15")
        self.BC6 = DoubleVar(self.master)
        self.BC6.set("2.6")
        self.platre=DoubleVar(self.master)
        self.platre.set("0")
        self.mortier=DoubleVar(self.master)
        self.mortier.set("0")

        TBC1 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC1, width=6, justify="left",state=DISABLED)
        TBC1.grid(row=2, column=1)
        BC1 = Radiobutton(self.f2, text="5 Cm", variable=self.var2, value=0.45, font=("arial", 18, "bold"))
        BC1.grid(row=2, column=0, sticky=W)

        TBC2 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC2, width=6, justify="left",state=DISABLED)
        TBC2.grid(row=3, column=1)
        BC2 = Radiobutton(self.f2, text="10 Cm", variable=self.var2, value=0.9, font=("arial", 18, "bold"))
        BC2.grid(row=3, column=0, sticky=W)

        TBC3 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC3, width=6, justify="left", state=DISABLED)
        TBC3.grid(row=4, column=1)
        BC3  = Radiobutton(self.f2, text="15 Cm", variable=self.var2, value=1.3,font=("arial", 18, "bold"))
        BC3 .grid(row=4, column=0, sticky=W)

        TBC4 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC4, width=6, justify="left",state=DISABLED)
        TBC4 .grid(row=5, column=1)
        BC4  = Radiobutton(self.f2, text="20 Cm", variable=self.var2, value=1.75, font=("arial", 18, "bold"))
        BC4 .grid(row=5, column=0, sticky=W)

        TBC5 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC5, width=6, justify="left",state=DISABLED)
        TBC5.grid(row=6, column=1)
        BC5  = Radiobutton(self.f2, text="25 Cm", variable=self.var2, value=2.15, font=("arial", 18, "bold"))
        BC5.grid(row=6, column=0, sticky=W)

        TBC6 = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.BC6, width=6, justify="left",state=DISABLED)
        TBC6.grid(row=7, column=1)
        BC6 =Radiobutton(self.f2, text="30 Cm", variable=self.var2, value=2.6, font=("arial", 18, "bold"))
        BC6.grid(row=7, column=0, sticky=W)

        lblenduits = Label(self.f2, text="Enduits  KN/m²", font=("arial", 16, "bold"), fg="blue", justify="left")
        lblenduits.grid(row=8, column=0)
        lblep2 = Label(self.f2, text="ep", font=("arial", 18, "bold"), bg="orange",fg="ivory", justify="left")
        lblep2.grid(row=8, column=1)

        self.Tplatre = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.platre, width=6, justify="left", state=DISABLED)
        self.Tplatre.grid(row=9, column=1)
        self.platre = Checkbutton(self.f2, text="Platre", variable=self.var4, onvalue=1, offvalue=0, font=("arial", 18, "bold"),command=self.checkplatre)
        self.platre.grid(row=9, column=0, sticky=W)

        self.Tmortier = Entry(self.f2, font=("arial", 18, "bold"), textvariable=self.mortier, width=6, justify="left", state=DISABLED)
        self.Tmortier.grid(row=10, column=1)
        self.mortier = Checkbutton(self.f2, text="mortier L hyd", variable=self.var5, onvalue=1, offvalue=0, font=("arial", 18, "bold"),command=self.checkmortier)
        self.mortier.grid(row=10, column=0, sticky=W)
        self.butT=Button(self.f2,text="G total",font=("arial", 18, "bold"), bg="#3a5d11",command=self.Gtotal)
        self.butT.grid(row=11, column=0)
        self.lblT = Label(self.f2, textvariable=self.var10, font=("arial", 18, "bold"), bg="white",fg="black",width=5)
        self.lblT.grid(row=11, column=1)

#_______________________________________frame 3______________________________________________
        self.contreplaques=StringVar(self.master)
        self.contreplaques.set("0")


        lblsous_toitures = Label(self.f3, text="Sous-toitures", font=("arial", 18, "bold"), fg="blue", justify="left")
        lblsous_toitures.grid(row=0, column=0)
        lblep4 = Label(self.f3, text="ep", font=("arial", 18, "bold"), bg="orange",fg="ivory", justify="left")
        lblep4.grid(row=0, column=1)
        self.panneaux=StringVar(self.master)
        self.panneaux.set("0")
        self.plaque=DoubleVar(self.master)
        self.plaque.set("0")
        self.paille=DoubleVar(self.master)
        self.paille.set("0")
        self.P12=DoubleVar(self.master)
        self.P12.set("2.5")
        self.P16 =DoubleVar(self.master)
        self.P16.set("2.8")
        self.P20 = DoubleVar(self.master)
        self.P20.set("3.2")
        self.P25 = DoubleVar(self.master)
        self.P25.set("3.9")


        self.Tcontreplaques = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.contreplaques, width=6, justify="left",state=DISABLED)
        self.Tcontreplaques.grid(row=1, column=1)
        self.contreplaques  = Checkbutton(self.f3, text="contreplaqués", variable=self.var6, onvalue=1, offvalue=0,font=("arial", 18, "bold"),command=self.checkcontreplaques)
        self.contreplaques .grid(row=1, column=0, sticky=W)

        self.Tpanneaux = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.panneaux, width=6,justify="left", state=DISABLED)
        self.Tpanneaux.grid(row=2, column=1)
        self.panneaux = Checkbutton(self.f3, text="panneaux de lin", variable=self.var7, onvalue=1, offvalue=0,font=("arial", 18, "bold"),command=self.checkpanneaux)
        self.panneaux.grid(row=2, column=0, sticky=W)

        self.Tplaque = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.plaque, width=6,justify="left", state=DISABLED)
        self.Tplaque.grid(row=3, column=1)
        self.plaque = Checkbutton(self.f3, text="plaques de platre", variable=self.var8, onvalue=1, offvalue=0,font=("arial", 18, "bold"),command=self.checkplaque)
        self.plaque.grid(row=3, column=0, sticky=W)

        self.Tpaille = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.paille, width=6, justify="left", state=DISABLED)
        self.Tpaille.grid(row=4, column=1)
        self.paille = Checkbutton(self.f3, text="paille compressée", variable=self.var9, onvalue=1, offvalue=0,font=("arial", 18, "bold"),command=self.checkpaille)
        self.paille.grid(row=4, column=0, sticky=W)

        lblplancherN = Label(self.f3, text="planchers nervurés", font=("arial", 18, "bold"), fg="blue", justify="left")
        lblplancherN.grid(row=5, column=0)
        lblentrevou = Label(self.f3, text="entrevous en béton", font=("arial", 18, "bold"), fg="blue", justify="left")
        lblentrevou.grid(row=6, column=0)
        lblmontage = Label(self.f3, text="avec table de compression", font=("arial", 18, "bold"), fg="blue", justify="left")
        lblmontage.grid(row=7, column=0)
        lblep3 = Label(self.f3, text="G", font=("arial", 18, "bold"), bg="orange",fg="ivory", justify="left")
        lblep3.grid(row=7, column=1)

        TP1 = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.P12, width=6, justify="left", state=DISABLED)
        TP1.grid(row=8, column=1)
        P1 = Radiobutton(self.f3, text="12+4 Cm", variable=self.var3, value=2.4, font=("arial", 18, "bold"))
        P1.grid(row=8, column=0, sticky=W)

        TP2 = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.P16, width=6, justify="left", state=DISABLED)
        TP2.grid(row=9, column=1)
        P2 = Radiobutton(self.f3, text="16+4 Cm", variable=self.var3, value=2.8, font=("arial", 18, "bold"))
        P2.grid(row=9, column=0, sticky=W)

        TP3 = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.P20, width=6, justify="left",state=DISABLED)
        TP3.grid(row=10, column=1)
        P3 = Radiobutton(self.f3, text="20+4 Cm", variable=self.var3, value=3.2, font=("arial", 18, "bold"))
        P3.grid(row=10, column=0, sticky=W)

        TP4 = Entry(self.f3, font=("arial", 18, "bold"), textvariable=self.P25, width=6, justify="left",state=DISABLED)
        TP4.grid(row=11, column=1)
        P4 =Radiobutton(self.f3, text="25+5 Cm", variable=self.var3, value=3.9, font=("arial", 18, "bold"))
        P4.grid(row=11, column=0, sticky=W)

    def checkplatre(self):
        if self.var4.get()==1:
            self.Tplatre.configure(state=NORMAL)
            self.platre.setvar("")
        elif self.var4.get()==0:
            self.Tplatre.configure(state=DISABLED)
            self.platre.setvar("0")
    def checkmortier(self):
        if self.var5.get()==1:
            self.Tmortier.configure(state=NORMAL)
            self.mortier.setvar("")
        elif self.var5.get()==0:
            self.Tmortier.configure(state=DISABLED)
            self.mortier.setvar("0")
    def checkcontreplaques(self):
        if self.var6.get()==1:
            self.Tcontreplaques.configure(state=NORMAL)
            self.contreplaques.setvar("")
        elif self.var6.get()==0:
            self.Tcontreplaques.configure(state=DISABLED)
            self.contreplaques.setvar("0")
    def checkpanneaux(self):
        if self.var7.get()==1:
            self.Tpanneaux.configure(state=NORMAL)
            self.panneaux.setvar("")
        elif self.var7.get()==0:
            self.Tpanneaux.configure(state=DISABLED)
            self.panneaux.setvar("0")

    def checkplaque(self):
        if self.var8.get() == 1:
            self.Tplaque.configure(state=NORMAL)
            self.plaque.setvar("")
        elif self.var8.get() == 0:
            self.Tplaque.configure(state=DISABLED)
            self.plaque.setvar("0")
    def checkpaille(self):
        if self.var9.get() == 1:
            self.Tpaille.configure(state=NORMAL)
            self.paille.setvar("")
        elif self.var9.get() == 0:
            self.Tpaille.configure(state=DISABLED)
            self.paille.setvar("0")
    def Gtotal(self):
        TOTALG=(self.platre.getvar()+(self.mortier.getvar()*0.18)+(self.contreplaques.getvar()*0.05)+(self.panneaux.getvar()*0.04)+(self.plaque.getvar()*0.09)+(self.paille.getvar()*0.03))
        self.var10.set(TOTALG)



if __name__ == '__main__':
    main()
