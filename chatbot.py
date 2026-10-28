import streamlit as st

st.title("🤖 Mein interaktiver Chatbot")
st.write("Hallo! Ich bin dein Chatbot. Lass uns ein bisschen quatschen.")

name = st.text_input("Was ist dein Name?")

if name:
    st.write(f"Hallo **{name}**! 👋")
    nationalitaet = st.text_input("Aus welchem Land kommst du?")

    if nationalitaet:
        st.write(f"Nice, **{nationalitaet}** ist schön! :)")
        antwort_alter = st.text_input("Wie alt bist du?")

        if antwort_alter:
            erlaubte_alter = ["11", "12", "13", "14", "15"]

            if any(einzelnes_alter in antwort_alter for einzelnes_alter in erlaubte_alter):
                antwort_spiele = st.radio(
                    "Cool, spielst du Videospiele?",
                    ("Bitte wählen...", "Ja", "Nein"),
                )

                if antwort_spiele == "Ja":
                    lieblingsspiel = st.text_input("Mega! Was ist dein Lieblingsspiel?")
                    if lieblingsspiel:
                        st.success(f"Ah, {lieblingsspiel} ist ein tolles Spiel!")

                elif antwort_spiele == "Nein":
                    freizeit = st.text_input("Ah, okay! Was machst du stattdessen so in deiner Freizeit?")
                    if freizeit:
                        st.info("Das klingt nach einem spannenden Hobby!")
            else:
                st.write("Ah, verstehe!")

            st.divider()
            st.subheader("Zusammenfassung:")
            st.write(f"Du bist **{antwort_alter}** Jahre alt, kommst aus **{nationalitaet}** und dein Name ist **{name}**.")
