# mUSDX: Staked USDX

## 6. mUSDX: Staked USDX

### 6.1 Motivation

Dollar-pegged stablecoins must keep their price at $1. A stablecoin that pays yield directly to its holders — by rebasing or by distributing tokens — is inferior to one that does not, because (a) it creates a moving price target, (b) it introduces tax complexity in many jurisdictions, and (c) it complicates composability with DeFi protocols that assume a fixed-unit accounting model.

The solution is a yield-bearing wrapper. mUSDX is a tokenized, non-rebasing, exchange-rate wrapper over staked USDX. Staking USDX mints mUSDX at the prevailing exchange rate; unstaking burns mUSDX and returns USDX at the updated exchange rate. The exchange rate rises monotonically as the underlying reserve portfolio generates yield. This design mirrors the successful precedent of sUSDe (Ethena), sDAI (MakerDAO), and cToken-style wrappers.

mUSDX is DeFi-native and permissionless. Any holder of USDX can stake into mUSDX and any holder of mUSDX can initiate an unstake, subject to protocol-level parameters. mUSDX composes freely with lending protocols, liquidity pools, and structured products across the ecosystem.

### 6.2 Mechanism

Let E_t be the mUSDX-to-USDX exchange rate at time t, with E_0 = 1. As the reserve portfolio accrues net yield Y[t, t+Δ] over the interval [t, t+Δ], the exchange rate updates as:

> E_{t+Δ} = E_t · (1 + Y[t, t+Δ] / Vstaked_t)

where Vstaked_t is the aggregate USDX value staked into mUSDX at time t.

A user staking X USDX at time t receives X/E_t mUSDX. Subsequently, the user can unstake to receive X' = (X/E_t) · E_{t+τ} USDX at time t+τ, where X' ≥ X whenever the portfolio has generated positive net yield over τ.

The exchange rate update is triggered by a keeper transaction that reads the most recent net-yield accrual from the protocol treasury contract. Update frequency is at least daily.

### 6.3 Unstaking Cooldown

mUSDX implements a 7-day unstaking cooldown. A user who wishes to convert mUSDX back to USDX initiates an unstake request, at which point the mUSDX is locked in the cooldown contract. After 7 days, the user may complete the unstake, burning the mUSDX and receiving the corresponding USDX.

The cooldown addresses a fundamental asset-liability mismatch. The reserve earns yield by holding assets that are not all instantly liquid — agency MBS and whole loans settle and fund on timescales of days, not seconds. A cooldown aligns the timescale on which stakers can exit with the timescale on which the protocol can convert yield-bearing assets into redemption liquidity in an orderly way, rather than through forced sales at unfavorable prices. This is the same rationale behind the cooldown on comparable staked-wrapper designs such as sUSDe.

Concretely, the cooldown serves two purposes:

1. **Orderly liquidity sourcing.** A predictable exit window lets the treasury rebalance from MBS and whole loans into liquid reserves in time to meet unstake requests, without fire-selling collateral.
2. **Run resistance.** In market stress, a cooldown dampens reflexive unstake cascades that would otherwise amplify stress on the portfolio.

During the cooldown period, mUSDX continues to accrue yield through the exchange rate mechanism. Users who need immediate liquidity may sell mUSDX in secondary markets at prevailing prices. During periods of stress, mUSDX may trade at a small discount to its exchange rate; this discount represents the market's valuation of the cooldown and is a normal feature of the design.

### 6.4 Yield Source

The yield accruing to mUSDX stakers consists of:

1. Agency MBS coupon income, net of custody and servicing fees.
2. Whole loan interest income, net of servicing fees and any credit losses.
3. Tokenized mortgage interest, accruing on directly originated loans held in the reserve.
4. Liquid reserve yield, reflecting the short-duration yield on supported stablecoins, Treasury bills, and whitelisted lending-protocol positions.

Minus:

- Protocol overhead allocated to reserve growth and operations.
- Any draws on the reserve associated with loss events.

The residual is distributed to mUSDX stakers through the exchange rate. USDX holders who do not stake earn no yield; their choice is between the composability and cash-equivalent behavior of USDX and the yield accrual of mUSDX.
