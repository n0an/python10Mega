import cv2
import os
import glob


def resize_images(items):

    for item in items:

        img = cv2.imread(item, -1)

        resized_image = cv2.resize(img, (100, 100))

        cv2.imshow('Hey', resized_image)
        cv2.waitKey(500)
        cv2.destroyAllWindows()

        cv2.imwrite(item[:-4] + '_resized.jpg', resized_image)


def main():

    os.chdir('sample-images')

    items = glob.glob('*.jpg')

    resize_images(items)

if __name__ == '__main__':
    main()
