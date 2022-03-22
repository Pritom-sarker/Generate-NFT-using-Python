import json
import random
from PIL import Image
import os


def createImage(pathArray,fileName):
    im1 = Image.open(pathArray[0]).convert('RGBA')
    im2 = Image.open(pathArray[1]).convert('RGBA')
    com = Image.alpha_composite(im1, im2)
    for path in range(2,len(pathArray)):
        imgData = Image.open(pathArray[path]).convert('RGBA')
        com = Image.alpha_composite(com, imgData)

    rgb_im = com.convert('RGB')
    rgb_im.save("./img/{}.png".format(fileName))



if __name__ == '__main__':

    try:
        os.rmdir('img')
    except:
        pass

    try:
        os.mkdir('img')
    except:
        pass

    f = open('config.json')
    layers = json.load(f)
    f.close()

    allUniqueHash = []
    baseAddress = './First-Draft/{}/{}'
    numOfImage = 20

    for img in range(0,numOfImage):
        print('Number Of Image: ',img)
        imgPathArray = []
        stringOfImgPath = ''
        for layer in layers:

            imgFileName = random.choices(layers[layer][0]['name'], layers[layer][0]['weight'])[0]
            imgPathArray.append(baseAddress.format(layer,imgFileName))
            stringOfImgPath+=layer+imgFileName

        if hash(stringOfImgPath) in allUniqueHash:
            print('Same! Img')
            continue
        else:
            allUniqueHash.append(hash(stringOfImgPath))

        createImage(imgPathArray,img)



