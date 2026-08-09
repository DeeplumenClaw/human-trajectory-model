# HTM Data Policy

Human trajectory research can involve identity, family, health, relationships, finances, location, and life history. This policy separates one owner-specific opt-out from the governance rules for all other data.

## 1. Absolute opt-out for the repository owner

The following material must never be used as HTM research data or committed to this repository:

- a trajectory record about the repository owner;
- the owner's birth details, life events, health, finances, relationships, family circumstances, legal history, or other personal trajectory information;
- facts, cases, notes, summaries, labels, features, or examples derived from the owner's private conversations, chats, messages, emails, consultations, or voice transcripts;
- synthetic records that are lightly altered versions of the owner or of material taken from those private communications.

Routine authorship, commit, and repository-administration metadata are not trajectory research data and are outside this rule.

A third-party fact mentioned in a private communication with the owner may not use that communication as its source. The same fact may be considered only when it is independently supported by an allowed third-party source and passes the applicable review below.

This owner-specific opt-out is absolute. Public availability elsewhere does not authorize HTM to create a trajectory record about the owner.

## 2. Allowed bases for third-party data

Other people are governed by a declared source and use basis rather than by the owner's personal opt-out. A non-synthetic record must use one of these bases:

### Public record

Public-figure or public-event data may be proposed when the contribution documents:

- a declared research purpose;
- source provenance and access dates;
- a license, terms-of-use analysis, or other lawful-use basis;
- data minimization;
- correction and conflict procedures;
- re-identification and harm review where relevant;
- an approved benchmark or research protocol.

Public availability alone does not guarantee scientific quality or unrestricted reuse.

### Consent

Volunteer or contributor-supplied data may be used under a separately reviewed consent process covering allowed uses, publication, withdrawal, retention, security, and downstream model use. A pull request by itself is not a complete consent protocol.

### Licensed dataset

A research or commercial dataset may be used when its license and access terms permit the intended processing and publication. The contribution must document the dataset version, permitted uses, restrictions, and whether raw records may be redistributed.

### Approved research protocol

Data may be processed under an institutional, ethics-reviewed, or otherwise approved research protocol when the repository contribution describes the approval basis, access controls, publication limits, and de-identification method. Restricted data should not be copied into the public repository merely because derived results may be published.

### Synthetic data

Synthetic records are the default for examples, tests, tutorials, and infrastructure development. They must:

- be intentionally fictional rather than lightly altered real cases;
- use `entity_type: synthetic` and `synthetic: true`;
- set both owner-protection flags to `false`;
- use `source_scope: synthetic` and `authorization_basis: synthetic`;
- avoid real names, contact details, addresses, account identifiers, and copied biographies;
- state the applicable license.

The v0.1 starter contains synthetic records only.

## 3. Repository-level limits

Regardless of data basis, do not commit raw passwords, authentication material, government identifiers, bank-account numbers, private correspondence, personal contact details, or other secrets that are unnecessary for the declared research task.

Health, financial, relationship, and other sensitive events are not categorically excluded from trajectory research, but their inclusion requires a precise research need, data minimization, provenance, appropriate access and publication controls, and explicit risk review.

## 4. Provenance and licensing

Every non-synthetic record and event must identify its source, source type, access date, evidence confidence, authorization basis, and usage rights. Unclear provenance or incompatible licensing is grounds for exclusion.

Repository code and documentation licensing does not automatically license contributed datasets. Each dataset release must state its own license and access conditions.

## 5. Leakage and scientific integrity

Data must not leak hidden outcomes into model inputs. In particular:

- events after the prediction cutoff must not appear in the permitted history;
- a biography title or description that directly states the target must not be used as input;
- information used to infer or correct an input must not also be scored as a hidden outcome;
- duplicate or near-duplicate records of one person must not cross evaluation splits.

## 6. Removal and incident response

A concern about the owner's opt-out, provenance, authorization, licensing, or unnecessary raw identifiers takes priority over benchmark continuity. Maintainers may immediately remove or quarantine material while it is reviewed. Git history may require additional remediation beyond deleting the current file.

Report a sensitive concern to the repository owner using the contact method on the owner's GitHub profile. Do not place sensitive details in a public issue.

## Pull-request declaration

Every pull request that adds or changes data must affirm that:

- it contains no trajectory record about the repository owner;
- it is not derived from the owner's private communications;
- every non-synthetic third-party record declares an allowed basis: public record, consent, dataset license, or approved protocol;
- provenance, redistribution rights, and publication limits are documented;
- synthetic records are intentionally fictional and not derived from the owner;
- the contributor has read this policy.
