from dataclasses import dataclass
import re

_ADDRESS = re.compile(r"^0x[a-fA-F0-9]{40}$")

@dataclass(frozen=True)
class PaymentIntent:
    payer: str
    payee: str
    amount: int
    token_symbol: str
    reference: str
    chain_id: int = 42220  # Celo mainnet; override for test environments.

def validate_payment_intent(intent: PaymentIntent) -> None:
    """Validate basic shape only; this does not authorize or submit a transaction."""
    if not _ADDRESS.match(intent.payer):
        raise ValueError("payer must be a 20-byte EVM address")
    if not _ADDRESS.match(intent.payee):
        raise ValueError("payee must be a 20-byte EVM address")
    if intent.payer.lower() == intent.payee.lower():
        raise ValueError("payer and payee must be different")
    if not isinstance(intent.amount, int) or intent.amount <= 0:
        raise ValueError("amount must be a positive integer in token base units")
    if not intent.token_symbol or len(intent.token_symbol) > 16:
        raise ValueError("token_symbol must contain 1–16 characters")
    if not intent.reference or len(intent.reference) > 128:
        raise ValueError("reference must contain 1–128 characters")
    if intent.chain_id <= 0:
        raise ValueError("chain_id must be positive")
