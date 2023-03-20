import speech_recognition as sr
import cv2
def takecommand():
    R = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        R.pause_threshold = 0.5
        audio = R.listen(source)

    try:
        print("recognizing...")
        query = R.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None.."

    return query

if __name__ == "__main__":



    query=takecommand().lower()
    if 'namaste' in query:

        cap = cv2.VideoCapture('video1.mp4')
        if not cap.isOpened():
            print("Error loading video file")
            exit()

        # Read the video frame by frame
        while True:
            ret, frame = cap.read()
            if ret:
                # Display the frame
                cv2.imshow('Video', frame)
            else:
                break
            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video and close all windows
        cap.release()
        cv2.destroyAllWindows()

    if 'name' in query:

        cap = cv2.VideoCapture('video2.mp4')
        if not cap.isOpened():
            print("Error loading video file")
            exit()

        # Read the video frame by frame
        while True:
            ret, frame = cap.read()
            if ret:
                # Display the frame
                cv2.imshow('Video', frame)
            else:
                break
            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video and close all windows
        cap.release()
        cv2.destroyAllWindows()
    if 'hobby' in query:

        cap = cv2.VideoCapture('video3.mp4')
        if not cap.isOpened():
            print("Error loading video file")
            exit()

        # Read the video frame by frame
        while True:
            ret, frame = cap.read()
            if ret:
                # Display the frame
                cv2.imshow('Video', frame)
            else:
                break
            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video and close all windows
        cap.release()
        cv2.destroyAllWindows()
    if 'future' in query:

        cap = cv2.VideoCapture('video4.mp4')
        if not cap.isOpened():
            print("Error loading video file")
            exit()

        # Read the video frame by frame
        while True:
            ret, frame = cap.read()
            if ret:
                # Display the frame
                cv2.imshow('Video', frame)
            else:
                break
            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video and close all windows
        cap.release()
        cv2.destroyAllWindows()

    if 'good day' in query:

        cap = cv2.VideoCapture('video5.mp4')
        if not cap.isOpened():
            print("Error loading video file")
            exit()

        # Read the video frame by frame
        while True:
            ret, frame = cap.read()
            if ret:
                # Display the frame
                cv2.imshow('Video', frame)
            else:
                break
            # Exit if 'q' is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video and close all windows
        cap.release()
        cv2.destroyAllWindows()

