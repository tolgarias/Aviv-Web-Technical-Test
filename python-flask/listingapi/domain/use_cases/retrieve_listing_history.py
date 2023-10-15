from listingapi.domain import ports


class RetrieveListingHistory:
    def __init__(self, listing_repository: ports.ListingRepository):
        self.listing_repository = listing_repository

    def perform(self, listing_id: int) -> list:
        listings = self.listing_repository.get_listing_history(listing_id)
        return listings
