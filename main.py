import streamlit as st

st.title("JEE MASTER TOOL")
st.write("Welcome! This tool checks your JEE Main and Advanced eligibility criteria.")

# --- PART 1: PERCENTILE PREDICTOR ---
st.write("### 1. Predict Percentile")
score = st.number_input("Enter your expected marks out of 300:", min_value=0.0, max_value=300.0, value=150.0)

res = "Below 70.0"
if score >= 250: res = "99.9 - 100.0"
elif score >= 200: res = "99.2 - 99.8"
elif score >= 170: res = "98.5 - 99.1"
elif score >= 150: res = "97.5 - 98.4"
elif score >= 130: res = "96.0 - 97.4"
elif score >= 110: res = "93.5 - 95.9"
elif score >= 90:  res = "89.0 - 93.4"
elif score >= 70:  res = "80.0 - 88.9"
elif score >= 50:  res = "70.0 - 79.9"

st.write("Your expected percentile range is:", res)


# --- PART 2: ELIGIBILITY CHECKER ---
st.write("### 2. Check Complete JEE Eligibility")

cat = st.selectbox("Enter your category:", ["GENERAL", "EWS", "OBC-NCL", "SC", "ST", "PwBD"])
per_12th = st.number_input("Enter Class 12th Aggregate %:", min_value=0.0, max_value=100.0, value=75.0)
top20 = st.radio("Are you in Top 20 percentile of your board? (yes/no):", ["no", "yes"])

# Board check logic
is_board_ok = False
if cat in ["SC", "ST", "PwBD"]:
    if per_12th >= 65.0 or top20 == "yes":
        is_board_ok = True
else:
    if per_12th >= 75.0 or top20 == "yes":
        is_board_ok = True

if not is_board_ok:
    st.write("Result: You don't satisfy Class 12th criteria for this category.")
else:
    st.write("Result: Board criteria satisfied.")

# Mains marks screening
mains_p = st.number_input("Enter your overall JEE Mains Percentile:", min_value=0.0, max_value=100.0, value=95.0)

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
    st.write("Result: Qualified for JEE Advanced!")
    
    # Advanced section opens up
    st.write("### 3. JEE Advanced Rank List Criteria Checking")
    p_val = st.number_input("Enter total marks in Physics (Paper 1 + 2):", value=15.0)
    c_val = st.number_input("Enter total marks in Chemistry (Paper 1 + 2):", value=15.0)
    m_val = st.number_input("Enter total marks in Mathematics (Paper 1 + 2):", value=15.0)

    final_sum = p_val + c_val + m_val
    
    # Python dictionary data fixed properly here
    adv_limits = {
        "GENERAL": [8, 92],
        "EWS": [7, 82],
        "OBC-NCL": [7, 82],
        "SC": [4, 46],
        "ST": [4, 46],
        "PwBD": [4, 46]
    }

    sub_limit = adv_limits[cat][0]
    agg_limit = adv_limits[cat][1]
    
    st.write("Passing rules for your category:")
    st.write("- Minimum marks required in EACH subject:", sub_limit)
    st.write("- Minimum aggregate marks required:", agg_limit)
    
    chk_p = p_val >= sub_limit
    chk_c = c_val >= sub_limit
    chk_m = m_val >= sub_limit
    chk_sub = chk_p and chk_c and chk_m
    chk_agg = final_sum >= agg_limit
    
    st.write("Your Advanced Scores:")
    st.write("Total Obtained:", final_sum, "/ 360")
    
    if chk_sub and chk_agg and is_board_ok:
        st.write("### Congratulations! You qualified for IIT Rank List!")
    else:
        st.write("Result: Not qualified for IIT Rank List.")
        if not is_board_ok:
            st.write("- Failed 12th board criteria.")
        if not chk_sub:
            st.write("- Failed subject-wise minimum passing marks.")
        if not chk_agg:
            st.write("- Total score is below required aggregate.")
else:
    st.write("Advanced analysis locked because JEE Main cutoff not cleared.")



