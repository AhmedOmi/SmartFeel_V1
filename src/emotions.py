import numpy as np
import argparse
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# command line argument
ap = argparse.ArgumentParser()
ap.add_argument("--mode", help="train/display")
mode = ap.parse_args().mode

# Define data generators
train_dir = '../dataset/train'
test_dir = '../dataset/test'

num_train = 28709
num_val = 7178
batch_size = 64
num_epoch = 50

train_data = ImageDataGenerator(rescale=1./255)
test_data = ImageDataGenerator(rescale=1./255)

train_generator = train_data.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    color_mode="grayscale",
    class_mode='categorical')

test_generator = test_data.flow_from_directory(
    test_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    color_mode="grayscale",
    class_mode='categorical')

# Create the model
# m == model of machine learning
m = Sequential()

m.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
m.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
m.add(MaxPooling2D(pool_size=(2, 2)))
m.add(Dropout(0.25))

m.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
m.add(MaxPooling2D(pool_size=(2, 2)))
m.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
m.add(MaxPooling2D(pool_size=(2, 2)))
m.add(Dropout(0.25))

m.add(Flatten())
m.add(Dense(1024, activation='relu'))
m.add(Dropout(0.5))
m.add(Dense(7, activation='softmax'))

# If you want to train the same model or try other models, go for this
if mode == "train":
    m.compile(loss='categorical_crossentropy', optimizer=Adam(
        lr=0.0001, decay=1e-6), metrics=['accuracy'])
    model_info = m.fit_generator(
        train_generator,
        steps_per_epoch=num_train // batch_size,
        epochs=num_epoch,
        validation_data=test_generator,
        validation_steps=num_val // batch_size)
    m.save_weights('model.h5')

# emotions will be displayed on your face from the webcam feed
elif mode == "display":
    m.load_weights('model.h5')
    # logging messages with OpenCl
    cv2.ocl.setUseOpenCL(False)

    # dictionary which assigns each label an emotion (alphabetical order)
    emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful",
                    3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

    # activate webcam
    camera = cv2.VideoCapture(0)
    while True:
        # Find haar cascade to draw bounding box around face
        ret, frame = camera.read()
        if not ret:
            break
        facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(
            gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(
                cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = m.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Video', cv2.resize(
            frame, (1600, 960), interpolation=cv2.INTER_CUBIC))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()
