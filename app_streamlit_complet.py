import streamlit as st
import joblib
import pandas as pd

# 1. Charger le modèle complet et l'encodeur
model = joblib.load(r"C:\\Users\\pieta\\OneDrive\\Bureau\\tracéo_justin\\Usual_analysis\\model\\model_rf_complet.joblib")
label_encoder = joblib.load(r"C:\\Users\\pieta\\OneDrive\\Bureau\\tracéo_justin\\Usual_analysis\\model\\label_encoder.joblib")

# 2. Formulaire utilisateur
st.title("Prédiction du Mode de Propulsion (tracéologie)")
st.markdown("Saisissez les caractéristiques de la trace d'impact pour prévoir le mode de propulsion.")

# Liste complète des features
features = {
    "Impacted material": ["Bone; Gel; Skin", "missing"],
    "State after shoot": ["Projectile broken", "Projectile intact", "missing"],
    "Initation": ["concave", "convex", "flat", "missing"],
    "Locus": ["middle", "proximal", "distal", "missing"],
    "Location of initiation": ["edge", "center", "missing"],
    "Profile of initation": ["concave", "convex", "flat", "missing"],
    "General Direction": ["apex to base", "diagonal towards the base", "missing"],
    "Location of termination": ["edge", "center", "missing"],
    "Termination": ["Fissure", "Hinge", "Step", "Fissure; Hinge", "missing"],
    "fracture composition": ["single", "multiple", "missing"],
    "Fracture part": ["distal", "proximal", "middle", "missing"],
    "Fracture group": ["A", "B", "missing"],
    "enought traces for determination": ["yes", "no", "missing"],
    "attribute group": ["sharp", "blunt", "missing"]
}

# Récupérer les entrées utilisateur
input_data = {}
for feat, options in features.items():
    input_data[feat] = st.selectbox(feat, options)

penetration = st.slider("Penetration", min_value=0.0, max_value=30.0, value=10.0, step=0.1)
input_data["Penetration"] = penetration

# 3. Préparer l'entrée
X_input = pd.DataFrame([input_data])

# 4. Prédiction
if st.button("Prédire le mode de propulsion"):
    prediction_encoded = model.predict(X_input)[0]
    prediction_label = label_encoder.inverse_transform([prediction_encoded])[0]
    st.success(f"👉 Mode de propulsion prédit : **{prediction_label}**")
