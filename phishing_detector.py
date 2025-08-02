# phishing_detector.py
# Script principal pour détecter des messages potentiellement frauduleux (phishing)

import re  # Import de re (non utilisé ici, mais prévu pour de futures améliorations)

def is_phishing(text):
    suspicious_keywords = [
        "urgent", "verify", "click here", "update", "password",
        "bank", "account", "login", "confirm", "limited time", "security alert"
    ]

    text = text.lower()  # Mise en minuscules pour la recherche
    matches = [kw for kw in suspicious_keywords if kw in text]  # Recherche des mots-clés

    if matches:
        print("🔒 Phishing détecté ! Mots suspects trouvés :", ", ".join(matches))
        return True
    else:
        print("✅ Aucun signe clair de phishing.")
        return False


def main():
    print("=== Détecteur de phishing ===\n")
    user_input = input(" Collez ici le texte d'un email ou message à analyser :\n\n> ")
    print("\n Analyse en cours...\n")
    is_phishing(user_input)


if __name__ == "__main__":
    main()
