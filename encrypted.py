import cv2
import os

def encrypt_message(image_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    d = {chr(i): i for i in range(256)}

    m, n, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    os.system(f"start {encrypted_image_path}")  # Open image (Windows)

    print("Message encrypted and saved as 'encryptedImage.jpg'.")
    return password, len(message)

# User inputs
image_path = "mypic.jpg"  # Use your correct image path
message = input("Enter secret message: ")
password = input("Enter a passcode: ")

password, message_length = encrypt_message(image_path, message, password)
