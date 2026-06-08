# Underwriting & Risk Management

### Scope

This page describes how collateral enters the USDX reserve, how it is monitored, and how the peg is defended on Solana.

### Borrower-side approval

#### Stable Home Accounts

Before any USDX is deployed against a Stable Home Account, the account holder must pass:

1. KYC / AML verification
2. Title check on the subject property
3. Lien check (existing encumbrances and position)
4. Proof of ownership
5. Verification of existing debts
6. Verification of current property insurance

After the account is approved, **each individual deployment of USDX against the account's home equity is separately approved**. Account approval does not automatically authorize any specific mint.

#### Institutional partners

Partners who wish to mint USDX with anything other than USDC, or redeem for anything other than USDC on Solana, go through KYB via the Stable partner portal. These flows are B2B-only and will remain so. See Minting USDX and Redeeming USDX for asset-class eligibility and minimums.

### Collateral-side diligence — mortgages

* **Geography:** US real property only
* **Property type:** Residential only
* **Lien position:** First-lien and second-lien permitted
* **Maximum combined LTV:** 85% across all liens on the property (senior liens and Stable's lien combined) unless a first lien [qualified mortgage](https://www.investopedia.com/terms/q/qualified-mortgage.asp)
* **Loan type:** Mortgages on US residential real property, represented on-chain as NFTs with recorded liens on the underlying property
* **Servicing:** Loans originated through Stable Home Accounts are serviced by Stable. Loans originated outside Stable Home Accounts are serviced by their respective third-party servicers.

### Ongoing monitoring

Loans in the reserve are monitored for:

* Payment status (current / 30 / 60 / 90+ delinquent)
* Insurance renewal and coverage
* Lien position changes (junior liens, tax liens)
* Collateral value reassessment on a **quarterly** cadence

### Peg stability on Solana

The USDX/USDC peg is defended in real time by an on-chain rebalancer that:

1. Streams the Raydium USDX/USDC CLMM pool via Alchemy Yellowstone gRPC
2. Detects peg deviation the moment it appears
3. Executes an arbitrage swap through Jupiter, routed via Helius RPC
4. Draws on the USDX program's express-redemption USDC vault when the swap requires it

A 5-minute cron-based rebalancing pass runs as a fallback in case the real-time stream is disrupted.

* **Primary liquidity venue:** Raydium USDX/USDC CLMM pool at `EXr7o3CswyovMVZzUoYcQhTqVSGqqZM233E9dMFyoycc`
* **External price feed:** Switchboard USDX/USD at `Z6yHUWH6inzJHruXzFFWsXTApbVsS15WBVoNb4mAAaR`

### Current minting and redemption operations

* **Minting with USDC** is permissionless via [app.trystable.co](https://app.trystable.co) and is instant. Minting with mortgages, MBS, or real estate equity is B2B-only through the partner portal.
* **Redemption for USDC** is permissionless via [app.trystable.co](https://app.trystable.co) and settles within **24 hours to 7 days** depending on the fee selected by the redeemer. Redemption for any other asset type is B2B-only.
* Minting and redemption will both move to KYC/KYB-gated flows in the future. The B2B-only rule for non-USDC mints and non-USDC redemptions on Solana is unchanged.
