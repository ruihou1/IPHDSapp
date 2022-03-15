import streamlit as st
import numpy as np
import pandas as pd
#把标准化过程打包
from tensorflow.keras.models import load_model
model = load_model('model.h6')
#构建网页
st.title("welecome to Isolated post-challenge hyperglycemia Decision System (IPHDS)")
# Using the "with" syntax
with st.form(key='my_form'):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("## Basic infor ")
        age=st.text_input("Age (years)",key="age")
        if not age :
            age=60
        if  float(age)<=18 or  float(age)>=120:
            st.warning('Please input a nubmer bewteen 18 and 120')
        Height=st.text_input("Height (cm)", key="Height")
        if not Height :
            Height=165
        if  float(Height)<=120 or  float(Height)>=240:
            st.warning('Please input a nubmer bewteen 120 and 240')
        Weight=st.text_input("Weight (kg)",key="Weight")
        if not Weight :
            Weight=65
        if  float(Weight)<=30 or  float(Weight)>=200:
            st.warning('Please input a nubmer bewteen 30 and 200')
        hr=st.text_input("Heart rate (bmp)", key="HR")
        if not hr :
            hr=100
        if  float(hr)<=40 or  float(hr)>=200:
            st.warning('Please input a nubmer older than 40 and 200')
        sbp=st.text_input("SBP (mmhg)", key="sbp")
        if not sbp :
            sbp=75
        if  float(sbp)<=40 or  float(sbp)>=200:
            st.warning('Please input a nubmer older than 40 and 200')
    with col2:
        st.markdown("## Blood test ")
        FPG=st.text_input("FPG (mmol/L)",key="FPG")
        if not FPG :
            FPG=6.0
        if  float(FPG)<=0 or  float(FPG)>=30:
            st.warning('Please input a nubmer older than 0 and 30')
        Hb=st.text_input("HbA1c (%)",key="Hb")
        if not Hb :
            Hb=6.0
        if  float(Hb)<=0 or  float(Hb)>=20:
            st.warning('Please input a nubmer older than 0 and 20')
        ALT=st.text_input("ALT (U/L)",key="ALT")
        if not ALT :
            ALT=6.0
        if  float(ALT)<=0 or  float(ALT)>=120:
            st.warning('Please input a nubmer older than 0 and 120')
        TG = st.text_input("TG (mmol/L)", key="TG")
        if not TG :
            TG=6.0
        if  float(TG)<=0 or  float(TG)>=10:
            st.warning('Please input a nubmer older than 0 and 10')
        HDL=st.text_input("HDL-C (mmol/L)", key="HDL")
        if not HDL :
            HDL=6.0
        if  float(HDL)<=0 or  float(HDL)>=10:
            st.warning('Please input a nubmer older than 0 and 10')
        LDL=st.text_input("LDL-C (mmol/L)",key="LDL")
        if not LDL :
            LDL=6.0
        if  float(LDL)<=0 or  float(LDL)>=10:
            st.warning('Please input a nubmer older than 0 and 10')
    if st.form_submit_button('Predict'):
        with col3:
            st.markdown("## Model result ")
            # input 转为 dataframe
            # 先把元组转成数据框
            bmi =  float(Weight) / ( float(Height) *  float(Height))
            # 预测数据  字典转成数据框
            c = {"Glu0":  float(FPG),
                 "HbAlc":  float(Hb),
                 "bmi": float(bmi),
                 "age":  float(age),
                 "hr":  float(hr),
                 "ALT":  float(ALT),
                 "TG":  float(TG),
                 "LDL":  float(LDL),
                 "sbp":  float(sbp),
                 "HDL": float(HDL),
                 }  # 将列表a，b转换成字典
            test = pd.DataFrame(c, index=[0])  # 将字典转换成为数据框
            mean = np.load("E:/DIAPRE/文章最终结果数据/mean.npy")
            std = np.load("E:/DIAPRE/文章最终结果数据/std.npy")
            test1 = (test-mean)/sd
            test2 = pd.DataFrame(test1, columns=test.columns)
            testreslut = model.predict(test2)
            st.write("IPH probility:",testreslut)
            st.write("Cut-off value: 0.070")
            if testreslut[0,0]>=0.070:
                st.write("Suggest: please test OGTT")
            else:
                st.write("Suggest: There is no need to test OGTT  ")







