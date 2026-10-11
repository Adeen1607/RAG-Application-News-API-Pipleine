# News Article Retrieval Pipeline

A retrieval prototype that indexes news metadata and returns source-grounded answers from the most relevant records. The repository demonstrates document preparation, chunking, vector search, prompt constraints, and secure configuration.

> The original notebook indexes article titles and authors from a local CSV. It is a proof of concept, not a full article-summarization system: article body text is not present in the current dataset.

## Problem

News collections become difficult to explore as volume grows. Keyword search can miss semantically related wording, while unconstrained text generation can introduce claims that are not supported by the retrieved records. This project tests a retrieval-first workflow that limits answers to the supplied context.

## Current workflow

1. Load a CSV containing `title` and `author`.
2. Remove incomplete and duplicate records.
3. Convert each record into a text document.
4. Split documents into small overlapping chunks.
5. Create vector embeddings and a FAISS index.
6. Retrieve the five nearest chunks for a question.
7. Generate an answer constrained to retrieved context.

## Repository structure

| Path | Purpose |
|---|---|
| `news API RAG Pipeline.ipynb` | Original retrieval experiment |
| `src/validate_news.py` | Input-schema and data-quality checks |
| `.env.example` | Environment-variable names without credentials |
| `docs/SECURITY.md` | Secret-handling and repository-history guidance |
| `requirements.txt` | Reproducible Python dependencies |

## Input contract

Create `data/raw/news.csv` with the following fields:

| Field | Required | Description |
|---|---:|---|
| `title` | Yes | Article headline |
| `author` | Yes | Author or publisher name |

Do not commit licensed article bodies, private feeds, or service credentials.

## Run validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/validate_news.py --data data/raw/news.csv
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Design limitations

- Titles and authors are insufficient for faithful article summaries.
- Retrieval quality is not yet measured against a labelled question set.
- Duplicate syndication and changing headlines can affect results.
- The notebook uses an external embedding and completion service, so cost, latency, and data-handling requirements must be reviewed.
- A production version needs source URLs, publication timestamps, article text or licensed excerpts, citations, evaluation cases, caching, monitoring, and deletion controls.

## Security

Configuration is read from environment variables. Never place credentials in notebooks, source files, screenshots, outputs, or commit messages. If a credential is ever committed, revoke it immediately; removing it from the latest file does not remove it from Git history.


## Rebuild the reading edition

```bash
python -m pip install -r requirements-research.txt
python scripts/build_research_site.py
```

This renders saved notebook outputs without rerunning model training or external APIs. To refresh findings, run the analysis commands above first, update `reports/research-findings.md`, and rebuild.

<!-- research-edition:start -->
## Research edition

[Research report and final visual results](research/report.md) · [Browser-ready notebook catalogue](research/notebooks.html)

The historical notebook demonstrates construction of a metadata vector index and one generated answer. **No numerical evaluation is available.** The saved answer includes details unsupported by the title/author-only context; treat it as a grounding failure example, not a factual result or demonstrated article summary.


The `research/` folder contains a professional static reading edition. The Pages workflow deploys it after GitHub Pages is enabled with **GitHub Actions** as the publishing source. Intended URL: `https://adeen1607.github.io/RAG-Application-News-API-Pipleine/`. Deployment status must be checked in Actions before treating that address as live.

<!-- research-edition:end -->
