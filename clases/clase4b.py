nombre = input("Cual es tu nombre? ").lower()
team =  input("Marvel o Capcom? ")
team = team.upper()
if (team == "marvel" and nombre < "m") or (team == "Capcom" and nombre > "n"):
    grupo = "A"
else:
    grupo = "B"
print("Sos grupo: " + grupo)




