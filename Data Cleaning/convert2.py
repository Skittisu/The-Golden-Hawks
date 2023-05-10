import hashlib
import os

# Set the path to the Flickr30K dataset folder
dataset_path = "C:/Users/vikas/Desktop/image/COVID_IEEE"

# Create a dictionary to store the md5 hash value and file path of each image
md5_dict = {}

# Iterate through each image file in the dataset folder
for subdir, dirs, files in os.walk(dataset_path):
    for file in files:
        # Check if the file is an image file
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # Compute the md5 hash value of the image file
            file_path = os.path.join(subdir, file)
            with open(file_path, 'rb') as f:
                md5_hash = hashlib.md5(f.read()).hexdigest()
            # Store the md5 hash value and file path in the dictionary
            if md5_hash in md5_dict:
                md5_dict[md5_hash].append(file_path)
            else:
                md5_dict[md5_hash] = [file_path]

# Iterate through the dictionary and print the duplicate images
duplicate_count = 0
for md5_hash, file_paths in md5_dict.items():
    if len(file_paths) > 1:
        print("Duplicate images with md5 hash {}: ".format(md5_hash))
        for file_path in file_paths:
            print(file_path)
        duplicate_count += len(file_paths) - 1
        # Remove all but one copy of the duplicate images
        for i in range(1, len(file_paths)):
            os.remove(file_paths[i])

print("Total number of duplicate images found: {}".format(duplicate_count))
