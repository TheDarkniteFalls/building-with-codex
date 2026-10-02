# Case studies: release preparation receipt

Date: 2 October 2026. Preparation status: author checks passed; independent local review and Lead acceptance completed. Release is authorized subject to the remaining checks. At this preparation snapshot, the case studies have not been published. This document records preparation, not completed publication.

## Candidate

Baseline: `d7269995c7aaa20c050e1c46e9796916e2260660`.

Changed files: `README.md`, `site/index.html`, `site/styles.css`.
Added files: `CASE_STUDIES_PLAN.md`, this receipt, three pages under `site/cases/` (`validation-repair.html`, `bazel-evidence.html`, `inspect-ai.html`), and `site/examples/unchanged-file-demo.py`.

The existing hero, artwork, starting routes and manual site-only deployment workflow remain unchanged. No dependencies were added. At this preparation snapshot, no staging, commit, push, pull request or deployment has been performed for these case studies. Profile changes remain outside this release.

## Checks performed

- Four HTML pages: 48 local links, assets and fragments resolved; IDs were unique. `git diff --check` passed.
- Executed `python3 site/examples/unchanged-file-demo.py`: assertions passed; changed-only coverage found 1 of 2 reviewed markers and the full snapshot found 2 of 2. This is the newly authored toy illustration, not a rerun of the historical local validation.
- Inspected the pinned public Bazel requests, event files and expected receipts. The truncated file is the first three events of the four-event complete file. Whole-source hashes match the expected receipt evidence; documented findings and retained non-authorization fields agree. The upstream adapter and its test suite were not run.
- Checked public Inspect issue, PR and review records against the article, including the merge identity and the author's reported 9,965 passes, 4,347 skips, 2 failures and 1,087 warnings. No Inspect, S3, cloud or model execution was performed.
- Target-only publication-lane preparation check passed: no obvious safety findings and no symlinks. This preparation check is not a pre-push or publication approval.
- Rendered QA passed in installed Chrome through existing Playwright 1.62.1 at 1440 × 1000 and 390 × 844. Browser plugin not available in this session; no browser or dependency was installed. The initial bundled-browser revision was absent; the installed Chrome channel required the supported permission route after a managed launch failed.
- Each page had the expected title and meaningful content, no error overlay, no horizontal document overflow, and no observed console warnings or errors. Keyboard skip navigation reached main content with a visible focus outline. Desktop and mobile screenshots were inspected.
- Exercised the actual flow at a loopback-only preview: homepage case card → example → evidence → next case → next case → Work delivered. Screenshots and detailed logs are kept outside the public candidate.

## Evidence boundaries

The local repair article is an author-reported historical account. Its 58-test and 8-test milestones are not current site tests; original temporary receipts are unavailable. Its reported independent acceptance is not independent verification of this article.

The Bazel walkthrough uses synthetic public sources pinned to `9c0cb0760a8fb56ebbabc5840b319557de2c9f08`. Expected output inspection is distinct from execution. The Inspect account uses public review and merge evidence with author-reported validation. Neither case supports general productivity, speed, capability or safety conclusions.

Remaining validation limits: no other browsers, assistive-technology session or additional viewport sizes were tested. Existing external start/tool destinations were retained, not comprehensively revalidated. Independent local review verified the exact nine-file candidate, source boundaries, privacy and screenshots, with no actionable findings. Lead acceptance is complete and release is authorized subject to checks. Commit, remote publication and live verification remain outstanding at this preparation snapshot.
