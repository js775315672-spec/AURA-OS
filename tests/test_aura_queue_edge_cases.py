import unittest
from aura_queue import Task, select_next

class QueueEdgeCases(unittest.TestCase):
    def test_empty_queue(self):
        self.assertIsNone(select_next([]))

    def test_unapproved_high_priority_cannot_preempt(self):
        tasks = [Task("unapproved", 1000), Task("approved", 1, approved=True)]
        self.assertEqual(select_next(tasks).task_id, "approved")

    def test_input_order_does_not_change_selection(self):
        tasks = [Task("b", 5, True), Task("a", 5, True)]
        self.assertEqual(select_next(tasks).task_id, select_next(reversed(tasks)).task_id)

    def test_task_records_are_immutable(self):
        from dataclasses import FrozenInstanceError
        task = Task("safe", 1, True)
        with self.assertRaises(FrozenInstanceError):
            task.approved = False
