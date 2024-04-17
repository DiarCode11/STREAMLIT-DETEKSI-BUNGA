import cv2
import os

def preprocess(dataset_folder):

    # Loop melalui setiap folder kategori di dalam folder dataset
    for category_folder in os.listdir(dataset_folder):
        category_path = os.path.join(dataset_folder, category_folder)
        if os.path.isdir(category_path):
            # Loop melalui setiap gambar di dalam folder kategori
            for filename in os.listdir(category_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(category_path, filename)

                    image = None
                    # Membaca gambar
                    image = cv2.imread(image_path)
                    
                    # Memastikan gambar berhasil dibaca
                    if image is not None:
                        # create the 'preprocessed/[category]' folder if it does not exist
                        if not os.path.exists(f"preprocessed/{category_folder}"):
                            os.makedirs(f"preprocessed/{category_folder}")

                        # resize the image
                        resized_image = cv2.resize(image, (224, 224))
                        # save to 'preprocessed/[category]' folder
                        cv2.imwrite(f"preprocessed/{category_folder}/{filename}", resized_image)

                        # flip the image horizontally
                        flipped_image = cv2.flip(resized_image, 1)
                        cv2.imwrite(f"preprocessed/{category_folder}/{filename}_flipped.jpg", flipped_image)

                        # rotate 90 degrees to the right
                        rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
                        cv2.imwrite(f"preprocessed/{category_folder}/{filename}_rotated.jpg", rotated_image)


preprocess('dataset')
