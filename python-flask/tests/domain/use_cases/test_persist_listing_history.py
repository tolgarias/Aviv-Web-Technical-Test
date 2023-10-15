import pytest
from freezegun import freeze_time

from listingapi.domain import entities, use_cases
from tests import factories


class TestPersistListingHistory:
    @pytest.fixture
    def listing_history_entity(self) -> entities.ListingHistoryEntity:
        listing_history_entity = (
            factories.entities.ListingHistory()
            .with_listing_id(1)
            .with_price(720000)
            .with_created_date("2023-10-15 15:30:05.300900")
            .build()
        )

        return listing_history_entity

    @freeze_time("2023-10-15 15:30:05.300900")
    def test_persist_listing_history(
        self,
        persist_listing_use_case: use_cases.PersistListing,
        listing_history_entity: entities.ListingHistoryEntity,
    ) -> None:
        persisted_listing_history_dict = persist_listing_use_case.listing_repository.create_listing_history(
            listing_history_entity
        )

        assert persisted_listing_history_dict["id"] == 1
        assert persisted_listing_history_dict["listing_id"] == 1
        assert persisted_listing_history_dict["latest_price_eur"] == 720000.0
        assert persisted_listing_history_dict["created_date"] == "2023-10-15T15:30:05.300900"
