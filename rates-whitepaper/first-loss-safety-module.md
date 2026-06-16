# First-Loss Safety Module

## 3. First-Loss Safety Module

A portion of staked RATES sits in the safety module — Tranche 1 of the USDX loss waterfall. On a reserve shortfall, safety-module stake is slashed pro rata to make USDX holders whole before any other tranche is affected. In exchange for first-loss exposure, stakers earn a share of protocol fees plus emissions.

Safety-module staking and validator staking are distinct activities backed by distinct stake pools. Validator self-stake lives in the validator contract and is exposed only to attestation-fault slashing; safety-module stake lives in the safety-module contract and is exposed only to loss-waterfall slashing. The two pools are independent: a validator's self-stake is not at first-loss risk in the waterfall, and safety-module stake is not at risk for attestation faults. A participant may operate a validator, stake into the safety module, or both — each choice is opted into separately and slashed only from the pool to which it belongs.
