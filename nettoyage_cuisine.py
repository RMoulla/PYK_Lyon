# Correction des caractères de la variable idtypecuisine

def nettoyer_cuisine(x):

   """
    Nettoie une chaîne de caractères contenant des erreurs d'encodage simples.

    Cette fonction :
    - remplace le motif '√©' par 'é',
    - transforme la valeur '0' en 'categorie_0',
    - transforme la valeur '-1' en 'categorie_1',
    - retourne la valeur inchangée si aucune condition n'est remplie.

    Paramètres
    ----------
    x : any
        Valeur à nettoyer (chaîne de caractères ou autre type).

    Retour
    ------
    str ou any
        Chaîne corrigée si x est une chaîne, sinon valeur inchangée.
    """
   if x == "-1":
      return "categorie_1"

   if x == "0":
      return "categorie_0"

   if "√©" in x:
      return x.replace("√©", "é")

   else:
      return x
