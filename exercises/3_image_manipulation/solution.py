import image
import random

def main():
  # Load an image from somewhere online
  #pic = image.Pic('http://www.eg.bucknell.edu/~emp017/images/me3.jpg')
  pic = image.Pic('https://eg.bucknell.edu/~cld028/images/Science_StepBro.png')
  # Modify our image
  print("Modifying image... ")
  #boost_red(pic)
  blur(pic, 8)
  print("Done modifying image")
  print("-------------------")
  # Save the image
  pic.save_image("myImage-red.jpeg")


# BOOST THE RED - DON'T DELETE
# This is ONE example of a function that changes a picture.
# You will create several other functions that look similar to this.
def boost_red(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by altering the red
      pixel.red = red + 100
      pixel.green = green
      pixel.blue = blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def invert(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by inverting each
      pixel.red = 255 - red
      pixel.green = 255 - green
      pixel.blue = 255 - blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def greyscale(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Find average of red, green, and blue
      av = int((red + green + blue)/3)

      # Resave them by setting red, green and blue to av
      pixel.red = av
      pixel.green = av
      pixel.blue = av

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def set_contrast(pic, contrast):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Find factor F using contrast
      F = 259 * ( contrast + 255 ) / ( 255 * ( 259 - contrast ) )

      # Resave them using the factor F
      pixel.red = int(F * ( red - 128 ) + 128)
      pixel.green = int(F * ( green - 128 ) + 128)
      pixel.blue = int(F * ( blue - 128 ) + 128)

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def grainy(pic):
  # Go through each row and column
  for row in range(pic.height):
    for col in range(pic.width):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # randomly select r, g, or b
      select_color = random.choice(["r", "g", "b"])
      # change the appropriate color

      if select_color == "r":
          pixel.red = red + 100
      if select_color == "g":
          pixel.green = green + 100
      if select_color == "b":
          pixel.blue = blue + 100

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def invertspot(pic, row1, col1, row2, col2):
  # Go through row1 to row2 and col1 to col2
  for row in range(row1, row2):
    for col in range(col1, col2):
      # Gets a pixel at row/col
      pixel = pic.pixels[row][col]

      # Get the RGB values of this pixel
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them by inverting each
      pixel.red = 255 - red
      pixel.green = 255 - green
      pixel.blue = 255 - blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def mirror_half(pic):
  # Go through each row and half of the columns
  for row in range(pic.height):
    half_way = pic.width//2
    for col in range(half_way):
      # Gets a pixel for mirror image
      pixel = pic.pixels[row][-(col+1)]

      # Get the RGB values of this pixel
      # The next 6 lines are not needed since the color values are not changed.
      red = pixel.red
      green = pixel.green
      blue = pixel.blue

      # Resave them
      pixel.red = red
      pixel.green = green
      pixel.blue = blue

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

def blur(pic, window):
  # Go through each row but not all the columns
  for row in range(pic.height):
    for col in range(pic.width - window + 1):
      # Initialize accumulators
      total_red = 0
      total_green = 0
      total_blue = 0
      for new_col in range(col, col + window):
        pixel = pic.pixels[row][new_col]

        # Get the RGB values of this pixel
        # Add to the accumulator
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue

      # Resave the average of the pixels in the window
      pixel.red = int(total_red/window)
      pixel.green = int(total_green/window)
      pixel.blue = int(total_blue/window)

      # Finally, reset the pixel stored at that spot
      pic.pixels[row][col] = pixel

main()
