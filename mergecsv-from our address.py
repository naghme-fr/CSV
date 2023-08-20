# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:39:03 2022

@author: Admin
"""
import os
import pandas as pd
import numpy as np

def get_df():
    df=pd.DataFrame()
    os.chdir("E:/99-CT/GLCM/excels/pyradiomics-all features of 2Ds-case/first-order/hypo")
    for file in os.listdir():
        if file.endswith('.csv'):
            aux=pd.read_csv(file, error_bad_lines=False)
            df=df.append(aux)
    return df


df=get_df()

df.to_csv(f"Whole-first-order-hypo.csv")


def get_df():
    df=pd.DataFrame()
    os.chdir("E:/99-CT/GLCM/excels/pyradiomics-all features of 2Ds-case/first-order/normal")
    for file in os.listdir():
        if file.endswith('.csv'):
            aux=pd.read_csv(file, error_bad_lines=False)
            df=df.append(aux)
    return df


df=get_df()

df.to_csv(f"Whole-first-order-normal.csv")