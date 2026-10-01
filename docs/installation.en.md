# Installation and updates

[简体中文](installation.md) | **English**

[Home](../README_EN.md) · [Quick start](quick-start.en.md) · [FAQ](faq.en.md)

## Prerequisites

- A Codex environment that can load local skills.
- The complete `gubai-visual-foundry` folder.
- Writing prompts needs neither Python nor a separate image-generation API key. Actual media generation requires a suitable tool and its permissions.

## Method 1: ask Codex to install

If your environment provides the built-in `skill-installer`, copy this request:

```text
Please use $skill-installer to install from https://github.com/gubai907/gubai-visual-foundry.
The repository root is the skill itself. Skill path: .; installation name: gubai-visual-foundry.
Keep every supporting file. If a skill with this name already exists, report its version first
and do not directly overwrite my local modifications.
```

The installer may use the skills directory configured in your environment; rely on its reported destination. Check availability in the next conversation turn.

## Method 2: download the source manually

1. Open the [GitHub repository](https://github.com/gubai907/gubai-visual-foundry).
2. Click the green **Code → Download ZIP** button.
3. Extract the download and find the folder directly containing `SKILL.md`, `agents`, `core`, and the other resources.
4. Rename `gubai-visual-foundry-main` to `gubai-visual-foundry`.
5. Copy the complete folder to one of these locations.

| Scope | Location |
|---|---|
| Personal, macOS / Linux | `~/.agents/skills/gubai-visual-foundry/` |
| Personal, Windows | `%USERPROFILE%\.agents\skills\gubai-visual-foundry\` |
| Current project only | `project-directory/.agents/skills/gubai-visual-foundry/` |

On macOS, use Finder **Go → Go to Folder**, enter `~/.agents/skills/`, and create missing directories if needed. On Windows, enter `%USERPROFILE%` in File Explorer, then create `.agents` and its `skills` subfolder. The leading dot is part of the name.

The installed structure should be:

```text
skills/
└── gubai-visual-foundry/
    ├── SKILL.md
    ├── agents/
    ├── core/
    ├── locks/
    └── remaining supporting files and folders
```

Do not copy only `SKILL.md` or place it inside another nested folder with the same name.

## Method 3: download a Release package

Open [Releases](https://github.com/gubai907/gubai-visual-foundry/releases), select a published version, and download the project's `gubai-visual-foundry-…zip` from **Assets**. If no Release exists, use Method 2.

The project package extracts to a `gubai-visual-foundry` folder. Install it at the path above. GitHub's automatic **Source code (zip)** is a source snapshot and may still require renaming the folder.

An accompanying `.zip.sha256` lets you check whether the downloaded package matches the supplied checksum. A checksum is not an author identity signature.

## Invocation

- In a desktop interface with a skill selector, type `@` and look for **Gubai Visual Foundry**.
- In Codex CLI or the IDE extension, use `/skills` or `$gubai-visual-foundry`.
- You can also explicitly request “Use Gubai Visual Foundry.” Invocation depends on whether your environment has discovered the skill.

Try this first:

```text
Please use $gubai-visual-foundry to write an English product-image prompt for an unbranded white ceramic cup.
Light-gray background, soft side lighting, 4:5 composition. Prompt only; do not generate an image yet.
```

If the skill is missing, check the path, folder nesting, and `SKILL.md` filename, then restart Codex. Follow the [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) and your actual interface.

## Updating an existing installation

1. Copy the complete old version to a backup location outside the skills directory.
2. Save your modified configuration and external project data.
3. Download the new version and compare the versions in `README.md`, `SKILL.md`, and the [Changelog](../CHANGELOG.md).
4. Replace the old folder with the complete new folder, avoiding mixed supporting files from different versions.
5. Check discovery and invocation in a new turn; restart if the update has not appeared.

A skill installed under a different name may coexist with `gubai-visual-foundry`. Installing the new name does not automatically replace it or migrate personal data. Check its location and local modifications before disabling it.

## Removal

Move this skill's folder out of the actual skills directory. Preserve your modifications and project data first. Check other locations for duplicate installations with the same name.
