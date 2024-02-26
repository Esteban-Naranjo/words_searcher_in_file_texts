class Files: 

    counter = 0

    def __init__ (self, name: str, content: str):
        self.name = name 
        self.content = content

    #Función que separa un string en palabras, la limpia de carácteres especiales y cuenta la cantidad de coincidencias de una palabra dada
    def search_word(self, word):
        specialChars = ["(", ",", ")", "."]
        words_list = self.content.split()

        for w in words_list:
            for specialChar in specialChars:
                w = w.replace(specialChar, "")

            if w == word:
                self.counter = self.counter + 1
        print(f"La palabra '{word}' aparece {self.counter} veces en el archivo {self.name}.")
        return self.counter


    

        