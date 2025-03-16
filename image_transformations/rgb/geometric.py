def flip_lr(img):
    flip = [row[::-1] for row in img]
    return flip