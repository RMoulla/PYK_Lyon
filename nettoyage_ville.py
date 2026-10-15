# Correction des caractères de la variable ville

def nettoyer_ville(x):

    if isinstance(x, str):

        if "√®" in x:
            x = x.replace("√®", "è")

        if "√©" in x:
            x = x.replace("√©", "é")

        if "√â" in x:
            x = x.replace("√â", "É")

        return x

    else:
        return x
