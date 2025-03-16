import fibo, sys, builtins
fib = fibo.fib
fib2 = fibo.fib2
import os

#from image_transformations.gray.conversions import rgb2gray
import image_transformations.rgb.geometric as rgb_geom
from image_transformations.rgb import conversions as rgb_conv
from image_transformations.gray import conversions as gray_conv



# matrix = [[[255, 0, 0] , [126, 255, 0]], 
#             [[127, 255, 128], [255, 255, 255] ]]
# print(rgb_conv.rgb2gray(matrix))
# print(gray_conv.binarize(rgb_conv.rgb2gray(matrix),150))
# print(gray_conv.minmax_scale(rgb_conv.rgb2gray(matrix)))
# print(rgb_geom.flip_lr(matrix))

rootdir = 'image_transformations'
files = {
    d: [f for f in os.listdir(os.path.join(rootdir, d))] for d in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, d))
}
print(files)


# print(fib(1000))
# print(fib2(1000))s

# print(dir(fibo))
# print(dir(sys))
#print(dir(builtins))