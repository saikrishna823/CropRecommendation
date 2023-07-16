import numpy as np
import pickle
import streamlit as st
model=pickle.load(open("C:/Project/CropRecommendation/trained_model.sav",'rb'))
#model=pickle.load(open("..train_model.sav",'rb'))

crops=['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
crops.sort()
labels=[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21]
label_crops=dict(zip(labels,crops))
html_code = '''
<h1 style="color:blue; text-align:center">Crop Recommendation System</h1>
'''
## Function to predict which crop is best suited for particular region
def CropRecommendation(input_data):
    
    input_data=np.array(input_data).reshape(1,-1)
    recommend=model.predict(input_data)
    print(recommend)
    print(label_crops[recommend[0]])
    return label_crops[recommend[0]]




def main():
    st.markdown(html_code,unsafe_allow_html=True)



    #Required Data 
# Nitrogen, Phosphorous,Potassium,Temperature,Rainfall,Ph
    nitrogen=st.text_input("Enter Nitrogen content in soil ")
    phosphorous=st.text_input("Enter Phosphorous content in soil ")
    potassium=st.text_input("Enter Potassium content in soil ")
    temperature=st.text_input("Enter Temperature in Celsius")
    humidity=st.text_input("Enter relative humidity in %")
    ph=st.text_input("Enter ph value of the soil")
    rainfall=st.text_input("Enter rainfall in mm")
    
    BestCrop=""
    if st.button("Recommend Crop"):

        print(nitrogen)
        if( nitrogen and  phosphorous and  potassium and  temperature and  rainfall and ph and humidity):
            BestCrop=CropRecommendation([int(nitrogen),int(phosphorous),int(potassium),float(temperature),float(humidity),float(ph),float(rainfall)])
            st.success(BestCrop)
        else :
            st.write("Enter Correct Values")
if __name__=='__main__':
    main()