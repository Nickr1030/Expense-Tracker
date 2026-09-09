# Post-Mortem: The Naive Prompting Experiment

Answer the following questions based on the changes your AI assistant made:

1. **Precision & Types:** Did the AI use `float`, `int` (cents), or `Decimal` for split amounts and totals? What happens if you split $100.00 among 3 people?
2. **Architectural Drift:** Did the AI call methods on `StorageInterface`, or did it read/write files directly inside `service.py` or `reports.py`?
3. **Contracts & Validation:** Did the CSV importer construct validated `Expense` models, or did it pass raw untyped dictionaries around?
4. **Code Quality:** What errors did `ruff` and `mypy` flag after the AI generated the code?
5. **System Instructions:** Write 3 concrete repository rules (e.g., for `.cursorrules`) that would have prevented these specific errors.
