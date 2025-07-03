from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """
    Compress an image using Pillow.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image file.
        quality (int): Compression quality (0-100). Higher is better quality, larger file size.
    """
    try:
        with Image.open(input_path) as img:
            img.save(output_path, "JPEG", quality=quality)
        print(f"Image compressed successfully: {input_path} -> {output_path}")
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        print(f"An error occurred during compression: {e}")

if __name__ == "__main__":
    input_image_file = r"D:\My photo\passport.jpg"
    output_compressed_file = r"D:\My photo\Passport photo.jpg"
    compress_image(input_image_file, output_compressed_file, quality=62)
