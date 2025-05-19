from mcp.server import Server
from mcp.types import Tool as ToolSpec
from databricks.labs.mcp.base import get_serveable_app
from databricks.labs.mcp.servers.unity_catalog.tools import (
    Content,
)
from databricks.labs.mcp.servers.unity_catalog.cli import get_settings

from databricks.labs.mcp._version import __version__ as VERSION
from databricks.labs.mcp.servers.unity_catalog.server import get_tools_dict


mcp_server = Server(name="mcp-unitycatalog", version=VERSION)
tools_dict = get_tools_dict(settings=get_settings())


@mcp_server.list_tools()
async def list_tools() -> list[ToolSpec]:
    return [tool.tool_spec for tool in tools_dict.values()]


@mcp_server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[Content]:
    tool = tools_dict[name]
    return tool.execute(**arguments)


app = get_serveable_app(mcp_server)
