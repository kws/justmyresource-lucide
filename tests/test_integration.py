"""Integration tests for LucideResourcePack with ResourceRegistry."""

from __future__ import annotations


from justmyresource import ResourceRegistry


def test_discovery() -> None:
    """Test that the pack is discoverable via ResourceRegistry."""
    registry = ResourceRegistry()

    # Should discover the lucide pack
    packs = list(registry.list_packs())

    # Should contain justmyresource-lucide/lucide
    lucide_pack = "justmyresource-lucide/lucide"
    assert lucide_pack in packs


def test_get_resource_with_prefix() -> None:
    """Test getting resource with lucide: prefix."""
    registry = ResourceRegistry()

    content = registry.get_resource("lucide:lightbulb")

    assert content.content_type == "image/svg+xml"
    assert content.encoding == "utf-8"
    assert content.data.startswith(b"<svg")


def test_get_resource_with_alias() -> None:
    """Test getting resource with luc: alias."""
    registry = ResourceRegistry()

    content = registry.get_resource("luc:lightbulb")

    assert content.content_type == "image/svg+xml"
    assert content.data.startswith(b"<svg")


def test_get_resource_with_qualified_name() -> None:
    """Test getting resource with fully qualified name."""
    registry = ResourceRegistry()

    content = registry.get_resource("justmyresource-lucide/lucide:lightbulb")

    assert content.content_type == "image/svg+xml"
    assert content.data.startswith(b"<svg")


def test_get_resource_with_default_prefix() -> None:
    """Test getting resource with default_prefix set."""
    registry = ResourceRegistry(default_prefix="lucide")

    # Bare name should resolve to lucide:lightbulb
    content = registry.get_resource("lightbulb")

    assert content.content_type == "image/svg+xml"
    assert content.data.startswith(b"<svg")


def test_list_resources_from_pack() -> None:
    """Test listing resources from the lucide pack."""
    registry = ResourceRegistry()

    resources = list(registry.list_resources(pack="lucide"))

    # Should have many icons
    assert len(resources) > 1500

    # Should contain known icons
    icon_names = [r.name for r in resources]
    assert "lightbulb" in icon_names
    assert "a-arrow-down" in icon_names

    # All should have correct pack
    assert all(r.pack == "justmyresource-lucide/lucide" for r in resources)

    # All should have correct content type
    assert all(r.content_type == "image/svg+xml" for r in resources)


def test_list_resources_all_packs() -> None:
    """Test listing resources from all packs."""
    registry = ResourceRegistry()

    resources = list(registry.list_resources())

    # Should include lucide icons
    lucide_resources = [
        r for r in resources if r.pack == "justmyresource-lucide/lucide"
    ]
    assert len(lucide_resources) > 1500


def test_prefix_map() -> None:
    """Test that prefix mappings work correctly."""
    registry = ResourceRegistry()

    prefix_map = registry.get_prefix_map()

    # Should contain lucide prefix
    assert "lucide" in prefix_map
    assert prefix_map["lucide"] == "justmyresource-lucide/lucide"

    # Should contain luc alias
    assert "luc" in prefix_map
    assert prefix_map["luc"] == "justmyresource-lucide/lucide"

    # Should contain qualified name
    assert "justmyresource-lucide/lucide" in prefix_map
