from Tkinter import * #for gui
import MySQLdb #for database connectivity
import unittest #for shamir library
from SSSA import sssa #for shamir library

root=Tk();

def generateKey(state,threshold,secret,infoL):
    sta=str(state.get());
    thr=int(threshold.get());
    sec=str(secret.get());
    
    sss=sssa()
    keys=sss.create(thr,3,sec)

    con=MySQLdb.connect(user="root",passwd="mpsk22",host="localhost",db="cdac")
    cur=con.cursor()
    cur.execute("SELECT COUNT(*) From state");
    fetch=cur.fetchone();
    totalStates=int(fetch[0])
    #print totalStates;

    cur.execute("SELECT * FROM state");
    tables=cur.fetchone()
    i=0;
    states=[None]*(totalStates);
    while tables is not None:
        states[i]=tables[1]
        i=i+1;
        tables=cur.fetchone()

    i=0;
    for stat in states:
        keyState="key"+stat;
        #query="insert into "+keyState+" values('"+stat+"','"+keys[0]+"');";
        query = "INSERT INTO "+keyState+"(state,keyss) VALUES(%s,%s)";
        args = (str(sta),str(keys[i]))
        i=i+1;
        cur1=con.cursor()
        cur1.execute(query,args)
        con.commit()

    minState="minkey"+sta;
    query= "INSERT INTO "+minState+"(number) VALUES("+str(thr)+")";
    cur2=con.cursor()
    cur2.execute(query)
    con.commit()

    infoL.config(text="you record succesfully entered");

    
    


stateL=Label(root,text="State");
thresholdL=Label(root,text="Minimum Key");
secretL=Label(root,text="Secret");
infoL=Label(root);
stateE=Entry(root);
thresholdE=Entry(root);
secretE=Entry(root);
generate=Button(root,text="generate key",command= lambda: generateKey(stateE,thresholdE,secretE,infoL))
#generate.bind("<Button-1>",generateKey(stateE,thresholdE,secretE))
#generate.bind(generateKey(stateE,thresholdE,secretE));

stateL.grid(row=0,column=0);
stateE.grid(row=0,column=1);
thresholdL.grid(row=1,column=0);
thresholdE.grid(row=1,column=1);
secretL.grid(row=2,column=0);
secretE.grid(row=2,column=1);
generate.grid(row=3,columnspan=2);
infoL.grid(row=4,columnspan=2);
root.mainloop();

