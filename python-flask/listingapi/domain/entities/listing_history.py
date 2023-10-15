from pydantic import BaseModel


class ListingHistoryEntity(BaseModel):
    latest_price_eur: float
