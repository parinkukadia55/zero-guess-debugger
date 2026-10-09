# Changed interfaces and connected surfaces

Use only the checks relevant to the changed behavior and the capabilities the product already supports.

- Trace a changed interaction from trigger through handler/API/store to its consumers. An endpoint without a UI caller may serve another client, webhook, or background job; investigate before classifying it as orphaned.
- For shared contracts, inspect callers and validate affected payloads, failure handling, and cache/state updates. Use the intended consistency model rather than assuming every surface must update instantly.
- For UI changes, exercise the relevant loading, success, empty, and error states. Check keyboard access and existing themes/viewports when affected. Do not introduce dark mode or a mobile shell as an incidental debugging requirement.
- For localized products, reuse their translation system and update affected keys in supported locales. Test representative long strings and scripts; no fixed expansion percentage proves layout safety. Do not introduce a project-specific locale storage key into another application.
- For native boundaries, inspect actual platform APIs, permissions, resource lifetime, and offline behavior. Use available device coverage and report what could not be exercised.

A local UI fix does not require a full application audit. Broaden checks when dependencies, a regression, or a requested audit justify doing so.
