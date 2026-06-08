# Background

## 2. Background

### 2.1 The U.S. Mortgage Market

The U.S. residential mortgage market is one of the largest debt markets in the world, with mortgage balances of approximately $13.2 trillion outstanding as of Q4 2025 and $524 billion of new mortgage originations in that quarter alone. A large majority of outstanding mortgages are either owned or guaranteed by Fannie Mae, Freddie Mac, or Ginnie Mae — the three agencies that support the conforming mortgage market. Mortgages that meet agency underwriting guidelines are typically pooled into mortgage-backed securities guaranteed by these agencies, creating agency MBS, with total agency MBS outstanding of approximately $11–12 trillion — a subset of the broader mortgage-debt total above. Measured by outstanding balance, agency MBS are the second-largest sector of the U.S. bond market, behind only U.S. Treasuries; measured by trading liquidity, the market in which they trade is likewise second only to the Treasury market (the TBA market, described below). It is worth being precise about the comparison: U.S. Treasury debt outstanding (roughly $28 trillion) exceeds total mortgage debt, so the mortgage market is not larger than the Treasury market by size. What sets the underlying asset class apart is not the size of the debt but the size of what secures it — the roughly $50 trillion of U.S. residential real estate behind that $13.2 trillion of debt, an asset base far larger than the Treasury market.

The agency MBS market exists to solve a structural problem in housing finance: individual mortgages are illiquid, heterogeneous, and long-dated, which makes them difficult for originators to hold and for investors to price. By pooling conforming loans and wrapping them in an agency guarantee, the securitization model converts millions of individual mortgages into standardized, liquid, credit-risk-free instruments. This innovation, developed from the late 1960s onward, is what allows a local mortgage to be funded by global capital, and is a primary reason U.S. mortgage rates are lower and mortgage credit more widely available than in most of the world.

Agency MBS are credit-risk-free from the investor's perspective: Fannie Mae and Freddie Mac guarantee timely payment of principal and interest on securities they issue, and Ginnie Mae securities carry the full faith and credit of the U.S. government. Investors in agency MBS bear interest rate risk, prepayment risk, and liquidity risk, but not credit risk on the underlying mortgages.

Agency MBS trade primarily in two venues:

- The **TBA (To-Be-Announced) market**, where pools of MBS are traded forward based on specified characteristics (coupon, issuer, maturity) rather than specific CUSIPs. The TBA market settles monthly and is the second most liquid fixed-income market in the world after Treasuries.
- The **specified pool market**, where buyers purchase specific MBS with known underlying loan characteristics, typically at a premium to TBA pricing.

Prices update continuously during trading hours (roughly 7:00 AM to 5:00 PM Eastern) through dealer quotes and platforms such as Tradeweb and Bloomberg. After hours, pricing relies on end-of-day marks from dealers or pricing services such as ICE and Bloomberg BVAL. This price discovery mechanism is an important input to any onchain representation of MBS collateral, as discussed in Section 10.

### 2.2 Stablecoins Today

As of May 2026, the total stablecoin market capitalization stands at approximately $322 billion, representing more than 50% growth since early 2025. USDC and USDT together account for the majority of circulation. These instruments are dollar-pegged, primarily by holding reserves in short-duration U.S. Treasuries, overnight repurchase agreements, and bank deposits. Their yields, when passed through to holders, approximate the Secured Overnight Financing Rate (SOFR) minus operating expenses. The July 2025 GENIUS Act established the first federal regulatory framework for "payment stablecoins" — digital assets designed for payment or settlement that the issuer is obligated to redeem for a fixed monetary value and represents will hold a stable value — requiring full one-to-one backing in cash and short-duration Treasuries and prohibiting issuers from paying interest or yield directly to stablecoin holders.

More recent entrants have experimented with diversified yield sources. Ethena's USDe uses delta-neutral positions in perpetual futures markets to generate yield. Maker's DAI, Ondo's USDY, and several tokenized Treasury products have introduced additional reserve compositions, though all remain concentrated in short-duration government or quasi-government paper.

USDX is distinguished by its collateral composition: a portfolio of amortizing, asset-backed cashflows rather than short-duration government securities. The reserve holds longer-duration assets, but the protocol's liquidity does not depend on those assets maturing — redemption liquidity is sourced from a liquid-reserve buffer, repo facilities against agency MBS (one of the deepest short-term funding markets in the world), and a tiered redemption queue. Longer asset duration introduces interest rate and prepayment risk that must be explicitly managed, but it does not make the protocol illiquid. The point is not that mortgage collateral yields more; it is that USDX makes one of the largest asset classes in American finance — residential mortgage debt — composable. Mortgage cashflows that today reach only a narrow set of institutional allocators become the backing for a dollar any wallet can hold, move, and redeem, and that plugs natively into the rest of onchain finance.

### 2.3 Asset-Backed Stablecoin Prior Art

Previous attempts at asset-backed stablecoins have included commodity-backed designs (Tether Gold, PAX Gold), real-estate-tokenized designs (RealT, Lofty), and fiat-collateralized designs (USDC, USDT). None of these have combined three properties simultaneously:

1. Backed by cashflowing real-world assets at institutional scale;
2. Redeemable against reserves through an onchain mechanism;
3. Yield-bearing for holders willing to stake.

USDX targets this intersection. The closest precedent is Maker's RWA vaults, which deposit tokenized private credit as a backing component for DAI. The USDX design differs in that the mortgage collateral is the primary reserve rather than a supplementary one, and in that the yield is passed through to stakers directly rather than being captured at the protocol level.

### 2.4 Design Principles

The USDX protocol adheres to a set of principles that shape every component of the system:

**Collateral simplicity.** The portfolio is composed of a small number of well-understood asset classes with clear legal frameworks, mature price discovery mechanisms, and established custody rails. Novelty is concentrated in how these assets are represented onchain, not in what they are.

**Redemption primacy.** The peg is anchored by direct redeemability against reserves for $1. The protocol is designed so that a holder can always redeem USDX for one dollar of value through the redemption process. Every other peg mechanism — liquidity pools, autonomous market operations, structural repayment demand — is a supplementary arbitrage surface, not a load-bearing substitute for redemption.

**Risk isolation.** Credit, market, and operational risks are absorbed by mechanisms other than USDX holders wherever possible. The RATES safety module, disciplined underwriting on directly originated collateral, and staged loss absorption all exist to keep the stablecoin itself boring.

**Economic separation.** The economics of USDX and the protocol derive only from the reserve portfolio — the mortgage and MBS cashflows that back the stablecoin. USDX holders and the protocol do not gain from, and are not exposed to, any separate commercial activities Stable Company may conduct, such as origination services, tokenization services, or marketplace activity. The reserve backs the stablecoin; the stablecoin does not underwrite the company.

**Regulatory compatibility.** The system is designed to be operable within a licensed financial infrastructure stack — qualified custodians, compliant origination, audited reserves, and a licensed issuer posture. This is a deliberate posture rather than a strict technical dependency: the core mint, redeem, staking, and reserve mechanics function independently of any single jurisdiction's framework, but the protocol assumes, rather than resists, a regulated future for dollar-pegged instruments, because that is the environment in which institutional capital and mortgage collateral actually operate.
