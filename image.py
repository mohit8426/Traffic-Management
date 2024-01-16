
import cv2

def detect_vehicles(image_path):
    # Load the pre-trained model
    net = cv2.dnn.readNetFromTensorflow('models/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb',
                                        'models/ssd_mobilenet_v2_coco_2018_03_29/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    # Load the image
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]

    # Create a blob and pass it through the net
    blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            
            # Check if the detected object is a car (class ID 3 in COCO dataset)
            if idx == 3:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # Draw the prediction on the image
                label = f"Car: {confidence * 100:.2f}%"
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the output image
    cv2.imshow("Output", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_vehicles("path/to/your/image.jpg")
