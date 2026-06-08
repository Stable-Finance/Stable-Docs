# Collateral Framework

## 4. Collateral Framework

### 4.1 Composition

The USDX reserve portfolio is composed of four asset classes. Each operates within an allocation range rather than a fixed target; the ranges below describe steady-state operation at scale, and the portfolio may sit well outside them in early operation (notably far more liquid) as described in this section:

| Asset Class | Allocation Range | Primary Function |
| --- | --- | --- |
| Agency MBS | 0%–80% | Credit-risk-free yield-generating reserve |
| Whole loans and warehouse lines | 0%–60% | Higher-yield, shorter-duration component |
| Tokenized mortgages | 0%–100% | Directly originated onchain collateral |
| Liquid reserves | 0%–100% | Redemption liquidity and operational buffer |

The ranges are wide by design. The protocol is built to operate across a spectrum of portfolio compositions reflecting both scale and market conditions. In early operation, when onchain origination is limited and MBS acquisition is ramping, the portfolio may be almost entirely liquid reserves — potentially close to 100%. As origination grows and institutional relationships mature, MBS and whole loans become meaningful components. The allocation ranges in the table describe the intended steady state, not a constraint the protocol must satisfy from day one.

Liquid reserves include supported stablecoins, short-duration U.S. Treasury bills held onchain or off-chain, balances at insured banking partners, pre-negotiated repurchase agreement capacity against MBS holdings, and positions in whitelisted onchain lending protocols that permit rapid withdrawal. What qualifies as a liquid reserve is any asset or facility that can produce redemption liquidity within one to three business days without forced sale of longer-duration collateral.

### 4.2 Agency Mortgage-Backed Securities

Agency MBS are a foundational reserve asset. The protocol maintains exposure to MBS issued by Fannie Mae, Freddie Mac, and Ginnie Mae, with a preference for pools with stable prepayment characteristics and coupons near current market rates.

Agency MBS are acquired through regulated broker-dealer relationships in the TBA market and the specified pool market. All securities are held by a qualified custodian in segregated accounts under the name of a bankruptcy-remote special purpose vehicle controlled by Stable Company. Stable Company does not commingle protocol assets with operating capital under any circumstances; the Articles of the SPV and associated trust documents enforce this separation.

The primary risks on agency MBS are interest rate and prepayment risk:

- Falling rates accelerate prepayments, causing MBS to pay down principal at par faster than scheduled. This creates reinvestment risk: the protocol must redeploy principal at lower yields.
- Rising rates decelerate prepayments and depress MBS market prices. The portfolio's book value declines, though held-to-maturity accounting allows the portfolio to continue earning its original coupon.

These risks are addressed by duration management, interest rate hedging where cost-effective, and transparency of the portfolio's current mark-to-market and book values to USDX and mUSDX holders via the proof-of-reserve infrastructure.

### 4.3 Whole Mortgage Loans

The protocol may hold an allocation to whole mortgage loans — loans owned directly by the reserve SPV rather than wrapped in an MBS structure. Whole loans typically yield 50–150 basis points above comparable MBS in ordinary market conditions, reflecting compensation for credit risk, illiquidity, and servicing complexity.

Whole loans held by the protocol are subject to underwriting and concentration guidelines that scale with the size of the portfolio:

- **Underwriting quality.** Whole loans are underwritten to agency-eligible standards or to defined non-QM standards with documented compensating factors. The protocol does not restrict itself exclusively to conforming product; it may hold agency-eligible non-QM loans where the credit profile and pricing justify inclusion.
- **Loan-to-value discipline.** For loans the protocol originates or underwrites directly, the reserve targets conservative loan-to-value ratios so that the underlying property provides an equity cushion against credit loss. This is an underwriting target for directly originated collateral, not a ceiling on every asset the reserve may hold: agency-guaranteed loans and seasoned bonds the protocol acquires may carry higher original LTVs (a conforming loan can be originated at up to 97% LTV), because on agency collateral the credit risk is borne by the agency guarantee rather than by the protocol.
- **Geographic diversification.** As the whole-loan portfolio grows, the protocol targets geographic diversification to avoid concentration in any single state or metropolitan area. Early portfolios will necessarily be more concentrated; diversification is a target the protocol grows into as origination volume scales, not a constraint that can be satisfied at small portfolio sizes.
- **Performance requirements.** Loans must be current at acquisition. A loan that becomes 60+ days delinquent is marked down or removed from the reserve calculation and classified as non-performing until resolution.

Whole loans are acquired through forward purchase agreements with originators and through warehouse lines against which the protocol funds inventory. Warehouse lines allow the protocol to hold loans temporarily while MBS pool formation or securitization is pending.

### 4.4 Tokenized Mortgages

Tokenized mortgages are loans the protocol sources through a native onchain origination channel, whether originated by Stable or by licensed partners. They are represented onchain with metadata encoding origination terms, current principal balance, payment history, and lien status, and they may enter the reserve at the moment of origination.

The underlying legal instrument is a traditional note and recorded lien, governed by applicable state law. Today the onchain representation tracks that off-chain legal record; where the two differ, the recorded legal instrument governs. The mechanics of onchain mortgage origination, servicing, and the legal architecture that supports them are specified in a separate paper and are outside the scope of this document.

The relevance of tokenized mortgages to USDX is narrow and specific: they let the reserve grow with newly originated collateral sourced directly, rather than only through secondary-market purchases, which aligns the quality of newly created collateral with the quality of the reserve. For the purposes of this paper, a tokenized mortgage is simply one of the four reserve asset classes, serviced by a licensed mortgage servicer and carried in the reserve like any other whole-loan exposure.

### 4.5 Liquid Reserves

The protocol maintains a liquid reserve allocation sized to meet anticipated redemption flow. In steady-state operation at scale this is a minority of the portfolio, but in early operation it may be the substantial majority — the protocol does not impose a fixed ceiling on how liquid it may be. Liquid reserves are composed of any combination of:

- Supported stablecoins held in smart contracts with multi-signature governance;
- Short-duration U.S. Treasury bills, held onchain as tokenized Treasuries or off-chain via a qualified broker-dealer;
- Cash at FDIC-insured banking partners;
- Repurchase agreement capacity against MBS holdings, both committed and uncommitted;
- Positions in whitelisted onchain lending protocols that permit rapid withdrawal.

On repo capacity: a committed line is one a counterparty is contractually obligated to fund against the protocol's MBS, typically in exchange for a commitment fee; an uncommitted line is one a counterparty is expected but not obligated to fund. The protocol distinguishes the two because only committed capacity is reliable in stressed markets — precisely when it is most needed — and the protocol sizes its committed lines accordingly rather than relying on uncommitted capacity that may not be available in a crisis.

The liquid reserve serves three purposes:

1. Redemption liquidity for the default and expedited redemption paths (Section 5).
2. Operational buffer for routine protocol expenses (custody fees, servicing fees, audit costs, legal fees).
3. Duration counterweight that offsets a portion of the longer-duration exposure in the MBS allocation, smoothing the portfolio's net interest rate sensitivity.

### 4.6 Overcollateralization

USDX is overcollateralized, but not by a single fixed ratio. Overcollateralization is produced by the combination of three structural features:

- **Credit protection on MBS:** Agency MBS carry no credit risk to the protocol. Every dollar of par value is guaranteed by the issuing agency.
- **Underwriting discipline on directly originated collateral:** Loans the protocol originates or underwrites directly are underwritten conservatively so that the underlying property provides an equity cushion against credit loss. (As noted in Section 4.3, this discipline applies to collateral the protocol underwrites itself, not to agency-guaranteed loans whose credit risk is borne by the agency.)
- **First-loss capital:** A layered stack of first-loss capital absorbs losses before any impact flows through to USDX holders (Section 8).

The protocol targets a portfolio book-value collateralization of at least 102%. This is a target maintained through reserve management — the accumulation of mint and redemption fees, retained spread, and disciplined asset selection — not a continuously guaranteed invariant. Market events can move the ratio, which is precisely why the loss waterfall (Section 8) exists. Formally, let A_t be the book value of reserves at time t and S_t be the outstanding USDX supply at time t. The target is:

> A_t ≥ 1.02 · S_t

Sustained or severe breaches of this target trigger governance review and, where necessary, draws on the loss waterfall to restore the ratio.

### 4.7 Custody

All reserve assets are held in custody arrangements that meet institutional fiduciary standards:

- **Agency MBS:** qualified custodian (e.g., Bank of New York Mellon, State Street), held in segregated accounts under the name of the reserve SPV.
- **Whole loans:** held in the name of the reserve SPV, with note custody by a document custodian and servicing rights contracted to a licensed sub-servicer.
- **Supported stablecoins and onchain assets:** multi-signature smart contract wallets with a threshold signing policy, including at least one independent signer.
- **Treasury bills:** qualified broker-dealer account in the name of the reserve SPV, or tokenized Treasury positions held in multi-signature custody onchain.
- **Cash:** FDIC-insured bank accounts at Stable Company's designated banking partner(s).

The protocol publishes a monthly third-party attestation of reserve composition and value, consistent with the disclosure cadence of the largest asset-backed stablecoin issuers, and supplements it with onchain proof-of-reserve infrastructure (Section 10) that lets anyone verify the published figures against the protocol's onchain holdings. The attestation confirms the existence, valuation, and unencumbered status of reserve assets.
