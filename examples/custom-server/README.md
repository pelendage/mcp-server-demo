# Example - custom MCP server on Databricks Apps

This example shows how to create and launch a custom agent on Databricks Apps. 
Please note that this example doesn't use any Databricks SDK, and is independent of the `mcp` package in the root dir of this repo.

## Prerequisites

- Databricks CLI installed and configured
- `uv`

## Local development

- run `uv` sync:

```bash
uv sync
```

- start the server locally. Changes will trigger a reload:

```bash
uvicorn custom-server.app:mcp --reload
```

## Deploying a custom MCP server on Databricks Apps

- In this directory, run the following command to deploy and run the MCP server on Databricks Apps:

```bash
uv build --wheel
databricks bundle deploy -p <name-of-your-profile>
databricks bundle run custom-server -p <name-of-your-profile>
```

## Connecting to the MCP server
To connect to the MCP server, use the `Streamable HTTP` transport with the following URL:

```
https://your-app-url.usually.ends.with.databricksapps.com/api/mcp/
```

For authentication, you can use the `Bearer` token from your Databricks profile.
You can get the token by running the following command:

```bash
databricks auth token -p <name-of-your-profile>
```

Please note that the URL should end with `/api/mcp/` (including the trailing slash), as this is required for the server to work correctly.