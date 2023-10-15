import pytest
from freezegun import freeze_time

from listingapi.domain import entities, use_cases
from tests import factories


class TestPersistListing:
    @pytest.fixture
    def listing_entity(self) -> entities.ListingEntity:
        listing_entity = (
            factories.entities.Listing()
            .with_name("Mikhail Schmiedt")
            .with_description("description")
            .with_building_type("APARTMENT")
            .with_rooms_count(6)
            .with_bedrooms_count(2)
            .with_surface_area_m2(167)
            .with_postal_address(
                factories.entities.PostalAddress()
                .with_street_address("Johan-Ernst-Ring 7")
                .with_postal_code("21810")
                .with_city("Berchtesgaden")
                .with_country("DE")
                .build()
            )
            .with_price(720000)
            .with_contact_phone_number("")
            .build()
        )

        return listing_entity

    @freeze_time("2023-01-18 08:50:03.761691")
    def test_persist_listing(
        self,
        persist_listing_use_case: use_cases.PersistListing,
        retrieve_listing_history_use_case: use_cases.RetrieveListingHistory,
        listing_entity: entities.ListingEntity,
    ) -> None:
        persisted_listing_dict = persist_listing_use_case.listing_repository.create(
            listing_entity
        )

        assert persisted_listing_dict["id"] == 1
        assert persisted_listing_dict["name"] == "Mikhail Schmiedt"
        assert persisted_listing_dict["postal_address"] == {
            "street_address": "Johan-Ernst-Ring 7",
            "postal_code": "21810",
            "city": "Berchtesgaden",
            "country": "DE",
        }
        assert persisted_listing_dict["description"] == "description"
        assert persisted_listing_dict["building_type"] == "APARTMENT"
        assert persisted_listing_dict["latest_price_eur"] == 720000.0
        assert persisted_listing_dict["surface_area_m2"] == 167
        assert persisted_listing_dict["rooms_count"] == 6
        assert persisted_listing_dict["bedrooms_count"] == 2
        assert persisted_listing_dict["contact_phone_number"] == ""
        assert persisted_listing_dict["created_date"] == "2023-01-18T08:50:03.761691"
        assert persisted_listing_dict["updated_date"] == "2023-01-18T08:50:03.761691"

        persisted_listing_history = persist_listing_use_case.listing_repository.get_listing_history(1)
        assert persisted_listing_history[0]["listing_id"] == 1
        assert persisted_listing_history[0]["id"] == 1
        assert len(persisted_listing_history) == 1
