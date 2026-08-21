import os
import urllib.request
from openai import OpenAI

client = OpenAI()

# Tell the model that we want a UFO abducting a chicken. 
# Need to add an image parameter
newImage = client.images.generate(
  prompt="A UFO abducting a chicken",
  # n=2,
  n=1,
  model="gpt-image-2",
  size="1024x1024" # this is a supported size, 2048x2048 might also be an option
)

print("Here are two generated images of a UFO abducting a chicken:\n")

# give a url to get the PNG image from if we want it 
print(newImage.data[0].url)
print(dir(newImage.data[0]))
# print("\n")

# print(newImage.data[1].url)

# Download the first one
# urllib.request.urlretrieve(newImage.data[0].url, "chicken.png")

# Ask for a variation (of chicken.png)
# newImage = client.images.create_variation(
#     image = open("chicken.png", "rb"),
#     n=1,
#     model="gpt-image-2",
#     size="1024x1024"
# )

# print("\nHere's a variation of the first image:\n")
# print(newImage.data[0].url)
# from OpenAI: https://developers.openai.com/api/docs/guides/image-generation
import base64
image_base64 = newImage.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("chicken2.png", "wb") as f:
    f.write(image_bytes)

# this chicken with the cluck farm sign turned out looking pretty high-def. 
# could not get dall-e-2 to work