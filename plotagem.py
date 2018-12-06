import cv2
from pprint import pprint
import numpy as np
import sys

def plota_img(img_nome):
    dicionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    charuco = cv2.imread("charucorot.png")


    corn_ori, id_ori, rejectedImgPoints = cv2.aruco.detectMarkers(charuco, dicionario)
    dic_ori = {k[0]: v for k, v in zip(id_ori, corn_ori)}
    img = cv2.imread(img_nome)
    img = cv2.resize(img, (charuco.shape[1], charuco.shape[0]))

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        corn_dest, id_dest, rejectedImgPoints = cv2.aruco.detectMarkers(frame, dicionario)

        if corn_dest == []:
            cv2.imshow("detecta marker", cv2.flip(frame,1))
        else:
            cc = [dic_ori[e[0]] for e in id_dest]

            rcc = np.reshape(cc, (4*len(cc),2))
            rcd = np.reshape(corn_dest, (4*len(corn_dest),2))

            Hocv, retval = cv2.findHomography(rcc,rcd)

            dst = cv2.warpPerspective(img, Hocv, (frame.shape[1], frame.shape[0]))

            dst[dst==0] = frame[dst==0]

            cv2.imshow("detecta marker", cv2.flip(dst,1))
        
        if not ret:
            break
        k = cv2.waitKey(30)

        if k%256 == 27:
            # ESC
            break

    cam.release()

    cv2.destroyAllWindows()