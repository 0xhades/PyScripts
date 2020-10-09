from PIL import Image
import sys
#RGBA
noice_rate = int(sys.argv[4])
img = Image.open(sys.argv[1])
target = sys.argv[2]
target = (int(target.split(',')[0]), int(target.split(',')[1]), int(target.split(',')[2]), 255)
infection = sys.argv[3]
infection = (int(infection.split(',')[0]), int(infection.split(',')[1]), int(infection.split(',')[2]), 255)
img = img.convert("RGBA")

pixdata = img.load()

i = 0
for y in range(img.size[1]):
    for x in range(img.size[0]):
        # RGBA = R:0 G:1 B:2 A:3 ±noice_rate
        f1 = target[0] - noice_rate <= pixdata[x, y][0] <= target[0] + noice_rate
        if target[0] - noice_rate < 0:
            f1 = pixdata[x, y][0] <= target[0] + noice_rate 

        f2 = target[1] - noice_rate <= pixdata[x, y][1] <= target[1] + noice_rate
        if target[1] - noice_rate < 0:
            f2 = pixdata[x, y][1] <= target[1] + noice_rate 
        
        f3 = target[2] - noice_rate <= pixdata[x, y][2] <= target[2] + noice_rate
        if target[2] - noice_rate < 0:
            f3 = pixdata[x, y][2] <= target[2] + noice_rate 

        if f1 and f2 and f3 and pixdata[x, y][3] > 50:
            pixdata[x, y] = infection
            i += 1
print(f'changed {i} pixels')
newFile = str(sys.argv[1]).replace('.png', '_modified.png').replace('.jpg', '_modified.jpg')
img.save(newFile)
print(f'saved at: {newFile}')
