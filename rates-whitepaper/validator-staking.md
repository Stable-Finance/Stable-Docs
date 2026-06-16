# Validator Staking

## 2. Validator Staking

Validators stake RATES to join the active validator set and are responsible for two classes of attestation that gate new USDX collateral: **origination attestations** (at the origination of a new tokenized mortgage, whether through Stable's channel or a partner pipeline) and **quarterly attestations** (re-attesting property valuation and lien status).

**Scope.** Validators attest to the cryptographic integrity of loan data produced by approved third-party providers — AVM vendors, title companies, credit bureaus, flood and tax data providers — rather than independently producing it. The role is verification-of-verification.

**Economic structure.** Validators earn modest flat or bps-capped fees per origination and per quarterly re-attestation, paid in USDX, priced below the combined cost of the traditional services they replace. 20% of validator USDX fees route to the RATES buyback-and-burn contract; the balance flows to the validator. Primary compensation is RATES emissions (Section 5), supplemented by safety-module rewards.

**Set composition.** Initial active set of 21 validators at origination launch, scaling toward a steady-state cap. Minimum self-stake of 1,000,000 RATES per seat. Delegation supported.

**Deferred to a follow-up implementation specification.** Detailed validator selection criteria, delegation mechanics (commissions, minimums, unbonding), and the precise slashing schedule (offenses, magnitudes, dispute process) are specified in a follow-up implementation document published ahead of validator launch. These parameters are operationally critical but separable from the framework specified in this paper.
