import tkinter as tk
from tkinter import messagebox


def ask_question(question):
    return messagebox.askyesno("Question", question)


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    custom_font = ("Helvetica", 24)  # Change the font and size as needed

    character = ""

    if ask_question("Is your character a boy?"):
        if ask_question("Does he wear spectacles?"):
            if ask_question("Does he get scolded in class frequently?"):
                if ask_question("Does he usually wear shirts?"):
                    if ask_question("Does he invest in the stock market?"):
                        if ask_question("Does he have a cat?"):
                            character = "Raihan"
                        else:
                            character = "Ganesh"
                    else:
                        if ask_question("Good at driving? (lol)"):
                            character = "Vedant Shetty"
                        else:
                            if ask_question("Does he live in Nerul?"):
                                if ask_question("Chamdi No 17?"):
                                    character = "Aditya Chaskar"
                                else:
                                    character = "Akshar Pawar"
                else:
                    if ask_question("Does he invest in the stock market?"):
                        if ask_question("Does he have a cat?"):
                            character = "Raihan"
                        else:
                            character = "Vedant Shetty"
                    else:
                        if ask_question("Good at driving cars?"):
                            character = "Vedant Shetty"
                        elif ask_question("Is he good at video games?"):
                            if ask_question("Does he sleep in class?"):
                                character = "Anish Masurkar"
                            else:
                                character = "Nidhish"

                        else:
                            if ask_question("Does he live in Nerul?"):
                                character = "Aditya Chaskar"
                            else:
                                if ask_question("Alibaug?"):
                                    character = "Manthan"
            else:
                if ask_question("Is he good at football?"):
                    character = "Soham Desai"
                else:
                    if ask_question("Is he really good at mathematics?"):
                        character = "Ashish!"
                    else:
                        if ask_question("Constant hairstyle since sem 1?"):
                            if ask_question("Ladies?"):
                                character = "Vedant Patil"
                            else:
                                character = "Vedant Borade"


        #non chashma
        else:
            if ask_question("Does he get scolded in class usually?"):
                if ask_question("Does he wear shirts frequently?"):
                    if ask_question("Does he have a beard?"):
                        if ask_question("Kashmir?"):
                            character = "Aditya Dogra"
                        else:
                            if ask_question("Is he into Video editing?"):
                                character = "Amruthesh"
                            elif ask_question("Hairline?"):
                                character = "Sohail"
                            elif ask_question("Fufu?"):
                                character = "Soham Chumbale"
                            elif ask_question("Niggeshwar?"):
                                character = "Tarun"


                    else:
                        if ask_question("Fufu?"):
                            character = "Danny"
                        else:
                            if ask_question("Does he go to gym?"):
                                if ask_question("Is he good at football?"):
                                    if ask_question("Is he known for his hair?"):
                                        character = "Aryan"
                                else:
                                    character = "Nangare"
                else:
                    if ask_question("Is he good at football?"):
                        if ask_question("Is he known for his hair?"):
                            character = "Aryan"
                        else:
                            if ask_question("South Indian?"):
                                character = "Dipesh"
                            else:
                                character = "Abaan"
                    else:
                        if ask_question("Is he into PC games?"):
                            if ask_question("Is he into Video editing?"):
                                character = "Amruthesh"
                            else:
                                if ask_question("Does he have a beard?"):
                                    character = "Saad"
                                else:
                                    character = "Suraj"
                        else:
                            if ask_question("Good Ball Knowledge?"):
                                character = "Atharva Nangu"
                            else:
                                character = "Anish Kharat"
            else:
                    if ask_question("Does he have good ball knowledge?"):
                        if ask_question("Does he help everyone with assignments?"):
                            character = "Sameer"
                        else:
                            if ask_question("Does he have a beard?"):
                                character = "Sai"
                            else:
                                character = "Atharva"
                    else:
                        if ask_question("Does he usually wear shirts?"):
                            if ask_question("Is he good in academics?"):
                                if ask_question("Is he in the college Drama team?"):
                                    character = "Sujit Asari"
                                else:
                                    if ask_question("Interest in camera?"):
                                        if ask_question("Kerala?"):
                                            character = "Amruthesh"

                                    else:
                                        if ask_question("Autistic?"):
                                            character = "Uday"
                                        else:
                                            if ask_question("Constant hairstyle since Sem 1?"):
                                                if ask_question("Good at chess?"):
                                                    if ask_question("Nepali Eyes?"):
                                                        character = "Siddhesh"
                                                    else:
                                                        character = "Hrishikesh"

                                                elif ask_question("Is he good at basketball?"):
                                                    character = "Abhishek"
                                                else:
                                                    character = "Vedant Borade"
                            else:
                                if ask_question("Niggeshwar?"):
                                    character = "Tarun"
                                else:
                                    character = "Aditya Venkat"
                        else:
                            if ask_question("Is he involved in any college clubs?"):
                                if ask_question("Is he south Indian?"):
                                    character = "Aditya Venkat"
                            else:
                                if ask_question("Is he good at basketball?"):
                                    character = "Abhishek"
                                else:
                                    if ask_question("Fish??"):
                                        character = "Pravanshu"
                                    else:
                                        if ask_question("Good in academics?"):
                                            if ask_question("Has helped everyone with assignments?"):
                                                if ask_question("Good ball knowledge?"):
                                                    character = "Sameer"
                                            else:
                                                if ask_question("Interest in camera?"):
                                                    if ask_question("Kerala?"):
                                                        character = "Amruthesh"
                                                    else:
                                                        if ask_question("Diploma?"):
                                                            character = "Harsh Patil"
                                                        else:
                                                            character = "Sahil Pawar"
                                                else:
                                                    if ask_question("EEEEEEE?"):
                                                        character = "Vishvesh"
                                                    else:
                                                        if ask_question("Is he autistic?"):
                                                            character = "Uday"
                                                        else:
                                                            if ask_question("Good in Cricket?"):
                                                                character = "Anish Kharat"
                                                            else:
                                                                character = "Hrishikesh"
                                        else:
                                            if ask_question("Is he an upcoming worlwide artist?"):
                                                character = "Krishna"
    else:
        if ask_question("Does she wear spectacles?"):
            if ask_question("Is she in any college clubs?"):
                if ask_question("Does she go to the gym?"):
                    character = "Kavya"
                else:
                    if ask_question("Is she good in academics?"):
                        if ask_question("Extrovert?"):
                            if ask_question("Good in singing?"):
                                if ask_question("Is she in the college choir team?"):
                                    character = "Janaki"
                                else:
                                    if ask_question("Airoli?"):
                                        character = "Vedshri"
                            else:
                                if ask_question("Airoli?"):
                                    character = "Vedshri"
                                else:
                                    character = "Arya"

                        else:
                            if ask_question("Is she in the college choir team?"):
                                character = "Janaki"
                            else:
                                if ask_question("Airoli?"):
                                    character = "Vedshri"
            else:
                if ask_question("Is she good in academics?"):
                    if ask_question("Khopoli?"):
                        character = "Ketki"
                    else:
                        character = "Aastha"
                else:
                    if ask_question("Gujju?"):
                        character="Hirtika"
                    else:
                        character="Bhavika"
        else:
            if ask_question("Is she in any college clubs?"):
                if ask_question("is she known for singing?"):
                    if ask_question("Is she good in academics?"):
                        if ask_question("Extrovert?"):
                            character = "Shruti"
                else:
                    character = "Archi"
            else:
                if ask_question("Does she have a pet cat?"):
                    character = "Fareen"
                else:
                    if ask_question("is she good in academics?"):
                        if ask_question("Helps Everyone With Her Notes?"):
                            character = "Pratiksha"
                        else:
                            character = "Anannya"
                    else:
                        character = "Alina"

    if character:
        messagebox.showinfo("Result", f"You are thinking of {character}!")
    else:
        messagebox.showinfo("Result", "No character matched the criteria!")

if __name__ == "__main__":
    main()

