# Release checklist

Current preparation does not publish anything. Proposed repository: `TheDarkniteFalls/building-with-codex`. Proposed site: `https://thedarknitefalls.github.io/building-with-codex/`.

## Local acceptance

- [ ] Accept independent content, source, privacy, scope, accessibility, and rendered usability review of the exact candidate.
- [ ] Verify README and website agreement, public source links, internal anchors, and website assets.
- [ ] Record mobile, tablet, desktop, keyboard, and console checks.
- [ ] Pass the publication lane check for this exact nested repository; resolve findings before release.
- [ ] Recheck current public PR status and destination links if the candidate has changed or evidence is stale.

## Separately authorized site release

- [ ] Obtain explicit authorization for the exact commit and each proposed external action.
- [ ] Create the intended GitHub repository only when authorized; verify exact owner, repository, and visibility.
- [ ] Commit only reviewed files. Run the lane pre-push gate after the authorized commit and before an authorized push.
- [ ] Configure GitHub Pages to use GitHub Actions only when authorized.
- [ ] Verify the reviewed workflow and source revision. Its sole trigger is manual dispatch and its sole uploaded directory is `site/`.
- [ ] Dispatch deployment only when separately authorized. Do not upload README, release notes, repository metadata, or local evidence as website assets.
- [ ] Verify the live site, its links, mobile layout, keyboard navigation, and console after deployment.

## Profile publication gate

**HOLD PROFILE PUBLICATION until Building with Codex is live and verified.** The proposed site returned HTTP 404 when checked on 13 September 2026.

Release order: separately authorize and release the site; verify it live; then separately authorize profile publication. A prepared profile link is not proof that its destination works. Actual GitHub pin changes also require separate authorization.

No publication, deployment, profile update, or pin change is performed by completing this checklist locally.
