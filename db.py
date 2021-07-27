import sqlite3


class db (object):
    def __init__(self, name):
        self.name= str(name)#+".db"
        self.dbconfig="""CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY,{1});"""
        #self.dbconfig1="""CREATE INDEX IF NOT EXISTS "INDEX_NAME" ON "{0}"("id")"""
        self.skript=""
        self.zahl=0
    def ausfuehren(self, sqlskript):
        verbindung = sqlite3.connect(str(self.name)+".db")
        zeiger = verbindung.cursor()
        zeiger.execute(sqlskript)
        self.inhalt = zeiger.fetchall()
        verbindung.commit()
        verbindung.close()
    def erstellen(self):
        self.dbconfig=self.dbconfig.format(self.name,self.skript)
        #self.dbconfig1=self.dbconfig1.format(self.name)
        self.ausfuehren(self.dbconfig)
        #self.ausfuehren(self.dbconfig1)
class benutzerdb(db):
    def __init__(self,name):
        db.__init__(self, name)
        self.skript =   """
    benutzername text NOT NULL,
    passwort text NOT NULL, 
    termine text"""



        self.sqlinput= """INSERT INTO benutzer (benutzername, passwort) VALUES("{0}","{1}");"""
        self.sqlselect="""SELECT benutzername, termine FROM benutzer WHERE benutzername="{0}" {1} ; """
    def hinzufuegen(self, benutzername, passwort):
        if self.pruefen(benutzername)== True:
            return("Benutzername existiert bereits")
        benutzer.ausfuehren(self.sqlinput.format(benutzername,passwort))
        return("Profil wurde erstellt")
    def anmelden(self,benutzername, passwort):
        self.ausfuehren(self.sqlselect.format(benutzername,'AND passwort="'+passwort+'"'))
        if self.inhalt!=[]:
            return(self.inhalt)
        return("Benutzername oder Passwort existiert nicht")
    def pruefen(self,benutzername):
        self.ausfuehren(self.sqlselect.format(benutzername,""))
        if self.inhalt==[]:
            return False
        return True

    def termin(self,benutzername,termin):
        self.ausfuehren(self.sqlselect.format(benutzername,""))
        print(self.inhalt)
        termine=[self.inhalt[0][1]]
        print(termine)
        if termine!= [None]:
            print(termine)
            for x in range(len(termine)):
                for y in range(len(termin)):
                    if termine[x]==termin[y]:
                        termin.pop(y)
            termine =termine.append(termin)
        else:
            termine=termin
        print(termine)
        if termine!= None:
            sqlinput="""UPDATE benutzer SET termine="{1}" WHERE benutzername="{0}";"""
            self.ausfuehren(sqlinput.format(str(benutzername),termine))
        
class gruppendb (db):
    def __init__(self,name):
        db.__init__(self, name)
        self.skript="""
    name text NOT NULL,
    benutzerliste text NOT NULL"""
        self.sqlinput= """INSERT INTO gruppen (name, benutzerliste) VALUES("{0}","{1}");"""
        self.sqlselect="""SELECT benutzername, termine FROM benutzer WHERE benutzername="{0}" {1} ; """
        
    def check(self,name, benutzerliste):
        sqlselect="""SELECT name FROM gruppen WHERE name="{0}"; """
        self.ausfuehren(sqlselect.format(name))
        if self.inhalt!=[]:
            return ("Gruppe existiert bereits")
        for x in benutzerliste:
            if benutzer.pruefen(x) == False:
                return("Benutzername " +str(x)+" existiert nicht")
        return False

    def change(self,nachher):
        self.speicher=self.name
        self.name=nachher
   
    def hinzufuegen(self, name, benutzerliste):
        if name == "":
            self.zahl+=1
            name="NeueGruppe"+str(self.zahl)
        if self.check(name,benutzerliste)== False:
            self.ausfuehren(self.sqlinput.format(name,benutzerliste))
            return name
        else:
            return(self.check(name,benutzerliste))

    def benutzerliste(self,name):
        sqlselect="""SELECT name,benutzerliste FROM gruppen WHERE name="{0}"; """
        self.ausfuehren(sqlselect.format(name))
        try:
            benutzerliste=self.inhalt[0][1]
            benutzerliste=eval(benutzerliste)
            return(benutzerliste)
        except:
            return ("Gruppenname nicht vorhanden")
    def termin(self,name):
        termine=[]
        benutzerliste= self.benutzerliste(name)
        self.change("benutzer")
        for x in benutzerliste:
            self.ausfuehren(self.sqlselect.format(x,""))
            termine.append([x,eval(self.inhalt[0][1])])
        self.change(self.speicher)
        return termine
    def tsuchen(self,name,t):
        ptermine=[]
        termine=t
        print(t)
        for x in range(len(self.benutzerliste(name))-1):
            print("x:",x)
            if x>=1:
                for a in range (len(ptermine)):
                    print("a:",ptermine[a][0])
                    for b in termine[x][1]:
                        print("b:",b)
                        if ptermine[a][0]==b:
                            print("zuvielt:",b)
                            termine[x][1].remove(b)
                print("termine bereinigt:",termine[x][1])
            for y in range(len(termine[x][1])):
                print(termine[x][1])
                for z in range (len(termine[x+1][1])):
                    
                    if termine[x][1][y]==termine[x+1][1][z]:
                        check=True
                        print("termin y=z:",termine[x][1][y])
                        for t in range(len(ptermine)-1):
                            if ptermine[t][0]==termine[x][1][y]:
                                check=False
                        if check== True:
                            ptermine.append([termine[x][1][y],0])
                        print("ptermine:", ptermine,"added termin:",termine[x][1][y])
                        for a in range (len(ptermine)):
                            try:
                                inde=ptermine[a][0].index(str(termine[x][1][y]))
                                print("t aus ptermine:",ptermine[a][0],"index added t:",a,"wert added t:", ptermine[a][1]+(len(termine)-x))
                                ptermine[a][1]+=(len(termine)-x)
                            except:
                                pass
        print(ptermine)                
        return ptermine
        
    def ptermin(self,name):
        ergebnis=[]
        termine= self.termin(name)
        ptermine= self.tsuchen(name,termine)
        for x in range(len(ptermine)):
            if ptermine[x][1]==len(termine):
                ergebnis.append(ptermine[x][0])
        try:
            return ergebnis
        except:
            return ("Es gibt keinen perfekten Termin")

    def fptermin (self,name):
        ergebnis=[]
        termine= self.termin(name)
        ptermine= self.tsuchen(name,termine)
        for x in range (len(ptermine)):
            if ptermine[x][1]==len(termine)-1:
                ergebnis.append(ptermine[x][0])
        try:
            return ergebnis
        except:
            return ("Es gibt keinen fast perfekten Termin")

    def funktion(self):
        print(benutzer.inhalt)


benutzer = benutzerdb("benutzer")
benutzer.erstellen()
gruppen = gruppendb("gruppen")
gruppen.erstellen()
