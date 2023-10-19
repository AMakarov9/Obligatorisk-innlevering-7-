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
  
    egen = Spilleliste("egen")
    egen.legg_til_sang(Sang("Boasy", "Avelino"))
    egen.legg_til_sang(Sang("Test", "Dave"))
    egen.legg_til_sang(Sang("Testtwo", "LS"))

    mine_spillelister["egen"] = egen
    mine_spillelister["egen"].spill_alle()
hovedprogram()
