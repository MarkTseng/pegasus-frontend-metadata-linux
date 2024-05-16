from xml.etree.ElementTree import Element, SubElement, Comment
from xml.etree import ElementTree
from xml.dom import minidom

from os import listdir
from os.path import isfile, isdir, join
import os, fnmatch

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

# add game information
def addGame(game, xml_tag, text):
    xml_tag = SubElement(game, xml_tag)
    xml_tag.text = str(text)

def generateGameListXML(metadataPath):
    # create xml tree
    gameList = Element('gameList')
    comment = Comment('metadata to gamelist.xml')
    gameList.append(comment)

    # parse metadata file
    metadataFile = open(metadataPath)
    print(metadataPath)
    for line in metadataFile.readlines():
        if line != "\n":
            if line.split(": ")[0] == "game":
                game = Element('game')
                gameList.append(game)
                addGame(game, "name", line.split(": ")[1][:-1])
            if line.split(": ")[0] == "file":
                name = line.split(": ")[1][:-5]
                PathName = line.split(": ")[1][:-1]
                imagePath = f"./media/{name}/boxFront.png"
                videoPath = f"./media/{name}/video.mp4"
                curPathName = f"./{PathName}"
                addGame(game, "path", curPathName)
                addGame(game, "image", imagePath)
                addGame(game, "video", videoPath)
            if line.split(": ")[0] == "description":
                addGame(game, "desc", line.split(": ")[1][:-1])
            if line.split(": ")[0] == "developer":
                addGame(game, "developer", line.split(": ")[1][:-1])
    metadataFile.close()

    # output xml string
    #print(prettify(gameList))
    gameListPath = os.path.dirname(metadataPath) + '/gamelist.xml'
    f = open(gameListPath, 'w')
    f.write(prettify(gameList))
    f.close()

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

# main loop
if __name__ == '__main__':
    # list metadata folders
    metadataList = find('metadata.pegasus.txt', 'metadata')
    print(metadataList)
    for metadata in metadataList:
        generateGameListXML(metadata)
