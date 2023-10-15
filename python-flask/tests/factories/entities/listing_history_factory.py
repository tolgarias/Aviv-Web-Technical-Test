import datetime

from faker import Faker

from listingapi.domain import entities
from tests import factories


class ListingHistory:
    def __init__(self, locale: str = "fr-FR"):
        fake = Faker(locale)
        self.price = float(fake.random_int(100_000, 2_000_000, 5000))

    def with_price(self, price: float) -> "ListingHistory":
        self.price = price
        return self

    def with_created_date(self, created_date: datetime.date) -> "ListingHistory":
        self.created_date = created_date
        return self

    def with_listing_id(self, listing_id: int) -> "ListingHistory":
        self.listing_id = listing_id
        return self

    def build(self) -> entities.ListingHistoryEntity:
        return entities.ListingHistoryEntity(
            listing_id=self.listing_id,
            latest_price_eur=self.price,
            created_date=self.created_date,
        )
