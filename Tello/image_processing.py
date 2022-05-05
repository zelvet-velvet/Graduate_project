import matplotlib.pyplot as plt

img = plt.imread('img.jpg')
plt.imshow(img);
plt.show();
print('Size of the Image:',img.shape);
print('At [0,0] the RGB components are:',img[0,0,:]);
print('At [99,0] the RGB components are:',img[99,0,:]);
print('At [0,199] the RGB components are:',img[0,199,:]);
print('At [99,199] the RGB components are:',img[99,199,:]);
