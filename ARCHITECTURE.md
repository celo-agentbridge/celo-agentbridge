# Architecture — Celo AgentBridge (proposed MVP)

## Components
1. **Agent Directory Adapter:** reads ERC-8004-compatible identity references and public metadata; provides search/resolve methods; does not claim to be the canonical registry.
2. **Self Identity Adapter:** verifies the required Self Agent ID reference using the current official Self Protocol flow. Never stores identity documents in public contract storage.
3. **Payment Intent:** typed object containing chain ID, token, payer, payee, amount, purpose/reference, expiry, and nonce. Payer authorization occurs through a wallet or scoped session key.
4. **Escrow/Settlement Contract:** holds only funds explicitly deposited by the payer; supports payee claim or payer refund after expiry; emits public events. Production use requires tests, review, verified source, and audit.
5. **SDK:** helpers to validate intents, resolve identity metadata, prepare transactions, and parse events. Keep interfaces framework-neutral.

## Trust boundaries
- Agent output is untrusted input.
- Identity metadata may be stale or malicious.
- On-chain identity proves control of an address/registration, not honesty or competence.
- Reputation is a signal, not a guarantee.
- Payment authorization remains with a human, wallet policy, or explicitly scoped delegated authority.
- Do not put personal data in permanent public events.

## MVP sequence
A. Local schema and SDK tests.
B. Testnet contract and two-agent demo.
C. Security review and threat-model updates.
D. Celo mainnet deployment and source verification.
E. ERC-8004 and Self Agent ID evidence.
F. Independent pilot integrations and real-use transaction evidence.

## Non-goals
General-purpose AI hosting, custody of user private keys, unrestricted autonomous spending, proprietary universal reputation scoring, or artificial transaction generation.
