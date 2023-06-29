import onnxruntime as ort
import numpy as np
import cv2
# from PIL import Image
class skin_type_check:
    def __init__(self,model_path) -> None:
        self.model_path=model_path
        self.model_session=ort.InferenceSession(model_path,providers=['CPUExecutionProvider'])
        self.classes=["Dry", "Oily","Normal"]
    def __call__(self,cv_img):
        # pil_img=pil_img.resize((224,224))
        cv_img=cv2.resize(cv_img,dsize=(224,224))
        cv_img=np.expand_dims(cv_img,axis=0).astype(dtype="float32")
        input_name  = self.model_session.get_inputs()[0].name
        output_name = self.model_session.get_outputs()[0].name
        output=self.model_session.run([output_name],{input_name:cv_img})[0]
        output=self.classes[np.concatenate((output,np.array([[0.7]])),axis=1)[0].argmax()]
        return output
