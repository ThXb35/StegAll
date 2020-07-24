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



print("")
option = input("Select an option : ")
print("")

#We display the picture
if option == "1":
    os.system("ristretto " + path)

elif option == "2":

    print("")
    print ("\033[31mExiftool\033[0m")
    print("")
    os.system("exiftool " + path + " | grep File")
    os.system("exiftool " + path + " | grep MIME")
    os.system("exiftool " + path + " | grep Encoding")
    os.system("exiftool " + path + " | grep Thumbnail")
    os.system("exiftool " + path + " | grep Comment")

    print("")
    print ("\033[31mFile\033[0m")
    print("")
    os.system("file " + path)

    print("")
    print ("\033[31mBinwalk\033[0m")
    print("")
    os.system("binwalk " + path)

    print("")
    print ("\033[31mForemost\033[0m")
    print("")
    os.system("rm -r output")
    os.system("foremost " + path)

elif option == "3":

    print("")
    print ("\033[31mExiftool\033[0m")
    print("")
    os.system("exiftool " + path + " | grep File")
    os.system("exiftool " + path + " | grep MIME")
    os.system("exiftool " + path + " | grep Encoding")
    os.system("exiftool " + path + " | grep Thumbnail")
    os.system("exiftool " + path + " | grep Comment")

    print("")
    print ("\033[31mFile\033[0m")
    print("")
    os.system("file " + path)

    print("")
    print ("\033[31mBinwalk\033[0m")
    print("")
    os.system("binwalk " + path)

    print("")
    print ("\033[31mForemost\033[0m")
    print("")
    os.system("rm -r output")
    os.system("foremost " + path)

    print("")
    print ("\033[31mSteghide\033[0m")
    print("")
    os.system("steghide extract -sf " + path)
