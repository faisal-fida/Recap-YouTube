import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class SummaryItem:
    id: uuid.UUID
    value: str


class DBHandler:
    summary_items: List[SummaryItem]

    def __init__(self):
        self.summary_items = [
            SummaryItem(
                id=uuid.uuid4(),
                value="YT Summary 1",
            ),
            SummaryItem(
                id=uuid.uuid4(),
                value="YT Summary 2",
            ),
        ]

    def get_todo_items(self):
        return self.summary_items

    def add_todo_item(self, value: str):
        self.summary_items.insert(
            0,
            SummaryItem(
                id=uuid.uuid4(),
                value=value,
            ),
        )

    def clear_todo_items(self):
        self.summary_items = []

    def remove_todo_item(self, item_id: str):
        self.summary_items = [
            item for item in self.summary_items if not str(item.id) == item_id
        ]


db_handler = DBHandler()
