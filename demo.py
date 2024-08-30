from image_dehazing.single_image import ImageDehazing
import matplotlib.pyplot as plt
from skimage.io import imread

# Read images
images = [
    imread('./dataset/image_1.jpg'),
    imread('./dataset/image_2.jpeg'),
    imread('./dataset/image_3.png'),
    imread('./dataset/image_4.jpg'),
    imread('./dataset/image_5.jpg'),
    imread('./dataset/image_6.jpg'),
    imread('./dataset/image_7.jpg'),
    imread('./dataset/image_8.jpg'),
    imread('./dataset/image_9.jpg'),
    imread('./dataset/image_10.jpg'),
    imread('./dataset/image_11.jpeg'),
    imread('./dataset/image_12.jpeg'),
    imread('./dataset/image_13.jpeg'),
    imread('./dataset/image_14.jpeg'),
    imread('./dataset/image_15.jpeg'),
    imread('./dataset/image_16.jpeg'),
    imread('./dataset/image_17.jpeg'),
    imread('./dataset/image_18.jpeg'),
    imread('./dataset/image_19.jpeg'),
    imread('./dataset/image_20.jpeg'),
    imread('./dataset/image_21.jpeg'),
    imread('./dataset/image_22.jpeg'),
    imread('./dataset/image_23.jpeg'),
    imread('./dataset/image_24.jpeg'),
    imread('./dataset/image_25.jpeg')
]

for image in images:
    # Create instance of ImageDehazing class
    dehazer = ImageDehazing(verbose=False)
    
    # Initiate dehazing process by call to dehaze method
    dehazed_data = dehazer.dehaze(image, pyramid_height=12)
    plt.figure()

    # Display results
    plt.subplot(1, 2, 1)
    plt.imshow(dehazed_data['hazed'])
    plt.title('Hazy Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(dehazed_data['dehazed'])
    plt.title('Dehazed Image')
    plt.axis('off')

    plt.show()