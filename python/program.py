from PIL import ImageTk, Image
import cv2
import os

class program:
    def __init__(self):
        self.resolution = 0
        self.pil_imgs = []
        self.column_stds = []
        self.column_avgs = []
        
        # Array of arrays. Each array in intensity_bins is for each frame (#1,000 to #4,999)
        # e.g. first array will have 25 bins (25 numbers in array) for frame #1,000
        self.intensity_bins = []
        
        self.frame_images = []
        self.extract_frames()
        
        
    # Populate frame_imgs folder with frames
    def generate_frame_imgs(self):
        pass
        
        
    # Extract frames from the video
    def extract_frames(self):
        # Set up video frame extraction
        print("Extracting frames...")     
        video_name = "20020924_juve_dk_02a.mpg"
        vidcap = cv2.VideoCapture(video_name)
        success,image = vidcap.read()
        
        # Real quick set resolution while we at it
                # Frame's      width           height  
        self.resolution = image.shape[1] * image.shape[0]
        
        count = 0 # First frame starts at 0
        
        # Locate frame_imgs folder to put frames in
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, 'frame_imgs')
        
        while success:
            # Analyze only frames #1,000 to #4,999
            if (count == 1000):
                filepath = os.path.join(path, "frame%d.jpg" % count)
                cv2.imwrite(filepath, image)  # Save frame as JPEG file
                
                # Add in Image types of PIL module to process
                img = Image.open(filepath)
                self.pil_imgs.append(img)
                
            success,image = vidcap.read()
            count += 1
            if (count == 4999):
                break
        print(f'{count} frames have been read')
    
    
    # Get histogram value for 25 bins according to Intensity Method 
    # Save this feature matrix to avoid future long wait times
    # Intensity method
    # Formula: I = 0.299R + 0.587G + 0.114B
    # 24-bit of RGB (8 bits for each color channel) color
    # intensities are transformed into a single 8-bit value.
    # There are 24 histogram bins.
    def intensity_method(self):
        self.pil_imgs
        self.intensity_bins
        # Array of arrays. Each array in intensity_bins is for each frame (#1,000 to #4,999)
        # e.g. first array will have 25 bins (25 numbers in array) for frame #1,000
        self.intensity_bins = []
        for y in range(height):  # reads pixels left to right, top down (by each row).
            for x in range(width):  # This example code reads the RGB (red, green, blue) values

                r, g, b = im.getpixel((x, y))  # in every pixel of a 'x' pixel wide 'y' pixel tall image.
                intensity = (0.299 * r) + (0.587 * g) + (0.114 * b)
                bin = int((intensity + 10) // 10)  # Division rounds down to bin number.. in this case bins will range 0-24 (25 bins).

                if bin == 26:  # last bin is 240 to 255, so bin of 24 and 25 will
                    bin = 25  # correspond to bin 24, BUT +1 since first index stores total pixels.
                InBins[bin] += 1  # allocate pixel to corresponding bin

        return InBins

    # Find the Manhattan Distance of each image and return a
    # list of distances between image i and each image in the
    # directory uses, the comparison method of the passed
    # binList

    # the "method" argument can have one of the two following values(as strings):
    # color_code_method
    # intensity_method
    def find_distance(self, method):
        # "chosen_image_index" is the index of the chosen image in the
        # image list
        chosen_image_index = int(str(self.chosen_image)[7:]) - 1
        weights = []
        bins_to_compare = []
        if method == "intensity_method":
            bins_to_compare = self.intensity_code
            for i in range(89):
                weights.append(1)

        # now apply the manhattan distance technique,
        # compute the distance between the chosen index image
        # and all other images
        chosen_image_bin = bins_to_compare[chosen_image_index]

        # print("chosen image bin: " + str(chosen_image_bin))
        image_info = []
        for i in range(len(bins_to_compare)):
            other_image_bin = bins_to_compare[i]
            other_image_img = self.photoList[i]
            other_image_file = self.fileList[i]  # all the images file name

            manhattan_distance = 0
            if (i != chosen_image_index):
                #NO NEED DIVIDE BY IMG SIZE SINCE ALL FRAMES HAVE SAME RESOLUTION1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                chosen_image_size = self.image_sizes[chosen_image_index]
                other_image_size = self.image_sizes[i]
                # iterate through the items in each bin
                for j in range(len(chosen_image_bin)):
                    chosen_image_bin_value = chosen_image_bin[j]
                    other_image_bin_value = other_image_bin[j]
                    manhattan_distance += weights[j] * abs(chosen_image_bin_value / chosen_image_size
                                                                    - other_image_bin_value / other_image_size)

            # tuple of the form (image, image file name, manhattan distance)
            info = (other_image_img, other_image_file, manhattan_distance)
            image_info.append(info)

        # sort the image info by their manhattan distances
        image_info.sort(key=lambda x: x[2])
        self.put_sorted_images_in_pages_array(image_info)
        self.update_results()

        return image_info

    # # Calculate each column's standard deviation
    # column_stds = []  # standard deviation for each column (index 0 number is std of first column)
    # for i in range(89):
    #     std_sum = 0
    #     for j in range(100):
    #         std_for_column = ((all_features[j][i] - column_avgs[i]) ** 2) / (100 - 1)
    #         std_sum += std_for_column
    #     column_std = std_sum ** 0.5  # column_std = math.sqrt(std_sum)
    #     column_stds.append(column_std)
    #     # std = square root of ( ( (each column's cell number - column's average)^2 / total number of cells in column ) + do for the rest.. its summation )
    # self.column_stds = column_stds




    # column_avgs = []  # average of each column (index 0 number is the average of first column)
    # # Calculate each column's average
    # for i in range(89):  # go through each bin in column order
    #     sum = 0
    #     for j in range(100):
    #         sum += all_features[j][i]
    #     column_average = sum / 100
    #     column_avgs.append(column_average)
    # self.column_avgs = column_avgs