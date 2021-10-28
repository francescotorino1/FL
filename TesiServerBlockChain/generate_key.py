from cryptography.fernet import Fernet


def write_key():
    # GENERO LA CHIAVE E LA SALVO IN UN FILE
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    # CARICO LA CHIAVE DAL FILE
    return open("key.key", "rb").read()

if "__name__" == "__main__":
    
	"""
	    SCRIPT DI TEST CHE GENERA UNA CHIAVE, LA SALVA IN UN
	    FILE CON ESTENSIONE .KEY, CRIPTA UNA STRINGA, LA STAMPA
	    ED INFINE LA DECRIPTA MOSTRANDO LA STRINGA ORIGINALE DI PARTENZA
	"""

	# GENERO IL FILE CON LA CHIAVE
	write_key()

	# CARICO LA CHIAVE DAL FILE
	key = load_key()

	# STRINGA CHE VOGLIO CRIPTARE
	message = "Messaggio di prova, Hello World !".encode()

	# CREO UNA ISTANZA DELLA CLASSE FERNET
	f = Fernet(key)

	# CRIPTO IL MESSAGGIO E LO STAMPO
	encrypted = f.encrypt(message)
	print(f"\nLa stringa criptata vale: {encrypted}")

	# DECRIPTO IL MESSAGGIO E LO STAMPO
	decrypted_encrypted = f.decrypt(encrypted)
	print(f"\nLa stringa decriptata vale: {decrypted_encrypted}")
