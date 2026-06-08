# Technical Overview of USDX

## Technical Overview of USDX

Let’s walk through a step process on how USDX is created, including technical details.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXdacXeYMZIt7K3XS9mbgo8eYF2hC6LAAU_g_mrkEpRDHtoUatcjXtL21SJtHy19NTBmJ8C4naISv-SezcDiUbRXgWww8nG0q64vAokKNi7iYHQ5Oir_Ml3TP9H68Cy9hPPctaXrmA?key=vW1rn2vc2I8X-NIJVoW3qXaj" alt=""><figcaption></figcaption></figure>

### 1. Tokenization of Real Estate (Assets)

Properties are transferred to a legal entity by the signing of one of a few possible documents by the existing owner or new buyer, and that entity is represented on-chain as an NFT.

In Solana Virtual Machine (“SVM”) environments those NFTs are currently Core NFTs, and in Ethereum Virtual Machine (“EVM”) environments those NFTs are currently ERC-721 tokens.&#x20;

Many tokens and standards have been proposed and experimented with in recent years; for now Stable sticks to these generalized standards because they are composable within the environments where they are deployed.&#x20;

Stable is building a new standard that is necessary to holistically represent the asset onchain.

### 2. USDX-Enabled

“USDX-Enabled” assets are able to borrow from a USDX line of credit at any time. Their value, credit, and debt (including any offchain debt) are constantly monitored and updated.

A combination of oracles and ZK technology that are integrated with Tokenized Property NFT connect offchain data, like the new appraised value or the status of an offchain debt, that is necessary for the NFTs to function properly.&#x20;

### 3. Borrowing USDX

Now that the USDX-Enabled Asset is setup onchain, the owner decides to borrow some USDX.

The asset has a defined line of credit that includes a maximum loan-to-value ratio (“LTV”) and a fixed or floating interest rate (APR) that is due on the 1st of each month. All values are currently defined in US dollars and the currencies that can be used to repay principal and interest are USDC, USDT, and USDX. If USDC or USDT are deemed to have depegged (e.g. fallen below $0.99 in value) then they may not be accepted by the protocol.

### 4. Outstanding USDX Debt

When the owner executes a loan (“borrows”), USDX is minted from the USDX Protocol to the owner’s wallet. Simultaneously a NFT representing the debt position (“Debt NFT”) that was created is minted to the protocol’s treasury. USDX is a standard ERC-20 token in EVM environments and a SPL in SVM environments. The Debt NFT is an ERC-721.&#x20;

Except for opportunities that make the protocol’s collateral less liquid, Debt NFTs can be liquidated by the protocol at any time for any reason in any way as long as the liquidation ensures USDX remains overcollateralized in US dollar terms. USDX can be redeemed for these Debt NFTs in chunks of 100,000.

If Stable has minted the USDX then yield payments will be noted on the debt NFT and passed through to the asset owner’s wallet.

### Privacy and Unlocks

1. Privacy and Risk Evaluation
   1. Risk Scores and Account Health for each NFT and the owner are provided by a growing number of community participants.
2. Unlock Period
   1. Stable tokenizes assets in a way that those assets do not lose their offchain functionality. Stable is the first to do this because it is not easy, but it is important.&#x20;
   2. Tokenized assets are therefore able to have a cooldown period before the asset is no longer tokenized. This cooldown period can be assumed to be 1 to 30 days.
   3. Cooldown periods are used to ensure outstanding debts and claims related to onchain activities are settled before the asset is no longer available onchain. All known, valid disputes must be resolved before this cooldown period begins.

### Zero Knowledge Proofs

Zero knowledge proofs (ZK) are used by the USDX Protocol to maintain an onchain system while preserving users’ personally identifiable and sensitive information. ZK enables onchain verification of if the loan is interest only or not, the total amount (principal + interest) a given borrower owes for a given month, if that borrower has missed payments, and more.&#x20;

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXePtI3M1qV1tkZAeAR0byYBW8q5Cynj5QH-ur9uzGrSYAR3QIjsSJc42kVMqKpegjKwQD-gUfkrspgWwZKPtT-46IJX-EjWhYoy7QOoND7tyjvn5rPbfoKTyh7LlvaeZAIU5k0i?key=vW1rn2vc2I8X-NIJVoW3qXaj" alt=""><figcaption></figcaption></figure>
