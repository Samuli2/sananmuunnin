# CT30A3300 Käyttöjärjestelmät ja ekosysteemit 
# codecamp 2
# Samuli Siitonen, Johannes Ruuni, Vilma Parkkila, Mia Kouhia

print(25 * "=")

while True:
	sana = input("Anna sana (0 = lopetus): ")  # Muokattava sana.

	# Jos halutaan lopettaa.
	if(sana == "0"):
		break

	# MUU RYHMÄ: KEKSIKÄÄ LISÄÄ TOIMINTOJA
	print("\nMitä tehdään?\n1) Isot kirjaimet\n2) Pienet kirjaimet\n3) Sana väärinpäin\n4) Iso etukirjain")


	valinta = int(input("Valintasi: "))  # Valinta valikkoon perustuen.

	# Tehdään toimintoja käyttäjän valintaan perustuen. 
	if(valinta == 1):
		sana = sana.upper()	
	elif(valinta == 2):
		sana = sana.lower()
	elif(valinta == 3):
		sana = sana[::-1]
	elif(valinta == 4):
		sana = sana.capitalize()
	else:
		print("Vireellinen valinta.")

	print("\nSanasi on nyt: ", end="")
	print(sana)	
	print(25 * "=")

print("Kiitos ohjelman käytöstä.")
	






