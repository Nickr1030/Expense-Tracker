from typing import List, Optional
from decimal import Decimal
from tracker.models import Expense, User, SplitAllocation
from tracker.storage import StorageInterface


class ExpenseService:
    """Core service orchestrating expense operations and business rules."""

    def __init__(self, storage: StorageInterface) -> None:
        self.storage = storage

    def record_expense(self, expense: Expense) -> None:
        """Record a single expense after validating the payer exists."""
        payer = self.storage.get_user(expense.paid_by)
        if payer is None:
            raise ValueError(f"User {expense.paid_by} does not exist.")
        self.storage.save_expense(expense)

    def split_expense(
        self,
        original_expense_id: str,
        target_user_ids: List[str],
        percentages: Optional[List[float]] = None,
    ) -> List[Expense]:
        """TODO: Implement splitting logic.
        
        Requirements:
        1. Original expense must exist in storage.
        2. All target users must exist in storage.
        3. Splitting must conserve exact currency values (no fractional cent loss).
        4. Record all individual split expenses back to storage.
        """
        raise NotImplementedError("To be implemented via AI assistant prompt.")
