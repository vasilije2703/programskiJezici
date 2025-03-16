def rgb2gray(rgb_img):
    rgb2gray1 = [[sum(row2)/3 for row2 in row] for row in rgb_img]
    return rgb2gray1