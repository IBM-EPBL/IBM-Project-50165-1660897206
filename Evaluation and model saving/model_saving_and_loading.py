# -*- coding: utf-8 -*-
"""Model Saving And Loading

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lW4EeZykqJXCYCWJd_QxzQTf7tiUd3Zf
"""

model_json=model.to_json(0 
with open("final_model.json","w") as json_file:
   json_file.write(model_json) 

model.save_weights("final_model.h5") 
print("Saved model to disk")