# Security and test plan

## Before testnet release
- Unit-test every contract state transition.
- Test zero addresses, zero amounts, self-payments, expired deadlines, duplicate release, refund/release races, reentrancy attempts, and failed transfers.
- Add ERC-20 support only with safe transfer handling and explicit token allowlists.
- Add chain-ID/domain separation and nonce/replay protection to signed intents.
- Run static analysis, fuzz tests, and invariant tests.
- Add CI for formatting, build, tests, and static analysis.

## Before mainnet
- Obtain independent security review/audit.
- Verify source code on the Celo explorer.
- Publish contract addresses, deployment transactions, ABI, chain ID, and reproducible build settings.
- Establish incident response and pause/upgrade policy, or document immutability.
- Confirm current Self Protocol and ERC-8004 requirements.
- Use limited pilot amounts and explicit spending limits.

## Product metrics
Independent developer integrations, weekly active agents, unique counterparties, successful payment intents, meaningful settlements, failed transaction rate, and security incidents. Do not optimize for raw transaction counts.
