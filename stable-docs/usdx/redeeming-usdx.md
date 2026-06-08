---
description: This Page Outlines How USDX is Redeemed
---

# Redeeming USDX

## Context

USDX can be redeemed for the underlying mortgage assets or fiat (USD).

### Redemption Execution

Stable is working towards USDX redemptions with instant settlement (atomic redemptions). Today, execution and time to settlement depend on the redemption asset, which can be mortgage asset(s), mortgage backed securities (MBS), stablecoin, or fiat.

* Mortgage asset and MBS redemptions occur onchain and can be processed 24/7/365.
  * Fractions of mortgage asset and MBS redemptions occur in USDC
    * Example: a 10,000,000 USDX mortgage asset redemption may receive 20 mortgage assets and 82,180.29 USDC
  * Stable may limit the type and number of mortgage assets and MBS available
* Fiat redemptions can execute:&#x20;
  * Onchain 24/7/365 with the redeemer receiving USDC, a GENIUS-compliant stablecoin backed by US Treasuries
  * Offchain as a Wire or ACH transfer
    * Offchain requires 1-3 business days to settle (1-5+ for international)&#x20;

### Redemption Details

Approved entities that have undergone KYB/KYC can redeem USDX for mortgages, mortgage backed securities, dollar-backed stablecoins, or dollars with various fees and settlement times.

<table><thead><tr><th>Redemption Instrument</th><th width="149.5">Minimum</th><th width="150.046875">Increment</th><th width="149.9609375">Fee</th></tr></thead><tbody><tr><td><strong>Mortgages</strong></td><td>500,000 USDX</td><td>500,000 USDX</td><td>Market Rate</td></tr><tr><td><strong>Mortgage Backed Securities</strong></td><td>1,000,000 USDX</td><td>100,000 USDX</td><td>Market Rate</td></tr><tr><td><strong>USDC</strong></td><td>100 USDX</td><td>1 USDX</td><td>0.5%</td></tr><tr><td><strong>USD Cash (1-3 Days)</strong></td><td>100,000 USDX</td><td>25,000 USDX</td><td>0.5%</td></tr></tbody></table>

If real estate was deposited, and USDX was minted against the value of that real estate, then USDX can be redeemed to pay off the balance of that debt subject to the terms of the relevant agreement(s).

Note: Currently redemptions take 7 days to process. This can be accelerated for a higher fee.
