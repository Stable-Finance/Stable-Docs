---
description: Permissioned APIs for institutional USDX issuance, redemption, and exchange integration.
---

# API overview

## Integrate Stable into institutional infrastructure

Stable's APIs connect approved counterparties to USDX minting, redemption, account management, and exchange workflows. Production access requires completed KYC/KYB and assigned actor credentials.

<a href="usdx-api.md" class="button primary">USDX API</a> <a href="exchange-api.md" class="button secondary">Exchange API</a>

<table data-view="cards">
  <thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
  <tbody>
    <tr>
      <td><strong>USDX API</strong></td>
      <td>Mint, redeem, and manage USDX through approved institutional accounts.</td>
      <td><a href="usdx-api.md">usdx-api.md</a></td>
    </tr>
    <tr>
      <td><strong>Exchange API</strong></td>
      <td>Connect institutional systems to tokenized asset exchange workflows.</td>
      <td><a href="exchange-api.md">exchange-api.md</a></td>
    </tr>
  </tbody>
</table>

{% hint style="info" %}
API credentials are confidential and must remain in server-side infrastructure. Never expose production credentials in browser code, public repositories, or client-distributed applications.
{% endhint %}
