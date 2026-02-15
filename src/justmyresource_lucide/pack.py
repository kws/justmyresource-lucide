"""Lucide icon resource pack implementation."""

from __future__ import annotations

import zipfile
from collections.abc import Iterator
from contextlib import contextmanager
from importlib.resources import files

from justmyresource.types import ResourceContent


class LucideResourcePack:
    """Resource pack for Lucide icons.

    Provides access to 1500+ SVG icons from the Lucide icon library.
    Icons are loaded from the upstream lucide package's lucide.zip archive.
    """

    def __init__(self) -> None:
        """Initialize the Lucide resource pack."""
        self._icon_names: list[str] | None = None

    @contextmanager
    def _open_zip(self):
        """Open the lucide.zip file from the lucide package.

        Yields:
            ZipFile instance for reading icons.
        """
        # Use importlib.resources to access the zip file from the lucide package
        lucide_package = files("lucide")
        zip_path = lucide_package / "lucide.zip"

        with zipfile.ZipFile(zip_path, "r") as zip_file:
            yield zip_file

    def _get_icon_names(self) -> list[str]:
        """Get cached list of all icon names.

        Returns:
            List of icon names (without .svg extension).
        """
        if self._icon_names is None:
            with self._open_zip() as zip_file:
                # Extract icon names from zip file list
                # Icons are stored as "icon-name.svg"
                self._icon_names = sorted(
                    name[:-4]  # Remove .svg extension
                    for name in zip_file.namelist()
                    if name.endswith(".svg")
                )
        return self._icon_names

    def get_resource(self, name: str) -> ResourceContent:
        """Get resource content for an icon name.

        Args:
            name: Icon name (e.g., "a-arrow-down", "alarm-clock-check").

        Returns:
            ResourceContent object containing the SVG data.

        Raises:
            ValueError: If the icon cannot be found.
        """
        # Ensure name doesn't have .svg extension
        if name.endswith(".svg"):
            name = name[:-4]

        icon_filename = f"{name}.svg"

        try:
            with self._open_zip() as zip_file:
                svg_bytes = zip_file.read(icon_filename)
        except KeyError:
            available = self._get_icon_names()
            # Provide helpful error message with suggestions
            suggestions = [
                n
                for n in available
                if name.lower() in n.lower() or n.lower() in name.lower()
            ][:5]
            suggestion_text = (
                f" Similar names: {', '.join(suggestions)}" if suggestions else ""
            )
            raise ValueError(
                f"Icon '{name}' not found in Lucide pack.{suggestion_text}"
            ) from None

        return ResourceContent(
            data=svg_bytes,
            content_type="image/svg+xml",
            encoding="utf-8",
        )

    def list_resources(self) -> Iterator[str]:
        """List all available icon names.

        Yields:
            Icon name strings (without .svg extension).
        """
        yield from self._get_icon_names()

    def get_prefixes(self) -> list[str]:
        """Return list of optional alias prefixes.

        Returns:
            List containing "luc" as a convenience alias.
        """
        return ["luc"]
