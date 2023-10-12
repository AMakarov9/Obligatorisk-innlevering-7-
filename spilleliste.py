from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
    
    def les_fra_fil(self): 
        fil = open(f"{self._navn}.txt")
        for linje in fil: 
            data = linje.strip().split(";")
            try: 
                self._sanger.append(Sang(data[0], data[1]))
            except: 
                continue
        
    
    def legg_til_sang(self, ny_sang: Sang): 
        self._sanger.append(ny_sang)
    
    def fjern_sang(self, sang: Sang): 
        self._sanger.remove(sang)
    
    def spill_alle(self): 
        for i in self._sanger: 
            i.spill()
    
    def finn_sang_tittel(self, tittel: str): 
        for i in self._sanger: 
            if i.sjekk_tittel(tittel): 
                return i
        return None
    
    def hent_artist_utvalg(self, artistnavn: str): 
        list = []
        for i in self._sanger: 
            if i.sjekk_artist(artistnavn): 
                list.append(i)
        
        return list
    
    def skriv_til_fil(self): 
        fil = open(f"{self._navn}.txt", "w")
        for i in self._sanger: 
            fil.write(f"\n{i.__str__()}")
        fil.close()
        
        
