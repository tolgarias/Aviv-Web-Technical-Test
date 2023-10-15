import datetime
from pydantic import BaseModel


class ListingHistoryEntity(BaseModel):
    listing_id: int
    latest_price_eur: float
    created_date: datetime.datetime
