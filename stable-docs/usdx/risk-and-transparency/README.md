# Risk & Transparency

This section documents how USDX is backed, how collateral is underwritten and monitored, and the risks that affect USDX holders. It is intended to be read by integrators, lending markets, risk teams, and anyone looking to hold or build against USDX.

### Scope

The pages in this section describe **USDX on Solana**. USDX is also deployed to Base, Monad, and Ethereum, but those deployments are treasury-isolated per chain and are not bridgeable to or from Solana today — so risks affecting those chains do not flow to Solana USDX holders, and vice versa. Where this section makes claims about "USDX," it means USDX on Solana unless otherwise noted.

### In this section

* [**Reserves & Proof of Reserves**](reserves-and-proof-of-reserves.md) — what backs USDX on Solana today, how USDC minting flows into reserves, custody, and how reserves can be verified.
* [**Underwriting & Risk Management**](underwriting-and-risk-management.md) — how Stable Home Accounts are approved, how mortgage collateral is diligenced, ongoing monitoring, and how the USDX/USDC peg is defended on Solana.
* [**Risk Disclosures**](risk-disclosures.md) — the categorized risk surface: credit, market, liquidity, peg, counterparty, regulatory, governance, and smart contract dependencies.

### Further reading

* [What is USDX](https://medium.com/stable-inc/what-is-usdx-1726a7425d49) — product overview and motivation
* [How Stable Manages Fed Policy Risk in USDX](https://medium.com/stable-inc/how-stable-manages-fed-policy-risk-in-usdx-98e3eef92222) — how the mortgage book is positioned against interest rate shocks

### Changelog

Pages in this section are living documents and are updated as reserves, counterparties, and protocol parameters change. The authoritative on-chain references are listed on Contract Addresses — when in doubt, verify against the chain.

### Reserves

Stable hosts a Reserves & Transparency page at [trystable.co/reserves](https://trystable.co/reserves) that displays a near real time report on mortgages, reserves, and the health of USDX including links to relevant addresses, collections, and documentation.
