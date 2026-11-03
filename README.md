# Celo AgentBridge — Frontier Pool Starter Kit
**Tagline:** Trust. Discover. Transact. Verify.

Celo AgentBridge is a proposed open-source infrastructure layer for AI agents. It is intended to help agent developers discover counterparties, verify identity references, request/authorize payments, and produce auditable transaction records on Celo.

> **STATUS: prototype scaffold — NOT deployed.** This package does not claim a Celo mainnet deployment, ERC-8004 registration, Self Agent ID, audited contracts, users, or transactions.

## Included
- Frontier grant application draft with honest status wording and completion fields.
- Technical architecture, implementation roadmap, and security plan.
- Solidity escrow prototype for local/testnet review only.
- Python SDK scaffold for validating payment intents.
- Two-agent demo plan.

## Proposed MVP
1. ERC-8004-compatible agent identity/discovery adapter.
2. Self Agent ID verification adapter, implemented against current official specifications.
3. Typed payment-intent schema.
4. Explicitly authorized agent-to-agent payment flow.
5. Optional conditional escrow contract and public event interface.
6. Developer SDK and reproducible examples.

## Safety rules
- Never store private keys in this repository, frontend, logs, or agent prompts.
- Agents may propose payments but must not silently authorize spending.
- Use testnet and local tests first; obtain independent security review before mainnet.
- Verify current ERC-8004 and Self Protocol specifications before implementing adapters.
- Do not submit this package as proof of deployment or traction.

## SDK quick start
```bash
cd sdk/python
python -m pip install -e .
python -c "from agentbridge import PaymentIntent, validate_payment_intent; p=PaymentIntent('0x'+'1'*40,'0x'+'2'*40,1000000,'cUSD','demo-001'); validate_payment_intent(p); print(p)"
```

## Contract development
Install Foundry, copy `contracts/AgentBridgeEscrow.sol` into a Foundry project's `src/`, then run `forge build` and write tests before any deployment.

## Submission gate
Complete every [VERIFY] field in `docs/FRONTIER_APPLICATION_DRAFT.md`. Frontier requires a working Celo mainnet deployment, applicable ERC-8004 registration, Self Agent ID, verifiable real-use on-chain activity, and a demo. Do not claim these until independently verifiable.
