from typing import Any
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server.
mcp = FastMCP("hackage_docs")

@mcp.tool()
async def get_docs(package: str, version: str, module: str) -> str:
    """
    Retrieve the documentation for a specific module of a Haskell package from Hackage.
    
    Args:
        package: The full Hackage package name (e.g. "yesod-persistent").
        version: The package version (e.g. "2.10.0").
        module: The module name to look up (e.g. "Database.Persist" or "Control.Lens").
    
    Returns:
        The extracted documentation text for the specified module, or an error message.
    
    Example calls:
      - get_docs("lens", "5.0.0", "Control.Lens")
      - get_docs("vector-algorithms", "0.8.0", "Data.Vector.Algorithms")
    """
    # Construct the URL for the package's documentation index.
    base_url = f"https://hackage.haskell.org/package/{package}-{version}"
    
    # Fetch the overall package page.
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(base_url, timeout=30.0)
            response.raise_for_status()
        except Exception as e:
            return f"Error fetching package page from {base_url}: {str(e)}"
    
    # Parse the overall package page.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Look for an <a> tag whose text exactly matches the module name.
    module_link_tag = soup.find("a", string=lambda s: s and s.strip() == module)
    if not module_link_tag:
        return f"Module '{module}' not found on the package page."
    
    # Extract the href attribute and convert it to an absolute URL.
    module_href = module_link_tag.get("href")
    module_url = urljoin(base_url, module_href)
    
    # Fetch the module's documentation page.
    async with httpx.AsyncClient() as client:
        try:
            mod_response = await client.get(module_url, timeout=30.0)
            mod_response.raise_for_status()
        except Exception as e:
            return f"Error fetching module page from {module_url}: {str(e)}"
    
    # Parse and clean the module page HTML.
    mod_soup = BeautifulSoup(mod_response.text, "html.parser")
    for tag in mod_soup(["script", "style"]):
        tag.decompose()
    
    text = mod_soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = "\n".join(line for line in lines if line)
    
    return cleaned_text

if __name__ == "__main__":
    # Run the MCP server using the stdio transport.
    mcp.run(transport="stdio")
