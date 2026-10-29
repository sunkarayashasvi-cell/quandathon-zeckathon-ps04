"""
Risk Profiling & Conflict Resolution Engine
Enforces capacity primacy over tolerance per SEBI guidelines.
"""

CAPACITY_SCORES = {"Low": 1, "Moderate": 2, "High": 3}
TOLERANCE_SCORES = {"Low": 1, "Moderate": 2, "High": 3, "Very High": 4}

PERSONA_PROFILES = {
    "Fresh Graduate (Bengaluru)": {
        "age": 23, "income": 55000, "dependents": 0,
        "capacity": "Moderate", "tolerance": "High",
        "details": "Take-home ₹55k/mo, single, zero debt. Target: Emergency fund + long-term wealth."
    },
    "Young Couple (Pune)": {
        "age": 31, "income": 120000, "dependents": 1,
        "capacity": "Moderate", "tolerance": "Moderate",
        "details": "Dual income, ongoing home loan EMI. Target: Child education in 15 yrs."
    },
    "Small Business Owner (Surat)": {
        "age": 44, "income": 200000, "dependents": 3,
        "capacity": "Moderate", "tolerance": "High",
        "details": "Irregular business cash flow, high liquid reserves. Target: Retirement at 58."
    },
    "Doctor (Patna)": {
        "age": 38, "income": 300000, "dependents": 2,
        "capacity": "High", "tolerance": "Low",
        "details": "High stable income, under-invested, risk-averse. Target: Retirement + Parents care."
    },
    "Retiree (Chennai)": {
        "age": 68, "income": 40000, "dependents": 1,
        "capacity": "Low", "tolerance": "Low",
        "details": "₹80 Lakh corpus + pension. Target: Stable monthly SWP for 25 yrs."
    },
    "Aggressive Trader (Mumbai)": {
        "age": 29, "income": 80000, "dependents": 0,
        "capacity": "Low", "tolerance": "Very High",
        "details": "F&O trading losses, unstable income, seeking rapid returns."
    }
}

def resolve_risk_profile(capacity: str, tolerance: str) -> dict:
    cap_val = CAPACITY_SCORES.get(capacity, 2)
    tol_val = TOLERANCE_SCORES.get(tolerance, 2)
    
    conflict = cap_val < tol_val
    
    # Enforce capacity primacy rule
    effective_score = min(cap_val, tol_val) if conflict else cap_val
    
    profile_map = {
        1: ("Conservative", "20/80 Equity-Debt", 0.20),
        2: ("Moderate / Balanced", "50/50 Equity-Debt", 0.50),
        3: ("Aggressive Growth", "75/25 Equity-Debt", 0.75)
    }
    
    name, allocation, equity_pct = profile_map.get(effective_score, ("Moderate", "50/50", 0.50))
    
    resolution_note = (
        "⚠️ CONFLICT DETECTED: Psychological risk tolerance exceeds financial capacity. "
        "Per SEBI suitability standards, risk profile is hard-capped to Financial Capacity level."
        if conflict else
        "Capacity and Tolerance are aligned. Standard allocation applied."
    )
    
    return {
        "conflict_flag": conflict,
        "effective_profile": name,
        "allocation_label": allocation,
        "equity_pct": equity_pct,
        "resolution_note": resolution_note
    }