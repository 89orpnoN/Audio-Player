import unidecode

def QNlinee():
    Nomi_linee= []
    LineaAttuale = "filevuoto"
    #directory = os.getcwd().replace("\\","/") + "/codici.txt"
    f = open("../Base del borgobio/msgcryptor 1.3/codici.txt", 'r')
    while LineaAttuale != "":
        j = 0
        i2 = 0
        LineaAttuale = f.readline().replace(" ","")
        if LineaAttuale != "":
            while j != 1 :
                if LineaAttuale[i2] != "=":
                    i2 = i2 + 1
                elif LineaAttuale[i2] == "=":
                    Nomi_linee.append(LineaAttuale[0:int(i2)])
                    j = 1
    f.close()
    return Nomi_linee

def CLinee():
    Chiavi_linee = []
    i = 0
    i2 = 0
    LineaAttuale = "filevuoto"
    NomeChiave = ""
    #directory = os.getcwd().replace("\\", "/") + "/codici.txt"
    f = open("../Base del borgobio/msgcryptor 1.3/codici.txt", 'r')

    while LineaAttuale != "":
        j = 0
        i2 = 0
        LineaAttuale = f.readline().replace(" ", "")
        i = i + 1
        if LineaAttuale != "":
            while j != 1:
                if LineaAttuale[i2] != "=":
                    i2 = i2 + 1
                elif LineaAttuale[i2] == "=":
                    Chiavi_linee.append(LineaAttuale[int(i2) + 1:(len(LineaAttuale))])
                    j = 1
    f.close()
    return(Chiavi_linee)

def encripter(testo,linguaggiodecrypt ):
    Ncicli = 0
    letteraconvertita = ""
    lunghezzatesto = len(testo)
    Nletteraesaminata = 0
    nuovotesto = ""
    Chiave = str(CLinee()[linguaggiodecrypt]).lower()

    for i in range(lunghezzatesto):
        if ord(testo[i]) > 97 and ord(testo[i]) < 123:
            nuovotesto = nuovotesto + Chiave[(ord(testo[i]) - 97)]
        else:
            nuovotesto = nuovotesto + testo[i]
    return nuovotesto


def decripter(testo,linguaggiodecrypt):
    lunghezzatesto = len(testo)
    nuovotesto = ""
    Chiave = str(CLinee()[linguaggiodecrypt]).lower()

    for i in range(lunghezzatesto):
        if ord(testo[i]) > 97 and ord(testo[i]) < 123:
            nuovotesto = nuovotesto + chr(int(Chiave.find(testo[i])) + 97)
        else:
            nuovotesto = nuovotesto + testo[i]

    return nuovotesto

def standardizzatore(Messaggio):
    Messaggio = unidecode.unidecode(Messaggio)
    Messaggio = Messaggio.lower()
    return  Messaggio

def riconoscimentochiave(Chiave):
    NomiChiavi = QNlinee()
    for i in range(len(NomiChiavi)):
        if Chiave.lower() == NomiChiavi[i].lower():
            ChiaveScelta = int(i)
            return ChiaveScelta
            exit()


