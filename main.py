import os
import streamlit as st

st.set_page_config(page_title="Resource Hub", page_icon="📋", layout="wide")

st.title("📋 Senior Healthcare Resource Hub")

# The list of files you expect to see
filenames = [
    "1_Doctor_Visit_Prep.pdf", 
    "2_Medication_Log.pdf", 
    "3_Medicare_Worksheet.pdf", 
    "4_Emergency_Wallet_Card.pdf", 
    "5_Specialist_Referral_Checklist.pdf", 
    "6_Hospital_Discharge_Checklist.pdf"
]

# SEARCH FOR FILES: This helps us find them if they are in a subfolder
base_path = os.path.dirname(__file__)
found_path = None

# Check main folder and common subfolders
for folder in [base_path, os.path.join(base_path, "pdfs"), os.path.join(base_path, "docs")]:
    if os.path.exists(os.path.join(folder, filenames[0])):
        found_path = folder
        break

st.divider()
col1, col2 = st.columns(2)

for index, fname in enumerate(filenames):
    col = col1 if index % 2 == 0 else col2
    
    with col:
        st.subheader(fname.replace("_", " ").replace(".pdf", ""))
        
        # Try to read the file from the path we found
        if found_path:
            file_path = os.path.join(found_path, fname)
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"📥 Download {fname}",
                    data=f.read(),
                    file_name=fname,
                    mime="application/pdf",
                    key=f"dl_{index}"
                )
        else:
            # If we still can't find it, show exactly where the app is looking
            st.error(f"⚠️ Cannot find {fname}. Current folder contains: {os.listdir(base_path)}")

        st.write("---")
