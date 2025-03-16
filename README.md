# Hackage Documentation MCP

## Overview

This Machine-Controlled Program (MCP) provides an interface for AI assistants to access Haskell documentation from Hackage. It allows AI models to retrieve precise, up-to-date documentation for specific Haskell modules, improving the AI's ability to assist with Haskell programming despite limited training data in this domain.

## Problem Statement

AI language models often have insufficient training data on Haskell compared to more mainstream programming languages. This results in:

- Less accurate code generation for Haskell
- Difficulty understanding Haskell's unique features and abstractions
- Inaccurate or outdated information about Haskell libraries and modules

This tool bridges that gap by enabling AI to retrieve authoritative documentation from Hackage in real-time.

## Features

- Retrieve documentation for specific modules from any package on Hackage
- Specify exact package versions to ensure accuracy
- Clean, text-based output that's easily consumable by AI assistants

## Installation

1. Ensure you have Python 3.7+ installed
2. Install the required dependencies:
   ```
   pip install httpx beautifulsoup4 fastmcp
   ```

## Usage

You can use this MCP with any AI assistant that supports the MCP protocol.

### Running the Server

```bash
python main.py
```

This will start the MCP server using stdio transport.

### API

The MCP exposes the following tool:

#### `get_docs(package, version, module)`

Retrieves documentation for a specific Haskell module.

**Parameters:**
- `package` (string): The Hackage package name (e.g., "lens", "yesod-persistent")
- `version` (string): The package version (e.g., "5.0.0", "2.10.0")
- `module` (string): The module name to look up (e.g., "Control.Lens", "Database.Persist")

**Returns:**
- The extracted documentation text for the specified module, or an error message if retrieval fails

**Examples:**
```python
# Get documentation for Control.Lens from lens 5.0.0
get_docs("lens", "5.0.0", "Control.Lens")

# Get documentation for Data.Vector.Algorithms from vector-algorithms 0.8.0
get_docs("vector-algorithms", "0.8.0", "Data.Vector.Algorithms")
```

## Use Cases

1. **Learning Haskell libraries**: Get detailed information about specific modules while working with the AI
2. **Understanding type signatures**: Access accurate type information for functions in Haskell modules
3. **Exploring module hierarchies**: Understand how modules are organized within Haskell packages
4. **Verifying AI-generated code**: Compare AI suggestions with official documentation

## Benefits

- Provides AI with access to accurate, up-to-date Haskell documentation
- Improves the quality of AI-generated Haskell code
- Enhances the AI's ability to explain Haskell concepts with authoritative references
- Reduces hallucinations when discussing Haskell libraries

## Limitations

- Requires an internet connection to access Hackage
- Only provides documentation content, not the implementation code
- Documentation quality varies between Haskell packages

## Contributing

Contributions to improve this tool are welcome! Some potential areas for enhancement:

- Adding support for downloading and parsing package source code
- Implementing caching to reduce network requests
- Expanding to support other Haskell documentation sources

## License

[Specify your license here] 