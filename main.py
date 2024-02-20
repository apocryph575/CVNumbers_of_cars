import cv2
from matplotlib import pyplot as plt



# def open_img(img_path):
#     carplate_img = cv2.imread(img_path)
#     carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
#     return carplate_img


def carplate_extract(image, carplate_haar_cascade):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in carplate_rects:
        carplate_img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
    return carplate_img


def main():
    carplate_haar_cascade = cv2.CascadeClassifier('numbers.xml')
    cap = cv2.VideoCapture('videos/car1.mp4')
    while True:
        success, carplate_img_rgb = cap.read()
        try:
            carplate_exctract_img = carplate_extract(carplate_img_rgb, carplate_haar_cascade)
        except:
            continue
        cv2.imshow("Result", carplate_exctract_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # carplate_img_rgb = open_img("images/numbers (3).jpg")
    # carplate_exctract_img = carplate_extract(carplate_img_rgb, carplate_haar_cascade)
    # plt.axis('off')
    # plt.imshow(carplate_exctract_img)
    # plt.show()

if __name__ == "__main__":
    main()

