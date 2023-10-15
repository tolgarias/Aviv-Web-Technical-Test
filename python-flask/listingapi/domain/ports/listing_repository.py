import abc

from listingapi.domain import entities


class ListingRepository(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def create(self, listing: entities.ListingEntity) -> dict:
        pass

    @abc.abstractmethod
    def get_all(self) -> list:
        pass

    @abc.abstractmethod
    def update(self, id_: int, listing: entities.ListingEntity) -> dict:
        pass

    @abc.abstractmethod
    def get_listing_history(self, listing_id_: int) -> list:
        pass
