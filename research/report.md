# News Metadata Retrieval Prototype

**Author:** Mohammed Adeen Shaik  
**Review date:** 11 October 2026

## Research question

Can titles and authors provide useful retrieval evidence, and where does generation exceed that evidence?

## Data and provenance

The notebook uses a local CSV of news metadata; full article bodies are absent.

Source materials are linked from the repository README. Input fingerprints are recorded in [the evidence manifest](evidence.json) so a reader can identify the exact committed artifacts used in this review.

## Method and analytical rationale

Title and author are formatted into strings, split into overlapping chunks, embedded and indexed in FAISS. A retriever requests five chunks before a legacy generation chain.

## Findings and interpretation

The historical notebook demonstrates construction of a metadata vector index and one generated answer. **No numerical evaluation is available.** The saved answer includes details unsupported by the title/author-only context; treat it as a grounding failure example, not a factual result or demonstrated article summary.


## Limitations

The saved answer contains claims beyond the indexed headline and author context, so it is not a verified research finding. There is no retrieval benchmark or grounded-answer evaluation. Legacy LangChain APIs may require migration. Never publish API keys.

## Reproduction

Use the setup commands and input contract in the [repository README](https://github.com/Adeen1607/RAG-Application-News-API-Pipleine#readme). Open the [notebook catalogue](notebooks.html) for annotated code and saved outputs. Keep raw records and model binaries local; public reports contain aggregate results or source-embedded figures.

## Final visual results

No verified numerical result figure is available in the current evidence. This status is shown explicitly rather than substituting fabricated data.
