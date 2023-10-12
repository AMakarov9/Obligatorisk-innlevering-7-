class Sang(): 
    def __init__(self, tittel: str, artist: str): 
        self.tittel = tittel
        self.artist = artist

    def spill(self): 
        print(f"Nå spilles {self.tittel} med {self.artist} ut til terminalen.")
    
    def sjekk_artist(self, navn: str): 
        if len(navn) <= 1: 
            return False
        
        else: 
            navn = navn.lower().split(" ")
            artistnavn = self.artist.lower().split(" ")
            for i in navn: 
                if i in artistnavn: 
                    return True
            return False
        
    def sjekk_tittel(self, tittel: str): 
        if tittel.lower() == self.tittel.lower(): 
            return True
        else: 
            return False
    
    def sjekk_artist_og_tittel(self, artist: str, tittel: str): 
        titteltest = self.sjekk_tittel(tittel)
        artisttest = self.sjekk_artist(artist)

        if artisttest and titteltest: 
            return True
        else: 
            return False
    
    def streng_til_fil(self):
        string = f"{self.tittel};{self.artist}\n" 
        return string
    
    def __str__(self): 
        string = f"{self.tittel};{self.artist}"
        return string
    
test = Sang("The Next Episode", "Dr. Dre and Snoop Dog")

#print(test.sjekk_artist_og_tittel("boasy", "mug"))
#print(test.sjekk_artist_og_tittel("The Next Episode", "Snoop"))