from fastapi import FastAPI
from mcp.server import Server
from mcp.types import Tool as ToolSpec
from databricks.labs.mcp.base import get_serveable_app
from databricks.labs.mcp.servers.unity_catalog.tools import (
    Content,
)
from databricks.labs.mcp.servers.unity_catalog.cli import get_settings

from databricks.labs.mcp._version import __version__ as VERSION
from databricks.labs.mcp.servers.unity_catalog.server import get_tools_dict
from databricks.labs.mcp.servers.unity_catalog.tools.base_tool import BaseTool


mcp_server = Server(name="mcp-unitycatalog", version=VERSION)
tools_dict: dict[str, BaseTool] = get_tools_dict(settings=get_settings())


from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="mcp-unitycatalog",
)

for tool_name, tool in tools_dict.items():
    mcp.add_tool(
        tool.execute,
        name=tool_name,
        description=tool.tool_spec.description,
        annotations=tool.tool_spec.annotations,
    )

app = FastAPI(
    lifespan=lambda _: mcp.session_manager.run(),
)

streamable_app = mcp.streamable_http_app()
streamable_app.router.redirect_slashes = False  # so both /api/mcp and /api/mcp/ work

app.mount("/api", streamable_app)
