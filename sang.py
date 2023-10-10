class Sang(): 
    def __init__(self, tittel: str, artist: str): 
        self.tittel = tittel.lower()
        self.artist = artist.lower()

    def spill(self): 
        print(f"Nå spilles {self.tittel} med {self.artist} ut til terminalen.")
    
    def sjekk_artist(self, navn: str): 
        if len(navn) <= 1: 
            return False
        
        else: 
            navn = navn.lower().split(" ")
            for i in navn: 
                if i == self.artist: 
                    return True
            return False
        
    def sjekk_tittel(self, tittel: str): 
        if tittel.lower() == self.tittel: 
            return True
        else: 
            return False
    
    def sjekk_artist_og_tittel(self, artist: str, tittel: str): 
        artisttest = self.sjekk_tittel(artist)
        titteltest = self.sjekk_tittel(tittel)
        if artisttest and titteltest: 
            return True
        else: 
            return False
    
    def streng_til_fil(self):
        string = f"{self.tittel};{self.artist}\n" 
        return string
    
    def __str__(self): 
        string = f"{self.tittel} med {self.artist}"
        return string
    