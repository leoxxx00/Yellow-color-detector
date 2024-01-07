import cv2
from util import get_limits
from PIL import Image

def main():
    yellow = [30, 50, 50]  # Hue value for yellow color in HSV colorspace
    # Open the default camera (usually 0, but it may vary)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_limit, upper_limit = get_limits(color=yellow)
        mask = cv2.inRange(hsvImage, lower_limit, upper_limit)

        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox

            frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

        print(bbox)



        # Display the resulting frame with detected yellow objects
        cv2.imshow('Yellow Object Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture when everything is done
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
