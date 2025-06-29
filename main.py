from PIL import Image  # Import the Pillow library for image processing

def compress_image(input_path, output_path, quality=85):
    """
    Compresses an image using Pillow.

    Args:
        input_path (str): The path to the input image file.
        output_path (str): The path to save the compressed image file.
        quality (int): The compression quality (0-100). Higher is better quality, larger file size.
    """
    try:
        # Open the input image file
        with Image.open(input_path) as img:
            # Save the image in JPEG format with the specified quality
            img.save(output_path, "JPEG", quality=quality)
        # Print success message if compression is successful
        print(f"Image compressed successfully: {input_path} -> {output_path}")
    except FileNotFoundError:
        # Print error message if the input file is not found
        print(f"Error: Input file not found at {input_path}")
    except Exception as e:
        # Print any other errors that occur during compression
        print(f"An error occurred during compression: {e}")

# Specify the path to the input image (make sure this file exists)
input_image_file = r"D:\My photo\passport.jpg"
# Specify the path where the compressed image will be saved
output_compressed_file = r"D:\My photo\Passport photo.jpg"
# Call the function to compress the image with quality set to 65
compress_image(input_image_file, output_compressed_file, quality=62)