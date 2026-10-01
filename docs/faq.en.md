# Frequently asked questions

[简体中文](faq.md) | **English**

[Home](../README_EN.md) · [Installation](installation.en.md)

## Does installation automatically generate images?

The skill writes prompts, edit requirements, or storyboards as requested. Actual generation needs an explicit request and an available tool. A prompt-only response is not presented as a generated image.

## Do I need Python?

Not for writing prompts. Maintainer package and regression checks require Python 3.10 or later, with no third-party dependencies.

## Must I choose a platform?

No. An unspecified platform receives generic natural-language wording directly. For any specified visual platform, the skill can adapt to its inputs and capabilities or follow your supplied format. Common built-in rules do not limit platform coverage; parameters, reference limits, and editing capabilities depend on the actual environment.

## How many references should I provide?

Provide the references your task needs and assign their roles. Maximum image counts depend on the platform. Product work without people does not need an identity reference.

## Can I use only SKILL.md?

A complete installation needs the supporting directories. The entry point loads task modules, preservation rules, adapters, and quality rules. Copying it alone cannot provide the full workflow.

## Why is the skill missing?

Check whether the install path is supported, whether the folder directly contains `SKILL.md`, and whether it has duplicate nesting. Check in the next turn and restart if necessary. See the installation guide for paths.

## Is identical identity or unchanged content outside an edit region guaranteed?

Prompts alone cannot guarantee either. The skill defines preservation, reference roles, and review priorities. Results depend on tool capabilities and must be inspected. Pixel-level preservation needs an appropriate editing method and comparison of actual results.

## Can I add my brand data?

Supply the required brand and character data in your local project. The public repository and installation package should contain generic interfaces and fictional examples. Keep private photos, credentials, history, and business data elsewhere.

## Does .gitignore block every private file from being uploaded?

No. It helps ignore matching untracked files, does not remove committed content, and does not replace browser-upload review. Inspect files, contents, and commit history before publication.

## How does a source ZIP differ from an installation package?

A source ZIP is GitHub's automatic repository snapshot; its folder name may include a version or branch suffix. A project Release package uses the `gubai-visual-foundry` top-level folder and includes corresponding instructions and a checksum. It is downloadable once its Release has actually been published.

## Can I use it commercially or redistribute it?

The project uses CC BY-NC 4.0. Noncommercial use, adaptation, and sharing are permitted under the terms; retain attribution, license, and source information and indicate modifications when sharing. Commercial use needs separate authorization. See [LICENSE](../LICENSE). This license does not grant rights to third-party references, people, brands, or other works.

## Can I request both Chinese and English output?

Yes. Ask for complete Chinese and English versions with the same subjects, reference roles, editing scope, and constraints. Specify one language when that is all you need. The README and guides have corresponding Chinese and English files; their reading language does not force output language.
