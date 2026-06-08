# Table of Contents

## Table of Contents

1. **Introduction**

> The U.S. dollar is a claim on a broad economic base whose largest single loan category is residential mortgages; today's stablecoins do not inherit that breadth.

2. **Background**

> The U.S. mortgage market, agency MBS, and the current state of stablecoins — the context USDX is designed for.

3. **System Overview**

> USDX is a multi-component protocol with four interacting subsystems: collateral, mint-and-redeem, yield, and the token-and-safety system.

4. **Collateral Framework**

> The reserve portfolio is composed of agency MBS, whole mortgage loans, tokenized mortgages, and liquid reserves, each operating within an allocation range.

5. **Mint and Redeem**

> Two minting surfaces — permissionless (stablecoin → USDX 1:1) and institutional (collateral → USDX) — and a tiered redemption queue against reserves.

6. **mUSDX: Staked USDX**

> A non-rebasing, exchange-rate staked wrapper that passes the mortgage portfolio's net yield to holders, with a cooldown for unstaking.

7. **Peg Stability**

> A layered apparatus: primary redemption against reserves, repo-backed liquidity, liquidity-pool arbitrage, an autonomous peg-maintenance bot, and structural mortgage-repayment demand.

8. **Risk Management and the Loss Waterfall**

> A four-step loss waterfall operating in strict seniority, routing losses through buffer mechanisms before they can impact USDX holders.

9. **The RATES Token**

> Validators stake RATES to attest loan data gating new collateral, and RATES stakers provide the first-loss safety module.

10. **Technical Architecture**

> Smart-contract system, multi-provider oracle design for MBS and whole-loan pricing, and proof-of-reserve.

11. **Native Origination Channel**

> Sourcing newly originated mortgage collateral directly, aligning origination quality with reserve quality.

12. **Regulatory Framework**

> A payment-stablecoin posture: licensed issuance, qualifying reserves, an enforceable redemption right, KYC/AML, and securities considerations.

13. **Roadmap**

> Phased development, each phase concluding with a publicly attested, audited protocol-level milestone.

14. **Related Work**

> How USDX relates to fiat-backed, crypto-collateralized, algorithmic, delta-neutral, and tokenized-RWA stablecoins.

15. **Conclusion**
16. **References**
17. **Appendix A — Glossary**
18. **Appendix B — Key Formulas and Parameters**
19. **Appendix C — RATES Reference**
