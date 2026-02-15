"""Tests for LucideResourcePack."""

from __future__ import annotations

import pytest

from justmyresource_lucide.pack import LucideResourcePack


def test_get_resource_existing_icon() -> None:
    """Test getting an existing icon."""
    pack = LucideResourcePack()

    # Test with a known icon
    content = pack.get_resource("a-arrow-down")

    assert content.content_type == "image/svg+xml"
    assert content.encoding == "utf-8"
    assert content.data.startswith(b"<svg")

    # Verify it's valid SVG text
    svg_text = content.text
    assert svg_text.startswith("<svg")
    assert "xmlns" in svg_text or "viewBox" in svg_text


def test_get_resource_without_extension() -> None:
    """Test getting resource works with or without .svg extension."""
    pack = LucideResourcePack()

    content1 = pack.get_resource("a-arrow-down")
    content2 = pack.get_resource("a-arrow-down.svg")

    assert content1.data == content2.data


def test_get_resource_nonexistent_icon() -> None:
    """Test getting a non-existent icon raises ValueError."""
    pack = LucideResourcePack()

    with pytest.raises(ValueError, match="Icon 'nonexistent-icon' not found"):
        pack.get_resource("nonexistent-icon")


def test_list_resources() -> None:
    """Test listing all resources."""
    pack = LucideResourcePack()

    resources = list(pack.list_resources())

    # Should have approximately 1535 icons
    assert len(resources) > 1500
    assert len(resources) < 1600

    # Should be sorted
    assert resources == sorted(resources)

    # Should contain known icons
    assert "a-arrow-down" in resources
    assert "alarm-clock-check" in resources
    assert "lightbulb" in resources

    # Should not contain .svg extensions
    assert all("." not in name for name in resources)


def test_get_prefixes() -> None:
    """Test getting prefix aliases."""
    pack = LucideResourcePack()

    prefixes = pack.get_prefixes()

    assert prefixes == ["luc"]


def test_resource_content_structure() -> None:
    """Test that ResourceContent has correct structure."""
    pack = LucideResourcePack()

    content = pack.get_resource("activity")

    # Verify ResourceContent structure
    assert hasattr(content, "data")
    assert hasattr(content, "content_type")
    assert hasattr(content, "encoding")
    assert hasattr(content, "text")

    # Verify data is bytes
    assert isinstance(content.data, bytes)

    # Verify text property works
    text = content.text
    assert isinstance(text, str)
    assert len(text) > 0
