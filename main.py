import streamlit as st

st.title("JEE MASTER TOOL")
st.write("Welcome! This tool checks your JEE Main and Advanced eligibility criteria.")

# --- PART 1: PERCENTILE PREDICTOR & RANK PREDICTOR ---
st.write("### 1. Predict Percentile & Rank")
score = st.number_input("Enter your expected marks out of 300:", min_value=0.0, max_value=300.0, value=140.0)

# परसेंटाइल का आपका खुद का बनाया हुआ सिंपल लॉजिक
res = "Below 70.0"
p_num = 65.0  

if score >= 250:
    res = "99.9 - 100.0"
    p_num = 99.9
elif score >= 200:
    res = "99.2 - 99.8"
    p_num = 99.5
elif score >= 170:
    res = "98.5 - 99.1"
    p_num = 98.8
elif score >= 150:
    res = "97.5 - 98.4"
    p_num = 98.0
elif score >= 130:
    res = "96.0 - 97.4"
    p_num = 96.7
elif score >= 110:
    res = "93.5 - 95.9"
    p_num = 94.7
elif score >= 90:
    res = "89.0 - 93.4"
    p_num = 91.2
elif score >= 70:
    res = "80.0 - 88.9"
    p_num = 84.5
elif score >= 50:
    res = "70.0 - 79.9"
    p_num = 75.0

st.write("Your expected percentile range is:", res)

# सीधा छात्र वाला गणित (12 लाख कुल छात्र मानकर ऑल इंडिया रैंक)
mains_rank = int((100.0 - p_num) * 12000)
if mains_rank < 1:
    mains_rank = 1

st.write("Your expected JEE Main All India Rank (CRL) is around:", mains_rank)


# --- PART 2: ELIGIBILITY CHECKER ---
st.write("### 2. Check Complete JEE Eligibility")

cat = st.selectbox("Enter your category:", ["GENERAL", "EWS", "OBC-NCL", "SC", "ST", "PwBD"])

# साधारण कैटेगरी रैंक कैलकुलेशन
cat_rank = mains_rank
if cat == "OBC-NCL":
    cat_rank = int(mains_rank * 0.27)
elif cat == "EWS":
    cat_rank = int(mains_rank * 0.10)
elif cat == "SC":
    cat_rank = int(mains_rank * 0.15)
elif cat == "ST":
    cat_rank = int(mains_rank * 0.07)
elif cat == "PwBD":
    cat_rank = int(mains_rank * 0.05)

if cat != "GENERAL":
    st.write("Your expected JEE Main Category Rank is around:", cat_rank)
else:
    st.write("Your JEE Main Category Rank is same as All India Rank (CRL).")


per_12th = st.number_input("Enter Class 12th Aggregate %:", min_value=0.0, max_value=100.0, value=75.0)
top20 = st.radio("Are you in Top 20 percentile of your board? (yes/no):", ["no", "yes"])

# बोर्ड चेक करने का लॉजिक
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
    
    # मेन्स मार्क्स स्क्रीनिंग
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
        
        # एडवांस सेक्शन
        st.write("### 3. JEE Advanced Rank List Criteria Checking")
        
        p_val = st.number_input("Enter total marks in Physics (Paper 1 + 2):", min_value=0.0, max_value=120.0, value=15.0)
        c_val = st.number_input("Enter total marks in Chemistry (Paper 1 + 2):", min_value=0.0, max_value=120.0, value=15.0)
        m_val = st.number_input("Enter total marks in Mathematics (Paper 1 + 2):", min_value=0.0, max_value=120.0, value=15.0)

        final_sum = p_val + c_val + m_val
        
        adv_limits = {
            "GENERAL":,
            "EWS":,
            "OBC-NCL":,
            "SC":,
            "ST":,
            "PwBD":
        }

        sub_limit = adv_limits[cat]
        agg_limit = adv_limits[cat]
        
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
        
        if chk_sub and chk_agg:
            st.write("### Congratulations! You qualified for IIT Rank List!")
            
            # बिल्कुल सिंपल और छात्र जैसा एडवांस रैंक प्रेडिक्शन लॉजिक
            adv_rank = 60000
            if final_sum >= 300:
                adv_rank = 100
            elif final_sum >= 250:
                adv_rank = 800
            elif final_sum >= 200:
                adv_rank = 2500
            elif final_sum >= 170:
                adv_rank = 5000
            elif final_sum >= 140:
                adv_rank = 9000
            elif final_sum >= 110:
                adv_rank = 15000
            elif final_sum >= agg_limit:
                adv_rank = 25000
                
            st.write("Your expected JEE Advanced All India Rank (CRL) is around:", adv_rank)
            
            # सिंपल एडवांस कैटेगरी रैंक लॉजिक
            adv_cat_rank = adv_rank
            if cat == "OBC-NCL":
                adv_cat_rank = int(adv_rank * 0.25)
            elif cat == "EWS":
                adv_cat_rank = int(adv_rank * 0.10)
            elif cat == "SC":
                adv_cat_rank = int(adv_rank * 0.15)
            elif cat == "ST":
                adv_cat_rank = int(adv_rank * 0.05)
            elif cat == "PwBD":
                adv_cat_rank = int(adv_rank * 0.03)
                
            if cat != "GENERAL":
                st.write("Your expected JEE Advanced Category Rank is around:", adv_cat_rank)
            else:
                st.write("Your JEE Advanced Category Rank is same as All India Rank (CRL).")
                
        else:
            st.write("Result: Not qualified for IIT Rank List.")
            if not chk_sub:
                st.write("- Failed subject-wise minimum passing marks.")
            if not chk_agg:
                st.write("- Total score is below required aggregate.")
    else:
        st.write("Advanced analysis locked because JEE Main cutoff not cleared.")




