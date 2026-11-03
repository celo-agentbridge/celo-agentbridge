# Prezenti Frontier Pool — Application Draft
## Celo AgentBridge

**Status: DRAFT ONLY.** Do not submit until every [VERIFY] item is completed and the product meets Frontier's technical requirements.

### Product name
Celo AgentBridge

### Team name
[VERIFY: enter the actual team or legal entity name.]

### Website
[VERIFY: publish a working project website and enter its real URL.]

### X Handle
[VERIFY: enter the project's actual handle, or N/A if permitted.]

### KarmaGAP profile
[VERIFY: create/confirm the real profile URL.]

### GitHub
[VERIFY: publish this repository under the team's real GitHub account/organization and enter the public URL.]

### ERC-8004 registration
[VERIFY: provide the actual registration reference and network. If claiming AI-infrastructure exemption, obtain confirmation that the exemption applies to this project.]

### Is your project fully open source?
Proposed answer: Yes, once the core contracts, SDK, schemas, and documentation are publicly released under MIT License. [VERIFY before selecting Yes.]

### Deployed on Celo mainnet
Current status: **No — not yet.** Do not select Yes until a working deployment is live and verifiable.

### Self Agent ID
Current status: **Not yet integrated.** Complete the required Self Protocol Agent ID integration and provide evidence before selecting Yes.

### Describe your project
Celo AgentBridge is an open-source agent-economy infrastructure layer designed to make autonomous software agents easier to discover, authenticate, and transact with on Celo. It combines identity-resolution adapters, a machine-readable agent directory interface, payment-intent standards, and an optional conditional escrow component. Developers can integrate the SDK into existing agents so an agent can resolve a counterparty's identity reference, inspect published capabilities and payment terms, request explicit payment authorization, and submit a verifiable settlement transaction on Celo.

The initial release focuses on a narrow workflow: Agent A discovers Agent B, resolves its identity metadata, checks declared capabilities, creates a payment intent, receives payer authorization, and settles a payment or conditional escrow on Celo. Settlements emit public events that indexers and downstream agents can inspect. The project is designed as reusable infrastructure for other builders, not a standalone consumer chatbot or marketplace.

### Infrastructure focus
AgentBridge is intended to be consumed by other agent developers through an SDK, documented API/schema, identity adapters, and smart-contract interfaces. A third-party developer should be able to add counterparty discovery and authorized on-chain payment capabilities to an existing agent without building a registry, payment-intent format, or escrow flow from scratch. The first reference demo will use two sample agents only to demonstrate integration with the reusable SDK and contracts.

### Verifiable on-chain activity
Current status: **No production activity is claimed.** Before submission, publish:
- Celo Mainnet contract address(es) and verified source-code links.
- Transaction hashes from genuine end-to-end agent payment/escrow use.
- Public explorer links and a short explanation for each transaction.
- Evidence that transactions represent real usage, not artificial volume or self-transfer farming.

[VERIFY: insert real links and transaction hashes. Never fabricate them.]

### Demo
Planned demo: two independent sample agents; one discovers the other, resolves identity metadata, requests scoped payment authorization, and settles a small transaction on Celo. The demo will show the SDK call, payer authorization boundary, transaction hash, and corresponding contract event.

[VERIFY: add a public demo URL or recording only after it exists.]

### How will you get agents to use your product? Activation path for first 10–100 users
**First 10:** recruit 5–10 Celo/AI-agent developers through targeted outreach; run 3–5 hands-on integration sessions; onboard 2–3 independent teams into an existing agent; publish examples and fix onboarding friction weekly.

**First 100:** publish stable SDK packages and documentation; run an integration bounty for useful third-party integrations; present technical demos in Celo and agent-builder communities; approach framework/tooling maintainers for concrete integrations; track activated developers, independent integrations, unique counterparties, and meaningful settlements.

[VERIFY: name only channels, partners, or events actually secured.]

### Distribution strategy and evidence
Distribution will be developer-led: open-source releases, concise documentation, sample integrations, technical demos, targeted outreach to agent-framework maintainers, and ecosystem workshops. The intended growth loop is composability: each developer integrating AgentBridge can expose compatible identity/payment capabilities to other agents.

Current evidence: this starter kit is the initial scaffold. It does not establish prior distribution, users, partnerships, or successful integrations. Before submission, add verifiable evidence such as repository history, developer interviews, documented pilot integrations, external contributions, and usage analytics.

### Previous work with Celo ecosystem
Select **None of the above** unless the team has formally engaged with one of the listed organizations. Informal chats do not count as formal engagement.

### Clear contribution to the ecosystem
AgentBridge aims to make Celo more useful as a settlement and coordination layer for autonomous agents. It contributes reusable identity-resolution adapters, agent discovery interfaces, payment-intent conventions, escrow primitives, and SDK tooling. These components can reduce integration work for Celo builders and make agent-to-agent commerce easier to verify on-chain. Success will be measured by independent integrations and meaningful transactions, not raw transaction counts.

### Technical credibility
The implementation is organized around a small, auditable workflow:
- Identity: standards-based identity references and adapters, not a proprietary identity claim.
- Authorization: explicit payer approval and scoped spending limits.
- Settlement: Solidity contracts with state boundaries and emitted events.
- Integration: typed payment-intent schema and SDK.
- Verification: public explorer references, reproducible tests, and a published threat model.

This repository is currently a scaffold. Technical credibility must be demonstrated through passing tests, deployed verified contracts, a working demo, public documentation, and independent review. Security review is required before real funds are used.

### Additional information
The team intends to build in public and prioritize a narrow, verifiable MVP. Grant funding would support engineering, testing, security review, documentation, and developer integration work—not liquidity or artificial activity.

### Required grant-delivery information
- Grant policies: [READ POLICIES; agree only if accepted.]
- Lead applicant name: [ENTER legal name exactly as shown on KYC document.]
- Email: [ENTER controlled email address.]
- Country company is registered: [ENTER actual jurisdiction. If no company is registered, ask Prezenti whether an individual/unincorporated team can contract.]
- Tech category: AI infrastructure / Agent tooling / Blockchain payments (choose closest available option).
- Logo: [UPLOAD final logo file.]
- Grant L2 delivery address: [ENTER a Celo-compatible address controlled by the applicant/team. Never share a seed phrase/private key.]

### Final submission gate
Do not submit until mainnet deployment, Self Agent ID, applicable ERC-8004 registration, verifiable real-use transactions, working demo, and public technical documentation are complete.
