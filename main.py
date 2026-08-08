import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Senior Healthcare Resource Hub",
    page_icon="📋",
    layout="wide",
)

# App Header
st.title("📋 Senior Healthcare Resource Hub")
st.write(
    "Easily search, preview information, and download printable healthcare worksheets and checklists."
)

# Set PDF directory to the root folder (where your script and PDFs are)
PDF_DIR = os.path.dirname(__file__)

# Document Database with Categories
documents = [
    {
        "filename": "1_Doctor_Visit_Prep.pdf",
        "title": "Doctor Visit Companion",
        "category": "Appointments",
        "desc": "Printable worksheet to organize symptoms, refill requests, and doctor notes during appointments.",
    },
    {
        "filename": "2_Medication_Log.pdf",
        "title": "Comprehensive Medication Log",
        "category": "Medications",
        "desc": "Track daily dosages, timing (morning/noon/evening), and allergies in one clean record.",
    },
    {
        "filename": "3_Medicare_Worksheet.pdf",
        "title": "Medicare Comparison Worksheet",
        "category": "Insurance & Legal",
        "desc": "Side-by-side plan comparison tool for premiums, copays, and out-of-pocket costs.",
    },
    {
        "filename": "4_Emergency_Wallet_Card.pdf",
        "title": "Emergency Health Wallet Card",
        "desc": "Foldable pocket card listing emergency contacts, conditions, and critical allergies.",
        "category": "Emergency Prep",
    },
    {
        "filename": "5_Specialist_Referral_Checklist.pdf",
        "title": "Specialist Care Checklist",
        "category": "Appointments",
        "desc": "Pre-appointment prep checklist and key questions to ask specialist physicians.",
    },
    {
        "filename": "6_Hospital_Discharge_Checklist.pdf",
        "title": "Hospital Discharge Checklist",
        "category": "Hospital & Recovery",
        "desc": "Step-by-step transition checklist for safely returning home from hospital or rehab.",
    },
]

# Sidebar Controls
st.sidebar.header("🔍 Filter & Search")

# Search Bar
search_term = st.sidebar.text_input(
    "Search documents:", placeholder="e.g., Medication, Medicare..."
)

# Category Filter
categories = ["All"] + sorted(list(set(doc["category"] for doc in documents)))
selected_category = st.sidebar.selectbox("Filter by Category:", categories)

# Apply Filtering Logic
filtered_docs = []
for doc in documents:
    matches_search = (
        search_term.lower() in doc["title"].lower()
        or search_term.lower() in doc["desc"].lower()
    )
    matches_category = (
        selected_category == "All" or doc["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_docs.append(doc)

st.divider()

# Display Results Count
st.subheader(f"Available Documents ({len(filtered_docs)})")

if not filtered_docs:
    st.warning("No documents found matching your search criteria.")
else:
    col1, col2 = st.columns(2)

    for index, doc in enumerate(filtered_docs):
        col = col1 if index % 2 == 0 else col2
        # Looks for the PDF in the same folder as this script
        file_path = os.path.join(PDF_DIR, doc["filename"])

        with col:
            st.markdown(f"### {doc['title']}")
            st.write(f"📁 **{doc['category']}**")
            st.write(doc["desc"])

            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    st.download_button(
                        label=f"📥 Download {doc['title']}",
                        data=file,
                        file_name=doc["filename"],
                        mime="application/pdf",
                        key=f"btn_{doc['filename']}",
                    )
            else:
                st.error(f"File missing: {doc['filename']}")

            st.write("---")
    
