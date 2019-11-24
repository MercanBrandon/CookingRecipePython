import recettes
import pymongo
import json

class RecetteManager():

    # mongoClient = pymongo.MongoClient("mongodb://appPython:brandonhitema@81.64.214.104:27018/")
    mongoClient = pymongo.MongoClient("mongodb://localhost:27018/")
    recetteDB = mongoClient["recette2"]
    recetteCol = recetteDB["recette"]

    # print(mongoClient.list_database_names())
    # def __init__(self,)

    def saveRecette(self, recette):
        # if isinstance(recettes.Recette)
        s = recette.__dict__
        # s = json.dumps(s)
        RecetteManager.recetteCol.insert_one(s)
    
    def getAllRecettes(self):
        recettes = RecetteManager.recetteCol.find({},{"_id":0})
        for rec in recettes:
            print(rec)
            # recette = recettes.newRecette(rec)
            # return recette
    
    def getRecetteByName(self, nom):
        # dictRecettes = json.loads(RecetteManager.recetteCol.find({"_nom" : nom},{"_id":0}))
        # print(dictRecettes)
        attribute = {"nom" : "", "ingredients" : {}, "etapes" : []}
        recette = recettes.newRecette(attribute)
        recette.__dict__ = json.loads(RecetteManager.recetteCol.find({"_nom" : nom},{"_id":0}))
        print(recette.__dict__)
        # return recette

    def nouvelleRecette(self):
        nom = input("Entrez le nom de votre recette :")
        
        input("pour ajouter un ingredient appuyez sur 'A' une fois vos ajouts terminés appuyez sur Entrée")
        arrayIngredients = []
        item = "a"
        while item != "":
            item = input(">>")
            if item != "" : arrayIngredients.append(item)
        
        dictIngredients = {}
        
        for ingredient in arrayIngredients:
            qty = input("Combien de {0} voulez vous ".format(ingredient))
            dictIngredients[ingredient] = qty
        
        input("pour ajouter une étape appuyez sur 'A' une fois vos ajouts terminés appuyez sur Entrée")
        etapes = []
        etape = "a"
        while etape != "":
            etape = input(">>")
            if etape != "" : etapes.append(etape)

        dictRecette = {"nom" : nom, "ingredients" : dictIngredients, "etapes" : etapes}

        nouvelleRecette = recettes.newRecette(dictRecette)
        self.saveRecette(nouvelleRecette)



        


ingredients = {"Pain rassis":1,"Lait":500, "Oeuf": 3, "cannelle" : "A la convenance", "beurre salé":"pour la cuisson"}
etapes =  ["couper le pain en rondelle", "melanger les oeufs, le lait et les epices", "préchauffer l'huile", "faire frire"]
# recette = recettes.Recette({"nom" : "Pain Perdu","ingredients" : ingredients ,"etapes" : etapes})

recetteManager = RecetteManager()
# recetteManager.getRecetteByName("crepes")
recetteManager.nouvelleRecette()

# recetteManager.saveRecette(recette)
# recetteManager.getAllRecettes()