from sang import Sang
from spilleliste import Spilleliste
def hovedprogram(): 
    mine_spillelister = {}

    musikk = Spilleliste("musikk")
    musikk.les_fra_fil()
    mine_spillelister["musikk"] = musikk
    
    queen = Spilleliste("queen")
    #for i in musikk.hent_artist_utvalg("Queen"):
        #queen.legg_til_sang(i)
    queen.les_fra_fil()
    mine_spillelister["queen"] = musikk
    

    mine_spillelister["queen"] = queen
    #mine_spillelister["queen"].skriv_til_fil()
    mine_spillelister["queen"].legg_til_sang(Sang("Bigman thing", "Queen"))
    print(mine_spillelister["queen"].finn_sang_tittel("Bigman thing"))
    mine_spillelister["queen"].spill_alle()
  
hovedprogram()
