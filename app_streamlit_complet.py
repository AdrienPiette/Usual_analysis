import streamlit as st
import joblib
import pandas as pd

# 1. Charger le modèle complet et l'encodeur
model = joblib.load(r"C:\\Users\\pieta\\OneDrive\\Bureau\\tracéo_justin\\Usual_analysis\\model\\model_rf_complet.joblib")
label_encoder = joblib.load(r"C:\\Users\\pieta\\OneDrive\\Bureau\\tracéo_justin\\Usual_analysis\\model\\label_encoder.joblib")

# 2. Titre
st.title("Prédiction du Mode de Propulsion (tracéologie)")
st.markdown("Saisissez les caractéristiques de la trace d'impact pour prévoir le mode de propulsion.")

# 3. Caractéristiques mises à jour avec les vraies valeurs
features = {
    "Impacted material": ["Bone; Gel; Skin", "Gel; Skin", "Gel", "Skin"],
    "State after shoot": ["No dammage", "Point broken in haft", "Point broken and dehafted"],
    "Initation": [
        "Bending", "Cone", "Absent", "Absent; Bending", "Bending; Cone", "Indetermined",
        "Absent; Cone", "Bending; Indetermined", "Absent; Bending; Cone", "Absent; Bending; Indetermined"
    ],
    "Locus": ["Distal", "Mesial", "Proximal", "Distal; Mesial"],
    "Location of initiation": ["Dorsal surface", "Ealier Fracture surface", "Ventral surface", "Right Lateral Edge"],
    "Profile of initation": [
        "convex", "Concave", "Straight", "Concave; convex", "convex; N/A", "Concave; Straight",
        "Concave; convex; N/A", "convex; Straight", "Concave; N/A"
    ],
    "General Direction": [
        "diagonal towards the base", "apex to base", "base to apex", "diagonal towards the apex",
        "perpendicular to the long axis", "diagonal towards the apex; diagonal towards the base",
        "diagonal towards the apex; diagonal towards the base; perpendicular to the long axis"
    ],
    "Location of termination": [
        "Ventral surface", "Dorsal surface", "Right Lateral Edge",
        "Left lateral edge; Ventral surface", "Left lateral edge", "Earlier fracture surface"
    ],
    "Termination": [
        "Fissure; Step", "Fissure; Hinge; Step", "Hinge", "Fissure; Hinge", "Step", "Fissure; Step to step",
        "Feather; Fissure; Step", "Feather", "Feather; Fissure; Hinge; Step", "Hinge to step",
        "Fissure; Hinge to hinge", "Fissure; Hinge to step", "Fissure", "Hinge; Step",
        "Feather; Fissure; Hinge", "Hinge to step; Step to step", "Feather; Hinge",
        "Fissure; Hinge; Snap; Step", "Fissure; Step to hinge", "Snap", "Fissure; Step; Step to step",
        "Fissure; Hinge; Step; Step to step", "Fissure; Hinge; Step; Step to hinge",
        "Fissure; Hinge; Hinge to hinge; Hinge to step; Step; Step to hinge; Step to step",
        "Absent", "Fissure; N/A", "Convex", "Fissure; Hinge; Hinge to hinge; Hinge to step; Step"
    ],
    "fracture composition": ["single", "multiple"],
    "Fracture part": ["negative", "positive"],
    "Fracture group": ["removal", " fracture"],
    "enought traces for determination": ["yes", "no", "middel"],
    "attribute group": ["LS", "BB", "SD"]
}

# 4. Récupération des données utilisateurs
input_data = {}
for feat, options in features.items():
    input_data[feat] = st.selectbox(feat, options)

# 5. Ajout de la valeur numérique
penetration = st.slider("Penetration", min_value=0.0, max_value=30.0, value=10.0, step=0.1)
input_data["Penetration"] = penetration

# 6. Préparation et prédiction
X_input = pd.DataFrame([input_data])

if st.button("Prédire le mode de propulsion"):
    prediction_encoded = model.predict(X_input)[0]
    prediction_label = label_encoder.inverse_transform([prediction_encoded])[0]
    st.success(f"👉 Mode de propulsion prédit : **{prediction_label}**")
