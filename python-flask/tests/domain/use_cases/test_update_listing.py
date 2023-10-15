from freezegun import freeze_time

from listingapi.domain import use_cases
from tests import factories


class TestUpdateListing:
    @freeze_time("2023-01-18 08:50:03.761691")
    def test_update_listing(
        self,
        persist_listing_use_case: use_cases.PersistListing,
        update_listing_use_case: use_cases.UpdateListing,
    ) -> None:
        listing_entity = (
            factories.entities.Listing().with_name("Mikhail Schmiedt").build()
        )
        persisted_listing = persist_listing_use_case.listing_repository.create(
            listing_entity
        )

        listing_entity.name = "My new name"
        with freeze_time("2023-01-19 08:50:03.761691"):
            updated_listing = update_listing_use_case.perform(
                persisted_listing["id"], listing_entity
            )

        assert updated_listing["name"] == "My new name"
        assert updated_listing["created_date"] == "2023-01-18T08:50:03.761691"
        assert updated_listing["updated_date"] == "2023-01-19T08:50:03.761691"

        persisted_listing_history = persist_listing_use_case.listing_repository.get_listing_history(1)
        assert len(persisted_listing_history) == 2
        assert persisted_listing_history[0]["listing_id"] == 1
        assert persisted_listing_history[0]["id"] == 1
        assert persisted_listing_history[0]["created_date"] == "2023-01-18T08:50:03.761691"

        assert persisted_listing_history[1]["listing_id"] == 1
        assert persisted_listing_history[1]["id"] == 2
        assert persisted_listing_history[1]["created_date"] == "2023-01-19T08:50:03.761691"

