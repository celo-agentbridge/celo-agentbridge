# Two-agent demo script (planned)

1. Start Agent A (buyer) and Agent B (service provider).
2. Agent B publishes its public identity reference, capabilities, supported token, and payment terms.
3. Agent A resolves Agent B through the directory adapter and validates the identity reference.
4. Agent A creates a payment intent with amount, token, chain ID, expiry, and unique reference.
5. A payer-controlled wallet displays recipient, token, amount, chain, and expiry for approval.
6. After approval, Agent A deposits funds into the escrow contract.
7. Agent B performs the service and claims escrow according to the MVP release rule.
8. The demo displays the Celo transaction hash, contract event, and explorer link.

Do not describe identity as Self-verified until Self Agent ID integration exists. Do not describe escrow as AI-output verified: this starter contract only supports payee release or payer refund after expiry.
