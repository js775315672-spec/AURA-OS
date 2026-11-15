import unittest
from aura_queue import Task, select_next

class QueueTests(unittest.TestCase):
    def test_no_approval_no_task(self):
        self.assertIsNone(select_next([Task("a", 100)]))
    def test_secret_and_deploy_blocked(self):
        self.assertIsNone(select_next([Task("a", 10, True, True), Task("b", 9, True, False, True)]))
    def test_priority_then_stable_id(self):
        tasks = [Task("z", 2, True), Task("a", 2, True), Task("low", 1, True)]
        self.assertEqual(select_next(tasks).task_id, "a")
if __name__ == "__main__":
    unittest.main()
