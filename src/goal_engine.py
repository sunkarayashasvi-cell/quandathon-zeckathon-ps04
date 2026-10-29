"""
Goal-Based Financial Planning & Glide Path Engine
"""

def calculate_goal_plan(current_cost: float, years: int, inflation_rate: float = 0.055, expected_return: float = 0.11):
    future_corpus = current_cost * ((1 + inflation_rate) ** years)
    
    r = expected_return / 12
    n = years * 12
    if n > 0 and r > 0:
        sip_amount = future_corpus / (((((1 + r) ** n) - 1) / r) * (1 + r))
    else:
        sip_amount = 0
        
    return {
        "future_corpus": round(future_corpus, 2),
        "monthly_sip": round(sip_amount, 2),
        "inflation_used": inflation_rate,
        "expected_return_used": expected_return
    }

def generate_glide_path(years: int, initial_equity_pct: float):
    trajectory = []
    for yr in range(1, years + 1):
        remaining = years - yr
        if remaining <= 2:
            eq = max(0.15, initial_equity_pct - 0.35)
        elif remaining <= 5:
            eq = max(0.30, initial_equity_pct - 0.20)
        else:
            eq = initial_equity_pct
            
        trajectory.append({
            "Year": f"Year {yr}",
            "Equity %": round(eq * 100, 1),
            "Debt %": round((1 - eq) * 100, 1)
        })
    return trajectory