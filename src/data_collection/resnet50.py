from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

def predict(img_paths):
    model = ResNet50(weights='imagenet')
    m = len(img_paths)
    predictions = [None]*m
    count = 0
    for i in img_paths:
        print("load file: ", str(i))
        try:
            img = image.load_img(i, target_size=(224, 224))
            img = image.img_to_array(img)
            x = np.expand_dims(img, axis=0)
            x = preprocess_input(x)
            preds = model.predict(x)
            preds = decode_predictions(preds, top=3)[0]
            predictions[count] = preds
            count+=1
        except:
            count+=1
            continue
            
    return predictions

if __name__=="__main__":
    import os
    pathlist = os.listdir('data_grab')
    count = 0
    for i in pathlist:
        pathlist[count] = os.path.join('data_grab', pathlist[count])
        count+=1
    predictions = predict(pathlist)
    '''
    predictions[0]
    [('n04447861', 'toilet_seat', 0.87126261), ('n04179913', 'sewing_machine', 0.027522231), ('n15075141', 'toilet_tissue', 0.020023976)]
    '''    
