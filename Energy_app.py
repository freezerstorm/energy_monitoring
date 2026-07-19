import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bilan Énergétique", page_icon="⚡", layout="centered")

# ---------------------------------------------------------------------------
# Appareils typiques par type d'établissement (nom -> puissance moyenne en W)
# ---------------------------------------------------------------------------
DEVICES_BY_ETABLISSEMENT = {
    "Maison": {
        "Réfrigérateur": 150, "Congélateur": 200, "Télévision": 100,
        "Machine à laver": 500, "Sèche-linge": 2500, "Four électrique": 2000,
        "Micro-ondes": 1200, "Chauffe-eau électrique": 2000,
        "Climatiseur": 1000, "Ordinateur portable": 65, "Éclairage LED": 40,
    },
    "Appartement": {
        "Réfrigérateur": 120, "Télévision": 80, "Machine à laver": 500,
        "Micro-ondes": 1000, "Climatiseur": 900, "Ordinateur portable": 65,
        "Éclairage LED": 30,
    },
    "Bureau": {
        "Ordinateur de bureau": 200, "Imprimante": 300, "Climatiseur": 1500,
        "Éclairage (plafonniers)": 100, "Photocopieuse": 800,
        "Serveur/routeur": 50, "Machine à café": 900,
    },
    "Pharmacie": {
        "Réfrigérateur médical": 200, "Climatiseur": 1200, "Éclairage": 150,
        "Ordinateur/caisse": 150, "Système de sécurité": 20,
    },
    "Bar": {
        "Réfrigérateur/frigo bar": 300, "Machine à glaçons": 400,
        "Sonorisation": 500, "Éclairage d'ambiance": 200,
        "Climatiseur": 1500, "Téléviseur": 150,
    },
    "Restaurant": {
        "Four professionnel": 5000, "Chambre froide": 500,
        "Lave-vaisselle": 2000, "Hotte aspirante": 400,
        "Climatiseur": 2000, "Éclairage": 200,
    },
    "Café": {
        "Machine à café professionnelle": 1500, "Réfrigérateur": 200,
        "Four à panini": 1000, "Éclairage": 100, "Climatiseur": 1200,
    },
    "Boutique": {
        "Éclairage vitrine": 300, "Climatiseur": 1200,
        "Système de caisse": 150, "Système antivol": 50,
        "Musique d'ambiance": 100,
    },
}

st.title("⚡ Bilan Énergétique")
st.caption("Sélectionnez votre établissement, ajustez les appareils utilisés et leur durée d'utilisation.")

# ---------------------------------------------------------------------------
# 1. Choix de l'établissement
# ---------------------------------------------------------------------------
etablissement = st.selectbox("Type d'établissement", list(DEVICES_BY_ETABLISSEMENT.keys()))

devices = DEVICES_BY_ETABLISSEMENT[etablissement]
default_df = pd.DataFrame([
    {"Appareil": nom, "Puissance (W)": p, "Utilisé": True, "Durée (h)": 1.0}
    for nom, p in devices.items()
])

st.subheader("Appareils")
st.caption("Décochez un appareil non utilisé, ajustez sa durée, ou ajoutez une ligne pour un appareil personnalisé.")

edited_df = st.data_editor(
    default_df,
    num_rows="dynamic",
    key=f"editor_{etablissement}",
    use_container_width=True,
    column_config={
        "Appareil": st.column_config.TextColumn(required=True),
        "Puissance (W)": st.column_config.NumberColumn(min_value=0, step=10, required=True),
        "Utilisé": st.column_config.CheckboxColumn(default=True),
        "Durée (h)": st.column_config.NumberColumn(min_value=0.0, step=0.5, required=True),
    },
)

tarif = st.number_input("Prix du kWh (MAD)", min_value=0.0, value=1.35, step=0.01)

# ---------------------------------------------------------------------------
# 2. Calcul du bilan
# ---------------------------------------------------------------------------
if st.button("Calculer le bilan", type="primary"):
    df = edited_df.copy()
    df = df.dropna(subset=["Appareil", "Puissance (W)", "Durée (h)"])
    df = df[df["Utilisé"] == True]

    if df.empty:
        st.warning("Aucun appareil sélectionné.")
    else:
        df["Énergie (kWh)"] = (df["Puissance (W)"] * df["Durée (h)"] / 1000).round(3)
        df["Coût (MAD)"] = (df["Énergie (kWh)"] * tarif).round(2)

        st.subheader("Bilan par appareil")
        st.dataframe(
            df[["Appareil", "Puissance (W)", "Durée (h)", "Énergie (kWh)", "Coût (MAD)"]],
            use_container_width=True, hide_index=True,
        )

        st.subheader("Bilan global")
        col1, col2 = st.columns(2)
        col1.metric("Énergie totale", f"{df['Énergie (kWh)'].sum():.2f} kWh")
        col2.metric("Coût total", f"{df['Coût (MAD)'].sum():.2f} MAD")

        st.bar_chart(df.set_index("Appareil")["Énergie (kWh)"])
