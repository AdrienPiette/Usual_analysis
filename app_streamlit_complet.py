# app_streamlit_propulsion.py

import streamlit as st
import pandas as pd
import joblib

# Chargement du pipeline et du label encoder
model = joblib.load(r'C:\Users\pieta\OneDrive\Bureau\tracéo_justin\Usual_analysis\model\model_rf_complet.joblib')
label_encoder = joblib.load(r'C:\Users\pieta\OneDrive\Bureau\tracéo_justin\Usual_analysis\model\label_encoder.joblib')

# Liste des features utilisées par le modèle (dans l'ordre attendu)
features = [
    'Impacted material','State after shoot','Initation','Locus','Location of initiation',
    'Profile of initation','General Direction','Location of termination','Termination',
    'fracture composition','Fracture part','Fracture group','enought traces for determination',
    'attribute group','Penetration'
]

st.title("Prédiction du Mode de Propulsion - Tracéologie")
st.markdown("Remplissez les caractéristiques de la trace ci-dessous pour obtenir une prédiction.")

# Interface utilisateur pour remplir les données
user_input = {}


