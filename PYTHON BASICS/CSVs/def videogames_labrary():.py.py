
import csv

def main():
    videogames = []
    while True:
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

        cont = input("Do you want to add another videogame? (y/n): ").strip().lower()
        if cont == 'n':
            print("Thank you for using the videogame library!")
            break
        if cont != 'y':
            print("Please enter a valid option (y/n). Assuming 'n'.")
            break

    if videogames:
        with open('videogames_library.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=videogames[0].keys())
            writer.writeheader()
            writer.writerows(videogames)
        print("Videogame library saved to videogames_library.csv")
    else:
        print("No videogames to save.")

if __name__ == '__main__':
    main()


