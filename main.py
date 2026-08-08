import os
import streamlit as st

st.set_page_config(page_title="Senior Healthcare Resource Hub", page_icon="📋", layout="wide")

st.title("📋 Senior Healthcare Resource Hub")

# Full document list with categories
documents = [
    {"filename": "1_Doctor_Visit_Prep.pdf", "title": "Doctor Visit Companion", "category": "Appointments", "desc": "Organize symptoms and notes for your next visit."},
    {"filename": "2_Medication_Log.pdf", "title": "Medication Log", "category": "Medications", "desc": "Track daily dosages and frequencies."},
    {"filename": "3_Medicare_Worksheet.pdf", "title": "Medicare Comparison", "category": "Insurance", "desc": "Compare plan costs and coverage details."},
    {"filename": "4_Emergency_Wallet_Card.pdf", "title": "Emergency Card", "category": "Emergency", "desc": "A foldable pocket card for vital information."},
    {"filename": "5_Specialist_Referral_Checklist.pdf", "title": "Specialist Checklist", "category": "Appointments", "desc": "Prepare specifically for specialist consultations."},
    {"filename": "6_Hospital_Discharge_Checklist.pdf", "title": "Discharge Checklist", "category": "Recovery", "desc": "Ensure a safe and organized transition home."},
]

# Sidebar Filters
st.sidebar.header("Filter Resources")
all_categories = ["All"] + sorted(list(set(doc["category"] for doc in documents)))
selected_category = st.sidebar.selectbox("Select a Category", all_categories)

# Filter the list
if selected_category == "All":
    filtered_docs = documents
else:
    filtered_docs = [doc for doc in documents if doc["category"] == selected_category]

# Layout
PDF_DIR = os.path.dirname(__file__)
st.divider()

col1, col2 = st.columns(2)

for index, doc in enumerate(filtered_docs):
    col = col1 if index % 2 == 0 else col2
    file_path = os.path.join(PDF_DIR, doc["filename"])

    with col:
        st.subheader(doc['title'])
        st.info(f"Category: {doc['category']}")
        st.write(doc["desc"])
        
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                btn_data = f.read()
            
            st.download_button(
                label=f"📥 Download {doc['title']}",
                data=btn_data,
                file_name=doc["filename"],
                mime="application/pdf",
                key=f"dl_{doc['filename']}"
            )
        else:
            st.error(f"⚠️ File '{doc['filename']}' not found on server.")
        
        st.write("---")
