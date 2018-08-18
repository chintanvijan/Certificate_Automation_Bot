from PIL import Image
mimage = Image.open("Images.jpg")
limage = Image.open("sidd.jpg")

# resize logo
wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
wpercent = (wsize / float(limage.size[0]))
hsize = int((float(limage.size[1]) * float(wpercent)))

simage = limage.resize((wsize, hsize))
mbox = mimage.getbbox()
sbox = simage.getbbox()

# right bottom corner
#box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
box=(40,10)
mimage.paste(simage, box)
mimage.show()
mimage.save("edited.jpg")