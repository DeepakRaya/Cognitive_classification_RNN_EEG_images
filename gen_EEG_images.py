from matplotlib import pyplot as plt
from utils import load_or_generate_images
file_path = 'C:/Users/home/Desktop/CVDL/CVDL Project/'
images_average, labels = load_or_generate_images(file_path, average_image=1)



plt.figure()
for i in range(4):
    if i==0:
        a=0
    elif i==1:
        a=1000
    elif i==2:
        a=1300
    else:
        a=2500
    plt.subplot(4,4,i+1+0),plt.imshow(images_average[0,a,:,:,0]),plt.axis('off')
    plt.subplot(4,4,i+1+4),plt.imshow(images_average[0,a,:,:,1]),plt.axis('off')
    plt.subplot(4,4,i+1+8),plt.imshow(images_average[0,a,:,:,2]),plt.axis('off')
    plt.subplot(4,4,i+1+12),plt.imshow(images_average[0,a,:,:,:]),plt.axis('off')
