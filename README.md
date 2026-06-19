# 🔐 Générateur de Mots de Passe Sécurisés (Python)

Une application console en Python permettant de générer des mots de passe robustes et aléatoires. Ce projet a été conçu pour mettre en pratique la gestion des variables d'environnement secrètes et le flux de travail avec Git et GitHub.

## 🚀 Fonctionnalités
* **Génération sécurisée :** Création de mots de passe hautement sécurisés combinant lettres (majuscules/minuscules), chiffres et caractères spéciaux.
* **Sécurisation par variable d'environnement :** L'application utilise une clé maître (`SECRET_KEY`) stockée de manière hermétique dans un fichier `.env`, totalement invisible sur GitHub grâce au fichier `.gitignore`.

## 🛠️ Prérequis et Installation

1. **Cloner le dépôt sur votre machine :**
   ```bash
   git clone [https://github.com/emmanuelbagin-eng/generateur-pass-git.git](https://github.com/emmanuelbagin-eng/generateur-pass-git.git)
   cd generateur-pass-git