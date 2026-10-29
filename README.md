# Quandathon Co-Pilot | SEBI RIA Workstation 📈
> **Zeckathon Problem Statement 04 Submission**

An AI Co-pilot that empowers SEBI-registered Investment Advisers (RIAs) to serve 1,000+ clients safely with Human-in-the-Loop approval, citation-backed RAG, and strict risk capacity matrix rules.

---

## 🎯 Features Implemented
1. **Risk Profiling & Conflict Engine**: Separates Risk Capacity from Risk Tolerance. Enforces **Capacity Primacy** during conflicts.
2. **Inflation-Adjusted Goal Engine**: Computes corpus target and SIP with glide path trajectory.
3. **AMFI Direct Fund Portfolio**: Real AMFI shortlist with 10-year backtest simulation.
4. **Citation-Backed RAG**: Page-level SID disclosures.
5. **Human-In-The-Loop Approval**: SEBI regulatory guardrails blocking guaranteed return claims.

---

## 🚀 Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py