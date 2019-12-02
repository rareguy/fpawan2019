from pytube import YouTube
import os

def checkIfDuplicates(elem, listOfElems): 
    if elem in listOfElems:
        return True
    return False

link = YouTube("https://www.youtube.com/watch?v=2ZIpFytCSVc")

thetitle = link.title
print(thetitle)
stream = link.streams.all()
print("What format do you want the download?")
print("Available downloads:")
list_of_media = []
counter = 1
for available in stream:
    if available.resolution:
        temp = {
                "id" : str(counter),
                "resolution" : available.resolution,
                "format" : available.mime_type
            }
    if not checkIfDuplicates(temp, list_of_media):
        list_of_media.append(temp)
    counter += 1
    
for i in list_of_media:
    print(i["id"] +  ". type " + i["format"] + " resolution " + i["resolution"])

choose = input("your choice >> ")
try:
    choice = int(choose)
    stream[choice-1].download()
except:
    print("Error parsing input")