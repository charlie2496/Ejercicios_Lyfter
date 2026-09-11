
import csv

def main():
    videogames = []
    num_of_videogames = int(input("How many videogames do you want to add? "))  
    for _ in range(num_of_videogames):
        name = input("Enter the videogame name: ")
        genre = input("Enter the genre of the videogame: ")
        developer = input("Enter the developer name of the videogame: ")
        classification_ESRB = input("Enter the ESRB classification of the videogame: ")
        videogames.append({
            "name": name,
            "genre": genre,
            "developer": developer,
            "classification_ESRB": classification_ESRB,
        })

    if videogames:
        with open('videogames_library.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=videogames[0].keys(), delimiter="\t")
            writer.writeheader()
            writer.writerows(videogames)
        print("Videogame library saved to videogames_library.csv")
    else:
        print("No videogames to save.")

if __name__ == '__main__':
    main()


