---
description: This Page Covers How USDX Collateral Maintains a 1:1 Value with USD
---

# Hedging Volatility

## Overview

Due to the interest payments and value of the collateral behind it, a $500,000 mortgage held in the reserve is almost immediately worth more than $500,000. This means that a mortgage carried in the USDX reserve not only fully collateralizes the USDX it backs, but **over-collateralizes** it. Additionally, the value of the real estate underlying the mortgage itself over-collateralizes the mortgage.

While it might seem that Stable could stop there, holding any mortgage introduces certain risks that must be hedged to ensure the USDX reserve always carries book value greater than the USDX it backs. Fortunately, solutions for these risks have been developed over hundreds of years and can be implemented by Stable behind the scenes to maintain full collateralization.&#x20;

Stable utilizes these tools in addition to the peg-stability mechanisms [outlined in the USDX Whitepaper](../../../usdx-whitepaper/peg-stability.md) to ensure USDX remains fully collateralized and liquid.&#x20;

This page delves deeper into how risks are tranched and how mortgage capital markets are used to shield USDX from market volatility.

## Distributing Risk and Stabilizing

**Tranching,** **Treasury Futures, and Interest Rate Swaps (IRS)** are a few methods that Stable uses to distribute and mitigate different risks across a diverse range of investors to ensure the collateral backing USDX remains fully collateralized and liquid. To fully understand these tools, let's take a step back and set up a situation.

### From Mortgages to MBS

Suppose Stable and Stable Partners have sourced 1,000 mortgage loans totaling $450,000,000 into the USDX reserve. All loans are residential and fall under [qualified mortgage](https://www.investopedia.com/terms/q/qualified-mortgage.asp) guidelines, and they back $450,000,000 of USDX in circulation.

The loans are then bundled and sent to a [mortgage-backed security](https://www.investopedia.com/terms/m/mbs.asp) (MBS) issuer—such as Fannie Mae. That issuer either buys the loans from Stable outright, or issues a MBS back to Stable.&#x20;

For example, Fannie Mae may note that the mortgages have an average rate of 6.5% and create an MBS offering a yield of 6.25%, retaining 0.25% to cover insurance costs. In return, Fannie Mae guarantees repayment of the principal and interest to MBS holders, which is a massive hedge in itself.

### Credit / Default Risk

> Credit risk is the broad category of potential loss a lender faces if a borrower fails to meet their debt obligations, while default risk is a specific type of credit risk that refers to the likelihood that a borrower will be unable to make timely payments on their debt.&#x20;

#### Tranching

**Tranching** means dividing the value, yield, and risk of an MBS into different pools. Tranching is one way Stable facilitates the full collateralization of USDX by shifting credit and default risks across different classes of investors.&#x20;

Here's an example of how different tranches may be sized:

* **Equity:** e.g., 5% of the MBS face value
* **Junior (Jr):** e.g., 10% of the MBS face value
* **Mezzanine**: e.g., 5 % of the MBS face value
* **Senior (Sr):** e.g., 80% of the MBS face value

Subordinate tranches, such as Equity, Jr, and Mezzanine, absorb losses first if the underlying mortgages or MBS experience defaults or write-downs, leaving the Sr tranche—which underpins USDX—largely insulated from credit risk. Those tranches are allocated a higher level of yield for taking on those risks and providing that security. This structure ensures that USDX remains fully collateralized even in adverse scenarios.&#x20;

> In essence, tranching transforms a single pool of mortgage assets into multiple layers of protection and opportunity, making the system both **safer and more efficient**.

To make it tangible, let's walk through a loss scenario on a $100,000,000 MBS:

| Tranche     | % of MBS | Face Value  | Role                                       |
| ----------- | -------- | ----------- | ------------------------------------------ |
| Equity      | 5%       | $5,000,000  | Absorbs first losses, high risk/high yield |
| Junior (Jr) | 10%      | $10,000,000 | Absorbs losses after Equity                |
| Mezzanine   | 5%       | $5,000,000  | Middle layer, moderate risk/yield          |
| Senior (Sr) | 80%      | $80,000,000 | Backing USDX, minimal credit risk          |

If defaults cause a $6,000,000 loss:

* Equity tranche is fully wiped out
* Junior tranche absorbs $1M of loss
* Mezzanine and Senior tranches remain intact

### **Interest Rate Risk**

> For investors in fixed-income securities like bonds, interest rate risk means the risk that bond prices fall because interest rates rise.

#### **Treasury Futures**

Even after credit risks have been hedged, the MBS still carries interest rate risk. While interest rate risk does not threaten the cash flow or interest yield that backs USDX, it has the potential to create an issue if Stable needs to sell an MBS during a period where the value of that MBS is negatively impacted by interest rates.

Here is an example of the impact interest rate risk can have if it is not hedged. Let's say the MBS from our previous example has a duration of 5 years.&#x20;

> Duration provides a numerical estimate of how much the price of an MBS will change for a 1% (100 basis point) movement in interest rates.
>
> Duration is essentially a weighted average time until investors receive the present value of an MBS's future payments, including both interest and principal.

If rates rise 1%, the market value of that $80,000,000 Sr tranche could drop roughly 5%:

$$
Valuedrop = $80,000,000 * 0.05 = $4,000,000
$$

$$
Valuedrop = $4,000,000
$$

To manage this, Stable can employ **treasury futures**—highly liquid contracts that offset interest rate movements. By taking positions in these futures, Stable can mitigate the impact of rate swings on the MBS’s market value, keeping the net value close to par.

Basically, Stable could sell treasury futures equivalent to $80,000,000 in notional value. If interest rates rise by 1%, the futures gain roughly $4,000,000, offsetting the MBS loss.&#x20;

This ensures USDX remains fully collateralized and the underlying collateral can be liquidated if needed, even during periods of market volatility.

#### **Interest Rate Swaps**

In addition to Treasury futures, Stable can hedge interest rate risk using **interest rate swaps (IRS)**. An IRS is a contract where Stable exchanges fixed interest payments for floating (or vice versa) with a counterparty. This allows Stable to offset MBS fluctuations without selling the underlying securities.

Example: To protect the $80,000,000 Senior tranche yielding 6%:

* Stable could enter a swap to pay fixed 6% and receive floating (e.g., tied to 3-month Treasury rates)
* If interest rates rise, the MBS value falls, but the floating payments from the swap increase, offsetting the loss
* If rates fall, the MBS value rises, and the swap cost partially offsets the gain — generally acceptable, since USDX remains fully collateralized
