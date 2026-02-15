import requests
import json

def analyze_loan(credit_score, ltv, dti):
    prompt = f"""Analyze this loan application and identify risk level (Low/Medium/High):

Credit Score: {credit_score}
LTV: {ltv}%
DTI: {dti}%

Respond in 2 sentences."""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:1b", "prompt": prompt, "stream": False}
    )
    
    return response.json()['response']

# Test cases
loans = [
    (740, 75, 32),  # Good loan
    (650, 92, 44),  # Risky loan
    (780, 65, 25),  # Excellent loan
]

print("\nLoan Risk Analysis using Local LLM\n" + "="*50)

for i, (score, ltv, dti) in enumerate(loans, 1):
    print(f"\nLoan {i}:")
    print(f"  Credit: {score}, LTV: {ltv}%, DTI: {dti}%")
    print(f"  Analysis: {analyze_loan(score, ltv, dti)}\n")