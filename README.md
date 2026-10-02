# Building with Codex

I use Codex to help build software, check changes and work through review. Here you can follow a contribution to Inspect AI, try a small validation example, or pick a guide for your own project.

[Visit the website](https://thedarknitefalls.github.io/building-with-codex/) to read the cases, or start with the handbook below.

## Work delivered

Start with the Inspect contribution to see how a change developed through review:

1. [Adding S3 ETag support to Inspect AI](https://thedarknitefalls.github.io/building-with-codex/cases/inspect-ai.html): why callers needed the token returned by an S3 write, what review caught, and what was merged.
2. [Why the validation check missed an unchanged file](https://thedarknitefalls.github.io/building-with-codex/cases/validation-repair.html): an author-reported repair, with a separate [runnable synthetic example](site/examples/unchanged-file-demo.py) you can try locally.
3. [Why a successful build target doesn’t prove an output exists](https://thedarknitefalls.github.io/building-with-codex/cases/bazel-evidence.html): compare two synthetic build records and see why missing evidence changes the result.

The Inspect case links public issue, review and merge records. The validation repair is my account of local work; its original receipts are unavailable. The Bazel case uses public synthetic records. Each article explains what its evidence supports. Reported historical tests were not rerun for the articles, and these examples make no claim about speed, productivity or general capability.

## Start building

If you are new to working with an AI coding assistant, start with the handbook. If you already have a recurring task in mind, try the starter.

1. [Agent Operator Handbook](https://github.com/TheDarkniteFalls/agent-operator-handbook): decide what to ask for, what information to provide, and how to check the answer.
2. [Reliable AI Work Starter](https://github.com/TheDarkniteFalls/reliable-ai-work-starter): write down one recurring task and the checks you will use to decide whether it worked.

## Improve your method

Choose a tool for the problem in front of you.

| Need | Tool |
| --- | --- |
| Tell Codex what it may change and how to check its work | [Codex Project Instructions Starter](https://github.com/TheDarkniteFalls/codex-project-instructions-starter) |
| Choose source material and record why it was included | [Context Contract Compiler](https://github.com/TheDarkniteFalls/context-contract-compiler) |
| Check that an important workflow still works | [Green-Spine QA Pattern](https://github.com/TheDarkniteFalls/green-spine-qa-pattern) |
| Record which version of your work the evidence applies to | [EvidenceGate](https://github.com/TheDarkniteFalls/evidencegate) |

[Explore Reliability Lab](https://github.com/TheDarkniteFalls/local-assistant-reliability-lab), the wider supporting collection of guides, tools, and patterns.

To compare a specific agent claim with evidence you provide, try [Agent Claim Check](https://thedarknitefalls.github.io/detecting-ai-deception/). It does not determine intent or gather or authenticate evidence.

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
