import functions

messaggio_chiaro="Ci sono voluti diversi tentativi"
messaggio_chiaro="Papà e mamma sono genitori"

key=functions.generate_key(messaggio_chiaro)
#key = "022QTNTXBI2W"
print("CHIAVE DI CIFRATURA: "+key+"\n")

messaggio_cifrato=functions.vernam_cipher(messaggio_chiaro,key)
print(messaggio_cifrato)


messaggio_decifrato = functions.vernam_decipher(messaggio_cifrato, key)
print(messaggio_decifrato)

exit(0)

