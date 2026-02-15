# justmyresource-lucide

JustMyResource pack for [Lucide icons](https://lucide.dev/) - provides access to 1500+ SVG icons from the Lucide icon library.

This is a resource pack for [JustMyResource](https://github.com/kws/justmyresource), a resource discovery and resolution library for Python.

## Installation

```bash
pip install justmyresource-lucide
```

This package requires:
- [`justmyresource`](https://github.com/kws/justmyresource) (>=0.1.0,<0.2.0)
- `lucide` (>=1.1.3,<2.0.0)

## Usage

### Basic Usage

```python
from justmyresource import ResourceRegistry

# Create registry with lucide as default prefix
registry = ResourceRegistry(default_prefix="lucide")

# Get an icon (bare name with default_prefix)
content = registry.get_resource("lightbulb")
svg_text = content.text  # SVG as string

# Or use explicit prefix
content = registry.get_resource("lucide:lightbulb")

# Or use the short alias
content = registry.get_resource("luc:lightbulb")

# Or use fully qualified name
content = registry.get_resource("justmyresource-lucide/lucide:lightbulb")
```

### Listing Icons

```python
from justmyresource import ResourceRegistry

registry = ResourceRegistry()

# List all icons in the lucide pack
for resource_info in registry.list_resources(pack="lucide"):
    print(f"{resource_info.name}")  # e.g., "lightbulb", "a-arrow-down"

# List all icons from all packs
for resource_info in registry.list_resources():
    if resource_info.pack == "justmyresource-lucide/lucide":
        print(f"{resource_info.name}")
```

### Working with SVG Content

```python
from justmyresource import ResourceRegistry

registry = ResourceRegistry(default_prefix="lucide")
content = registry.get_resource("activity")

# Access as text (SVG markup)
svg_markup = content.text

# Access as bytes
svg_bytes = content.data

# Content type is always "image/svg+xml"
assert content.content_type == "image/svg+xml"
assert content.encoding == "utf-8"
```

## Icon Names

Icons use kebab-case naming (e.g., `a-arrow-down`, `alarm-clock-check`, `lightbulb`). 
You can browse all available icons at [lucide.dev/icons](https://lucide.dev/icons).

## Upstream Sources

This package is a resource pack adapter that provides access to icons from:

- **[JustMyResource](https://github.com/kws/justmyresource)**: Resource discovery and resolution library
- **Lucide Icons**: [https://lucide.dev/](https://lucide.dev/) - 1500+ SVG icons (ISC License)
- **lucide Python Package**: [https://github.com/franciscobmacedo/lucide](https://github.com/franciscobmacedo/lucide) - Django/Jinja template integration (MIT License)

See [NOTICE](NOTICE) for full license and attribution information.

## License

This adapter package is licensed under the MIT License. See [LICENSE](LICENSE) for details.

The Lucide icons themselves are licensed under the ISC License, with portions derived from Feather Icons (MIT License). See [NOTICE](NOTICE) for complete attribution.

