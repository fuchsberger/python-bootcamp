import image

def main():
  # Load an image from somewhere online
  pic = image.Pic('http://www.eg.bucknell.edu/~af033/images/me.jpg')
  # Modify our image
  print("Modifying image... ")
  boost_red(pic)
  print("Done modifying image")
  print("-------------------")
  # Save the image
  pic.save_image("myImage-red.jpeg")


# BOOST THE RED - DON'T DELETE
# This is ONE example of a function that changes a picture.
# You will create several other functions that look similar to this.
def boost_red(pic):
  # Go through each row and column
  for row_index in range(pic.height):
    for col_index in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row_index][col_index]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by altering the red
      pixel.red = red + 100
      pixel.green = green
      pixel.blue = blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row_index][col_index] = pixel


main()
