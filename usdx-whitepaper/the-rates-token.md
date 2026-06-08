# The RATES Token

## 9. The RATES Token

RATES is a component of the USDX protocol rather than a standalone product. This paper describes RATES only to the extent necessary to understand USDX. A separate RATES paper specifies distribution, supply schedule, and detailed tokenomics.

RATES has three core utilities within the USDX system:

### 9.1 Validator Staking

Validators stake RATES to join the active validator set. Validators are responsible for two classes of attestations that gate the minting of new USDX collateral:

- **Origination attestations.** At the origination of a new tokenized mortgage, whether sourced through Stable's own channel or an institutional partner pipeline, validators attest that loan data, appraisals, and title documentation supplied by approved third-party providers meet protocol underwriting requirements. Threshold signatures from the active validator set are required for the new loan to be admitted to the USDX reserve portfolio.
- **Quarterly attestations.** On a quarterly cadence, validators re-attest property valuation and lien status for tokenized mortgages in the portfolio, ensuring that the onchain representation remains synchronized with the off-chain legal reality.

**Scope of attestation.** Validators attest to the cryptographic integrity of loan data produced by approved third-party providers — AVM vendors, title companies, credit bureaus, flood and tax data providers — rather than independently producing that data. The validator's role is verification-of-verification: confirming that the data feeds supplying a new or existing loan are correctly signed, provenanced, and compliant with protocol underwriting requirements. Independent production of underlying data (appraisals, title searches, credit pulls) remains the responsibility of the licensed service providers that perform those functions today.

**Economic structure.** Validators earn modest flat or bps-capped fees per origination and per quarterly re-attestation, priced to be materially below the combined cost of the traditional services they replace (quality control, document custody, and ongoing portfolio oversight). All validator fees are paid in USDX. A portion of each validator fee (specified in the RATES paper) is routed to the RATES buyback-and-burn contract; the balance flows to the validator. Validator fees are structured as cost-recovery for the attestation work performed; the primary compensation for operating a validator is the RATES emissions distribution specified in the RATES paper, supplemented by safety module rewards earned on staked RATES (Section 9.2).

**Set composition.** Validating activates alongside the native origination channel (Roadmap Phase 2), not at stablecoin launch, since attestations are only required once the protocol originates collateral directly. The initial active validator set is sized for threshold-signature robustness — targeted at 21 validators at origination launch and scaling toward a steady-state cap as the protocol matures, with a minimum self-stake per seat and support for delegation. Specific selection, self-stake, delegation, and slashing parameters are specified in the separate RATES paper and finalized ahead of origination launch.

**Validating and first-loss are distinct.** Staking RATES to validate is a separate activity from staking RATES into the first-loss safety module (Section 9.2). A validator earns attestation fees and emissions for verification work; a safety-module staker accepts loss exposure in exchange for first-loss rewards. A participant may do one without the other. Operating a validator does not, by itself, place a validator's stake at first-loss risk in the loss waterfall.

### 9.2 First-Loss Safety Module

Separately from validating, RATES holders may stake into the safety module — the senior-most tranche of the USDX loss waterfall (Section 8). If the reserve experiences losses it cannot absorb itself, safety-module stake is slashed pro rata to make USDX holders whole before any other tranche is affected. This is a deliberate acceptance of first-loss exposure, and it is what distinguishes a safety-module staker from a validator.

Compensation for first-loss exposure shifts as the protocol matures. In the bootstrap phase, before fee revenue scales, safety-module rewards are paid primarily in RATES emissions (specified in the RATES paper). As origination and protocol revenue grow, a share of protocol fees supplements and eventually predominates over emissions. The intent is that first-loss capital is always compensated, with the source of that compensation migrating from token emissions toward real fee revenue over time.

### 9.3 Governance

RATES is intended to carry governance rights over a deliberately narrow set of protocol parameters — matters such as approved data vendors, approved counterparties, and risk parameters — rather than broad control of the protocol. The specific governable parameters, vote-weighting method, and procedures are defined in the separate RATES paper and may evolve ahead of token distribution.

Governance scope is intentionally limited. USDX is designed to operate within a licensed financial infrastructure stack, and operational decisions — custody relationships, servicing contracts, regulatory interactions — are retained by Stable Company as the licensed operator. RATES governance is complementary to, not a replacement for, the regulated operating entity.

### 9.4 Emergency Response

As the licensed operator, Stable Company retains a narrow set of emergency powers — pausing mints, pausing redemptions, halting the APMB, or triggering a loss-waterfall draw — to respond to active incidents. Stable Company discloses material emergency actions as appropriate and as required by its regulatory and contractual obligations, exercising operational discretion over the timing and detail of disclosure during a live incident.
