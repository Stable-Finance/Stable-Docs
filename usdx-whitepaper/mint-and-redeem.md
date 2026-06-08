# Mint and Redeem

## 5. Mint and Redeem

### 5.1 Minting Surfaces

USDX supports two minting surfaces, each serving a distinct user class:

**Permissionless Mint.** Any user with a supported stablecoin can deposit to the mint contract and receive USDX 1:1, less a mint fee of 10 basis points. At launch the supported set begins with the most liquid, most credible dollar stablecoin and expands by governance as warranted. This surface is open, pseudonymous, and available 24/7 onchain. Deposited stablecoins are routed by the protocol treasury into the reserve portfolio, with the allocation mix determined by the current rebalancing schedule.

**Institutional Mint.** Institutional participants with appropriate KYC/KYB and custody arrangements may deposit eligible collateral — whole mortgage loans or agency MBS — and receive USDX at a value reflecting the mark-to-market price of the deposited assets, less a mint-side haircut. This surface is permissioned, off-chain-initiated, and settled onchain once collateral custody is confirmed by the protocol.

Both surfaces ultimately route deposits into the same reserve portfolio, and both produce the same USDX token.

### 5.2 Redemption

USDX redemption is structured as a tiered queue rather than an instant-settlement guarantee. The protocol offers two redemption paths at the permissionless level and a third at the institutional level. No redemption path is a same-day obligation of the protocol; industry-standard stablecoin redemption settlement is typically one to three business days, but the protocol does not commit to this schedule prior to scale.

**Default redemption (7-day window, 20 bps fee).** A USDX holder initiates a redemption request by depositing USDX to the redemption contract. The request is queued; redemption is processed within seven days, with the holder receiving dollars (in a supported stablecoin) at par less a 20 basis point redemption fee. This is the protocol's standard redemption path and is designed to match or improve on industry redemption practices.

**Expedited redemption (1–3 business day window, 60 bps fee).** For time-sensitive redemption needs, holders may elect an expedited path with a 1–3 business day target settlement window and a 60 basis point fee. Expedited redemption is best-effort: the protocol does not guarantee that sufficient rapid liquidity is available to fulfill every expedited request at every moment. Expedited requests that cannot be filled within the target window are automatically re-queued to the default 7-day path at the default fee.

**Extended settlement window.** In periods of elevated redemption demand or collateral market stress, redemption settlement may extend up to 45 days to allow orderly liquidation of reserve assets without forced sale at unfavorable prices. Holders are notified if their redemption request enters the extended window.

**Institutional redemption.** Institutional participants may redeem starting at 100,000 USDX per request against a pro rata share of the reserve portfolio, with a settlement window negotiated between the institution and the protocol and typically ranging from T+1 to T+5 business days.

The redemption-queue architecture is analogous to structures used in tokenized-credit protocols such as USDai's queue-based redemption and is consistent with how regulated asset-management products redeem against underlying portfolios. The design prioritizes peg integrity and reserve stability over the unfounded expectation of instantaneous settlement.

### 5.3 Fees

Mint and redemption fees accrue to the protocol and are used primarily to build reserves for USDX. Fees flow into the reserve portfolio, reinforcing collateralization over time, and may also cover operating expenses to the extent that portfolio yield alone is insufficient. Fee parameters (mint fee, default redemption fee, expedited redemption fee) are adjustable within protocol-defined bounds. Initial values are stated in Appendix B.
