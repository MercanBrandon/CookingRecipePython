class Recette:

    def __init__(self,recetteAttributes):
        # for attr_name, attr_value in recetteAttributes:
        self._nom = recetteAttributes['nom']
        self._ingredients = recetteAttributes['ingredients']
        self._etapes = recetteAttributes['etapes']
        self.nb_personne = 4
            # setattr(self,attr_name,attr_value)
    
    def _get_nom(self):
        return self.nom

    def _set_nom(self,nom):
        self._nom = nom


    def _get_ingredients(self):
        txt = "Pour réliser vos {} vous aurez besoin de\n".format(self.nom)
        for cle,valeur in self.ingredients.items() :
            txt += "    - {0} : {1}\n".format(cle, valeur )
        return txt
    
    def _set_ingredients(self, ingredients):
        self._ingredients = ingredients
    
    def _get_etapes(self):
        txt = ""
        for etape, i in enumerate(self.etapes) :
            txt += "    {1} - {0}\n".format(i,etape)
        return txt
    
    def _set_etapes(self,etapes):
        self._etapes = etapes

    nom = property(_get_nom,_set_nom)
    ingredients = property(_get_ingredients,_set_ingredients)
    etapes = property(_get_etapes,_set_etapes)

class newRecette:
    def __init__(self,recetteAttributes):
        self.nom = recetteAttributes['nom']
        self.ingredients = recetteAttributes['ingredients']
        self.etapes = recetteAttributes['etapes']
        self.nb_personne = 4
    
    def get_ingredients(self):
        txt = "Pour réliser vos {} vous aurez besoin de\n".format(self.nom)
        for cle,valeur in self.ingredients.items() :
            txt += "    - {0} : {1}\n".format(cle, valeur )
        return txt
    
    def get_etapes(self):
        txt = ""
        for etape, i in enumerate(self.etapes) :
            txt += "    {1} - {0}\n".format(i,etape)
        return txt
# ingredients = {"Pain rassis":1,"Lait":500, "Oeuf": 3, "cannelle" : "A la convenance", "beurre salé":"pour la cuisson"}
# print(type(ingredients))
# etapes =  ["couper le pain en rondelle", "melanger les oeufs, le lait et les epices", "préchauffer l'huile", "faire frire"]
# print(type(etapes))
# recette = Recette("Pain Perdu", ingredients ,etapes)


# print(recette.ingredients)
# print(recette.etapes)