import qrcode

image = qrcode.make("https://www.youtube.com/")
image.save("python idea generator\youtubeQR.jpg")