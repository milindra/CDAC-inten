from Tkinter import * #for gui
import MySQLdb #for database connectivity
import unittest #for shamir library
from SSSA import sssa #for shamir library
import random # for random number generation

root=Tk();
statesName=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli','Daman and Diu','National Capital Territory of Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

def getInfo(showL):
    sss=sssa()

    con=MySQLdb.connect(user="root",passwd="mpsk22",host="localhost",db="cdac")
    cur=con.cursor()
    cur.execute("SELECT COUNT(*) From state");
    fetch=cur.fetchone();
    totalStates=int(fetch[0])

    cur.execute("SELECT * FROM state");
    tables=cur.fetchone()
    i=0;
    
    states=[None]*(totalStates);
    
    while tables is not None:
        states[i]=tables[1]
        i=i+1;
        tables=cur.fetchone()

    totalPopulation=0;
    for stat in states:
        curM=con.cursor()
        query="SELECT number FROM minkey"+stat;
        curM.execute(query);
        minS=curM.fetchone();
        selectS=random.sample(range(0,(totalStates) ), int(minS[0]))
        #print selectS
        secret=[None]*(int(minS[0]));
        j=0;
        curS=con.cursor()
        for i in selectS:

            query="SELECT keyss FROM key"+states[i]+" where state='"+stat+"'";
            #print query;
            curS.execute(query);
            sec=curS.fetchone();
            secret[j]=sec[0];
            #print "llll==="+secret[j]
            j=j+1;

        statePopulation=int(sss.combine(secret));
        totalPopulation=totalPopulation+statePopulation;

    #print totalPopulation
    showL.config(text="total population="+str(totalPopulation));


def numDrop(numState,root):
    myVar=1;
    if 'stateframe' in globals():
        print "exist"
    else:
        print "no"
    stateframe = Frame(root)
    stateframe.grid(row=6);
    
    print numState.get();
    num=int(numState.get());
    print len(statesName);
    totalState=len(statesName);
    
    dropState=[None]*totalState;

    for i in range(0,36):
        if(dropState[i]!=None):
            dropState[i].grid_remove();
            
    for i in range(0,num):
        defaultState=StringVar();
        defaultState.set('Select one State');
        dropState[i] = OptionMenu(stateframe, defaultState, *statesName)
        dropState[i].grid(row=i)
    
    
       
    

centerGov=Label(root,text="Center Goverment",);
infoLabel=Label(root);
infoButton=Button(root,text="Total Population",command=lambda: getInfo(infoLabel));
numState = Spinbox(root, from_=1, to=36)

numButton=Button(root,text="Number of states",command=lambda: numDrop(numState,root));

delButton=Button(root,text="Delete states",command=lambda: delDrop(numState,root));


centerGov.grid(row=0);
infoButton.grid(row=1);
infoLabel.grid(row=2);
numState.grid(row=3);
numButton.grid(row=4);
delButton.grid(row=5);




root.mainloop();
