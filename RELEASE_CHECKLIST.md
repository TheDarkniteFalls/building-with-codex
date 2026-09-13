# Release checklist

## Initial release — 13 September 2026

[Building with Codex](https://thedarknitefalls.github.io/building-with-codex/) is live from the [public repository](https://github.com/TheDarkniteFalls/building-with-codex).

- [x] Independently reviewed content, sources, privacy, scope, accessibility, and rendered usability of the release candidate.
- [x] Verified README and website agreement, public source links, internal anchors, and assets.
- [x] Completed desktop, tablet, mobile, keyboard, and console checks before release.
- [x] Passed the publication lane check and post-commit pre-push checks, including secret scans.
- [x] Obtained explicit authorization for publication and created the intended public repository.
- [x] Published reviewed commit [7960ef3aa8ff24eba2438833103236a7589315b7](https://github.com/TheDarkniteFalls/building-with-codex/commit/7960ef3aa8ff24eba2438833103236a7589315b7) with a normal push.
- [x] Configured Pages to use GitHub Actions and completed manual [deployment run 34732655451](https://github.com/TheDarkniteFalls/building-with-codex/actions/runs/34732655451) successfully for that exact revision.
- [x] Verified live HTML, CSS, and artwork returned HTTP 200 and matched the reviewed files byte-for-byte. Live mobile layout, keyboard navigation, expandable evidence, and console checks passed.
- [x] Published the separately authorized profile update after the site was live and verified: [profile PR #26](https://github.com/TheDarkniteFalls/TheDarkniteFalls/pull/26), merge [19ebff307cc727208f9b1088cb80cce29651d34e](https://github.com/TheDarkniteFalls/TheDarkniteFalls/commit/19ebff307cc727208f9b1088cb80cce29651d34e).
- [x] Verified the public profile's two pins in order: `detecting-ai-deception`, then `building-with-codex`.

## Future changes

- Obtain explicit authorization for the intended commit and each external action. Passing checks does not grant publication authority.
- Review the exact changed files and rerun relevant content, source, privacy, accessibility, and functionality checks. Refresh public evidence when it is stale or affected by changes.
- Run the publication lane check before committing and the pre-push gate after the intended commit, before every push. Resolve findings without weakening the gate.
- Keep the Pages workflow manually triggered and its uploaded directory restricted to `site/`. README, release notes, repository metadata, and local evidence are not website assets.
- Dispatch a deployment only when authorized and needed for website changes. Verify its exact revision and live behavior afterward.
- Verify any new site destination before publishing profile links to it. Profile updates and pin changes require their own explicit authorization.
