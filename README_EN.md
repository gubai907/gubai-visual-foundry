# Gubai Visual Foundry

[简体中文](README.md) | **English**

**Turn your visual brief, reference images, and edit requirements into actionable visual prompts.**

For product, ecommerce, advertising, fashion, portrait, poster, and short-video work. Assign a role to each reference, state what must stay and what may change, then prepare prompts or storyboards for your target platform.

V2 public edition: `2.0.0-public.5` · Maintainer attribution: **Gubai**

[Quick start](docs/quick-start.en.md) · [Installation](docs/installation.en.md) · [Examples](docs/examples.en.md) · [FAQ](docs/faq.en.md) · [Changelog](CHANGELOG.md) · [Downloads](https://github.com/gubai907/gubai-visual-foundry/releases)

## Reading guide

- [What you can do](#what-you-can-do) and [Core capabilities](#core-capabilities)
- [One-minute start](#one-minute-start) and [Installation](#installation)
- [Complete input card](#complete-input-card) and [Expected output](#expected-output)
- [Platforms and output](#platforms-and-output), [Directory guide](#directory-guide)
- [Project data and privacy](#project-data-and-privacy), [Maintainer checks](#maintainer-checks), [License and releases](#license-and-releases)

## What you can do

| Task | Example uses | Deliverable |
|---|---|---|
| Product, ecommerce, and advertising | Product hero images, contextual images, ad visuals | Prompts specifying product features, composition, light, and materials |
| Fashion and people | A chosen identity, outfit, and reference composition | Prompts with assigned reference roles |
| Image editing and refinement | Change a chosen background, preserve the subject, repair a local issue | Edit prompts specifying changes and preservation requirements |
| Posters and social content | Organize subjects, copy, and layout | Visual and layout prompts |
| Short videos and storyboards | Product demonstrations, continuous shots, start/end-state planning | Shot tables and individual shot prompts |

For actual image or video generation, explicitly request it and use a generation tool available in your environment. A written prompt is not a generated media asset.

## Core capabilities

- **Give each reference a specific role**: identity, clothing, product, prop, composition, environment, or lighting.
- **Separate changes from preservation**: describe permitted changes for the current task and keep the remaining requirements.
- **Organize prompts for the intended use**: dedicated modules for products, people, edits, posters, and storyboards.
- **Manage continuity across a series**: reuse confirmed characters, clothing, objects, and scene settings.
- **Repair results locally**: identify the current problem and focus the repair on one main variable.

These are prompt and review rules. Identity, product details, text, and preservation still require checking the actual generated result.

## One-minute start

After installation, select the skill in Codex or submit the request below. The insulated cup is fictional; supply a product reference when you need to preserve a real product.

```text
Please use $gubai-visual-foundry:
Write a product scene prompt for an unbranded matte light-gray insulated cup.
Use: an ecommerce product detail page.
Scene: the cup stands on a light wooden table, with soft window light and a simple background.
Aspect ratio: 4:5.
Preserve: body proportions, lid structure, and the light-gray surface.
Do not add branding, text, water droplets, or decorative props.
Output only the English prompt. Do not generate an image yet.
```

When using references, upload them and assign roles: image A defines the product shape; image B contributes only composition and lighting. See [Quick start](docs/quick-start.en.md) and [Examples](docs/examples.en.md).

## Installation

The repository root is the skill itself. Its entry point is [SKILL.md](SKILL.md). Keep the full directory when installing.

1. Download source via **Code → Download ZIP**, or obtain a published installation package from [Releases](https://github.com/gubai907/gubai-visual-foundry/releases).
2. Extract it and locate the folder that directly contains `SKILL.md`. Rename a source folder such as `gubai-visual-foundry-main` to `gubai-visual-foundry`.
3. Place the entire folder in your personal skills directory or the project's `.agents/skills/` directory.

| System | Personal installation path |
|---|---|
| macOS / Linux | `~/.agents/skills/gubai-visual-foundry/` |
| Windows | `%USERPROFILE%\.agents\skills\gubai-visual-foundry\` |

You can also ask the built-in `skill-installer` to install from this repository, specifying the repository root as the skill path and `gubai-visual-foundry` as the installation name.

See [Installation](docs/installation.en.md) for steps, updates, and troubleshooting. Discovery and invocation follow the [official OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills).

## Complete input card

For complex tasks, copy this card and fill only the relevant fields. Omit fields you have not specified. Upload real reference images as attachments, then identify their roles by image number.

```text
Please use $gubai-visual-foundry:
Task: product / portrait / poster / edit / refinement / video storyboard
Use and channel:
Subject and scene:
Reference roles: image A defines ...; image B contributes only ...
Must preserve:
Changes allowed in this task:
Unwanted elements or effects:
Target platform (omit if unknown):
Aspect ratio; shot count and target duration for video, where relevant:
Output language and level of detail:
Deliverable: prompt only / complete plan / generated media
```

If preservation and permitted changes conflict, clarify the current scope. Operations and parameters must fit the capabilities of the target tool.

## Expected output

| Request | Expected deliverable |
|---|---|
| Prompt only | A copyable prompt in the requested language and length |
| Complete single-image plan | Use, reference roles, positive prompt, relevant exclusions, and aspect ratio |
| Edit or local repair | Specific changes, preservation requirements, and an edit prompt |
| Video storyboard | A shot table and prompts describing actions, target durations, and visible end states |
| Actual media generation | Generation with an available tool and review of the returned result |

The Chinese and English guides have corresponding sections, with language links at the top of each page. For bilingual prompts, request complete Chinese and English versions. Documentation language does not fix the language of your output.

## Platforms and output

Designed for visual generation, editing, and video platforms across web tools, applications, and API workflows. Adapt prompts to the target platform's input format, reference-image handling, editing scope, and output requirements, or follow a format supplied by the user.

The repository includes the following common adapter rules. Other visual platforms use the generic adapter, adjusted to their actual capabilities. An unspecified platform receives a generic prompt directly.

| Common adapter | Purpose |
|---|---|
| Generic | Natural-language prompts when no platform is specified |
| ChatGPT Image | Image creation and editing briefs |
| Jimeng | Image or video prompts organized for the current request |
| TapNow | Compact wording with essential control requirements |

Platform coverage is not limited to this table. Reference limits, edit methods, dimensions, and video duration depend on the actual tool. Language and verbosity follow your request. Unknown product dimensions, brand copy, and parameters are not invented as facts.

## Directory guide

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Skill entry point, task handling, and reading rules |
| `agents/` | Skill display metadata |
| `core/` | Task routing, reference roles, output, and continuity |
| `locks/` | Preservation rules for identity, body, clothing, products, props, and text |
| `modules/` | 11 specialized task modules |
| `platforms/` | Generic and common platform rules, adaptable to other platforms |
| `knowledge/` | Camera, lighting, composition, materials, and color references |
| `profiles/` | Defaults and interfaces for external brand and character data |
| `qa/` | Result review and local repair rules |
| `docs/` | Installation, quick start, examples, and FAQ |
| `examples/` | Fictional brand data examples |
| `scripts/`, `tests/` | Package checks and regression specifications |

## Project data and privacy

Real brand, product, and character data come from your current project. See the [brand schema](profiles/profile-schema.md) and [character interface](profiles/model-library.md). The [brand example](examples/brand-profile-example.md) is fictional.

Keep your project data, photographs, credentials, conversations, and backups outside the public repository. `.gitignore` helps ignore matching untracked files; it does not replace upload review or remove committed content.

## Maintainer checks

Writing prompts does not require Python. Check scripts require Python 3.10 or later, with no third-party dependencies. Run from the skill directory:

```sh
python3 scripts/validate_skill.py
python3 scripts/run_prompt_regression.py
python3 tests/test_validation.py
```

Use `--private-terms-file` with a local exclusion list outside the public package. See the [regression inventory](tests/regression-cases.md). Deterministic checks do not replace independent model testing, real media generation, or pixel-region comparisons.

## License and releases

Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), Attribution–NonCommercial 4.0 International. Noncommercial use, adaptation, and sharing are permitted under its terms. Retain attribution, license, and source information when sharing, and indicate changes. Commercial use requires separate authorization from the maintainer.

Attribution: **Gubai**. See [LICENSE](LICENSE) for the full terms and [NOTICE.md](NOTICE.md) for attribution and rights information. The noncommercial restriction means this is not described as an open-source-licensed project.

See [RELEASE_NOTES.md](RELEASE_NOTES.md) for release notes and [PUBLISHING.md](PUBLISHING.md) for maintainer procedures. Download the version actually published on the releases page; a version mentioned in this document alone does not establish that a Release exists.
