import os
import glob



if __name__ == '__main__':
    files = glob.glob('./First-Draft/*/*.png')
    layer_data = []
    layers = []
    for file in files:
        temp = file.split('/')
        if temp[2] not in layers:
            layers.append(temp[2])
        layer_data.append([temp[2],file,(str(temp[-1]).split('#')[-1][:-4])])

    final_file = {}
    for layer in layers:
        files = []
        weight = []
        for data in layer_data:
            if layer in data:
                files.append(data[1])
                weight.append(data[2])

        final_file[layer] = [files,weight]

