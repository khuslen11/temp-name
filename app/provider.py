from typing import List, Dict, Optional

# In-memory provider data (mock)
_PROVIDERS: List[Dict] = [
    {
        "id": 1,
        "name": "Plumber One",
        "service": "Plumbing",
        "location": "Ulaanbaatar",
    },
    {
        "id": 2,
        "name": "Electrician Pro",
        "service": "Electrical",
        "location": "Ulaanbaatar",
    },
    {
        "id": 3,
        "name": "FixIt",
        "service": "Repair",
        "location": "Darkhan",
    },
]


def get_providers() -> List[Dict]:
    """
    US-03: Return all available service providers.
    """
    return list(_PROVIDERS)


def get_provider_profile(provider_id: int) -> Optional[Dict]:
    """
    US-04: Return a single provider profile by ID.
    """
    if not isinstance(provider_id, int):
        raise TypeError("provider_id must be an integer")

    for provider in _PROVIDERS:
        if provider["id"] == provider_id:
            return provider
    return None


def search_providers_by_location(location: str) -> List[Dict]:
    """
    US-12: Search providers by location.
    """
    if location is None:
        raise ValueError("location must not be None")
    if not isinstance(location, str):
        raise TypeError("location must be a string")

    location = location.strip().lower()
    if not location:
        return []

    return [
        p for p in _PROVIDERS
        if p["location"].lower() == location
    ]
