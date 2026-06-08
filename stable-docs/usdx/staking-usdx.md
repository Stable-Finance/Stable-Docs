---
description: This Page Outlines How to Stake USDX and the mUSDX Liquid Staking Token
---

# Staking USDX

## Context

Users are able to stake their USDX for mUSDX and earn yield generated from USDX's liquidity provision, packaging fees, and payments from the mortgage assets in the USDX treasury reserves. Yield accrues in the mUSDX vault as USDX and is reflected in the value of mUSDX.

## Overview

When a user stakes USDX they are minting mUSDX ("Staked USDX") which is returned to their wallet and earns yield from the mortgage assets and market activity backing USDX. Yield accrues to the mUSDX pool in the form of USDX, increasing the value of each mUSDX. Yield compounds daily.

For example, 1,000 USDX is staked on day 0, and, for simplicity, the mUSDX yield is 10% forever:

<table><thead><tr><th>Days</th><th>Total mUSDX</th><th>Total USDX in Vault</th><th data-type="number">Value of 1 mUSDX</th></tr></thead><tbody><tr><td>100</td><td>1,000</td><td>1,027.80</td><td>1.0278</td></tr><tr><td>365</td><td>1,000</td><td>1,105.16</td><td>1.10516</td></tr><tr><td>730</td><td>1,000</td><td>1,221.36</td><td>1.22136</td></tr><tr><td>1,095</td><td>1,000</td><td>1,331</td><td>1.331</td></tr></tbody></table>

## Important to Note

* Users do NOT need to do anything but hold mUSDX to receive rewards
* Rewards aren’t earned directly by mUSDX holders; rather, they accumulate within the staking contract, which results in the "value" of mUSDX rising over time.
  * Users are able to unstake their mUSDX at any time and receive an amount USDX reflecting the staked amount plus any increase in value of mUSDX from the time the user staked until unstaking
* The amount of mUSDX a user will receive when staking USDX will depend on the current value of mUSDX
  * At launch the value will be 1 mUSDX = 1 USDX, but mUSDX is expected to slowly increase in value as protocol level rewards are transferred into the Staking smart contract
  * Therefore, while a staker might receive less mUSDX than USDX staked, the value of the mUSDX will always be equal to or greater than the USDX they staked
* Unstaking USDX activates a cooldown period of 7 days. USDX will be available to withdraw after that period

## Note: Staking is not yet enabled on some chains.

<br>
