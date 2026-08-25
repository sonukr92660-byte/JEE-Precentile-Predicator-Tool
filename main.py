import streamlit as st

# Page ka title set karne ke liye
st.set_page_config(page_title="JEE Target Tracker", page_icon="🎓")

st.title("JEE & IIT Target Tracker")
st.write("Apna score criteria check karein boards, mains, aur advanced ke liye.")

# Student ki category select karne ke liye dropdown
category = st.selectbox("Select Category:", ["GENERAL", "EWS", "OBC-NCL", "SC", "ST", "PwBD"])

# ---- SECTION 1: BOARD EXAM CHECK ----
st.subheader("Section 1: Board Exam Percentage")
col1, col2 = st.columns(2)

with col1:
    board_marks = st.number_input("Your 12th percentage score:", min_value=0.0, max_value=100.0, value=75.0)
with col2:
    top20 = st.radio("Are you inside Top 20 percentile?", ["No", "Yes"])

# Board eligibility ka logic
board_ok = False
if category in ["SC", "ST", "PwBD"]:
    if board_marks >= 65.0 or top20 == "Yes":
        board_ok = True
else:
    if board_marks >= 75.0 or top20 == "Yes":
        board_ok = True

if board_ok:
    st.success(f"Passed board exam condition for {category}.")
else:
    st.error(f"Failed board exam condition for {category}.")


# ---- SECTION 2: JEE MAINS SCREENING ----
st.subheader("Section 2: JEE Mains Screening")
mains_percentile = st.number_input("Overall percentile in Mains:", min_value=0.0, max_value=100.0, value=95.0, step=0.01)

# Alag alag category ke cutoffs set kiye hain
mains_cutoff = 93.41
if category == "EWS": 
    mains_cutoff = 82.42
elif category == "OBC-NCL": 
    mains_cutoff = 80.92
elif category == "SC": 
    mains_cutoff = 63.92
elif category == "ST": 
    mains_cutoff = 52.02
elif category == "PwBD": 
    mains_cutoff = 0.0023

mains_ok = mains_percentile >= mains_cutoff

if mains_ok:
    st.success(f"Eligible for Advanced! Cutoff required was {mains_cutoff}")
else:
    st.error(f"Not eligible for Advanced. Cutoff required is {mains_cutoff}")


# ---- SECTION 3: JEE ADVANCED (IIT RANK LIST) ----
if mains_ok:
    st.subheader("Section 3: JEE Advanced IIT Rank Analysis")
    
    # Teeno subjects ke marks inputs
    c1, c2, c3 = st.columns(3)
    with c1: 
        physics = st.number_input("Physics Marks:", value=15.0)
    with c2: 
        chemistry = st.number_input("Chemistry Marks:", value=15.0)
    with c3: 
        maths = st.number_input("Maths Marks:", value=15.0)
    
    total_advanced_marks = physics + chemistry + maths
    
    # Sub limit aur Aggregate limit category ke hisab se set karne ke liye
    subject_limit = 8
    aggregate_limit = 92
    
    if category in ["EWS", "OBC-NCL"]:
        subject_limit = 7
        aggregate_limit = 82
    elif category in ["SC", "ST", "PwBD"]:
        subject_limit = 4
        aggregate_limit = 46
        
    st.write(f"IIT passing rule for {category}: Minimum {subject_limit} marks in each subject, and minimum {aggregate_limit} in total.")
    
    # Conditions check karne ke liye variables
    physics_check = physics >= subject_limit
    chemistry_check = chemistry >= subject_limit
    maths_check = maths >= subject_limit
    
    subjects_ok = physics_check and chemistry_check and maths_check
    aggregate_ok = total_advanced_marks >= aggregate_limit
    
    st.info(f"Your Total Obtained Advanced Marks: {total_advanced_marks} / 360")
    
    # Final check agar sab criteria pass ho jaye
    if subjects_ok and aggregate_ok and board_ok:
        st.balloons() # Kuch balloons celebrate karne ke liye screen par
        st.success("Amazing! You are qualified for IIT Rank List!")
    else:
        st.warning("You missed the required cutoff matrix.")
        if not board_ok:
            st.write("- Reason: Class 12th board eligibility issue.")
        if not subjects_ok:
            st.write(f"- Reason: Individual subject score is less than {subject_limit} marks.")
        if not aggregate_ok:
            st.write(f"- Reason: Overall advanced marks are less than {aggregate_limit} marks.")

