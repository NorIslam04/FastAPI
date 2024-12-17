import pymysql

# Configuration de la connexion
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "islam",
}

# Définition de la classe Etudiant
class Etudiant:
    def __init__(self, id, nom, prenom, point):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.point = point
    
    def __str__(self):
        return f"ID: {self.id}, Nom: {self.nom}, Prénom: {self.prenom}, Point: {self.point}"

def etablir_connexion():
    try:
        connection = pymysql.connect(**config)
        print("Connexion réussie avec PyMySQL !")
        return connection
    except pymysql.MySQLError as e:
        print(f"Erreur de connexion MySQL : {e}")
        return None

def selectionner_base_de_donnees(cursor, nom_base):

    try:
        cursor.execute(f"USE {nom_base}")
        return True
    except pymysql.MySQLError as e:
        print(f"Erreur lors de la sélection de la base de données : {e}")
        return False

def recuperer_etudiants():
    # Liste pour stocker les étudiants
    liste_etudiants = []
    
    # Établir la connexion
    connection = etablir_connexion()
    if not connection:
        return liste_etudiants
    
    try:
        # Créer un curseur pour exécuter des requêtes SQL
        with connection.cursor() as cursor:
            # Sélectionner la base de données
            if not selectionner_base_de_donnees(cursor, "hotel"):
                return liste_etudiants
            
            # Récupérer tous les étudiants
            cursor.execute("SELECT * FROM etudiants")
            resultats = cursor.fetchall()
            
            # Créer des objets Etudiant et les ajouter à la liste
            for resultat in resultats:
                etudiant = Etudiant(
                    id=resultat[0],
                    nom=resultat[1],
                    prenom=resultat[2],
                    point=resultat[3]
                )
                liste_etudiants.append(etudiant)
            
            # Affichage des étudiants
            afficher_etudiants(liste_etudiants)
            
            return liste_etudiants
    
    except pymysql.MySQLError as e:
        print(f"Erreur MySQL lors de la récupération des étudiants : {e}")
        return liste_etudiants
    except Exception as ex:
        print(f"Une erreur inattendue est survenue : {ex}")
        return liste_etudiants
    finally:
        # Fermer la connexion
        if connection:
            connection.close()

def afficher_etudiants(etudiants):
    print("Liste des étudiants :")
    for etudiant in etudiants:
        print(etudiant)
