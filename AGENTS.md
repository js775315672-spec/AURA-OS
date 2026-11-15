# Codex agent instructions

## Scope
Work only on an isolated feature branch. Do not modify main directly. Prefer small, reviewable changes with tests and a Draft Pull Request.

## Autonomous loop
1. Inspect repository and open issues; propose a scoped change.
2. Research upstream projects, verify licenses and provenance. Never copy incompatible code.
3. Implement one bounded improvement.
4. Run tests, lint, security checks, and record commands and outputs.
5. Open a Draft PR with evidence, limitations, and next steps. Never merge automatically.

## Hard approval gates
Never execute live trading orders, enable live trading, access or expose secrets, deploy, merge PRs, or change branch protection without explicit user approval. Never place credentials, private datasets, or account data in this public repository.
Do not claim tests or backtests passed unless actually executed. On missing runtime/data, report BLOCKED.

## AURA OS
Build an auditable agent orchestrator with checkpointing, bounded retries, permission gates, and rollback. Keep execution logs and reproducible tests. Integrate GitHub open source only after license, dependency and security review.
