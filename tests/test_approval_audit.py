import unittest
from approval_audit import ReviewRequest, evaluate, BLOCKED

class ReviewGateTests(unittest.TestCase):
    def test_deny_by_default(self):
        self.assertFalse(evaluate(ReviewRequest('feature_commit')).allowed)

    def test_all_restricted_actions_remain_blocked_even_with_checks(self):
        for action in BLOCKED:
            with self.subTest(action=action):
                result = evaluate(ReviewRequest(action, True, True, True, True))
                self.assertFalse(result.allowed)
                self.assertIn('restricted_action_manual_only', result.reasons)

    def test_reviewed_draft_is_allowed(self):
        self.assertTrue(evaluate(ReviewRequest('draft_pr', True, True, True, True)).allowed)

    def test_unknown_action_denied(self):
        self.assertFalse(evaluate(ReviewRequest('delete_repository', True, True, True, True)).allowed)

    def test_each_gate_required(self):
        for field in ('explicitly_approved','tests_passed','license_reviewed','security_reviewed'):
            values = dict(explicitly_approved=True, tests_passed=True, license_reviewed=True, security_reviewed=True)
            values[field] = False
            with self.subTest(field=field):
                self.assertFalse(evaluate(ReviewRequest('draft_pr', **values)).allowed)
