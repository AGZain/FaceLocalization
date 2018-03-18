import numpy
from PIL import Image
import scipy.misc
from matplotlib import pyplot as plt
from matplotlib import colors
import cv2
img = Image.open("images/exercise-1.jpg").convert("RGB")
imgarr = numpy.array(img)
imgarr = imgarr/255.0
imgarr = colors.rgb_to_hsv(imgarr)
print(imgarr)

print(len(imgarr))
for i in range(0, len(imgarr)):
    for x in range(0,len(imgarr[i])):
        print(imgarr[i][x][0])
        print(imgarr[i][x][1])
        print(imgarr[i][x][2])
        check0 = imgarr[i][x][0] >= 0.05 or imgarr[i][x][0] <= 0.06703910614
        check1 = imgarr[i][x][1] >= 0.20392156862 and imgarr[i][x][1] <= 0.41960784313
        check2 = (imgarr[i][x][2] >= 0.53333333333 and imgarr[i][x][2] <= 0.97647058823)
        if(check0 and check1 and check2):
            print("good")
            imgarr[i][x][0] = 0
            imgarr[i][x][1] = 0
            imgarr[i][x][2] = 255
        else:
            print("bad")
            imgarr[i][x][0] = 0
            imgarr[i][x][1] = 0
            imgarr[i][x][2] = 0

# for i in range(0,len(imgarr)):
#     for x in range(0,len(imgarr[i])):
#         print(imgarr[i][x][0])
#         print(imgarr[i][x][1])
#         print(imgarr[i][x][2])
imgarr = colors.hsv_to_rgb(imgarr)
#plt.imshow(imgarr)
#plt.show()
scipy.misc.imsave('out1.jpg', imgarr)
image = cv2.imread("images/exercise-1.jpg")

top = 999999999999.0
bottom = 0.0
right = 0.0
left = 99999999999.0
print(imgarr)

white = False
blacks = 0
end = False
maxRight = 0
maxLeft = 0
done = False
for i in range(0,len(imgarr)):
    left = 0
    right = 0
    for x in range(0,len(imgarr[0])):
        if(imgarr[i][x][0] == 255 and imgarr[i][x][1] == 255 and imgarr[i][x][2] == 255):
            if white == False:
                white = True
                if(done == False):
                    top = i
                    done = True
                blacks = 0
                left = x
            blacks = 0
        else:
            if white:
                blacks += 1
                if(blacks >= len(imgarr[0])*0.01):
                    white = False
                    blacks = 0
                    right = x
                    break
    if (right - left > maxRight - maxLeft):
        maxRight = right
        maxLeft = left



distance = maxRight -maxLeft
# for i in range(0,len(imgarr)):
#     for x in range(0,len(imgarr[0])):
#         if(imgarr[i][x][0] == 255 and imgarr[i][x][1] == 255 and imgarr[i][x][2] == 255):
#             if i < top:
#                 top = i
#             if i > bottom:
#                 bottom = i
#             if x < left:
#                 left = x
#             if x > right:
#                 right = x
# distance = right - left
cv2.rectangle(image, (maxLeft, top), (maxLeft+distance, top+distance), (255,0,0), 2)
cv2.imwrite('out.jpg', image)
