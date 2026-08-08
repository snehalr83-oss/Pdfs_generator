import os
import streamlit as st

st.set_page_config(page_title="Senior Healthcare Resource Hub", page_icon="📋", layout="wide")

st.title("📋 Senior Healthcare Resource Hub")

# 1. DEBUG: Check what files the server actually sees
PDF_DIR = os.path.dirname(__file__)
all_files = os.listdir(PDF_DIR)
# st.write(f"Debug - Files found in folder: {all_files}") # Uncomment this line to see file list on screen

documents = [
    {"filename": "1_Doctor_Visit_Prep.pdf", "title": "Doctor Visit Companion", "category": "Appointments", "desc": "Organize symptoms and notes."},
    {"filename": "2_Medication_Log.pdf", "title": "Medication Log", "category": "Medications", "desc": "Track daily dosages."},
    {"filename": "3_Medicare_Worksheet.pdf", "title": "Medicare Comparison", "category": "Insurance", "desc": "Compare plan costs."},
    {"filename": "4_Emergency_Wallet_Card.pdf", "title": "Emergency Card", "category": "Emergency", "desc": "Foldable pocket card."},
    {"filename": "5_Specialist_Referral_Checklist.pdf", "title": "Specialist Checklist", "category": "Appointments", "desc": "Prep for specialist visits."},
    {"filename": "6_Hospital_Discharge_Checklist.pdf", "title": "Discharge Checklist", "category": "Recovery", "desc": "Safe transition home."},
]

st.divider()

col1, col2 = st.columns(2)

for index, doc in enumerate(documents):
    col = col1 if index % 2 == 0 else col2
    file_path = os.path.join(PDF_DIR, doc["filename"])

    with col:
        st.subheader(doc['title'])
        st.write(doc["desc"])
        
        # 2. Improved File Reading
        if os.path.exists(file_path):
            try:
                with open(file_path, "rb") as f:
                    pdf_data = f.read()
                
                st.download_button(
                    label=f"📥 Download {doc['title']}",
                    data=pdf_data,
                    file_name=doc["filename"],
                    mime="application/pdf",
                    key=f"btn_{doc['filename']}"
                )
            except Exception as e:
                st.error(f"Error reading file: {e}")
        else:
            # This will tell you EXACTLY which filename is failing
            st.warning(f"File not found: {doc['filename']}. Please check GitHub filenames.")
        
        st.write("---")
