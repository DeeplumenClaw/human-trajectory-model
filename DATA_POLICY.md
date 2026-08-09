# HTM Data Policy

Human trajectory data can expose intimate information about identity, family, health, relationships, finances, location, and life history. This policy is a binding contribution rule, not a suggestion.

## Absolute prohibition: private-conversation cases

Do not commit, quote, summarize, encode, label, or derive a record from:

- private conversations, chats, messages, emails, consultations, or voice transcripts;
- cases discussed privately with an AI assistant, researcher, practitioner, or contributor;
- information about a contributor's family, friends, clients, colleagues, or acquaintances;
- a private person's birth details, life events, health, finances, relationships, legal history, or other personal circumstances;
- any record whose inclusion relies on the assumption that sharing information in a conversation implied consent for research or publication.

Access is not consent. Anonymization after collection does not cure an unauthorized source.

## Data permitted in the repository

### 1. Synthetic records

Synthetic records are the default for examples, tests, tutorials, and infrastructure development. They must:

- be intentionally fictional rather than lightly altered real cases;
- use `entity_type: synthetic` and `synthetic: true`;
- set `contains_private_conversation_data: false`;
- avoid real names, contact details, addresses, account identifiers, and copied biographies;
- state the applicable license.

### 2. Public-record data

Public availability does not automatically make collection ethical or legally reusable. A public-record proposal requires, before inclusion:

- a declared research purpose;
- source provenance and access dates;
- a documented license or lawful-use analysis;
- data minimization;
- conflict and correction procedures;
- privacy and re-identification review;
- an approved benchmark protocol.

No public-person records are part of the v0.1 starter.

### 3. Consented volunteer data

Consented data requires a separate protocol covering informed consent, allowed uses, withdrawal, retention, security, publication, and downstream model use. A pull request is not an adequate consent process. No volunteer records should be added until that protocol is reviewed and approved.

## Prohibited fields and materials

Do not include raw private addresses, personal email addresses, phone numbers, private correspondence, passwords, authentication material, financial-account details, private medical records, government identifiers, or information about non-public relatives.

Sensitive attributes should be collected only when necessary for a declared research question and when their risks, benefits, and governance are documented.

## Provenance and licensing

Every non-synthetic record and event must identify its source, source type, access date, evidence confidence, and usage rights. Unclear provenance or licensing is grounds for exclusion.

Repository code and documentation licensing does not automatically license contributed datasets. Each dataset release must state its own license and access conditions.

## Leakage and scientific integrity

Data must not leak hidden outcomes into model inputs. In particular:

- events after the prediction cutoff must not appear in the permitted history;
- a biography title or description that directly states the target must not be used as input;
- information used to infer or correct a birth time must not also be scored as a hidden outcome;
- duplicate or near-duplicate biographies of one person must not cross evaluation splits.

## Removal and incident response

A privacy concern takes priority over benchmark continuity. Maintainers may immediately remove or quarantine a record while provenance, consent, licensing, or re-identification risk is reviewed. Git history may require additional remediation beyond deleting the current file.

Report a sensitive concern to the repository owner using the contact method on the owner's GitHub profile. Do not place private details in a public issue.

## Pull-request declaration

Every pull request that adds or changes data must affirm that:

- it contains no private-conversation material;
- it contains no unconsented private-person data;
- provenance and licensing are documented;
- the contributor has read this policy;
- synthetic records are not derived from real private cases.
