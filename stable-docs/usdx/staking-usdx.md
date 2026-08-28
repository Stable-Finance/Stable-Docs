---
description: Understand how staking USDX for mUSDX accrues mortgage-backed yield.
---

# Staking USDX

## Earn through the mUSDX exchange rate

Staking USDX mints mUSDX, a non-rebasing token that represents a share of the staking vault. Yield from eligible protocol activity and mortgage assets accrues to the vault as USDX, increasing the amount of USDX redeemable for each mUSDX over time.

<a href="https://app.trystable.co/stake" class="button primary">Stake USDX</a> <a href="https://trystable.co/reserves" class="button secondary">View reserves</a>

{% hint style="warning" %}
Displayed APY is variable, not guaranteed, and may change with protocol revenue, mortgage cash flows, reserve composition, and market conditions. Staking may not be available on every supported network.
{% endhint %}

## How mUSDX works

1. A user deposits USDX into the staking vault.
2. The vault mints mUSDX at the current exchange rate.
3. Yield retained by the vault increases the USDX value of each mUSDX.
4. The user initiates an unstake and receives USDX after the cooldown period.

Users do not need to claim recurring rewards. The mUSDX token balance remains unchanged while its exchange rate against USDX is designed to increase as yield enters the vault.

## Illustrative compounding

The following example assumes a constant 10% annual yield solely to demonstrate exchange-rate mechanics. It is not a forecast or promised return.

<table><thead><tr><th>Days</th><th>Total mUSDX</th><th>Total USDX in vault</th><th data-type="number">Value of 1 mUSDX</th></tr></thead><tbody><tr><td>100</td><td>1,000</td><td>1,027.80</td><td>1.0278</td></tr><tr><td>365</td><td>1,000</td><td>1,105.16</td><td>1.10516</td></tr><tr><td>730</td><td>1,000</td><td>1,221.36</td><td>1.22136</td></tr><tr><td>1,095</td><td>1,000</td><td>1,331</td><td>1.331</td></tr></tbody></table>

## Key mechanics

- The amount of mUSDX received depends on the exchange rate when staking.
- A user may receive fewer mUSDX than the USDX deposited, while receiving the equivalent USDX value at that exchange rate.
- Yield accumulates inside the staking contract rather than being distributed as additional mUSDX tokens.
- Unstaking initiates a **7-day cooldown** before USDX is available to withdraw.

{% hint style="info" %}
Review [Risk & Transparency](risk-and-transparency/) and verify the current staking terms in the app before transacting.
{% endhint %}
