import os
import numpy as np
from PIL import Image

# Function to process images in a folder
def process_images(folder_path, output_folder):
    # Get the list of image file names in the folder
    image_files = os.listdir(folder_path)

    # Loop through each image file
    for image_file in image_files:
        # Read the image
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize((224, 224), Image.BILINEAR)

        # Turn the image into an array to be able to split the channels
        image_array = np.array(resized_image)

        # three channels of the RGB color space are separated.
        red_channel, green_channel, blue_channel = resized_image.split()

        # Apply intensity normalization to the green channel
        normalized_green_channel = (np.array(green_channel) - np.min(green_channel)) / (np.max(green_channel) - np.min(green_channel))

        # Combine the channels back into an image
        processed_image = Image.merge('RGB', (Image.fromarray(red_channel), Image.fromarray(normalized_green_channel), Image.fromarray(blue_channel)))

        # Save the processed image to the output folder
        output_path = os.path.join(output_folder, image_file)
        processed_image.save(output_path)

# Define the input and output folder paths
input_folder = "input"
output_folder = "preprocessed_input"

# Get the current directory (makees it flexible to avoid path errors)
current_directory = os.getcwd()

drusen_folder = os.path.join(current_directory, input_folder, "Drusen")
preprocessed_drusen_folder = os.path.join(current_directory, output_folder, "PreProcessed_Drusen")
process_images(drusen_folder, preprocessed_drusen_folder)

normal_folder = os.path.join(current_directory, input_folder, "Normal")
preprocessed_normal_folder = os.path.join(current_directory, output_folder, "PreProcessed_Normal")
process_images(normal_folder, preprocessed_normal_folder)

exudates_folder = os.path.join(current_directory, input_folder, "Exudates")
preprocessed_exudates_folder = os.path.join(current_directory, output_folder, "PreProcessed_Exudates")
process_images(exudates_folder, preprocessed_exudates_folder)
