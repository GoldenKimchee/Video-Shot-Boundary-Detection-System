# Intensity method
# Formula: I = 0.299R + 0.587G + 0.114B
# 24-bit of RGB (8 bits for each color channel) color
# intensities are transformed into a single 8-bit value.
# There are 24 histogram bins.
def intensity_method(self, im, width, height, InBins):
    total_pixels = width * height
    InBins[0] = total_pixels

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
    if method == "color_code_method":
        bins_to_compare = self.colorCode
        for i in range(89):
            weights.append(1)
    elif method == "intensity_method":
        bins_to_compare = self.intenCode
        for i in range(89):
            weights.append(1)
    elif method == "inten_color_method":
        bins_to_compare = pixInfo.get_normalized_feature()
        for i in range(89):
            weights.append(1/89)
    elif method == "relevance_method":
        bins_to_compare = pixInfo.get_normalized_feature()
        weights = self.update_weights_procedure()

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

# Calculate each column's standard deviation
column_stds = []  # standard deviation for each column (index 0 number is std of first column)
for i in range(89):
    std_sum = 0
    for j in range(100):
        std_for_column = ((all_features[j][i] - column_avgs[i]) ** 2) / (100 - 1)
        std_sum += std_for_column
    column_std = std_sum ** 0.5  # column_std = math.sqrt(std_sum)
    column_stds.append(column_std)
    # std = square root of ( ( (each column's cell number - column's average)^2 / total number of cells in column ) + do for the rest.. its summation )
self.column_stds = column_stds



column_avgs = []  # average of each column (index 0 number is the average of first column)
# Calculate each column's average
for i in range(89):  # go through each bin in column order
    sum = 0
    for j in range(100):
        sum += all_features[j][i]
    column_average = sum / 100
    column_avgs.append(column_average)
self.column_avgs = column_avgs



#extract frames from video python
import cv2
video_name = "name.mp4" # or any other extension like .avi etc
vidcap = cv2.VideoCapture(video_name)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1