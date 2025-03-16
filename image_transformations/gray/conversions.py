def minmax_scale(gray_img):
    minimum = min([min(row) for row in gray_img])
    maximum = max([max(row) for row in gray_img])
    minMaxscale = [[(pix - minimum)/(maximum - minimum) for pix in row]for row in gray_img]
    return minMaxscale

def binarize(gray_img, threshold):
    binarize = [[1 if row[i] > threshold else 0 for i in range(len(row))]for row in gray_img]
    return binarize