from PIL import Image
import bitarray
def hide_message(image_path, message):
# Open the image
image =Image.open(image_path)
width, height = image.size
# Convert the message to binary
ba=bitarray.bitarray()
ba.frombytes (message.encode('utf-8'))
binary_message = ba.to01()
# Calculate the starting position for hiding the message
start_x = width // 2
start_y = height // 2
# Hide the message in the image
index = 0
for y in range(start_y, height):
for x in range(start_x, width):
if index < len(binary_message):
pixel =list(image.getpixel((x, y)))
pixel[0] =pixel[0] & ~1 | int(binary_message[index])
image.putpixel((x, y), tuple(pixel))
index += 1
else:
break
# Save the modified image
image.save('hidden_message.png')
def retrieve_message(image_path, message_length):
# Open the image
image = Image.open(image_path)
width, height =image.size
# Calculate the starting position for retrieving the message
start_x = width // 2
start y = height // 2
# Retrieve the message from the image
binary_message=' '
index = 0
for y in range(start_y, height):
for x in range(start_x, width):
if index < message_length * 8:
pixel = list(image.getpixel((x, y)))
binary_message += str(pixel[0] & 1)
index += 1
else:
break
# Convert the binary message to text
ba =bitarray.bitarray(binary_message)
message = ba.tobytes().decode('utf-8')
return message
# Hide a message in an image
print("1. Hide Message")
print("2. Retrieve Message")
choice =int(input("Enter a choice: "))
if choice == 1:
mess = input("Enter the message: ")
fname = input("Enter the filename or path of the image file: ")
hide_message(fname, mess)
elif choice == 2:
fname = input("Enter the filename or path of the image file: ")
length = int(input("Enter the length of the hidden message: "))
message = retrieve_message(fname, length)
else:
print(message)
print("Invalid choice")
