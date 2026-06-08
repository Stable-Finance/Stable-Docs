# System Overview

## 3. System Overview

USDX is a multi-component protocol comprising four interacting subsystems:

1. The **collateral system**, which holds reserves in agency MBS, whole mortgage loans, tokenized mortgages, and liquid assets.
2. The **mint-and-redeem system**, which processes stablecoin issuance against eligible deposits and redemption against reserves.
3. The **yield system**, through which USDX holders can stake into mUSDX to receive the net yield of the underlying collateral portfolio.
4. The **token and safety system**, in which the RATES token gates new-collateral minting through validator attestations and backstops the portfolio against shortfalls through a first-loss safety module.

The operator, Stable Company, runs the off-chain components: custody relationships, mortgage servicing, and the origination channel. The onchain components — mint, redeem, staking, yield distribution, safety module, and validator attestations — are implemented as smart contracts on the deployed chains. A key design choice is the separation of off-chain operational responsibilities from onchain financial rails: the former are necessarily human and institutional, while the latter are cryptographically verifiable.

The protocol is chain-agnostic. USDX is deployed natively across multiple EVM and SVM environments, with each deployment's supply accounted for within the protocol's aggregate reserve framework.
