# Security guidance

## Credential handling

- Store local credentials in environment variables or an untracked `.env` file.
- Commit only `.env.example`, using placeholders.
- Keep `.env`, notebook checkpoints, raw feeds, indexes, and generated outputs out of version control.
- Use restricted credentials with the minimum required permissions.
- Set usage limits and monitor service activity.

## If a credential is committed

1. Revoke or rotate it immediately in the service dashboard.
2. Replace hard-coded values with environment-variable access.
3. Review account activity and billing for unexpected use.
4. Remove the secret from repository history using an approved history-rewrite procedure.
5. Notify collaborators that old clones and forks may still contain the value.
6. Re-run secret scanning before making the repository public.

Deleting the value from the newest revision is not sufficient because earlier commits remain retrievable.

## Data handling

News feeds can contain licensed text, personal information, and source-specific retention restrictions. Store only data you are permitted to use, document its origin, and avoid committing raw feeds or generated indexes unless their licence explicitly permits redistribution.
