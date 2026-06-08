# Maintaining USDX Peg Stability

## Maintaining USDX Peg Stability

USDX maintains its $1 peg through several mechanisms.

### Overcollateralized Treasury

The value of USDX is backed by a reserve of debts and liquid assets.

### Debt Repayment Incentives

Borrowers of USDX can always repay their positions in-kind, and are therefore incentivized to purchase USDX at any price below $1 and repay their debts.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7YNtXmE-YTTtI7Pq71OfQTPXzLoElFdUqyrxrNPyhPP6VPnvNgJP8ou8Q0JzrC48jNMNk-SsO2lFjEJTPLAkixmqi5VncE-iN3qfH0YYq5ysjg8M8vyO5YIIate54cq_V6soD-w?key=vW1rn2vc2I8X-NIJVoW3qXaj" alt=""><figcaption></figcaption></figure>

For example, if a real estate depositor borrowed 10 Million USDX against $30 Million in real estate deposits and USDX depegged to $0.97 that depositor could purchase 10 Million USDX for about $9.7 Million, repay their loan, and profit about $300,000.

Similarly, if USDX depegged upwards to $1.023, any holder is incentivized to repay their debts and make a profit of about 2.3% (depending on costs to facilitate e.g. swaps, bridges).

### Stable’s Market Operations

Stable buys below-peg USDX and repays any credit it has borrowed. For example, if Stable has issued 1 Billion USDX against 2 Billion in real estate deposits, and USDX depegged to $0.98, Stable will purchase as many USDX as it can until USDX is repegged, then it will repay however much it was able to buy below-peg. Stable earns the upside of tokens purchased for less than $1 by repaying any borrows and using the rest after things have returned to normal.

### Maintenance Pool and Staked USDX

Stable sponsors an autonomous vault where USDC, USDT, and USDX holders can deposit their stablecoins and earn yield. The stablecoins are used to maintain the peg between USDX and other stablecoins on strategic exchanges.&#x20;

Other vaults deploy USDX into delta-neutral strategies or AI-managed arbitrage opportunities. No cap exists on any of these pools and yield can be claimed at any time without withdrawing.

### Dollar Value Interest

Interest payments on borrowed USDX must be paid in USDC, USDT, or USDX. This creates implicit demand for more USDX than exists.&#x20;

For example;

* 100MM USDX is borrowed at 6% APR for 2 years
* No other USDX is borrowed during that time
* The total repayment requires $112MM of value (112MM USDX)
* At least $12MM of that must come from somewhere else (USDC or USDT)&#x20;

If all interest and principal repayments were made in USDC or USDT, so that no debt exists and 100MM USDX are still in the market, the USDX protocol must do one of the following:&#x20;

1. Repurchase that outstanding USDX and burn it
2. Purchase approved debt (e.g. mortgages)
3. Purchase approved assets and issue debt against them (e.g. bonds at 10%, debt at 9%).  &#x20;

### Peg-Only Repayment for Other Stablecoins

In the event that USDC or USDT has depegged recently (past 72 hours) they cannot not be accepted by the protocol until stability has returned for a sustained period of time (144 hours).

Debts and interests due on the USDX Protocol can be paid by anyone. This enables Stable and other businesses to accept USD transfers which can be ZK proven to the blockchain as payment. This could provide awesome value in the event that all major stablecoins have depegged, leaving only USDX (on the market or newly minted) for debtors to facilitate their monthly interest payment or principal repayment.&#x20;

### Liquidation Protocols

The USDX Protocol follows set and rigorous liquidation protocols to, if necessary, liquidate the position of any depositor and any collateral that was used in the CDP. Those protocols are different for different assets.&#x20;

#### **Liquidation Policy for Real Estate Deposits**

When real estate is used as collateral in a CDP (Collateralized Debt Position), the protocol continuously monitors its value through Stable’s internal assessment tools and trusted third-party appraisers. If the value of the property falls below a defined threshold, the account is frozen until the borrower either repays a portion of their loan or the asset is partially or fully liquidated.

#### _**Example Scenario**_

Suppose a borrower deposits a property valued at $1,000,000 and borrows $800,000 USDX—an 80% LTV. If the property's assessed value drops below $950,000, Stable issues an early warning to the borrower, providing time to adjust their position or repay part of their loan.

If the property's value continues to fall and reaches $875,000, the CDP is deemed undercollateralized, and the liquidation process is triggered.

#### _**Step-by-Step Liquidation Process**_

1\. Soft Liquidation

Stable initiates a "soft liquidation" by auctioning an option to purchase 10–20% of the property's value to a pool of qualified participants. This is not a sale of the property itself, but a strategic action to reduce exposure.

* The borrower has the right to reclaim this option at the original deposit value within a defined timeframe.
* For instance, if $175,000 worth of value is recovered through the option sale, and the property's post-auction value is now assessed at $700,000, the outstanding loan of $800,000 is now backed by $700,000—effectively making the position \~112% overcollateralized.

2\. Ongoing Decline and Further Liquidation

If the property’s value continues to decline, Stable may conduct another soft liquidation round. If that still does not restore collateral health, full liquidation of the property may be initiated.

3\. Owner Redemption Window

Throughout this process, borrowers have a window to repay their USDX debt and reclaim their full property rights, with no additional penalties. This ensures fairness and gives real estate holders the opportunity to recover from temporary market fluctuations.

#### _**Risk Management**_

It’s important to note that unleveraged real estate deposits (i.e., those not used to mint USDX) carry no risk of liquidation. Borrowers who choose to leverage their deposits conservatively—below the maximum allowable LTV—substantially reduce their exposure to forced liquidation events.

#### **Liquidation Policy for Non-Real Estate Deposits**

USDX supports a variety of asset classes as collateral, including non-real estate assets such as tokenized commodities. Among these, gold represents a key example of a highly liquid and reliable form of collateral.

_**Loan-to-Value (LTV) Parameters**_

For gold, USDX allows users to borrow up to 90% LTV, reflecting the high liquidity and relative price stability of the asset. This means that for every $100 worth of gold deposited, users may borrow up to 90 USDX stablecoins.

_**Liquidation Threshold**_

To maintain the protocol’s solvency and protect against market volatility, liquidation is triggered when the LTV of a collateralized loan on gold reaches 93%. At this point, the borrower's position is considered undercollateralized and subject to partial liquidation.

_**Liquidation Mechanism**_

Upon reaching the liquidation threshold:

* A portion of the collateral is liquidated automatically.
* The system continues liquidating collateral until the LTV returns to 90% or lower.
* Liquidated collateral is sold through an open auction or routed to designated liquidators to recover the borrowed USDX.

This dynamic mechanism ensures minimal disruption to users while maintaining the protocol's solvency. By capping LTV recovery at 90%, USDX avoids over-liquidation, preserving user collateral and stabilizing protocol health.

_**Example Scenario**_

* A user deposits $10,000 worth of tokenized gold.
* The user borrows $9,000 in USDX (90% LTV).
* If the gold value drops to \~$9,677, the LTV becomes 93%, triggering liquidation.
* Collateral is sold in tranches until the LTV returns to 90%, meaning approximately $290 of USDX debt is repaid through liquidation.

This policy balances capital efficiency with risk mitigation, ensuring users can access high LTV borrowing while protecting the protocol from rapid devaluation events.

### Credit Default Swaps

Stable hedges risk for USDX by acquiring credit default swaps on deposited real estate. This helps ensure USDX and Stable will survive a catastrophic real estate market crash. Such a crash would need to cause real estate values to fall more than 20% before USDX is at risk of being undercollateralized; though an event like that is unlikely in the foreseeable future Stable takes additional measures to increase that buffer even further.

### Insurance Fund

Stable utilizes profits to build an Insurance Fund and may open pools for the community to provide liquidity to the Insurance Fund. Liquidity in that pool earns yield in ways that are risk free regarding contagion from USDX, and may be used to purchase further insurance.

### Debt Redemption and Liquidation

Stable allows holders of 1,000,000+ USDX to redeem USDX for the debt positions backing USDX in denominations of 100,000 (e.g. 1,000,000, 1,100,000, 10,200,000, …). Each redemption is atomically swapped for Debt NFTs that represent 100,000 USDX of debt from 10 or more properties. The properties are chosen randomly from different risk tranches.

USDX Debt NFTs offer direct exposure to the debts, and are therefore not securities. Where most debt is sold at a significant premium (e.g. a $500,000 6% mortgage may be sold for $530,000), USDX Debt NFTs can be claimed for a 0.25%-1.25% redemption fee, depending on demand for the given tranche and maturity of the debt, or swapped back to USDX for a 0.5%-1.5% fee. Stable may offer insurance for a fee. Additionally, Stable liquidates USDX Debt through onchain and offchain pipelines with select partners and the open market.
