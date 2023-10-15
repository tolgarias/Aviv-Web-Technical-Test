from datetime import datetime

from sqlalchemy.orm import scoped_session

from listingapi.adapters.sql_alchemy_listing_repository import mappers, models
from listingapi.domain import entities, ports
from listingapi.domain.entities import exceptions


class SqlAlchemyListingRepository(ports.ListingRepository):
    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        models.Base.metadata.create_all(self.db_session.get_bind())

    def create(self, listing: entities.ListingEntity) -> dict:
        listing_model = mappers.ListingMapper.from_entity_to_model(listing)
        listing_history_model = models.ListingHistoryModel(
            price=listing.latest_price_eur,
        )
        listing_model.listing_history.append(listing_history_model)
        self.db_session.add(listing_model)
        self.db_session.commit()
        data = mappers.ListingMapper.from_model_to_dict(listing_model)
        return data

    def get_all(self) -> list:
        listing_models = self.db_session.query(models.ListingModel).all()
        listings = [
            mappers.ListingMapper.from_model_to_dict(listing)
            for listing in listing_models
        ]
        return listings

    def update(self, listing_id: int, listing: entities.ListingEntity) -> dict:
        existing_listing = self.db_session.get(models.ListingModel, listing_id)
        created_at = existing_listing.created_date
        if existing_listing is None:
            raise exceptions.ListingNotFound

        # removed to keep history
        # self.db_session.delete(existing_listing)

        existing_listing = mappers.ListingMapper.from_entity_to_model(listing)
        existing_listing.created_date = created_at
        existing_listing.updated_date = datetime.utcnow()
        listing_history_model = models.ListingHistoryModel(
            price=listing.latest_price_eur,
            listing_id=listing_id
        )
        self.db_session.add(listing_history_model)
        self.db_session.commit()
        listing_dict = mappers.ListingMapper.from_model_to_dict(existing_listing)
        return listing_dict

    def get_listing_history(self, listing_id: int) -> list:
        listing_history_models = self.db_session.query(models.ListingHistoryModel).filter_by(
            listing_id=listing_id).all()
        listing_histories = [
            mappers.ListingHistoryMapper.from_model_to_dict(listing_history)
            for listing_history in listing_history_models
        ]
        return listing_histories
