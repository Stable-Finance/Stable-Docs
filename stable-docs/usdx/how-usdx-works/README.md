---
description: This Page Outlines How USDX Works
---

# How USDX Works

## Overview

USDX is a USD-pegged stablecoin backed by a reserve portfolio of U.S. residential mortgages, agency mortgage-backed securities (MBS), and liquid reserves. Stable built USDX to bring the collateral class that underwrites the American dollar — residential mortgage debt — onchain, and to make the yield of mortgage capital markets composable as a digital asset.

USDX is overcollateralized: the protocol targets a reserve book value of at least 102% of outstanding USDX supply. Redemption against reserves is the primary peg mechanism, supported by repo facilities against agency MBS, onchain liquidity pools, and structural mortgage-repayment demand. See [Redeeming USDX](../redeeming-usdx.md) for how dollar liquidity is delivered.

By staking USDX, holders can gain exposure to the [yield of the mortgage portfolio](../staking-usdx.md) through mUSDX, a non-rebasing yield-bearing token.

## How USDX Works

#### 1. The reserve

USDX is backed by a reserve portfolio composed of four asset classes: agency MBS (credit-risk-free, guaranteed by Fannie Mae, Freddie Mac, or Ginnie Mae), whole mortgage loans, tokenized mortgages sourced through Stable's native origination channel, and liquid reserves (supported stablecoins, short-duration Treasuries, and cash). Every USDX in circulation is backed by this reserve.

#### 2. Minting

USDX is minted through two surfaces. Anyone can mint permissionlessly by depositing a supported stablecoin and receiving USDX 1:1, less a small mint fee. Institutional partners who have completed KYB/KYC can mint by depositing eligible mortgage collateral — whole loans or agency MBS — and receiving USDX against the mark-to-market value of those assets. Both surfaces route deposits into the same reserve portfolio and produce the same USDX token. See [Minting USDX](../minting-usdx.md) for asset-class eligibility.

#### 3. Earning yield (mUSDX)

The reserve portfolio generates yield from mortgage coupons, MBS interest, and liquid-reserve returns. Holders who stake USDX receive [mUSDX](../staking-usdx.md), whose exchange rate rises as that net yield accrues — so each mUSDX redeems for a growing amount of USDX over time. USDX held unstaked does not earn yield and behaves as a cash-equivalent dollar.

#### 4. Redemption

USDX holders can redeem for dollars against the reserve through a tiered redemption queue (a standard window and an expedited window for a higher fee), or — for approved institutional participants — for the underlying mortgage assets or MBS. Redemption against reserves at par is what anchors the USDX peg. See [Redeeming USDX](../redeeming-usdx.md).

## Whitepaper

You can find the USDX Whitepaper [here in the docs](../../../usdx-whitepaper/) or in full in the [Whitepaper GitHub Repository](https://github.com/Stable-Finance/whitepaper/).
