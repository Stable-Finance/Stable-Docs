# Appendix B — Key Formulas and Parameters

## 18. Appendix B — Key Formulas and Parameters

**Collateralization Target.**

> A_t ≥ 1.02 · S_t

Where A_t is the aggregate book value of reserves at time t, and S_t is the outstanding USDX supply.

**mUSDX Exchange Rate Update.**

> E_{t+Δ} = E_t · (1 + Y[t, t+Δ] / Vstaked_t)

**Initial Parameter Set.**

| Parameter | Initial Value |
| --- | --- |
| Permissionless mint fee | 10 bps |
| Default redemption window | 7 days |
| Default redemption fee | 20 bps |
| Expedited redemption window | 1–3 business days (best effort) |
| Expedited redemption fee | 60 bps |
| Extended redemption window (max) | 45 days |
| Institutional redemption minimum | 100,000 USDX |
| mUSDX unstaking cooldown | 7 days |
| APMB depeg trigger (baseline) | ± 50 bps ($0.995 / $1.005) |
| Single-transaction cap | 2% of supply |
| Agency MBS allocation range | 0% – 80% |
| Whole loans / warehouse lines range | 0% – 60% |
| Tokenized mortgages range | 0% – 100% |
| Liquid reserves range | 0% – 100% |
| Whole loan and tokenized mortgage LTV cap | 85% |
| Stablecoin depeg threshold | 1% below par |
| Stablecoin suspension window | 72 hours |
| Stablecoin recovery window | 144 hours |
| Loss waterfall Step 1 (T1) cap | To exhaustion |
| Loss waterfall Step 2 (T2) cap | To exhaustion |
| Loss waterfall Step 3 (T3) cap | 67% of accumulated mUSDX yield |
| mUSDX exchange-rate floor in waterfall | 33% of accumulated yield above 1.00 |
| Loss waterfall Step 4 (T4) cap | Uncapped |

All parameters are subject to adjustment within protocol-defined ranges through the governance mechanism specified in Section 9.3.
