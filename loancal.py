#!/usr/bin/env python3
"""Loan Risk Assessment Calculator - Simple Version"""

class LoanApplication:
    def __init__(self, loan_id, credit_score, ltv, dti, income, employment_years):
        self.loan_id = loan_id
        self.credit_score = credit_score
        self.ltv = ltv
        self.dti = dti
        self.income = income
        self.employment_years = employment_years
        
    def calculate_risk_score(self):
        """Calculate risk score (1-10, higher = more risky)"""
        risk_score = 0
        
        # Credit score component (0-3 points)
        if self.credit_score < 620:
            risk_score += 3
        elif self.credit_score < 680:
            risk_score += 2
        elif self.credit_score < 720:
            risk_score += 1
            
        # LTV component (0-3 points)
        if self.ltv > 0.95:
            risk_score += 3
        elif self.ltv > 0.85:
            risk_score += 2
        elif self.ltv > 0.80:
            risk_score += 1
            
        # DTI component (0-2 points)
        if self.dti > 0.45:
            risk_score += 2
        elif self.dti > 0.40:
            risk_score += 1
            
        # Employment stability (0-2 points)
        if self.employment_years < 1:
            risk_score += 2
        elif self.employment_years < 2:
            risk_score += 1
            
        return risk_score
    
    def get_recommendation(self):
        """Return loan recommendation based on risk score"""
        risk_score = self.calculate_risk_score()
        
        if risk_score <= 3:
            return "APPROVE", "Low risk profile"
        elif risk_score <= 6:
            return "APPROVE WITH CONDITIONS", "Medium risk - require additional documentation"
        else:
            return "DECLINE", "High risk - does not meet lending standards"
    
    def display_analysis(self):
        """Print formatted loan analysis"""
        recommendation, reason = self.get_recommendation()
        risk_score = self.calculate_risk_score()
        
        print(f"\n{'='*60}")
        print(f"LOAN ANALYSIS: {self.loan_id}")
        print(f"{'='*60}")
        print(f"\nApplicant Profile:")
        print(f"  Credit Score:    {self.credit_score}")
        print(f"  LTV Ratio:       {self.ltv*100:.1f}%")
        print(f"  DTI Ratio:       {self.dti*100:.1f}%")
        print(f"  Annual Income:   ${self.income:,}")
        print(f"  Employment:      {self.employment_years} years")
        print(f"\nRisk Assessment:")
        print(f"  Risk Score:      {risk_score}/10")
        print(f"  Recommendation:  {recommendation}")
        print(f"  Reason:          {reason}")
        print(f"\n{'='*60}\n")


def main():
    """Test the loan risk calculator with sample applications"""
    print("\nLOAN RISK ASSESSMENT SYSTEM")
    print("="*60)
    
    # Sample loan applications
    loans = [
        LoanApplication("L001", 740, 0.75, 0.32, 95000, 5),
        LoanApplication("L002", 650, 0.92, 0.44, 68000, 1.5),
        LoanApplication("L003", 620, 0.96, 0.48, 52000, 0.8),
        LoanApplication("L004", 780, 0.65, 0.25, 125000, 8),
    ]
    
    # Analyze each loan
    for loan in loans:
        loan.display_analysis()
    
    # Summary statistics
    print(f"\n{'='*60}")
    print("PORTFOLIO SUMMARY")
    print(f"{'='*60}")
    print(f"Total Applications: {len(loans)}")
    
    avg_risk = sum(loan.calculate_risk_score() for loan in loans) / len(loans)
    print(f"Average Risk Score: {avg_risk:.1f}/10")
    
    recommendations = [loan.get_recommendation()[0] for loan in loans]
    print(f"\nRecommendation Breakdown:")
    print(f"  Approve:                 {recommendations.count('APPROVE')}")
    print(f"  Approve with Conditions: {recommendations.count('APPROVE WITH CONDITIONS')}")
    print(f"  Decline:                 {recommendations.count('DECLINE')}")
    print(f"\n{'='*60}\n")


if __name__ == "__main__":
    main()