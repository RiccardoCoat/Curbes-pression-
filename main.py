import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Fonction pour lire les données à partir du fichier CSV et tracer le graphique
def plot_spar_pressure(file_path):
    # Lire les données à partir du fichier CSV
    df = pd.read_csv(file_path, delimiter=';')

    # Sélectionner les colonnes nécessaires
    df = df[['Date', 'Local time', 'spar_mbar', 'spr_mbar', 'spap_mbar']]

    # Convertir les colonnes Date et Local time en datetime
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Local time'])

    # Tracer les courbes de pression SPAR
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df['DateTime'], df['spar_mbar'], label='spar_mbar')
    ax.plot(df['DateTime'], df['spr_mbar'], label='spr_mbar')
    ax.plot(df['DateTime'], df['spap_mbar'], label='spap_mbar')
    ax.set_xlabel('Date et Heure')
    ax.set_ylabel('Pression (mbar)')
    ax.set_title('Courbes de Pression SPAR')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Fonction pour ouvrir le fichier CSV à l'aide de la boîte de dialogue
def open_file():
    file_path = st.file_uploader("Uploader le fichier CSV", type=["csv"])
    if file_path is not None:
        plot_spar_pressure(file_path)

# Mise en page Streamlit
st.title("Graphique des Courbes de Pression SPAR")
st.write("\nCette application permet de visualiser les courbes de pression SPAR à partir d'un fichier CSV.")

# Ajout du logo
logo_image = Image.open("coat-x-logo.png")  # Charger l'image depuis le fichier
logo_image = logo_image.resize((300, 150), Image.ANTIALIAS)  # Redimensionner l'image
st.image(logo_image)

# Bouton pour ouvrir le fichier CSV
open_file()
