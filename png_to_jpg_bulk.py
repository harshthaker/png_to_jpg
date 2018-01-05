
#Usage of the function - png_to_jpg(path-to-input_dir,path-to-output_dir)

import os
from PIL import Image


def png_to_jpg(input_dir,output_dir):
    #get list of directories within input directory- store it in an array
    directories = [d for d in os.listdir(input_dir) 
                   if os.path.isdir(os.path.join(input_dir, d))]
    
    dir_names = [] #array to store directory names
    output_paths = []
    
    for d in directories:
        dir_names.append(d)
        #print(d)
    
    for dir_name in dir_names:
        output_path = os.path.join(output_dir, dir_name)
        output_paths.append(output_path)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
    
    #for path in output_paths:
       # print(path)
    
    for d,path in zip(directories,output_paths):
        label_dir = os.path.join(input_dir, d) #full path to inner dir
        file_names = [os.path.join(label_dir, f) 
                      for f in os.listdir(label_dir) 
                      if f.endswith(".png")]
        
        for f in file_names:
            base_name = os.path.basename(f)
            base_name = base_name[:-4]
            im = Image.open(f)
            rgb_im = im.convert('RGB')
            rgb_im.save(os.path.join(path,base_name+".jpg"))
            


