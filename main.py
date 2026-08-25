import streamlit as st

# Page layout aur config set karne ke liye
st.set_page_config(page_title="JEE Master Tool", page_icon="🎓", layout="wide")

st.title("🚀 JEE MASTER TOOL")
st.write("Welcome! This interactive web tool is built to track and analyze your JEE and IIT target criteria.")

# Aapka main while loop menu ab beautiful web tabs me badal diya hai
tab1, tab2 = st.tabs(["📊 1. Predict Percentile", "📋 2. Check Complete JEE Eligibility"])

# ==========================================
# TAB 1: MARKS TO PERCENTILE PREDICTOR
# ==========================================
with tab1:
    st.header("--- JEE Main Percentile Predictor ---")
    st.write("Apne 300 me se expected marks daliye, yeh tool aapka percentile range batayega.")
    
    # Input box web user ke liye
    score = st.number_input("Enter your expected marks out of 300:", min_value=0.0, max_value=300.0, value=150.0, key="score_input")
    
    # Aapka exact conditions wala logic
    if score >= 250: 
        res = "99.9 - 100.0"
    elif score >= 200: 
        res = "99.2 - 99.8"
    elif score >= 170: 
        res = "98.5 - 99.1"
    elif score >= 150: 
        res = "97.5 - 98.4"
    elif score >= 130: 
        res = "96.0 - 97.4"
    elif score >= 110: 
        res = "93.5 - 95.9"
    elif score >= 90:  
        res = "89.0 - 93.4"
    elif score >= 70:  
        res = "80.0 - 88.9"
    elif score >= 50:  
        res = "70.0 - 79.9"
    else: 
        res = "Below 70.0"
        
    st.success(f"Your expected percentile range is: **{res}**")


# ==========================================
# TAB 2: ELIGIBILITY CHECKER
# ==========================================
with tab2:
    st.header("--- JEE Eligibility Checker ---")
    
    # Dropdown menu options select karne ke liye
    cat = st.selectbox("Select your category:", ["GENERAL", "EWS", "OBC-NCL", "SC", "ST", "PwBD"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        per_12th = st.number_input("Enter Class 12th Aggregate %:", min_value=0.0, max_value=100.0, value=75.0)
    with col_b:
        top20 = st.radio("Are you in Top 20 percentile of your board?", ["no", "yes"])

    # Board criteria logic check
    is_board_ok = False
    if cat in ["SC", "ST", "PwBD"]:
        if per_12th >= 65.0 or top20 == "yes":
            is_board_ok = True
    else:
        if per_12th >= 75.0 or top20 == "yes":
            is_board_ok = True

    if not is_board_ok:
        st.error(f"❌ You don't satisfy Class 12th criteria for {cat}.")
    else:
        st.success(f"✅ Board criteria satisfied for {cat} category.")

    # Mains percentage inputs
    st.subheader("Mains Percentile Screening")
    mains_p = st.number_input("Enter your overall JEE Mains Percentile:", min_value=0.0, max_value=100.0, value=95.0, step=0.01)

    mains_data = {
        "GENERAL": 93.41,
        "EWS": 82.42,
        "OBC-NCL": 80.92,
        "SC": 63.92,
        "ST": 52.02,
        "PwBD": 0.0023
    }

    is_mains_ok = mains_p >= mains_data[cat]

    if is_mains_ok:
        st.success(f"🎉 Qualified for JEE Advanced! (Cutoff for {cat} was {mains_data[cat]})")
        
        # Section 3 unlock ho jata hai agar mains qualified hai
        st.markdown("---")
        st.header("--- JEE Advanced Rank List Criteria Checking ---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            p_val = st.number_input("Total marks in Physics (Paper 1 + 2):", value=15.0)
        with col2:
            c_val = float(st.number_input("Total marks in Chemistry (Paper 1 + 2):", value=15.0))
        with col3:
            m_val = float(st.number_input("Total marks in Mathematics (Paper 1 + 2):", value=15.0))

        final_sum = p_val + c_val + m_val
        
        adv_limits = {
            "GENERAL":,
            "EWS":,
            "OBC-NCL":,
            "SC":,
            "ST":,
            "PwBD": [4, 46]
        }

        sub_limit = adv_limits[cat][0]
        agg_limit = adv_limits[cat][1]
        
        st.info(f"Passing rules for {cat}: \n- Minimum marks required in EACH subject: **{sub_limit}** \n- Minimum aggregate marks required: **{agg_limit}**")
        
        # Advanced validations
        chk_p = p_val >= sub_limit
        chk_c = c_val >= sub_limit
        chk_m = m_val >= sub_limit
        chk_sub = chk_p and chk_c and chk_m
        chk_agg = final_sum >= agg_limit
        
        st.write(f"**Your Total Obtained Advanced Marks:** {final_sum} / 360")
        
        if chk_sub and chk_agg and is_board_ok:
            st.balloons() # Background me balloons udane ke liye
            st.success("🏆 Congratulations! You have cleared all cutoffs and qualified for IIT Rank List!")
        else:
            st.danger("Result: Not qualified for IIT Rank List.") if hasattr(st, "danger") else st.error("Result: Not qualified for IIT Rank List.")
            if not is_board_ok:
                st.write("- Failed 12th board criteria.")
            if not chk_sub:
                st.write("- Failed subject-wise minimum passing marks.")
                if not chk_p: st.write(f"  -> Physics marks below {sub_limit}")
                if not chk_c: st.write(f"  -> Chemistry marks below {sub_limit}")
                if not chk_m: st.write(f"  -> Mathematics marks below {sub_limit}")
            if not chk_agg:
                st.write(f"- Total score is below required aggregate of {agg_limit}")
    else:
        st.warning("🔒 Advanced analysis locked because JEE Main cutoff not cleared.")


