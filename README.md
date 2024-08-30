# image-dehazing

## Directory Structure

- _image-dehazing_
- [_image_dehazing_](image_dehazing) : Image dehazing package
  - [_\_\_init\_\_.py_](image_dehazing/__init__.py)
  - [_single_image.py_](image_dehazing/single_image.py) : ImageDehazing class
- [_demo.py_](demo.py) : Demo script
- [_height_variance.py_](height_variance.py) : Sample script to display variance in quality of dehazed results with height of image pyramid
- [_LICENSE_](LICENSE) : License
- [_README.md_](README.md) : Documentation
- [_requirements.txt_](requirements.txt) : Package requirements

## Pre-requisites

Below are the pre-requisites to be satisfied before the package can be used.

- pip install -r requirements.txt
- Package requirements:
  - `matplotlib`
  - `numpy`
  - `opencv-python`
  - `scikit-image`

## Usage

- Once the pre-requisites are satisfied, the [demo](demo.py) can be run by running the following command:

  ```bash
  python demo.py
  ```
- The **_ImageDehazing_** class from the package can be used as shown in the below example:

  ```python
  from skimage.io import imread
  import matplotlib.pyplot as plt

  # Import ImageDehazing class
  from image_dehazing.single_image import ImageDehazing

  # Read image
  path_to_image = './dataset/image_1.jpg'  # Path to hazy image
  hazy_image = imread(path_to_image)

  # Create object of ImageDehazing class
  dehazer = ImageDehazing(verbose=True)

  # Dehaze the the image using th dehaze method of the object
  dehaze_data = dehazer.dehaze(hazy_image, pyramid_height=12)

  # Display dehazed image
  plt.figure()
  plt.subplot(1, 2, 1)
  plt.imshow(dehaze_data['hazed'])
  plt.title('Hazy Image')
  plt.axis('off')
  plt.subplot(1, 2, 2)
  plt.imshow(dehaze_data['dehazed'])
  plt.title('Dehazed Image')
  plt.axis('off')
  plt.show()
  ```
- To see results on analysis of the changes observed due to variation in height of the pyramid, run the [height_variance.py](height_variance.py) script as follows:
  ```bash
  python height_variance.py
  ```
