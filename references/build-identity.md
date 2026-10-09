# Verify the running build

Use this when interpreting tests against compiled, installed, cached, or remotely served artifacts.

1. Identify the test target: process, URL, package/application ID, device, container, or deployment.
2. Identify the relevant inputs: source revision plus uncommitted changes, build configuration, lockfile/dependencies, and environment settings. A commit ID alone misses dirty working-tree changes.
3. Use available build manifests, content digests, embedded version IDs, or deployment records to connect those inputs to the artifact. Confirm that the target is running that artifact, rather than merely finding a new file on disk.
4. When identity cannot be established, use the project's existing build/deploy workflow within the authorized environment. Rebuild relevant outputs, install or restart as required, and confirm the new target identity before interpreting behavior.

Timestamps are a warning signal, not proof of identity: copied files, clock differences, caches, preserved timestamps, and a different installed package can invalidate that inference. Do not require a clean rebuild when the existing build system can reliably update the relevant outputs.

For development servers, check the workspace/process/port, compilation status, and observed updated behavior. Investigate a service worker or cache only when relevant evidence suggests stale content. Do not delete caches or deploy to production merely to satisfy this checklist.

Record the identity evidence and any gaps with the test result. If deployment access is unavailable, report runtime verification as not tested; source inspection can still be useful.
