# Risk Disclosures

### Scope

This page covers material risks affecting **USDX on Solana**. USDX deployments on Base, Monad, and Ethereum have treasury-isolated reserves with no bridging to or from Solana today, so risks affecting those deployments are not in scope and do not flow to Solana USDX holders.

### Credit risk

The mortgage portion of Solana USDX reserves is exposed to borrower default and property value decline. Exposure is mitigated by:

* US residential properties only
* Maximum combined LTV of 85% across all liens on the property at the time of deployment unless a first lien [qualified mortgage](https://www.investopedia.com/terms/q/qualified-mortgage.asp)
* Lien position recorded on the property (first-lien or second-lien), with the NFT representing a claim on the underlying loan
* Title, lien, ownership, existing-debt, and insurance verification before any USDX is deployed against a Stable Home Account
* Per-deployment approval on top of initial Home Account approval
* Quarterly real estate value reassessment
* Ongoing monitoring of payment status and lien position

**Second-lien exposure.** A portion of the mortgage book is held in second-lien position, which is subordinate to the senior lienholder in the event of default. Losses on second-lien loans are absorbed before losses on first-lien loans, and recoveries depend on property value net of the senior lien balance. The 85% combined LTV cap limits this exposure.

A severe US housing downturn or a spike in residential mortgage defaults would impair the mortgage reserve and could affect redemption capacity, with second-lien loans absorbing impairment first.

### Market risk

Mortgage collateral is valued against US residential real estate prices, which can decline. The first-lien-and-second-lien-with-85%-combined-LTV policy provides buffer, but reserve value moves with the US housing market.

### Liquidity risk

Mortgage collateral is not natively liquid. Solana USDX mitigates this by holding a portion of reserves in USDC — either idle against pending redemptions or deployed into on-chain lending pools (Kamino, Jupiter Lend) that are callable on a short timescale. Under a simultaneous redemption surge and a frozen secondary market for residential mortgages, permissionless redemptions may run at the longer end of the 24-hour-to-7-day processing window.

### Peg risk

The on-chain peg defender operates against the Raydium USDX/USDC pool. Under extreme stress — particularly if the pool is thin relative to sell pressure, or if the program's express-redemption USDC reserve is depleted — USDX may temporarily trade below $1 on Solana. The peg defender requires reserves and can be overwhelmed in the tail.

### Counterparty risk

Solana USDX depends on:

* **On-chain venues holding reserves:** Kamino, Jupiter Lend
* **On-chain venues supporting peg defense:** Raydium (primary USDX/USDC liquidity), Jupiter (swap routing), Helius (RPC), Alchemy (Yellowstone gRPC stream)
* **Off-chain counterparties:** Stable (servicer for Home Account loans), third-party servicers for non-Home-Account loans

Failure of any of these counterparties may impair reserves, delay redemptions, or degrade peg defense.

### Regulatory risk

USDX on Solana is backed by mortgages on US residential real property, which are subject to US mortgage regulation. Stable Home Accounts involve KYC/AML and title verification of US consumers. Changes in law, regulatory interpretation, or enforcement posture could affect the availability of eligible collateral, servicing arrangements, the legal characterization of USDX, or the set of available redemption paths.

### Governance / admin risk

USDX programs on Solana are currently upgradeable by the upgrade authority listed on Contract Addresses. A compromise of upgrade authority could result in malicious program upgrades.

### Smart contract dependencies

USDX on Solana is made up of multiple Anchor programs listed on Contract Addresses. External program dependencies (Kamino, Jupiter Lend, Raydium, Jupiter router) each carry their own smart contract surface that propagates to USDX reserves and peg defense.

### Chain isolation

USDX on Monad, Base, and Ethereum has treasury reserves isolated per chain and is not bridgeable to or from Solana today. Risks affecting those deployments are not in scope for this page and do not affect Solana USDX holders.
