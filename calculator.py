import streamlit as st

# Function to evaluate Buffett's criteria
def evaluate_buffett_strategy(earnings_history, roe, debt_equity, management_score, price_to_value):
    # Implement logic to evaluate the company based on the criteria
    # For simplicity, this example uses basic checks
    score = 0
    if earnings_history == 'Consistent':
        score += 1
    if roe >= 15:  # Example threshold
        score += 1
    if debt_equity < 0.5:  # Example threshold
        score += 1
    if management_score > 7:  # Out of 10
        score += 1
    if price_to_value == 'Undervalued':
        score += 1

    return score

# Streamlit UI
st.title("Warren Buffett's Trading Strategy Calculator")

with st.form("buffett_form"):
    st.subheader("Enter Company Financials:")
    earnings_history = st.selectbox("Earnings History:", ['Consistent', 'Inconsistent'])
    roe = st.number_input("Return on Equity (ROE) %:", min_value=0.0, max_value=100.0, value=15.0)
    debt_equity = st.number_input("Debt-to-Equity Ratio:", min_value=0.0, max_value=10.0, value=0.5)
    management_score = st.slider("Management Score (1-10):", 1, 10, 5)
    price_to_value = st.selectbox("Price to Intrinsic Value:", ['Undervalued', 'Fair', 'Overvalued'])

    submitted = st.form_submit_button("Evaluate")
    if submitted:
        score = evaluate_buffett_strategy(earnings_history, roe, debt_equity, management_score, price_to_value)
        st.write(f"Buffett Strategy Score: {score}/5")

