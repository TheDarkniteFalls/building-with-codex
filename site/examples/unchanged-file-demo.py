"""Pedagogical coverage example; not a security scanner. Python 3, no dependencies."""

snapshot = {"edited.txt": "REVIEW_MARKER_A", "unchanged.txt": "REVIEW_MARKER_B"}
changed_paths = {"edited.txt"}
reviewed = {("edited.txt", "REVIEW_MARKER_A"), ("unchanged.txt", "REVIEW_MARKER_B")}


def observed(paths):
    return {(path, marker) for path, marker in reviewed
            if path in paths and marker in snapshot[path]}


changed_only = observed(changed_paths)
full_snapshot = observed(snapshot)
assert changed_only == {("edited.txt", "REVIEW_MARKER_A")}
assert full_snapshot == reviewed
print(f"changed-only: {len(changed_only)} of {len(reviewed)} reviewed markers found")
print(f"full snapshot: {len(full_snapshot)} of {len(reviewed)} reviewed markers found")
