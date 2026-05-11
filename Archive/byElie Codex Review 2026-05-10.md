# byElie Codex Review 2026-05-10

Timestamp: 2026-05-10 02:04 CEST

1/ General architecture:

- The static-site shape is appropriate, but the repeated page structure across service pages points to a maintainability issue.
- `scripts/site_maintenance.py` is a good foundation. It should become the main guardrail for version, cache-bust, links, sitemap, and page consistency.

2/ UI:

- The site should keep using restrained service-page layouts, but repeated sections need consistent spacing and CTA placement.
- Asset usage is light. Add real portfolio/process imagery where it clarifies CAD, prints, and web work rather than relying mainly on copy.

3/ UX:

- Each service page should answer: what you get, what the process is, what examples look like, and how to inquire.
- Keep PhotosByElie as a canonical external link rather than duplicating gallery functionality here.

4/ Testing:

- There are no browser tests. Add responsive smoke checks for every public page and a static check for broken links/assets.
- Add a check that `VERSION` and cache-bust query strings match across HTML files.

5/ Everything else:

- The README’s review-to-`TODO.md` process is useful; continue turning review items into the backlog rather than leaving many root review files.
- Consider a tiny content inventory so repeated service-page claims stay consistent.

6/ My suggetions:

1. Extract repeated page data into a small metadata source or template generator.
2. Expand `scripts/site_maintenance.py --check` for links, SEO, versions, sitemap, and cache busts.
3. Add responsive smoke checks for all public pages.
4. Tighten each service page around examples, process, offer, fit, and inquiry CTA.
5. Keep PhotosByElie links canonical and external to this site's implementation.
