"""Deterministic, side-effect-free agent task selection."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Task:
    task_id: str
    priority: int
    approved: bool = False
    requires_secret: bool = False
    requires_deployment: bool = False

def select_next(tasks):
    """Return highest-priority safe task; never authorize execution."""
    safe = [t for t in tasks if t.approved and not t.requires_secret and not t.requires_deployment]
    return sorted(safe, key=lambda t: (-t.priority, t.task_id))[0] if safe else None
