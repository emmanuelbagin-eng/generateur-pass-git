import os
import random
import string
# On importe l'outil pour lire le fichier .env
from dotenv import load_dotenv

# On charge les variables du fichier .env
load_dotenv()

# On récupère notre variable secrète
cle_secrete = os.environ.get("SECRET_KEY")

print("--- Générateur de Mots de Passe Sécurisés ---\n")

# Petite vérification de sécurité
if not cle_secrete:
    print("❌ Erreur : La variable SECRET_KEY est introuvable. Vérifie ton fichier .env !")
else:
    # On génère un mot de passe aléatoire
    longueur = 16
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = "".join(random.choice(caracteres) for i in range(longueur))
    
    print("🔒 Application déverrouillée avec succès.")
    print(f"✨ Ton nouveau mot de passe sécurisé : {mot_de_passe}")