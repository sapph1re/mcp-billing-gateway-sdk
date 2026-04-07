"""MCP Billing Gateway — Demo server showing billing infrastructure capabilities."""
from fastmcp import FastMCP

mcp = FastMCP(
    name="mcp-billing-gateway",
    version="1.0.0",
    instructions=(
        "MCP Billing Gateway: Add Stripe subscriptions, per-call credits, tiered pricing, "
        "and x402 crypto micropayments to any MCP server. Self-hosted billing infrastructure "
        "for MCP server operators. See https://github.com/sapph1re/mcp-billing-gateway-sdk "
        "for full documentation and integration guide."
    ),
)


@mcp.tool()
def get_billing_info() -> dict:
    """Get information about the MCP Billing Gateway service and integration options."""
    return {
        "service": "MCP Billing Gateway",
        "version": "1.0.0",
        "payment_methods": ["stripe_subscription", "stripe_metered", "x402_crypto"],
        "features": [
            "Per-call usage tracking",
            "Tiered pricing (free/pro/growth)",
            "Stripe subscriptions and metered billing",
            "x402 micropayments (USDC on Base)",
            "Operator dashboard",
            "API key management",
        ],
        "docs": "https://github.com/sapph1re/mcp-billing-gateway-sdk",
        "deployment": "Self-hosted on Railway, Fly.io, or any Docker host",
    }


if __name__ == "__main__":
    mcp.run()
