---
description: This Section Provides an Overview of the RATES Token
---

# RATES

## Overview

RATES is the protocol token of [USDX](usdx/). It is a component of the USDX protocol rather than a standalone product: it exists to secure, backstop, and govern the stablecoin. RATES has three core utilities:

* **Validator staking** — validators stake RATES to attest the loan data and property attestations that gate the minting of new USDX collateral.
* **First-loss safety module** — RATES stakers provide the senior-most tranche of the USDX loss waterfall, backstopping the reserve before any loss can reach USDX holders.
* **Governance** — RATES holders govern a deliberately narrow set of protocol parameters.

These three activities are opted into separately. A participant may run a validator, stake into the safety module, both, or neither.

## Validator Staking

Validators stake RATES to join the active validator set. They are responsible for two classes of attestation that gate new USDX collateral:

* **Origination attestations** — at the origination of a new tokenized mortgage (whether sourced through Stable's own channel or an institutional partner pipeline), validators attest that loan data, appraisals, and title documentation meet protocol underwriting requirements before the loan can be admitted to the reserve.
* **Quarterly attestations** — on a quarterly cadence, validators re-attest property valuation and lien status for mortgages already in the portfolio, keeping the onchain representation synchronized with off-chain legal reality.

The validator's role is **verification-of-verification**: they confirm that data produced by approved third-party providers — AVM vendors, title companies, credit bureaus, flood and tax data providers — is correctly signed, provenanced, and compliant, rather than independently producing that data.

Validators earn modest flat or bps-capped fees per origination and per quarterly re-attestation, paid in USDX and priced below the combined cost of the traditional services they replace. **20% of validator USDX fees** are routed to the RATES buyback-and-burn contract; the balance flows to the validator. A validator's primary compensation, however, is RATES emissions, supplemented by safety-module rewards on any stake they choose to place there.

The initial active set targets **21 validators** at origination launch, scaling toward a steady-state cap, with a minimum self-stake of **1,000,000 RATES** per seat and support for delegation. Validating activates alongside the native origination channel (Roadmap Phase 2), not at stablecoin launch, since attestations are only required once the protocol originates collateral directly.

## First-Loss Safety Module

Separately from validating, RATES holders may stake into the safety module — **Tranche 1** of the USDX loss waterfall. If the reserve experiences a shortfall it cannot absorb itself, safety-module stake is slashed pro rata to make USDX holders whole **before any other tranche is affected**. This is a deliberate acceptance of first-loss exposure, and it is what distinguishes a safety-module staker from a validator.

The two stake pools are independent. Validator self-stake lives in the validator contract and is exposed only to attestation-fault slashing; safety-module stake lives in the safety-module contract and is exposed only to loss-waterfall slashing. Operating a validator does not, by itself, place a validator's stake at first-loss risk.

In exchange for first-loss exposure, safety-module stakers earn a share of protocol fees plus emissions. Compensation shifts as the protocol matures: in the bootstrap phase it is paid primarily in RATES emissions, and as origination and protocol revenue grow, real fee revenue supplements and eventually predominates.

## Governance

RATES carries governance rights over a narrow set of protocol parameters — matters such as approved AVM vendors, approved repo counterparties, loan-product whitelisting, validator set size, and slashing parameters — rather than broad control of the protocol. Vote weight is stake-weighted with a lock-duration multiplier (ve-style).

Governance scope is intentionally limited. USDX operates within a licensed financial infrastructure stack, and operational decisions — custody relationships, servicing contracts, regulatory interactions — are retained by Stable Company as the licensed operator. A narrow set of emergency powers (pausing mints or redemptions, halting the autonomous peg-maintenance bot, or triggering a loss-waterfall draw) is likewise reserved to Stable Company, publicly logged and subject to retrospective review. RATES governance is complementary to, not a replacement for, the regulated operating entity.

## Supply at a Glance

RATES has a fixed initial supply of **1,000,000,000 tokens (1B)** at genesis. Beyond genesis, RATES are emitted on a geometrically decaying annual schedule applied to the initial 1B supply:

* Year-one emission rate is **12%** of the initial supply.
* Each subsequent year's rate is **88%** of the prior year's (a 0.88 decay ratio).
* The schedule sums to exactly 1B over infinite time, capping total supply at **exactly 2.0B RATES** under the emissions schedule alone.

<figure><img src="../.gitbook/assets/emissions_diagram.png" alt="RATES emissions and total supply trajectory: annual emission rate decays from 12% in Year 1 toward zero, while cumulative supply rises from 1.0B at genesis toward a 2.0B asymptote"><figcaption><p>Annual RATES emission rate (decaying at a 0.88 ratio) and cumulative supply (asymptoting at 2.0B) over the first 25 years.</p></figcaption></figure>

Emissions are split **50% to validators / 50% to tranche stakers**, with the tranche half sub-allocated 60% / 25% / 15% across the Tranche 1 (safety module), Tranche 2 (stablecoin vault), and Tranche 3 (mUSDX) stakers. Supply is further shaped by two activity-linked mechanisms:

* **Buyback-and-burn** — the 20% of validator USDX fees routed to the buyback contract is used to purchase RATES on the open market and burn it, tying deflationary pressure directly to protocol activity (analogous to Ethereum's EIP-1559 base-fee burn).
* **Activity-gated emissions** — validator emissions are gated by attestation volume; amounts withheld when activity is low are forgone, never minted.

| Supply dimension | Value |
| --- | --- |
| Initial supply | 1,000,000,000 RATES |
| Year-one emission rate | 12% |
| Annual emission rate decay | Multiplicative ratio of 0.88 |
| Emissions split (validators / tranche stakers) | 50% / 50% |
| Tranche sub-split (T1 / T2 / T3) | 60% / 25% / 15% |
| Buyback-and-burn share of validator USDX fees | 20% |
| Asymptotic supply (emissions schedule alone) | 2.0B (exactly) |

## Whitepaper

For the full specification of RATES — validator mechanics, the first-loss safety module, governance, and the complete supply, distribution, and emissions model — see the [RATES Whitepaper](../rates-whitepaper/) in the docs.

---

_RATES is a staking and governance token whose characterization is jurisdiction-specific. Nothing here constitutes an offer to sell, or the solicitation of an offer to buy, any security or financial instrument._
