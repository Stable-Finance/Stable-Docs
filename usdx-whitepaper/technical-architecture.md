# Technical Architecture

## 10. Technical Architecture

### 10.1 Smart Contract System

The protocol's smart contract system consists of the following core modules, each deployed on every supported chain:

**Mint/Redeem Contract.** Processes USDX issuance and redemption against supported-stablecoin deposits on the permissionless path. Maintains the tiered redemption queue (default, expedited, extended).

**Treasury Contract.** Manages onchain reserve holdings, triggers rebalancing operations, and routes yield income to the Distributor Contract.

**Staking Contract.** Handles USDX → mUSDX deposits and mUSDX → USDX withdrawal requests. Maintains the USDX/mUSDX exchange rate and manages the cooldown queue.

**Distributor Contract.** Distributes protocol fees to RATES validators and the RATES safety module, updates the mUSDX exchange rate with the allocated share, and routes the balance to the Treasury.

**RATES Safety Module.** Staking contract for RATES tokens. Governs slashing events in response to loss waterfall triggers and recovery flows.

**Validator Contract.** Maintains the active validator set, processes origination and quarterly attestations, and aggregates threshold signatures gating new-collateral minting.

**APMB Contract.** Autonomous peg-maintenance bot with locked parameters and a pre-funded inventory.

**Proof-of-Reserve Adapter.** Reads the off-chain reserve attestation and publishes an onchain hash that can be verified against the published attestation document.

All contracts are upgradeable through a time-locked governance mechanism. Upgrade paths are restricted to parameter changes and security patches; logic upgrades that materially alter the protocol's economic behavior require extended timelock.

### 10.2 Oracle Design

The protocol relies on oracle feeds for three purposes: stablecoin price monitoring (for the stablecoin acceptance policy), agency MBS pricing (for portfolio valuation), and whole loan valuation (for book-value accounting). Oracle feeds are sourced from multiple leading providers, including Chainlink, Pyth, RedStone, Switchboard, and other established price-feed networks. The protocol does not depend on any single provider.

- **Stablecoin oracles.** Sourced across multiple providers with a median aggregation and a deviation guard that triggers circuit-breaker behavior if any source disagrees with the median by more than 1%.
- **Agency MBS pricing.** Sourced from a consortium of institutional pricing services (ICE, Bloomberg BVAL) and published onchain via a Stable-operated oracle adapter with multi-signer attestation. MBS prices update intraday during trading hours and end-of-day via dealer mark. The oracle adapter includes sanity bounds: no single update may move a CUSIP's price by more than 2% relative to the prior update without a second independent attestation.
- **Whole loan valuation.** Whole loans are carried at book value for protocol accounting, marked down only in the event of delinquency or credit events. A quarterly independent valuation serves as a check on book-value accounting and is published alongside the reserve attestation.

The oracle architecture is deliberately conservative. MBS and whole loan valuations are primary inputs to the invariant that governs mint capacity (Section 5.4); any oracle manipulation or data error could lead to over-minting. The multi-source, attestation-gated, bounded-update architecture ensures that oracle anomalies surface as pauses rather than as silent mispricings.

### 10.3 Proof of Reserve

The proof-of-reserve system produces a daily onchain attestation of the reserve portfolio. The attestation includes:

- Aggregate book value of reserves.
- Decomposition by asset class (MBS, whole loans, tokenized mortgages, liquid reserves).
- Outstanding USDX supply across all deployed chains.
- The collateralization ratio A_t/S_t.
- A cryptographic commitment to the detailed reserve schedule, verifiable against an off-chain published schedule.

The attestation is signed by Stable Company's treasurer and an independent auditor, both of whom maintain hardware-secured signing keys. The onchain hash of the attestation serves as the canonical reserve-status oracle for all protocol operations.

Consistent with Section 4.7, an independent third party issues a monthly attestation of the reserve portfolio, covering existence, ownership, valuation methodology, and encumbrance status. The current reserve composition, collateralization ratio, and published attestations are available on the protocol's live reserves page at [trystable.co/reserves](https://trystable.co/reserves), where anyone can verify the published figures against the protocol's onchain holdings.
