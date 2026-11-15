"""Pure, deny-by-default review gate; never performs side effects."""
from dataclasses import dataclass
from typing import Tuple

BLOCKED = frozenset({'merge', 'deploy', 'live_trade', 'read_secret', 'paid_api', 'main_write'})

@dataclass(frozen=True)
class ReviewRequest:
    action: str
    explicitly_approved: bool = False
    tests_passed: bool = False
    license_reviewed: bool = False
    security_reviewed: bool = False

@dataclass(frozen=True)
class ReviewDecision:
    allowed: bool
    reasons: Tuple[str, ...]

def evaluate(request: ReviewRequest) -> ReviewDecision:
    """Gate only; even an allow decision never invokes the requested action."""
    if not isinstance(request, ReviewRequest):
        raise TypeError('ReviewRequest required')
    reasons = []
    if request.action not in {'draft_pr', 'feature_commit', *BLOCKED}:
        reasons.append('unknown_action')
    if request.action in BLOCKED:
        reasons.append('restricted_action_manual_only')
    if not request.explicitly_approved:
        reasons.append('missing_explicit_approval')
    if not request.tests_passed:
        reasons.append('tests_not_passed')
    if not request.license_reviewed:
        reasons.append('license_not_reviewed')
    if not request.security_reviewed:
        reasons.append('security_not_reviewed')
    return ReviewDecision(not reasons, tuple(reasons))
