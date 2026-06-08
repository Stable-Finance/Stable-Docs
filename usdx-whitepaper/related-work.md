# Related Work

## 14. Related Work

**Fiat-backed stablecoins.** USDC, USDT, and similar instruments have established the pattern of a regulated issuer backing a dollar-pegged token with short-duration government securities. USDX shares the redemption primitive and the regulatory posture, but departs by holding longer-duration, cashflowing collateral.

**Crypto-collateralized stablecoins.** MakerDAO's DAI, Liquity's LUSD, and related designs back their stablecoins with crypto collateral using overcollateralized CDPs. These designs achieve decentralization at the cost of capital efficiency, and have historically struggled in market stress events where collateral and liability are correlated. USDX's collateral is structurally uncorrelated with crypto markets, addressing this failure mode.

**Algorithmic stablecoins.** Terra's UST, Iron Finance's IRON, and prior algorithmic designs attempted to maintain a peg without full collateralization. The failure modes of these designs are well-documented; USDX does not pursue this design and is fully collateralized in all operational states.

**Delta-neutral yield stablecoins.** Ethena's USDe backs its stablecoin with delta-neutral positions in crypto perpetual futures, generating yield from funding rate spreads. This shares the staked-wrapper pattern (sUSDe) with USDX's mUSDX, but differs fundamentally in collateral — USDe is backed by derivatives positions while USDX is backed by real-asset cashflows.

**Tokenized real-world assets.** Ondo's USDY, Backed Finance's products, and Maker/Sky's RWA vaults have introduced tokenized T-bills and private credit to the onchain ecosystem. USDX extends this trajectory into the residential mortgage asset class, the largest single RWA category by outstanding principal.

**Hardware-backed stablecoins.** USDai backs its synthetic dollar with tokenized AI hardware collateral and introduces a queue-based redemption mechanism. USDX shares the queue-based redemption architecture while applying it to a different collateral class — residential mortgages rather than GPU infrastructure.

**Onchain mortgage credit.** Recent efforts have begun directing onchain capital toward residential mortgage credit — most visibly through private-credit facilities and warehouse-style funding lines that channel stablecoin-ecosystem capital to mortgage originators, such as arrangements connecting the Sky ecosystem with originators like Better. These structures principally provide a funding channel: onchain capital funds mortgage lending, with the loans warehoused or held on the originator's side. USDX differs in architecture rather than degree. Rather than supplying a credit line to a third-party lender, USDX holds mortgage and MBS collateral directly in its own reserve, can source newly originated loans into that reserve through a native origination channel, diversifies across four reserve asset classes including agency MBS, passes portfolio yield to holders through mUSDX, and protects holders through an explicit four-step loss waterfall. The distinction is between funding someone else's mortgage book and building the stablecoin's own reserve out of mortgage collateral.
