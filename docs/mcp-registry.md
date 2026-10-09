# Official MCP Registry publication

The repository's [`server.json`](../server.json) describes the hosted ExcelDashboard AI MCP service, separately from the report skill. The remote endpoint is `https://api.exceldashboard.ai/mcp`; users must complete OAuth before calling report tools.

## Metadata

- Registry name: `io.github.AlgForce/exceldashboard-ai`. Use the organization namespace granted by the Registry; match its spelling when authenticating.
- Website: https://www.exceldashboard.ai/mcp
- Transport: Streamable HTTP.
- Version: `0.1.0`, matching the current local MCP implementation's workspace package version. Confirm the deployed implementation version before publication if deployment differs from the local source.

The optional `repository` field is omitted because this repository contains skill instructions and examples, rather than the MCP server implementation. Remote-only publication does not require an npm package.

## Publish

The [publication workflow](../.github/workflows/publish-mcp.yml) uses the official GitHub Actions OIDC flow to authenticate as the AlgForce repository owner, without storing a personal access token. It runs when `server.json` or the workflow changes on `main`, and can be started manually from the repository's Actions tab. Forks and other branches cannot publish through this job. The job checks the configured identity and verifies the published metadata through the Registry API.

### Interactive alternative

Install `mcp-publisher` from the [official releases](https://github.com/modelcontextprotocol/registry/releases). Authenticate from a private working directory outside this repository, so credentials cannot be committed:

```bash
mcp-publisher login github
```

Follow the device authorization prompt in your browser. The authenticating personal GitHub account must be an Owner of AlgForce to publish under its organization namespace. See the [latest authentication documentation](https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/authentication.mdx).

If interactive authentication grants only your personal namespace, do not rename the listing as a workaround. Use the OIDC publication workflow above to retain the AlgForce identity. An Owner's role alone does not prove that the OAuth login has granted organization publishing permissions.

Then publish using the absolute path to this repository's `server.json`:

```bash
mcp-publisher publish /absolute/path/to/exceldashboard-skills/server.json
```

Confirm publication using the Registry API; check the exact name, version, and remote URL in the response:

```bash
curl 'https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.AlgForce/exceldashboard-ai'
```

GitHub publisher authentication and end-user MCP OAuth are separate. Never add access tokens, private keys, or login state to `server.json` or Git.

Publication is complete only after the Registry confirms the entry. A committed configuration alone is not evidence of a published listing.

Official references: [publishing tutorial](https://modelcontextprotocol.io/registry/quickstart), [remote server publication](https://modelcontextprotocol.io/registry/remote-servers), [server schema](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json).
