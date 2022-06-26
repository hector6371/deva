import os

import cv2
import numpy as np
from tensorflow.python.keras.models import load_model
import imutils
from solver import *
from config import ROOT_DIR

classes = np.arange(0, 10)
model = load_model(os.path.join(ROOT_DIR, 'ocr', 'model-OCR.h5'))
# print(model.summary())
input_size = 48
img = None
board = None
location = None
predicted_number = None


def load_board(cv2_image):
    global img
    global board
    global location
    global predicted_number
    global model

    # Read image
    img = cv2_image

    # extract board from input image
    board, location = find_board(img)

    gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    # print(gray.shape)
    rois = split_boxes(gray)
    rois = np.array(rois).reshape(-1, input_size, input_size, 1)

    # get prediction
    prediction = model.predict(rois)
    # print(prediction)

    predicted_numbers = []
    # get classes from prediction
    for i in prediction:
        index = (np.argmax(i))  # returns the index of the maximum number of the array
        predicted_number = classes[index]
        predicted_numbers.append(predicted_number)

    # print(predicted_numbers)

    # reshape the list
    board_num = np.array(predicted_numbers).astype('uint8').reshape(9, 9)
    return board_num



def get_perspective(img, location, height=900, width=900):
    """Takes an image and location os interested region.
        And return the only the selected region with a perspective transformation"""
    pts1 = np.float32([location[0], location[3], location[1], location[2]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result


def get_inv_perspective(img, masked_num, location, height=900, width=900):
    """Takes original image as input"""
    pts1 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    pts2 = np.float32([location[0], location[3], location[1], location[2]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(masked_num, matrix, (img.shape[1], img.shape[0]))
    return result


def find_board(img):
    global location

    """Takes an image as input and finds a sudoku board inside of the image"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 13, 20, 20)
    edged = cv2.Canny(bfilter, 30, 180)
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)

    newimg = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)
    # cv2.imshow("Contour", newimg)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]
    location = None

    # Finds rectangular contour
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 15, True)
        if len(approx) == 4:
            location = approx
            break
    result = get_perspective(img, location)
    return result, location


# split the board into 81 individual images
def split_boxes(board):
    """Takes a sudoku board and split it into 81 cells.
        each cell contains an element of that board either given or an empty cell."""
    rows = np.vsplit(board, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            box = cv2.resize(box, (input_size, input_size)) / 255.0
            # cv2.imshow("Splitted block", box)
            # cv2.waitKey(50)
            boxes.append(box)
    cv2.destroyAllWindows()
    return boxes


def display_numbers(img, numbers, color=(0, 255, 0)):
    """Displays 81 numbers in an image or mask at the same position of each cell of the board"""
    W = int(img.shape[1] / 9)
    H = int(img.shape[0] / 9)
    for i in range(9):
        for j in range(9):
            if numbers[(j * 9) + i] != 0:
                cv2.putText(img, str(numbers[(j * 9) + i]), (i * W + int(W / 2) - int((W / 4)), int((j + 0.7) * H)),
                            cv2.FONT_HERSHEY_COMPLEX, 2, color, 2, cv2.LINE_AA)
    return img


def generate_solved_image(initial_board, solved_board):
    global board
    global img
    global location

    try:
        binArr = np.where(np.array(initial_board.flatten()) > 0, 0, 1)
        # print(binArr)
        # get only solved numbers for the solved board
        flat_solved_board_nums = solved_board.flatten() * binArr
        # create a mask
        mask = np.zeros_like(board)
        # displays solved numbers in the mask in the same position where board numbers are empty
        solved_board_mask = display_numbers(mask, flat_solved_board_nums)
        # cv2.imshow("Solved Mask", solved_board_mask)
        inv = get_inv_perspective(img, solved_board_mask, location)
        # v2.imshow("Inverse Perspective", inv)
        return cv2.addWeighted(img, 0.7, inv, 1, 0)

    except Exception as e:
        print("Solution doesn't exist. Model misread digits.")
        print(e)


# load_board()
