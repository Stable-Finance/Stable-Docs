# Peg Stability

## 7. Peg Stability

The USDX peg is maintained by a layered system in which the primary mechanism — direct redemption against reserves — is supported by secondary arbitrage mechanisms that exist to minimize reliance on the primary mechanism in normal operations.

### 7.1 Primary Mechanism: Redemption Against Reserves

The load-bearing peg mechanism is the redemption right. Any holder of USDX can redeem to dollars through the tiered redemption structure specified in Section 5.2. If USDX trades below $1 in the secondary market, arbitrageurs profit by buying USDX at a discount and redeeming at par (net of fees). If USDX trades above $1, the mint path allows arbitrageurs to deposit a supported stablecoin and sell the minted USDX at a premium.

This is the same arbitrage mechanism that anchors every major stablecoin to its peg, and its effectiveness depends on two conditions:

1. Sufficient reserve capacity to process redemption requests on the advertised schedule.
2. Credibility of the redemption right. Users must believe, with justification, that redemptions will be honored on the stated timeline.

Both conditions are addressed by the protocol's reserve management policy (Section 4) and its public audit and proof-of-reserve infrastructure (Section 10).

### 7.2 Repo Facilities for Intraday Liquidity

In periods of elevated redemption demand, the protocol may exhaust its liquid reserves before redemption flow subsides. Rather than force the sale of MBS into the market — which would realize mark-to-market losses and could depress the protocol's book value — the treasury accesses repurchase agreements collateralized by its MBS holdings.

A repo transaction is a short-term borrowing against securities: the protocol delivers MBS to a counterparty in exchange for cash, agreeing to repurchase the MBS at a slightly higher price on a specified future date (typically overnight, but up to 90 days). Agency MBS repo is one of the most liquid short-term funding markets in the world, with daily volumes measured in hundreds of billions of dollars.

The protocol maintains pre-negotiated repo lines with primary dealers and bank counterparties. As described in Section 4.5, the protocol sizes its committed lines — the capacity counterparties are obligated to fund — to be sufficient for stressed conditions, rather than relying on uncommitted capacity that may evaporate in a crisis.

### 7.3 Liquidity Pool Arbitrage

USDX is paired with supported stablecoins in decentralized liquidity pools across its deployed chains. These pools provide a continuous two-sided market for USDX that allows price discovery and small redemption flows to occur onchain without interacting with the protocol treasury. When USDX trades off peg in these pools, arbitrageurs correct the imbalance by routing through the mint or redeem paths.

### 7.4 Autonomous Peg Maintenance

An autonomous peg-maintenance bot (APMB) holds deployable stablecoin capital and uses it to capture arbitrage on meaningful depegs: when USDX trades materially below par on a deployed chain's primary pool the APMB buys USDX to provide bid pressure, and when it trades materially above par the APMB mints and sells USDX to provide supply pressure. A baseline trigger of roughly ±50 basis points applies, though the bot may respond to smaller dislocations where the expected arbitrage is positive after fees.

The APMB draws its operating inventory from the Tranche 2 stablecoin staking vault (Section 8.2), so peg-defense capital scales with external staking interest rather than relying solely on operator treasury. Its activity is automatically suspended whenever the loss waterfall is active, since Tranche 2 capital is then reserved for loss absorption. The APMB is not a mandatory peg mechanism; it smooths short-term pool fluctuations, and the fundamental peg anchor remains redemption against reserves.

### 7.5 Dollar-Denominated Interest Demand

For the institutional mint pathway, borrowers receiving USDX against posted collateral may be required to pay interest in USDX (or in a supported stablecoin at the borrower's option). This creates a structural demand channel for USDX that is independent of speculative flows: interest obligations must be serviced regardless of the prevailing market price of USDX.

### 7.6 Mortgage Repayment Demand

Where the protocol holds mortgage collateral denominated in USDX, borrowers repay principal and interest in USDX at face value. Because each such loan represents a scheduled stream of future USDX-denominated payments, the aggregate originated portfolio produces a recurring, contractual demand for USDX that scales with origination volume. This is a structural demand source independent of speculative flows, and it strengthens the peg in two ways.

**Counter-depeg bid.** A borrower with an upcoming payment can acquire USDX on the open market; if USDX trades below $1.00, the borrower satisfies a face-value obligation with discounted tokens, capturing the discount. This incentive applies to every such borrower simultaneously and creates bid pressure on USDX whenever it trades below par, with depth that scales with the size of the originated portfolio.

**Structural supply contraction.** USDX received in satisfaction of principal is retired from circulation. When a borrower repays a dollar of principal in USDX, the protocol burns the received USDX and reduces the outstanding balance of the corresponding loan in the reserve by the same amount. Both the liability (USDX supply) and the asset (the loan receivable) decrease equally, preserving the collateralization ratio. Over the life of a loan, the full principal minted at origination is contractually returned to the burn contract through scheduled amortization. USDX received for interest is not burned; it flows to the mUSDX exchange rate and the protocol treasury as ordinary portfolio yield.

Importantly, denominating the loan in USDX does not make the underlying debt riskier. The borrower's obligation is a fixed dollar amount; USDX is a dollar instrument redeemable for $1, so repaying in USDX is economically identical to repaying in dollars. The borrower bears no currency or peg risk on their obligation, because the protocol stands ready to treat one USDX as one dollar of principal regardless of secondary-market price. The mechanism is analogous to the peg contribution that CDP repayment provides for crypto-collateralized stablecoins, with two differences of degree: the collateral is residential mortgage debt rather than cryptocurrency, so the repayment stream is decoupled from crypto-market volatility; and the potential scale is far larger, since U.S. mortgage originations run in the hundreds of billions of dollars per quarter.

### 7.7 Supported-Stablecoin Acceptance Policy

A supported mint-accepted stablecoin is automatically suspended from the mint contract if either of two conditions occurs: it trades more than 1% below par within a trailing 72-hour window, or its issuer's redemption process is impaired such that it can no longer be reliably redeemed for a dollar. Acceptance is judged on redeemability, not price alone — a stablecoin that holds its market price but cannot be redeemed at par is as dangerous to the reserve as one trading off-peg.

Once suspended, a stablecoin is re-admitted only after it has both maintained its peg (above $0.99) and demonstrated reliable at-par redemption for a sustained 144-hour (6-day) period. The 144-hour clock begins only after the disqualifying condition has fully cleared; any recurrence resets it.

This policy prevents the protocol from absorbing devalued or unredeemable stablecoins during a crisis. During such periods, USDX remains mintable against MBS and whole-loan collateral via the institutional path.
