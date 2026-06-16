# Supply, Distribution, and Emissions

## 5. Supply, Distribution, and Emissions

This section is the canonical specification of RATES supply. It specifies initial supply, distribution, the emissions schedule, and supply dynamics. Additional supply is created post-genesis only via the loss waterfall ([USDX whitepaper Section 8](../usdx-whitepaper/risk-management-and-the-loss-waterfall.md)) and the emissions schedule below. Tokens burnt via the buyback mechanism (Section 5.4) reduce circulating and total supply; scheduled emissions withheld by the activity-gating mechanism (Section 5.5) are forgone — never minted — and so reduce realized supply growth relative to the schedule.

### 5.1 Initial Supply

The total initial supply of RATES at genesis is 1,000,000,000 tokens (1B). The full allocation across protocol, operator, investor, team, treasury, safety-module seed, and community categories — together with vesting schedules — is specified in the implementation specification published ahead of RATES distribution. A portion of initial supply is staked in the Tranche 1 safety module at genesis to provide immediate protocol-owned backstop capacity; this stake is slashed pro rata alongside external safety-module stakers in any loss event.

### 5.2 Emissions Schedule

Beyond the initial 1B supply, RATES are emitted on a geometrically decaying annual schedule applied to the initial 1B supply. The year-one emission rate is 12% of the initial supply. Each subsequent year's rate is 88% of the prior year's rate. Formally, the year-_n_ emission rate is _r&#8345; = 0.12 · 0.88&#8319;&#8315;&#185;_, and the year-_n_ emission amount (in tokens) is _E&#8345; = r&#8345; · S&#8320;_, where _S&#8320;_ is the genesis supply of 1B RATES. The emission base does not compound: each year's emission is a fixed share of the original 1B, not of the prevailing outstanding supply.

| Year | Rate | Emission (M) | End-of-year supply (M) |
| --- | --- | --- | --- |
| 1 | 12.00% | 120.0 | 1,120.0 |
| 2 | 10.56% | 105.6 | 1,225.6 |
| 3 | 9.29% | 92.9 | 1,318.5 |
| 5 | 7.20% | 72.0 | 1,472.3 |
| 10 | 3.80% | 38.0 | 1,721.5 |
| 20 | 1.06% | 10.6 | 1,922.4 |

The sum of future emission rates over infinite time converges to exactly 100% of initial supply: _&#8721; 0.12 · 0.88&#8319;&#8315;&#185; = 0.12 / (1 − 0.88) = 1_. Cumulative emissions therefore total exactly 1B RATES, capping total supply at **exactly 2B RATES** under the emissions schedule alone, absent waterfall mints and buyback burns.

<figure><img src="../.gitbook/assets/emissions_diagram.png" alt="RATES emissions and total supply trajectory: annual emission rate decays at a 0.88 ratio from 12% in Year 1, while cumulative supply rises from 1.0B at genesis toward a 2.0B asymptote"><figcaption><p>Figure 1: Annual RATES emission rate (decaying at 0.88 ratio) and cumulative supply (asymptoting at 2B) over the first 25 years.</p></figcaption></figure>

### 5.3 Emissions Split

Emissions are split between validators and tranche stakers as follows:

* **50% to validators** — distributed pro rata based on attestations signed during the emission epoch. Validators receive this emission in addition to the per-origination and per-attestation USDX fees (Section 2).
* **50% to tranche stakers** — sub-allocated by risk seniority:
  * 60% (30% of total emissions) to Tranche 1 (RATES safety module) stakers
  * 25% (12.5% of total emissions) to Tranche 2 (stablecoin vault) stakers
  * 15% (7.5% of total emissions) to Tranche 3 (mUSDX) stakers

The split parameters are adjustable by governance within protocol-defined bounds.

### 5.4 Buyback and Burn

20% of validator USDX fees are automatically allocated to the buyback-and-burn contract, which uses these proceeds to purchase RATES on the open market and burn the acquired tokens. Validators earn 80% of their stated USDX fees on attestations; the remaining 20% is deducted pre-distribution and routed to the buyback contract. The effect is to tie RATES supply dynamics directly to protocol economic activity: every origination attestation and every quarterly re-attestation generates buyback demand. The mechanism is analogous to the base-fee burn in Ethereum (EIP-1559) — usage creates deflationary pressure on the token.

### 5.5 Activity-Gated Emissions

Validator emissions are gated by validator activity — specifically, the number of unique properties attested in a given month. An attestation event is either an origination attestation (new mortgage admitted to the reserve) or a quarterly re-attestation (property value and lien status refreshed). The gating mechanism operates on a linear scale between a minimum and maximum threshold:

* **Below the minimum threshold:** 0% of scheduled validator emissions are distributed. The full scheduled amount is forgone — never minted.
* **At the minimum threshold:** 10% of scheduled validator emissions are distributed to active validators pro rata.
* **Between minimum and maximum:** the distributed fraction grows linearly from 10% at the minimum to 100% at the maximum. Any undistributed fraction is forgone — never minted.
* **At or above the maximum threshold:** 100% of scheduled emissions are distributed.

**Year-1 thresholds:** minimum of 100 attested properties per month, maximum of 1,000.

**Threshold growth:** the minimum and maximum grow by 10% annually until the minimum reaches 1,000 properties per month (approximately year 26 at 10% compounding). Once the minimum reaches 1,000, both thresholds lock at 1,000 and 10,000 respectively, maintaining the 10x ratio in steady state.

### 5.6 Tranche Coverage Bands

Each tranche operates within a coverage band defined by a minimum and a maximum, both expressed as percentages of outstanding USDX supply. The band governs how tranche emissions are split between stakers and capacity building (Section 5.7).

| Tranche | Minimum coverage | Maximum coverage |
| --- | --- | --- |
| Tranche 1 — RATES safety module | 0.5% | 10% |
| Tranche 2 — Stablecoin vault | 1% | 10% |
| Tranche 3 — mUSDX | 2% | 10% |

Coverage _c(T)_ for tranche _T_ is computed as the USDX-equivalent value of capital staked in the tranche divided by the outstanding USDX supply. There is no cap on tranche coverage above the maximum; stakers may provide additional capacity freely, and the yield per staker naturally dilutes as the pool grows.

### 5.7 Emissions Behavior by Coverage

A tranche's allocated emissions are split between two destinations: staker rewards (distributed to tranche stakers pro rata) and capacity building (used to increase the tranche's protocol-owned capacity). The split depends on where current coverage sits within the tranche's band.

* **Below minimum coverage:** the tranche earns no staker rewards. 100% of its allocated emissions go to building capacity.
* **Between minimum and maximum:** the split scales linearly — 10% to stakers / 90% to building at minimum coverage, 100% to stakers / 0% to building at maximum coverage, linearly in between.
* **At or above maximum coverage:** 100% of allocated emissions go to stakers. No further capacity building occurs.

### 5.8 Permanent Protocol Capital

Capital acquired through the capacity-building mechanism is protocol-owned and permanent. It cannot be withdrawn by external parties and is moved only by governance action. Protocol-owned tranche capital is slashed pro rata alongside external staker capital in any loss event.

### 5.9 Net Supply Dynamics

The mechanisms above interact to produce a supply trajectory responsive to protocol activity and coverage state rather than a fixed curve:

* Scheduled emissions (5.2) set an upper bound on annual mint volume.
* Activity gating (5.5) withholds validator emissions when attestation volume is low; the withheld amounts are never minted.
* Below-minimum tranche emissions (5.7) are minted and converted to permanent coverage capital.
* Validator fee buyback (5.4) reduces supply in proportion to protocol economic activity.
* Waterfall mints ([USDX whitepaper Section 8, Step 4](../usdx-whitepaper/risk-management-and-the-loss-waterfall.md)) increase supply in loss events to recapitalize the reserve.

### 5.10 Summary

| Supply dimension | Value |
| --- | --- |
| Initial supply | 1,000,000,000 RATES |
| Year-one emission rate | 12% |
| Annual emission rate decay | Multiplicative ratio of 0.88 |
| Emissions split (validators / tranche stakers) | 50% / 50% |
| Tranche sub-split (T1 / T2 / T3) | 60% / 25% / 15% |
| Buyback-and-burn share of validator USDX fees | 20% |
| T1 coverage band | 0.5% – 10% of USDX supply |
| T2 coverage band | 1% – 10% of USDX supply |
| T3 coverage band | 2% – 10% of USDX supply |
| Asymptotic supply (emissions schedule alone) | 2.0B (exactly) |
