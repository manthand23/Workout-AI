import numpy as np
import os
from keras_preprocessing import image
from keras.models import load_model

class ImageAnalysis: 
    def __init__(self, unknown_images_path_file):
        self.unknown_images_path_file = unknown_images_path_file
    
    def analyzeImage(self): 
        model = load_model(os.path.join(os.getcwd(), 'model.h5'))
        path = self.unknown_images_path_file


        #load the react image in the first path here
        test_image = image.load_img(path+"/userImage.jpg", target_size=[64, 64])

        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        #if result = 0, the form is bad, if result = 1, the form is good
        if result == 0:
            print('bad')
        elif result == 1:
            print('good')
            
        return result
            
userAnalysis = ImageAnalysis("./Content/analyze")
