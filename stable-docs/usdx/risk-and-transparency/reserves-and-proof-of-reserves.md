# Reserves & Proof of Reserves

### Scope

This page describes reserves backing **USDX on Solana**. USDX is also deployed to Base, Monad, and Ethereum, but those deployments are treasury-isolated per chain and are not bridgeable to or from Solana today, so Solana USDX is backed only by reserves held on behalf of Solana USDX holders.

### Reserve composition

Solana USDX is currently backed by two things:

* **Mortgage NFTs.** First-lien and second-lien mortgages on US residential real property, represented on-chain as NFTs. Each NFT corresponds to a specific loan with a recorded lien on the underlying property. See How USDX Works for the Debt NFT framework.
* **On-chain USDC reserves.** USDC deployed into Kamino and Jupiter Lend, where it earns low-risk permissionless-lending-market yield while remaining callable on a short timescale. USDC may also be held idle against a pending redemption rather than deployed.

### How USDC minting flows into reserves

When USDX is minted against USDC on Solana, the incoming USDC is deployed according to current reserve policy:

1. If there is a pending redemption that matches the inflow, the USDC is held against that redemption and not deployed.
2. Otherwise, the USDC is deployed into Kamino or Jupiter Lend.

### Stable Home Accounts — lien-backed mints

USDX minted against a Stable Home Account's home equity is backed by two instruments:

1. A lien on the underlying US residential property
2. A mortgage debt instrument evidencing the obligation

Home Accounts are subject to a layered approval process before any USDX is deployed against them. See Underwriting & Risk Management for the full approval flow.

### Custody

* **On-chain reserves** (USDC held in the USDX program's vaults, in Kamino, and in Jupiter Lend) are custodied in Solana programs. See Contract Addresses for the full list.
* **Off-chain loan documentation and lien recordation** (note, deed of trust, servicing records) are custodied by US document custodians.

### Proof of Reserves

* **On-chain USDC reserves** are fully verifiable in real time via the published program and vault addresses.
* **Mortgage collateral** is held on-chain as NFTs, each corresponding to a specific loan with a recorded lien on the underlying US residential property.&#x20;
  * The NFT collection and its ownership are independently verifiable on Solana.&#x20;
  * See Contract Addresses for the mortgage NFT collection address.

Stable hosts a Reserves & Transparency page at [trystable.co/reserves](https://trystable.co/reserves) that displays a near real time report on mortgages, reserves, and the health of USDX including links to relevant addresses, collections, and documentation.
