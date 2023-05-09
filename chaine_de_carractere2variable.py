nom=(input ("entrer nom"))
postnom=(input("entrer postnom"))
prenom=(input("entrer prenom"))
age=int(input("entrer age"))
if age <18:
   print(f"bonjour{nom}{postnom} {prenom} vous etes mineur")
else:      
  print(f"bojour{nom}{postnom} {prenom} vous avez {age}ans")
if age >=18 and age <50 : 
    print(f"bonjour{nom}{postnom} {prenom} vous etes jeune")

elif age >100 :# precision de l age au de la de 50 ans ici  la personne est majeur  
    print(f"bonjour{nom}{postnom} {prenom} vous etes jeune")
 