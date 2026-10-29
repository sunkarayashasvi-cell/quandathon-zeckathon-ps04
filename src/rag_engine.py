"""
RAG Research Engine with Direct Document & Page Citations
"""

MOCK_SID_DATABASE = [
    {
        "scheme": "Parag Parikh Flexi Cap Direct",
        "doc": "SID_ParagParikh_FlexiCap_2025.pdf",
        "page": 14,
        "content": "The scheme allocates up to 35% in foreign equities (e.g., Alphabet, Microsoft). Exit load is 2% if redeemed within 365 days and 1% between 366-730 days."
    },
    {
        "scheme": "HDFC Short Term Debt Direct",
        "doc": "SID_HDFC_ShortTermDebt_2025.pdf",
        "page": 22,
        "content": "Macaulay duration of the portfolio is maintained between 1 to 3 years. Primary investment in AAA & AA+ rated corporate bonds and G-Secs."
    },
    {
        "scheme": "UTI Nifty 50 Index Direct",
        "doc": "SID_UTI_Nifty50_2025.pdf",
        "page": 8,
        "content": "Tracking error over the last 1 year is maintained below 0.05%. Total Expense Ratio (TER) for Direct plan is capped at 0.18%."
    }
]

def query_rag_engine(query: str) -> dict:
    query_lower = query.lower()
    matches = [entry for entry in MOCK_SID_DATABASE if any(w in entry["content"].lower() or w in entry["scheme"].lower() for w in query_lower.split())]
    
    res = matches[0] if matches else MOCK_SID_DATABASE[0]
    return {
        "answer": res["content"],
        "source_doc": res["doc"],
        "page": res["page"],
        "scheme": res["scheme"],
        "citation": f"Source: {res['doc']} (Page {res['page']}) - SEBI Scheme Disclosure"
    }