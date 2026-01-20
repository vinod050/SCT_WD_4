from PIL import Image
import numpy as np


# -------------------------------
# METHOD 1: XOR PIXEL ENCRYPTION
# -------------------------------

def xor_encrypt_decrypt(image_path, output_path, key):
    """
    Encrypt or decrypt an image using XOR pixel manipulation.
    Same function works for both encryption and decryption.
    """
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply XOR operation
    encrypted_array = img_array ^ key

    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Operation completed. Saved to {output_path}")


# -------------------------------
# METHOD 2: PIXEL SWAPPING
# -------------------------------

def swap_encrypt(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = np.array(img)
    h, w, c = pixels.shape

    np.random.seed(key)
    indices = np.random.permutation(h * w)

    flat = pixels.reshape(-1, c)
    encrypted_flat = flat[indices]

    encrypted_img = Image.fromarray(encrypted_flat.reshape(h, w, c))
    encrypted_img.save(output_path)
    print(f"Image encrypted (swap). Saved to {output_path}")


def swap_decrypt(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = np.array(img)
    h, w, c = pixels.shape

    np.random.seed(key)
    indices = np.random.permutation(h * w)

    inverse_indices = np.argsort(indices)

    flat = pixels.reshape(-1, c)
    decrypted_flat = flat[inverse_indices]

    decrypted_img = Image.fromarray(decrypted_flat.reshape(h, w, c))
    decrypted_img.save(output_path)
    print(f"Image decrypted (swap). Saved to {output_path}")


# -------------------------------
# MAIN MENU
# -------------------------------

if __name__ == "__main__":
    print("Simple Image Encryption Tool")
    print("1. XOR Encrypt/Decrypt")
    print("2. Swap Encrypt")
    print("3. Swap Decrypt")

    choice = input("Choose option (1/2/3): ").strip()
    image_path = input("Enter image path: ").strip().strip('"')
    output_path = input("Enter output image path: ").strip().strip('"')
    key = int(input("Enter numeric key (0–255 recommended): ").strip())

    if choice == "1":
        xor_encrypt_decrypt(image_path, output_path, key)
    elif choice == "2":
        swap_encrypt(image_path, output_path, key)
    elif choice == "3":
        swap_decrypt(image_path, output_path, key)
    else:
        print("Invalid choice.")
