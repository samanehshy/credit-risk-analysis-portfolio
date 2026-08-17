SELECT * FROM credit_risk_db.cleaned_credit_risk LIMIT 10;
SELECT 
    AVG(person_income) AS average_income, 
    AVG(loan_int_rate) AS average_interest_rate
FROM credit_risk_db.cleaned_credit_risk;
DESCRIBE credit_risk_db.cleaned_credit_risk;
SELECT 
    loan_intent, 
    COUNT(*) AS total_loans, 
    AVG(loan_amnt) AS avg_loan_amount, 
    AVG(loan_int_rate) AS avg_interest_rate
FROM credit_risk_db.cleaned_credit_risk
GROUP BY loan_intent;
