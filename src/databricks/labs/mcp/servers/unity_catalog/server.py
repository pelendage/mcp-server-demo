from databricks.labs.mcp.servers.unity_catalog.app import get_prepared_mcp_app


def start() -> None:
    mcp = get_prepared_mcp_app()
    mcp.run(transport="stdio")
