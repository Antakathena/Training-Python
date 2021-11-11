import abc
import datetime
from dataclasses import dataclass
# import UIBase non car pb import circulaire, solution : la vue n'a pas à connaitre les controleurs

MENUS_CHOICES = {
    "Menu principal" : ("Menu tournois","Menu joueurs","Menu rapports"),
    "Menu joueurs": ("Entrer un nouveau joueur","Menu des rapports (joueurs)","Retourner au menu principal"),
    "Menu tournois": ("Entrer un nouveau tournoi","Lancer le tournoi","Menu des rapports (tournois)","Retourner au menu principal"),
    "Menu lancer le tournoi": ("Entrer un nouveau tournoi","Lancer le tournoi","Retourner au menu principal"),
    "Menu lancer le round": ("Lancer le round","Retourner au menu principal"),
    "Menu des rapports (joueurs)":("Retourner au menu principal"),
    "Menu des rapports (tournois)":("Retourner au menu principal"),
}

FORMS_FIELDS = {
    "Entrer un nouveau joueur" : (
        "Nom :", 
        "Prénom :",
        "Date de naissance (**/**/****) :",
        "Genre (h/f):",
        "Classement :"),
    "Entrer un nouveau tournoi" : (
        "Nom :",
        "Lieu :", 
        "Date de début (**/**/****):",
        "Date de fin (**/**/****):",
        "Nombre de tours :",
        "Contrôle du temps :", 
        "Description :")
}

class View(abc.ABC):
    """ méthode appelée par un contrôleur, affiche des choses à l'écran, les renvoie au contrôleur"""
    def __init__(self, name):
        self.name = name
        
    def show_title(self):
        title = self.name.upper()
        print(f"-----------{title}-----------")

    @abc.abstractmethod
    def show(self):
        self.show_title()

    def verify_the_answer(self, sollicitation, answer):
        return NotImplementedError
    
      
class Welcome(View):
    def __init__(self, name = "Outil de gestion de tournois d'échecs" ):
        super().__init__(name)

    def show(self):
        super().show()    
        print ("Bienvenue")


class MenuView(View):
    def __init__(self, name, start=1):
        super().__init__(name)
        self.start = start
  
    def show(self):
        super().show()
        choices = MENUS_CHOICES[self.name]
        nbr_of_choices = len(choices)
        for num, choice in enumerate(choices, start= self.start):
            print(f"{num}) {choice}")
        while True :
            answer = input("Votre choix:")
            # on vérifie que l'utilisateur entre une valeur correcte
            try :
                answer = answer.strip()
                len(answer) == 1
                answer.isdigit()
                answer = int(answer)
                print(answer)
            except ValueError :
                print(f"{answer} n'est pas un choix possible.")
                continue
            if answer >= (nbr_of_choices + 1):
                print(f"{answer} ne fait pas partie des choix. Veuillez saisir un chiffre entre 1 et {nbr_of_choices}")
                continue
            else:
                break
        answer = int(answer) - self.start
        # On obtient un int coorespondant à choix -1:
        return answer
                


class FormView(View):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        super().show()
        answer : list = []
        questions = FORMS_FIELDS[self.name]
        
        for question in questions :
            print(question)
            current = input()
            if current == "q":
                break
            while "(**/**/****)" in question:
                try:
                    # faire fonction pour check if birthdate (fichier fonctions et exceptions persos)
                    #  + vérif 1920 <= birthyear <= 2016
                    current = datetime.datetime.strptime(current, "%d/%m/%Y") 
                except ValueError:
                    print("Vous n'avez pas respecté le format de date, veuillez réessayer")
                    print(question)
                    current = input()
                else : 
                    answer.append(current)
                    break
            else :
                answer.append(current)
        self.verify_the_answer(questions,answer)
        return answer

    def verify_the_answer(self, questions,answer : list):
        try :
            assert isinstance(answer,list)
        except ValueError :
            print(f"{answer} n'est pas une liste !")
        try : 
            len(answer) == len(questions)# on vérifie que les types sont respectés
        except AssertionError :
            print(f"Vous n'avez pas répondu à toutes les questions.")
        else :
            print("La liste des réponses est complète.")
            return answer

"""
class UIView(View):
    Determine l'affichage des interfaces utilisateurs : menus et formulaires
    def __init__(self, ui: UIBase.UI):
        super().__init__(ui.name)
        self.ui: UIBase.UI = ui

    def show(self):
        super().show()
        if self.name.startswith("menu"):
            for num, choice in enumerate(self.ui.items, start=self.ui.start):
                print(f"{num}) {choice[0]}")
            selection = input("Votre choix:")
            return selection
        # le else est la vue questionnaire :    
        else : 
            answers = list()
            for question in self.ui.items[0] :
                print(question)
                current = input()
                if current == "q":
                    break
                else :
                    answers.append(current)
            print(answers)
            return answers
"""     
    
class ReportView(View):
    """ Défini comment les infos des rapports apparaissent à l'utilisateur"""
    pass

class PlayerView :
    """ Défini comment les infos sur les joueurs apparaissent à l'utilisateur"""
    # sauf si c'est dans le modèle
    pass

class TournamentView :
    """ Défini comment les infos sur les tournois apparaissent à l'utilisateur"""
    # sauf si c'est dans le modèle
    pass

if __name__ == "__main__":
    print("\n\n----------Essais sur les vues de training ----------")
    
    #welcome = Welcome()
    #welcome.show()

    menu_principal = MenuView("Menu principal")
    menu_principal.show()


    #menu_joueur = MenuView("menu joueurs")
    #menu_joueur.show()

    #new_player_form = FormView("Entrer un nouveau joueur")
    #new_player_form.show()





