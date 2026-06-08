# Introduction

## 1. Introduction

The U.S. dollar, when measured by the assets that support it, is a claim on an extraordinarily broad economic base. Of the approximately $22.6 trillion M2 money supply as of early 2026, roughly $18 trillion resides in the commercial banking system as deposits backed by loans. The single largest loan category on U.S. bank balance sheets is not commercial lending, consumer credit, or corporate debt, but residential mortgages. The Federal Reserve itself holds approximately $2.2 trillion of agency MBS on its balance sheet as of early 2026, making it the largest single mortgage investor in the country. In aggregate, residential mortgages and agency MBS underwrite a substantial share of the institutional dollar.

Stablecoins, in their current form, do not inherit this breadth. Circle's USDC and Tether's USDT — the two largest dollar-pegged tokens by circulation — are backed predominantly by short-duration Treasury bills, overnight repo, and cash held at commercial banks. This is a valid design choice for money-market-like exposure, but it produces a different animal from the fully diversified dollar. Stablecoin reserves today look like the asset side of a government money market fund; the institutional dollar looks like the combined balance sheet of the banking system and the Federal Reserve.

This whitepaper proposes a stablecoin whose collateral composition more closely resembles the latter. USDX is backed by agency MBS, whole mortgage loans, tokenized mortgages, and liquid reserves. Its yield derives from mortgage coupon payments and MBS interest distributions — cashflows that have been the foundation of American housing finance for over fifty years. Its redemption guarantee is rooted in a combination of dollar reserves and repo facilities against MBS holdings, the same liquidity mechanism that the largest money managers and central banks rely on.

The asset class is chosen deliberately. U.S. household real estate is valued at approximately $47.6 trillion as of Q3 2025, against $13.2 trillion in mortgage debt outstanding, yielding roughly $34.4 trillion of homeowner equity — a figure that exceeds the market capitalization of every major public equity index. Most homeowners cannot readily access this equity without refinancing or selling. On the institutional side, agency MBS trade in the To-Be-Announced (TBA) market, which is the second most liquid fixed-income market in the world after U.S. Treasuries. Bringing this collateral onchain addresses inefficiency at both ends of the market: it gives stablecoin holders exposure to an asset class from which they are currently excluded, and it extends the distribution of mortgage cashflows from a small set of institutional allocators to anyone, anywhere, with an internet connection — the largest potential distribution any financial asset has ever had.

The contributions of this paper are:

1. A collateral framework that specifies how agency MBS, whole loans, tokenized mortgages, and liquid reserves combine to back a dollar-pegged stablecoin, including allocation ranges and custody requirements.
2. A dual mint-and-redeem mechanism that accommodates both permissionless user flows (supported stablecoins ↔ USDX) and institutional collateral deposits (MBS or whole loans ↔ USDX), with tiered redemption against underlying reserves.
3. A yield-bearing, permissionless, DeFi-native staked token, mUSDX, that passes mortgage portfolio returns through to holders with exchange-rate accounting and a cooldown for unstaking.
4. A peg-stability apparatus composed of primary redemption, repo-backed liquidity, autonomous onchain market operations, and structural mortgage-repayment demand.
5. A four-step loss waterfall with strict seniority — RATES safety module slashed to exhaustion, stablecoin vault drawn to exhaustion, mUSDX exchange rate reduced up to 67% of accumulated yield, and uncapped new RATES minting as the final backstop — capitalized in the first tranche by RATES token stakers, isolating protocol-level credit and operational risk from stablecoin holders.
6. A native origination channel that allows the reserve to source newly originated mortgage collateral directly, rather than only through secondary-market purchases, aligning origination quality with reserve quality.
7. A technical architecture specification covering smart contracts, multi-provider oracle design for MBS and whole-loan pricing, and proof-of-reserves.

The remainder of this paper develops each of these in detail.
