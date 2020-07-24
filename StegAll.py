# Create by Thxb35 :)
# A small script gathering the most powerful Steganography software.

import os

print ("\033[34mThis is blue\033[0m") # Affiche "This is blue" en bleu, faut modifier le chiffre 34 par un autre nombre pour changer la couleur
print("###############################################################");
print("");
print(" $$$$$$\    $$\                          $$$$$$\  $$\ $$\ ");
print("$$  __$$\   $$ |                        $$  __$$\ $$ |$$ | ");
print("$$ /  \__|$$$$$$\    $$$$$$\   $$$$$$\  $$ /  $$ |$$ |$$ |  ");
print("\$$$$$$\  \_$$  _|  $$  __$$\ $$  __$$\ $$$$$$$$ |$$ |$$ | ");
print(" \____$$\   $$ |    $$$$$$$$ |$$ /  $$ |$$  __$$ |$$ |$$ | ");
print("$$\   $$ |  $$ |$$\ $$   ____|$$ |  $$ |$$ |  $$ |$$ |$$ | ");
print("\$$$$$$  |  \$$$$  |\$$$$$$$\ \$$$$$$$ |$$ |  $$ |$$ |$$ | ");
print(" \______/    \____/  \_______| \____$$ |\__|  \__|\__|\__| ");
print("                              $$\   $$ | ");
print("                              \$$$$$$  | ");
print("                               \______/  ");
print("");
print("Created by Thibault H.");
print("###############################################################");


path = input("Please enter the absolute path of the image to be analyzed ");

print("1. Display the picture")
print("2. Analyze the picture")
print("3. Analyze the picture with a password")
print("4. Analyze the picture with a text to search")
print("5. Apply color filters to the picture")
print("6. Display the binary and hexadecimal of the picture")




def analyse(path1):

    print("")
    print ("\033[31mExiftool\033[0m")
    print("")
    os.system("exiftool " + path1 + " | grep File")
    os.system("exiftool " + path1 + " | grep MIME")
    os.system("exiftool " + path1 + " | grep Encoding")
    os.system("exiftool " + path1 + " | grep Thumbnail")
    os.system("exiftool " + path1 + " | grep Comment")

    print("")
    print ("\033[31mFile\033[0m")
    print("")
    os.system("file " + path1)

    print("")
    print ("\033[31mBinwalk\033[0m")
    print("")
    os.system("binwalk " + path1)

    print("")
    print ("\033[31mForemost\033[0m")
    print("")
    os.system("rm -r output")
    os.system("foremost " + path1)



print("")
option = input("Select an option : ")
print("")

#We display the picture
if option == "1":

    os.system("ristretto " + path)

elif option == "2":

    analyse(path)

elif option == "3":

    analyse(path)

    print("")
    print ("\033[31mSteghide\033[0m")
    print("")
    os.system("steghide extract -sf " + path)

elif option == "4":

    analyse(path)

    string = input("What text do you want to search ? ")

    print("")
    print ("\033[31mStrings\033[0m")
    print("")
    os.system("strings " + path + " | grep " + string)

elif option == "5":

    print("You just have to oppen the picture that you want in the java window")
    os.system("java -jar stegsolve.jar " + path)

elif option == "6":

    os.system("ghex " + path)
