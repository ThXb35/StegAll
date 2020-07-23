# Create by Thxb35 :)
# A small script gathering the most powerful Steganography software.

import os

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

print("")
option = input("Select an option : ")
print("")

#We display the picture
if option == "1":
    os.system("ristretto " + path)

elif option == "2":
    print("Exiftool : ")
    print("")
    os.system("exiftool " + path + " | grep File")
    os.system("exiftool " + path + " | grep MIME")
    os.system("exiftool " + path + " | grep Encoding")
        os.system("exiftool " + path + " | grep Thumbnail")
