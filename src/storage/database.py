from src.log import Logger
from src.storage.base import Session, engine, Base


class Database:

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def add_entry(self, entry):
        self.session.add(entry)
        Logger.log(entry, f"Added")
        self.commit_changes()

    def add_entries(self, entries):
        self.session.add_all(entries)
        Logger.log(type(entries[0]), f"Added {len(entries)} new entries")
        self.commit_changes()

    def commit_changes(self):
        try:
            self.session.commit()
        except:
            self.session.rollback()
            raise
