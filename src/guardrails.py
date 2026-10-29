"""
SEBI Compliance & Adviser Approval Guardrails
"""

BANNED_KEYPHRASE = ["guarantee", "assured return", "risk free 20%", "double my money"]

def AuditGuardrails(user_prompt: str, persona_age: int, requested_equity: float) -> dict:
    flags = []
    is_safe = True
    
    if any(phrase in user_prompt.lower() for phrase in BANNED_KEYPHRASE):
        flags.append("VIOLATION: Promising or requesting guaranteed/fixed returns is illegal under SEBI RIA Regs 2013.")
        is_safe = False
        
    if persona_age >= 65 and requested_equity > 0.40:
        flags.append("WARNING: Senior Citizen persona allocation exceeds safe equity exposure threshold (Max 40%).")
        is_safe = False
        
    return {
        "passed": is_safe,
        "flags": flags,
        "disclaimer": "DISCLAIMER: Mutual Fund investments are subject to market risks. Read all scheme related documents carefully."
    }