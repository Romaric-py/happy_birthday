import streamlit as st
from datetime import datetime

# Configurer la page
st.set_page_config(page_title="Joyeux Anniversaire Papa!", page_icon="🎉")

# Ajouter un titre
st.title("🎂 Joyeux Anniversaire Papa ! 🎂")

# Message principal
st.markdown(
    """
    ## Cher Papa,
    
    Aujourd'hui, nous célébrons une personne extraordinaire : **VOUS** ! 🎉
    Merci pour tout l'amour, le soutien et les précieux moments partagés. 
    
    Que cette journée soit remplie de bonheur, de sourires et de joie. Vous le méritez plus que tout ! 💖
    
    Passez une journée inoubliable, et sachez que nous vous aimons très fort !
    """
)

# Ajouter une image festive
st.image(
    "photo-1529994476526-5a7f0737d5f1.avif",
    caption="Un gâteau rien que pour vous, Papa !",
)

# Ajouter une interaction
if st.button("🎁 Cliquez pour ouvrir votre cadeau 🎁"):
    st.balloons()
    st.success("Votre cadeau : Un énorme câlin et tout notre amour ! ❤️")

# Message de fin
st.markdown(
    f"""
    ---
    **Date d'aujourd'hui :** {datetime.now().strftime('%d %B %Y')}  
    """
)
