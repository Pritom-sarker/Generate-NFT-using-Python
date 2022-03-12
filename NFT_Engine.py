import os
import glob
import shutil
import random
from PIL import Image

def createLayerConfig(folder_name):
    files = glob.glob('./{}/*/*.png'.format(folder_name))
    layer_data = []
    layers = []
    for file in files:
        temp = file.split('/')
        if temp[2] not in layers:
            layers.append(temp[2])
        layer_data.append([temp[2], file, (str(temp[-1]).split('#')[-1][:-4])])

    final_file = {}
    for layer in layers:
        files = []
        weight = []
        for data in layer_data:
            if layer in data:
                files.append(data[1])
                weight.append(int(data[2]))

        final_file[layer] = [files, weight]

    return final_file

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

    # Put Layer names in sequence
    layers = ['Base','Belly','Color','Pattern',"Ring"]
    try:
        shutil.rmtree('img')
    except:
        pass

    try:
        os.mkdir('img')
    except:
        pass




    layers_data = createLayerConfig('First-Draft')
    allUniqueHash = []
    numOfImage = 5000
    img = 0
    layers = ['Base','Belly','Color','Pattern',"Ring"]
    for num in range(0,numOfImage):
        for key, value in layers_data.items():
            # try:
                img+=1
                print('Number Of Image: ', img)
                imgPathArray = []
                stringOfImgPath = ''
                for layer in layers:
                    weight = list(layers_data[layer][1])
                    files = list(layers_data[layer][0])
                    imgFileName = random.choices(files, weight,k=len(weight))[0]
                    imgPathArray.append(imgFileName)
                    stringOfImgPath +=  imgFileName
                    print(imgFileName)

                if hash(stringOfImgPath) in allUniqueHash:
                    print('Same! Img')
                    continue
                else:
                    allUniqueHash.append(hash(stringOfImgPath))
                #createImage(imgPathArray, img)
            # except:
            #     print("error!!")


