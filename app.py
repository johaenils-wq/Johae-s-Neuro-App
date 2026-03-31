import streamlit as st
import openai

# 🔑 API Key (später sicher über Streamlit Secrets einfügen!)
openai.api_key = "DEIN_OPENAI_API_KEY"

# 🎨 Seitenlayout
st.set_page_config(page_title="Johae's Neuro Assistent", layout="wide")

# 🧠 Header
st.markdown("""
<h1 style='text-align: center; color: #1F4E79;'>Johae's Neuro Assistent 🧠</h1>
<p style='text-align: center;'>KI-gestützte Unterstützung zur Einschätzung neurologischer & neuropsychologischer Zustände</p>
""", unsafe_allow_html=True)

# ⚠️ Rechtlicher Hinweis
st.warning("⚠️ Diese Anwendung dient ausschließlich zur Orientierung und ersetzt keine ärztliche Diagnose oder Behandlung.")

# 📊 Erweiterte Symptomliste (100+ möglich, hier starke Basis)
symptome_liste = [
    "Verwirrtheit", "Desorientierung", "Halluzinationen", "Gedächtnisstörungen",
    "Amnesie", "Sprachstörungen (Aphasie)", "Dysarthrie", "Tremor", "Ataxie",
    "Krampfanfälle", "Schwindel", "Koordinationsstörungen",
    "Parästhesien", "Hypästhesien", "Lähmungen", "Sehstörungen",
    "Doppelbilder", "Kopfschmerzen", "Migräne", "Aura",
    "Bewusstseinsverlust", "Synkope", "Schlafstörungen", "Unruhe",
    "Aggression", "Angst", "Depression", "Stimmungsschwankungen",
    "Apathie", "Konzentrationsstörungen", "Psychomotorische Unruhe",
    "Verlangsamtes Denken", "Desorganisiertes Denken",
    "Wahnvorstellungen", "Reizbarkeit", "Erschöpfung",
    "Gangstörungen", "Feinmotorik-Störungen", "Muskelzuckungen",
    "Nackensteifigkeit", "Lichtempfindlichkeit"
]

# 🧠 Layout
col1, col2 = st.columns(2)

with col1:
    symptome = st.multiselect("🧠 Symptome auswählen", symptome_liste)
    verhalten = st.text_area("🧍 Verhalten / Auffälligkeiten")

with col2:
    diagnosen = st.text_area("📋 Bekannte Diagnosen")
    medikamente = st.text_area("💊 Medikamente")
    bio = st.text_area("🧪 Biologische Daten / Laborwerte")

# 🚀 Analyse
if st.button("🔍 Analyse starten"):

    prompt = f"""
Du bist ein medizinischer Assistent mit Spezialisierung auf Neurologie und Neuropsychologie.

Analysiere folgende Patientendaten:

Symptome: {symptome}
Verhalten: {verhalten}
Diagnosen: {diagnosen}
Medikamente: {medikamente}
Biologische Daten: {bio}

Ziel:
1. Einschätzung Delir (hoch / mittel / niedrig)
2. Wahrscheinlichste alternative neurologische oder neuropsychologische Erkrankungen
3. Kurze medizinische Begründung
4. Empfehlungen für nächste diagnostische Schritte (keine Diagnose!)

Wichtig:
- Antworte strukturiert
- Präzise und sachlich
- Keine endgültige Diagnose stellen
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    result = response['choices'][0]['message']['content']

    st.markdown("### 📝 Analyse-Ergebnis")
    st.success(result)
