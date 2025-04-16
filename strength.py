import streamlit as st
 import re
 
 def calculate_strength(password):
     strength = 0
     length = len(password)
     
     # Points for length
     if length >= 9:
         strength += 1
     if length >= 14:
         strength += 1
         
     # Points for character types
     if re.search(r"[a-z]", password):
         strength += 1
     if re.search(r"[A-Z]", password):
         strength += 1
     if re.search(r"\d", password):
         strength += 1
     if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
         strength += 1
         
     return strength
 
 def strength_level(score):
     if score < 3:
         return "Very Weak", "blue"
     elif score < 6:
         return "Weak", "purple"
     elif score < 9:
         return "Moderate", "pink"
     elif score < 12:
         return "Strong", "green"
     else:
         return "Very Strong", "brown"
 
 st.title("Password Strength Meter")
 
 password = st.text_input("Enter your password:", type="password")
 
 if password:
     score = calculate_strength(password)
     level, color = strength_level(score)
     
     # Display strength level text
     st.markdown(f"Password Strength: <span style='color:{color};'>{level}</span>", unsafe_allow_html=True)
     
     # Display strength bar
     # We map the score (0-6) to a percentage (0-100) for the progress bar
     # Max score is 6 (length>=12 gives 2 points, plus 4 char types)
     strength_percent = min(int((score / 6) * 100), 100) 
     st.progress(strength_percent)
 
     # Feedback based on criteria
     feedback = []
     if len(password) < 8:
         feedback.append("❌ Too short (minimum 8 characters)")
     elif len(password) < 12:
         feedback.append("✔️ Good length (longer is better)")
     else:
          feedback.append("✅ Excellent length (12+ characters)")
 
     if not re.search(r"[a-z]", password):
         feedback.append("❌ Missing lowercase letters")
     else:
         feedback.append("✅ Contains lowercase letters")
         
     if not re.search(r"[A-Z]", password):
         feedback.append("❌ Missing uppercase letters")
     else:
         feedback.append("✅ Contains uppercase letters")
 
     if not re.search(r"\d", password):
         feedback.append("❌ Missing numbers")
     else:
         feedback.append("✅ Contains numbers")
 
     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
         feedback.append("❌ Missing special characters")
     else:
         feedback.append("✅ Contains special characters")
 
     st.markdown("---")
     st.subheader("Feedback:")
     for item in feedback:
         st.markdown(item)
 else:
     # Show placeholder feedback when no password is typed
     st.markdown("---")
     st.subheader("Feedback:")
     st.markdown("Enter a password to see feedback.")
 
 st.caption("Password strength is calculated based on length and character types (lowercase, uppercase, numbers, special characters").