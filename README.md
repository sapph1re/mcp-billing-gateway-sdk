<!-- mcp-name: io.github.sapph1re/mcp-billing-gateway -->
# MCP Billing Gateway

[![Glama MCP Server](https://glama.ai/mcp/servers/sapph1re/mcp-billing-gateway-sdk/badge)](https://glama.ai/mcp/servers/sapph1re/mcp-billing-gateway-sdk)

Add **Stripe subscriptions**, **per-call credits**, and **x402 crypto payments** to any MCP server — without writing billing code.

Live service: **https://mcp-billing-gateway-production.up.railway.app**

---

## What it does

MCP Billing Gateway is a proxy that sits in front of your MCP server and handles all billing automatically:

- **Per-call billing** — charge callers per tool call (fiat or crypto)
- **Subscriptions** — monthly/annual Stripe plans with call limits
- **Tiered pricing** — free tier + paid tiers based on usage
- **x402 micropayments** — accept USDC on Base from AI agents with no API keys
- **Operator dashboard** — track revenue, usage, and callers in real time

## How it works

```
AI Agent → MCP Billing Gateway → Your MCP Server
            (billing enforced here)
```

1. Register as an operator
2. Register your MCP server URL + pricing plan
3. Point callers to your proxy slug: `https://mcp-billing-gateway.../proxy/{your-slug}/...`
4. Callers pay via Stripe API key or x402 USDC — billing is handled transparently

## Quick Start

### Register as operator

```bash
curl -X POST https://mcp-billing-gateway-production.up.railway.app/api/v1/operator/register \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com", "name": "Your Name"}'
```

### Register your MCP server

```bash
curl -X POST https://mcp-billing-gateway-production.up.railway.app/api/v1/servers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My MCP Server",
    "upstream_url": "https://your-mcp-server.com/mcp",
    "proxy_slug": "my-server"
  }'
```

### Create a pricing plan

```bash
curl -X POST https://mcp-billing-gateway-production.up.railway.app/api/v1/servers/{server_id}/plans \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Pay as you go",
    "billing_model": "per_call",
    "price_per_call_usd_micro": 10000,
    "free_calls_per_month": 100
  }'
```

### Callers connect to your proxied server

```json
{
  "mcpServers": {
    "my-server": {
      "url": "https://mcp-billing-gateway-production.up.railway.app/proxy/my-server/mcp",
      "headers": {
        "Authorization": "Bearer CALLER_API_KEY"
      }
    }
  }
}
```

## Payment Methods

| Method | Best for | How |
|--------|----------|-----|
| Stripe subscription | Human developers | Monthly/annual plan |
| Stripe per-call | Human developers | Credits consumed per call |
| x402 micropayments | AI agents | USDC on Base, no API keys |

## Operator Dashboard

Access your dashboard at:
```
https://mcp-billing-gateway-production.up.railway.app/dashboard
```

Track revenue, usage, active callers, and configure your servers.

## API Reference

Full API docs at: https://mcp-billing-gateway-production.up.railway.app/health

### Operator endpoints
- `POST /api/v1/operator/register` — create operator account
- `GET /api/v1/operator/profile` — view profile and API keys
- `GET /api/v1/operator/stats` — revenue and usage stats

### Server management
- `POST /api/v1/servers` — register an MCP server
- `GET /api/v1/servers` — list your servers
- `POST /api/v1/servers/{id}/plans` — create pricing plan

### Proxy
- `* /proxy/{slug}/*` — proxied calls with billing enforcement

## Self-hosted

The gateway is open for use. If you need a self-hosted deployment, contact us.

## License

MIT

<!-- mcp-name: io.github.sapph1re/mcp-billing-gateway -->
