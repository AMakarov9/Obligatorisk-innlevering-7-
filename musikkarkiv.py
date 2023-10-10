from sang import Sang
from spilleliste import Spilleliste
def hovedprogram(): 
    mine_spillelister = {}

    musikk = Spilleliste("musikk")
    musikk.les_fra_fil()
    mine_spillelister["musikk"] = musikk
    
    queen = Spilleliste("queen")

    for i in musikk.hent_artist_utvalg("Queen"):
        queen.legg_til_sang(i)
   
    mine_spillelister["queen"] = queen
    mine_spillelister["queen"].skriv_til_fil()



hovedprogram()
