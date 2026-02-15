"""JustMyResource pack for Lucide icons."""

from justmyresource_lucide.pack import LucideResourcePack

__all__ = ["get_resource_provider", "LucideResourcePack"]


def get_resource_provider():
    """Entry point factory for JustMyResource.

    Returns:
        LucideResourcePack instance.
    """
    return LucideResourcePack()
