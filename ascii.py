import PIL.Image
import requests

image_url = "simp"


ascii_char = ["@","&","#","%","(","/","*",",","."," "," "]

def resize(image,nwidth):
    width,height = image.size
    r = height/width
    nheight = int(nwidth*r/1.5)
    nimage = image.resize((nwidth,nheight))

    return(nimage)

def grayify(image):
    grayscale_image = image.convert("L")

    return(grayscale_image)

def to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ascii_char[int(pixel//25.5)] for pixel in pixels])
    return(characters)

def ascii(nwidth = 130):
    try:
      print("lol simp == "+image_url)
      image = PIL.Image.open(requests.get(url=image_url, stream=True).raw)
    except:
      print("Error")
    
    final_image = to_ascii(grayify(resize(image,nwidth)))
    pixel_count = len(final_image)
    ascii_image = "\n".join(final_image[i:(i+nwidth)] for i in range(0,pixel_count,nwidth))
   

    with open("ascii_image.txt","w") as f:
        f.write(ascii_image)


