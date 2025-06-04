from fastapi import FastAPI
from databricks.labs.mcp.servers.unity_catalog.cli import get_settings

from databricks.labs.mcp._version import __version__ as VERSION
from mcp.server.fastmcp import FastMCP
from databricks.labs.mcp.servers.unity_catalog.tools import get_tools_dict
from databricks.labs.mcp.utils import logger


def get_prepared_mcp_app() -> FastMCP:
    logger.info(
        f"Starting MCP Unity Catalog server version {VERSION} with settings: {get_settings()}"
    )
    mcp = FastMCP(
        name="mcp-unitycatalog",
    )
    tools_dict = get_tools_dict()

    @mcp._mcp_server.list_tools()
    async def list_tools():
        return [tool.tool_spec for tool in tools_dict.values()]

    @mcp._mcp_server.call_tool()
    async def call_tool(name: str, arguments: dict):
        tool = tools_dict[name]
        return tool.execute(**arguments)

    logger.info(f"Registered {len(tools_dict)} tools: {', '.join(tools_dict.keys())}")
    return mcp


mcp = get_prepared_mcp_app()

app = FastAPI(
    lifespan=lambda _: mcp.session_manager.run(),
)

streamable_app = mcp.streamable_http_app()

app.mount("/api", streamable_app)
