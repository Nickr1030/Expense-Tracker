from typing import Dict, Any, Optional
from tracker.storage import StorageInterface
from tracker.models import Category


class ReportService:
    """Generates summaries and spending metrics."""

    def __init__(self, storage: StorageInterface) -> None:
        self.storage = storage

    def generate_monthly_report(self, year: int, month: int) -> Dict[str, Any]:
        """TODO: Implement monthly breakdown.
        
        Requirements:
        1. Calculate total spending for the given year and month.
        2. Breakdown total by Category.
        3. Identify the highest spending Category.
        4. Return a structured summary dictionary or model.
        """
        raise NotImplementedError("To be implemented via AI assistant prompt.")
