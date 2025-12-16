import pytest
from app.provider import (
    get_providers,
    get_provider_profile,
    search_providers_by_location
)


def test_get_providers_returns_list():
    providers = get_providers()
    assert isinstance(providers, list)
    assert len(providers) >= 1

def test_provider_structure():
    provider = get_providers()[0]
    assert "id" in provider
    assert "name" in provider
    assert "service" in provider
    assert "location" in provider


def test_get_provider_profile_found():
    provider = get_provider_profile(1)
    assert provider is not None
    assert provider["id"] == 1

def test_get_provider_profile_not_found():
    assert get_provider_profile(999) is None

def test_get_provider_profile_invalid_type():
    with pytest.raises(TypeError):
        get_provider_profile("1")


def test_search_providers_by_location_found():
    results = search_providers_by_location("Ulaanbaatar")
    assert len(results) >= 1

def test_search_providers_by_location_case_insensitive():
    results = search_providers_by_location("ulaanbaatar")
    assert len(results) >= 1

def test_search_providers_by_location_empty_string():
    results = search_providers_by_location("")
    assert results == []

def test_search_providers_by_location_none():
    with pytest.raises(ValueError):
        search_providers_by_location(None)