# Building with Codex

Practical ways to complete substantial useful work with Codex—from a clear brief to a checked result.

Define the work. Build and check. Review the result.

## Work delivered

Three linked case studies put concrete examples before evidence details:

1. [Repair the check, preserve the boundary](site/cases/validation-repair.html): an author-reported local validation repair, with a separate [runnable synthetic coverage example](site/examples/unchanged-file-demo.py).
2. [When a successful target is not enough](site/cases/bazel-evidence.html): complete and truncated public synthetic Bazel BEP records, pinned to an exact adapter revision.
3. [Follow a contribution through review](site/cases/inspect-ai.html): [Inspect AI PR #4713](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4713), including maintainer feedback, a Trio repair and the accepted merge.

[Open the website overview](https://thedarknitefalls.github.io/building-with-codex/#work). The three case pages share example, evidence and previous/home/next navigation. Repository HTML links show source on GitHub; use the local preview below to read the pages as a website.

The local repair is an author-reported account, not publicly reproducible historical evidence. The Bazel walkthrough uses public synthetic sources. The Inspect case uses public issue, review and merge records; reported tests were not rerun for the article. AI assistance and the limits of each claim are stated in the articles. None establishes speed, productivity or general capability.

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

The website is plain HTML and CSS in `site/`. It has no JavaScript, backend, accounts, analytics, build step, or package dependencies. The optional downloadable Python example uses only the standard library; it is not executed by the site.

From the repository root:

```sh
python3 -m http.server --bind localhost --directory site 8817
```

Open `http://localhost:8817/`. Stop the server with Ctrl-C.

## Published website

[Visit Building with Codex](https://thedarknitefalls.github.io/building-with-codex/) or [browse the public repository](https://github.com/TheDarkniteFalls/building-with-codex). The initial release was published and verified on 13 September 2026.

The manual `workflow_dispatch` Pages workflow uploads **only `site/`**. It has no push or pull-request trigger. Future commits, pushes, repository settings changes, and deployments require explicit authorization and the applicable checks. See [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) for the initial release record and future release guidance.

By Mike Parsons. Built with AI assistance. This is an independent project, not an official OpenAI site.
