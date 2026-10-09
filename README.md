# Google AI Overview Citation & Brand Tracker

Track which sources and domains Google AI Overview cites for each search query, with brand mentions and organic rank in one row.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/google-ai-overview-citation-tracker) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/google-ai-overview-citation-tracker/)

**from $14.00 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Google AI Overview Citation & Brand Tracker checks a list of Google search queries and tells you, for each one, whether Google shows an AI Overview, which sources it cites and in what order, whether your brand is named in the answer, and where your domain ranks in the organic results. Every query becomes one flat row you can export as JSON, CSV or Excel, call through the Apify API, or feed into n8n, Make and AI agents through MCP.
It is built for SEO and content teams, agencies and brand owners who want to measure visibility inside AI answers (often called AEO or GEO) instead of only in the ten blue links.

## Quick start

1. Open [Google AI Overview Citation & Brand Tracker on Apify Store](https://apify.com/datagrit/google-ai-overview-citation-tracker) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "queries": [
    "how to lower blood pressure",
    "what is kubernetes",
    "best running shoes for flat feet",
    "how does a heat pump work",
    "is intermittent fasting safe",
    "what causes inflation",
    "how to learn python fast",
    "symptoms of vitamin d deficiency",
    "how to start a vegetable garden",
    "what is a roth ira",
    "how to remove a stripped screw",
    "what is a good credit score"
  ],
  "trackedDomains": [
    "kubernetes.io",
    "mayoclinic.org"
  ],
  "brandNames": [
    "Kubernetes"
  ],
  "maxItems": 14
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `queries` (required) | array | Google search queries to check. Each query is one Google results page and produces one row. Duplicates are removed. |
| `gl` | string | Two-letter country code of the Google market, for example us, gb, de or pl. Controls which results and which AI Overview Google serves. |
| `hl` | string | Language code of the Google results page, for example en, de, pl or pt-BR. The AI Overview is written in this language. |
| `trackedDomains` | array | Your own domains or competitor domains, for example example.com. Subdomains match too. Rows then show whether the domain is cited in the AI Overview, at which citation position, and its organic rank. Leave empty to only list all citations. |
| `brandNames` | array | Brand or product names to look for in the AI Overview text, case-insensitive. Rows show whether each name is mentioned and how many times. |
| `maxItems` | integer | Stop after this many result rows in total across all queries. You are charged per result row, so this caps the cost of a run. |

## Output

| Field | Type | Description |
|---|---|---|
| `query` | string | The search query this row belongs to. |
| `gl` | string | Country code of the Google market the query was checked in. |
| `hl` | string | Interface language of the Google results page. |
| `found` | boolean | False only on a status row, which is free and carries the reason in the reason and message fields. |
| `aiOverviewPresent` | boolean | True when Google showed an AI Overview for the query, false when it did not. |
| `aiOverviewText` | string | Plain text of the AI Overview with line breaks between paragraphs and list items. Null when there is no AI Overview. |
| `citationCount` | integer | Number of distinct source pages cited by the AI Overview. |
| `citedDomains` | array | Distinct domains cited by the AI Overview, in order of first appearance. |
| `citations` | array | Cited source pages in the order Google lists them: position, URL, domain and site name. |
| `trackedDomainCited` | boolean | True when at least one of your tracked domains is cited in the AI Overview. Null when no domains were tracked. |
| `trackedDomainsCited` | array | Which of your tracked domains are cited in the AI Overview. Null when no domains were tracked. |
| `bestCitationPosition` | integer | Position of the first citation that belongs to a tracked domain. Null when none is cited or no domains were tracked. |
| `brandMentioned` | boolean | True when at least one tracked brand name appears in the AI Overview text. Null when no brand names were tracked. |
| `brandsMentioned` | array | Which tracked brand names appear in the AI Overview text. Null when no brand names were tracked. |
| `brandMentionCount` | integer | Total number of times tracked brand names appear in the AI Overview text. Null when no brand names were tracked. |
| `organicResultCount` | integer | Number of organic results parsed from the first results page. |
| `trackedDomainOrganicRank` | integer | Position of the first organic result that belongs to a tracked domain. Null when none ranks on the first page or no domains were tracked. |
| `organicResults` | array | Organic results of the first page: position, title, domain and displayed URL. |
| `reason` | string | Only on a status row: noResults or fetchFailed. |
| `message` | string | Only on a status row: plain-language explanation of why the query produced no result row. |
| `sourceUrl` | string | Google search URL the row was read from. |
| `scrapedAt` | string | ISO 8601 timestamp of the run that produced the row. |

Sample record:

```json
{
  "query": "what is kubernetes",
  "gl": "us",
  "hl": "en",
  "found": true,
  "aiOverviewPresent": true,
  "aiOverviewText": "Kubernetes is an open-source system for automating deployment, scaling and management of containerized applications.",
  "citationCount": 7,
  "citedDomains": [
    "kubernetes.io",
    "redhat.com"
  ],
  "citations": [
    {
      "position": 1,
      "url": "https://kubernetes.io/docs/concepts/overview/",
      "domain": "kubernetes.io",
      "site": "Kubernetes"
    }
  ],
  "trackedDomainCited": true,
  "trackedDomainsCited": [
    "kubernetes.io"
  ],
  "bestCitationPosition": 1,
  "brandMentioned": true,
  "brandsMentioned": [
    "Kubernetes"
  ],
  "brandMentionCount": 4,
  "organicResultCount": 9,
  "trackedDomainOrganicRank": 2,
  "organicResults": [
    {
      "position": 1,
      "title": "Kubernetes",
      "domain": "kubernetes.io",
      "displayedUrl": "https://kubernetes.io"
    }
  ],
  "reason": "fetchFailed",
  "message": "Google did not return a readable results page for this query after several attempts.",
  "sourceUrl": "https://www.google.com/search?q=what+is+kubernetes&hl=en&gl=us",
  "scrapedAt": "2026-10-08T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~google-ai-overview-citation-tracker/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"queries":["how to lower blood pressure","what is kubernetes","best running shoes for flat feet","how does a heat pump work","is intermittent fasting safe","what causes inflation","how to learn python fast","symptoms of vitamin d deficiency","how to start a vegetable garden","what is a roth ira","how to remove a stripped screw","what is a good credit score"],"trackedDomains":["kubernetes.io","mayoclinic.org"],"brandNames":["Kubernetes"],"maxItems":14}'
```

## FAQ

**Does it cover Google AI Mode?**  
No. It reads the AI Overview shown on the regular results page.

**Do results match what I see in my browser?**  
Google personalises and varies AI Overviews, so a single check is a sample. Run the same list on a schedule and compare over time.

**How many queries per run?**  
Up to 10,000 queries; runs read several queries in parallel.

**Can I schedule runs?**  
Yes, use Apify schedules or call the Actor from your own workflow.

## More from datagrit

- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.
- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.
- [Poland KRS New Company Registrations Feed](https://github.com/getdatagrit/poland-krs-new-companies) - Newly registered Polish companies, foundations and associations from the official KRS court register: NIP, address, PKD, capital, email, with filters and change detection.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/google-ai-overview-citation-tracker). Examples are MIT licensed.
