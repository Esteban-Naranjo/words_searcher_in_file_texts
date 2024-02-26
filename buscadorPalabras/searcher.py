import os
import os.path
import pathlib
from files import Files
from extensions import Extension


class Searcher:
    files = []
    #Constructor de la clase
    def __init__ (self, path: str, word: str):
        self.path = path
        self.word = word

    #Función que recorre un Enum con las extensiones aceptadas por el programa.
    def validate_extension(self, extension):
        for extensions in Extension:
            if (extension == extensions.value):
                return True
        return False
    

    def iterate_files(self):
        directory = pathlib.Path(self.path)
        #Iteración que filtra carpetas, y archivos con diferentes extensiones.
        files = [file for file in directory.iterdir() if file.is_file() and self.validate_extension(file.suffix)]

        #Validación sobre si existen al menos 1 archivo de texto en el fichero
        if len(files)==0:
            raise Exception("La ruta especificada no contiene archivos de texto") 
            
        # Creación de objetos "Archivo" luego de la filtración
        for file in files: 
            self.files.append(Files(file.name, file.read_text()))
            

        return self.files

    #Función que verifica si la ruta es correcta.
    def find_route(self):
        if os.path.exists(self.path):
            try: 
                self.iterate_files()
                return self.total_count()
            except Exception:
                print("Error: No hay archivos de texto en el fichero")
        else:
            print("Error: La ruta especificada no existe")
    
    #Función que recorre los archivos creados. 
    def total_count(self):
        count = 0
        for file in self.files:
            count = count + file.search_word(self.word)
        return print(f"Cantidad total de veces de la palabra en el fichero: {count}")

print("Escriba la ruta deseada:")
path = input()
print("Escriba la palabra a buscar:")
word = input()

#Llamadas de la función con las entradas
searcher = Searcher(path, word)
searcher.find_route()