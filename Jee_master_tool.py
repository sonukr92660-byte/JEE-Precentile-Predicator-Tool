import sys

def main_predictor():
    print("\n--- JEE Main Percentile Predictor ---")
    try:
        score = float(input("Enter your expected marks out of 300: "))
        if score < 0 or score > 300:
            print("Invalid marks! Enter between 0 and 300.")
            return
        
        if score >= 250: res = "99.9 - 100.0"
        elif score >= 200: res = "99.2 - 99.8"
        elif score >= 170: res = "98.5 - 99.1"
        elif score >= 150: res = "97.5 - 98.4"
        elif score >= 130: res = "96.0 - 97.4"
        elif score >= 110: res = "93.5 - 95.9"
        elif score >= 90:  res = "89.0 - 93.4"
        elif score >= 70:  res = "80.0 - 88.9"
        elif score >= 50:  res = "70.0 - 79.9"
        else: res = "Below 70.0"
        
        print(f"Your expected percentile range is: {res}")
    except ValueError:
        print("Please enter numeric digits only.")

def check_jee_eligibility():
    print("\n--- JEE Eligibility Checker ---")
    print("Options: GENERAL, EWS, OBC-NCL, SC, ST, PwBD")
    cat = input("Enter your category: ").strip().upper()
    
    list_cat = ["GENERAL", "EWS", "OBC-NCL", "SC", "ST", "PwBD"]
    if cat not in list_cat:
        print("Wrong category entered.")
        return

    try:
        12th_per = float(input("Enter Class 12th Aggregate %: "))
        top20 = input("Are you in Top 20 percentile of your board? (yes/no): ").strip().lower()
    except ValueError:
        print("Invalid percentage input.")
        return

    is_board_ok = False
    if cat in ["SC", "ST", "PwBD"]:
        if 12th_per >= 65.0 or top20 == "yes":
            is_board_ok = True
    else:
        if 12th_per >= 75.0 or top20 == "yes":
            is_board_ok = True

    if not is_board_ok:
        print(f"You don't satisfy Class 12th criteria for {cat}.")
    else:
        print(f"Board criteria satisfied for {cat} category.")

    try:
        mains_p = float(input("Enter your overall JEE Mains Percentile: "))
    except ValueError:
        print("Invalid percentile input.")
        return

    mains_data = {
        "GENERAL": 93.41,
        "EWS": 82.42,
        "OBC-NCL": 80.92,
        "SC": 63.92,
        "ST": 52.02,
        "PwBD": 0.0023
    }

    is_mains_ok = False
    if mains_p >= mains_data[cat]:
        is_mains_ok = True
        print(f"Qualified for JEE Advanced! (Cutoff for {cat} was {mains_data[cat]})")
    else:
        print(f"Not qualified for JEE Advanced. Cutoff was {mains_data[cat]}")

    if is_mains_ok:
        print("\n--- JEE Advanced Rank List Criteria Checking ---")
        try:
            p_val = float(input("Enter total marks in Physics (Paper 1 + 2): "))
            c_val = float(input("Enter total marks in Chemistry (Paper 1 + 2): "))
            m_val = float(input("Enter total marks in Mathematics (Paper 1 + 2): "))
        except ValueError:
            print("Invalid marks input.")
            return

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
        
        print(f"\nPassing rules for {cat}:")
        print(f"- Minimum marks required in EACH subject: {sub_limit}")
        print(f"- Minimum aggregate marks required: {agg_limit}")
        
        chk_p = p_val >= sub_limit
        chk_c = c_val >= sub_limit
        chk_m = m_val >= sub_limit
        chk_sub = chk_p and chk_c and chk_m
        chk_agg = final_sum >= agg_limit
        
        print(f"\nYour Advanced Scores:")
        print(f"Total Obtained: {final_sum} / 360")
        print(f"P = {p_val}, C = {c_val}, M = {m_val}")
        
        if chk_sub and chk_agg and is_board_ok:
            print(f"\nCongratulations! You have cleared all cutoffs and qualified for IIT Rank List!")
        else:
            print(f"\nResult: Not qualified for IIT Rank List.")
            if not is_board_ok:
                print("- Failed 12th board criteria.")
            if not chk_sub:
                print("- Failed subject-wise minimum passing marks.")
                if not chk_p: print(f"  -> Physics marks below {sub_limit}")
                if not chk_c: print(f"  -> Chemistry marks below {sub_limit}")
                if not chk_m: print(f"  -> Mathematics marks below {sub_limit}")
            if not chk_agg:
                print(f"- Total score is below required aggregate of {agg_limit}")
    else:
        print("\nAdvanced analysis locked because JEE Main cutoff not cleared.")

def start():
    while True:
        print("\n*** JEE MASTER TOOL ***")
        print("1. Predict Percentile")
        print("2. Check Complete JEE Eligibility")
        print("3. Exit")
        
        user_choice = input("Select option (1/2/3): ").strip()
        if user_choice == "1":
            main_predictor()
        elif user_choice == "2":
            check_jee_eligibility()
        elif user_choice == "3":
            print("Exiting tool. Good luck!")
            sys.exit()
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    start()
