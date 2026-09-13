# Building with Codex

Practical ways to complete substantial useful work with Codex—from a clear brief to a checked result.

Define the work. Build and check. Review the result.

## Work delivered

Mike Parsons ([@TheDarkniteFalls](https://github.com/TheDarkniteFalls)) contributed [Inspect AI PR #4713](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4713), “Return ETags from write_eval_log.”

- **Problem:** [Issue #4699](https://github.com/UKGovernmentBEIS/inspect_ai/issues/4699) requested the ETag from an S3 log write so callers could chain conditional writes.
- **Implementation:** `WriteEvalLogResult` returns the S3 write ETag from `write_eval_log`, or `None` for non-S3 writes.
- **Review and repairs:** maintainer @ransomr requested changes. Repairs covered ETag capture, tracing, missing-file behavior, documentation, and the [Trio S3 read path](https://github.com/UKGovernmentBEIS/inspect_ai/commit/41d1eea0a1250882f185164006537cf470f81890). See the [repair summary](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4713#issuecomment-5423644553).
- **Accepted outcome:** @ransomr [approved the repaired PR](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4713#pullrequestreview-5043840043), which was [merged on 27 August 2026](https://github.com/UKGovernmentBEIS/inspect_ai/commit/e789de9a2a38961ce4d8051d04f62a5bc8f66c46).

**AI assistance:** OpenAI Codex assisted implementation, review, and validation. The public PR says the final diff and results were reviewed before publication. Maintainer review comments also disclose AI generation with maintainer review before posting.

**Limits:** this public record shows one specific contribution and its repair cycle. It does not establish speed, productivity, or general capability. A measured case study is a future possibility, not a result reported here. Public status and selected routes were checked on 13 September 2026.

## Start building

Learn the method. Then make it concrete.

1. [Agent Operator Handbook](https://github.com/TheDarkniteFalls/agent-operator-handbook): learn to set scope, choose sources, and review AI-assisted work.
2. [Reliable AI Work Starter](https://github.com/TheDarkniteFalls/reliable-ai-work-starter): apply the method to one recurring workflow in your own workspace.

## Improve your method

Choose a tool for the problem in front of you.

| Need | Tool |
| --- | --- |
| Make scope and working expectations explicit | [Codex Project Instructions Starter](https://github.com/TheDarkniteFalls/codex-project-instructions-starter) |
| Select context with explicit obligations and a checkable receipt | [Context Contract Compiler](https://github.com/TheDarkniteFalls/context-contract-compiler) |
| Check that an important workflow still works | [Green-Spine QA Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern) |
| Bind evidence receipts to a specific revision | [EvidenceGate](https://github.com/TheDarkniteFalls/evidencegate) |

[Explore Reliability Lab](https://github.com/TheDarkniteFalls/local-assistant-reliability-lab), the wider supporting collection of guides, tools, and patterns.

Building with Codex is independent of [Detecting AI Deception](https://thedarknitefalls.github.io/detecting-ai-deception/), which helps people examine bounded AI claims against observable evidence. Neither direction is an umbrella for the other.

## Website and local preview

The website is plain HTML and CSS in `site/`. It has no JavaScript, backend, accounts, analytics, build step, or package dependencies.

From the repository root:

```sh
python3 -m http.server --bind localhost --directory site 8817
```

Open `http://localhost:8817/`. Stop the server with Ctrl-C.

## Published website

[Visit Building with Codex](https://thedarknitefalls.github.io/building-with-codex/) or [browse the public repository](https://github.com/TheDarkniteFalls/building-with-codex). The initial release was published and verified on 13 September 2026.

The manual `workflow_dispatch` Pages workflow uploads **only `site/`**. It has no push or pull-request trigger. Future commits, pushes, repository settings changes, and deployments require explicit authorization and the applicable checks. See [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) for the initial release record and future release guidance.

By Mike Parsons. Built with AI assistance. This is an independent project, not an official OpenAI site.
