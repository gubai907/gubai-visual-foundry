# Quick start

[简体中文](quick-start.md) | **English**

[Home](../README_EN.md) · [Installation](installation.en.md) · [Examples](examples.en.md)

## Writing your first request

At minimum, state **the task, subject, preservation requirements, permitted changes, and desired output**. Add the platform, aspect ratio, or duration when specified. An unknown platform receives generic natural-language wording directly. You may name any visual platform and let the skill adapt to its supported inputs, or supply your own format.

```text
Please use $gubai-visual-foundry:
Task: write a product scene prompt for an unbranded dark-blue canvas bag.
Use: an image for social content.
Scene: the bag rests on a clean wooden stool under natural side-window light.
Preserve: bag color, two handles, and its rectangular silhouette.
Exclude: brand text, extra zippers, and decorative charms.
Aspect ratio: 4:5.
Output: a complete English prompt. Do not generate an image yet.
```

This is a fictional text specification. Supply a reference image to preserve a real product, and assign it responsibility for product shape and details.

## Multiple references

Upload images, then give each one a role:

```text
Image A: character identity.
Image B: clothing and footwear only; identity still comes from A.
Image C: composition and lighting only; do not import its people, outfits, or props.
Write an English fashion-image prompt preserving A's identity and B's outfit.
Prompt only; do not generate an image yet.
```

When references conflict, state which image has final responsibility for the affected field. Text inside a reference becomes a task requirement only when you explicitly authorize it.

## Editing or refinement

Upload the original and define the changes for this task:

```text
Based on the original, change only the background to a light-gray indoor wall.
Preserve identity, pose, clothing, hand action, held objects, and the original crop.
Provide an edit prompt. Do not generate an image yet.
```

Refinement needs a concrete goal, such as reducing overly smooth skin. Without such a goal, refinement should not be interpreted as replacing the person, outfit, or scene.

## Video and storyboards

Specify shot count, target durations, starting states, and permitted changes:

```text
Create a three-shot product storyboard for a fictional unbranded white diffuser bottle, targeting 3 seconds per shot.
Keep the bottle shape, cap, blank label, and light-beige background consistent.
Show the whole product, a cap detail, then return to the whole product.
Output a shot table and an English prompt for each shot. Do not generate video yet.
```

Duration is a creative target and must fit the actual generation tool.

## After receiving the output

- For prompts: copy them into your target platform and upload the corresponding references.
- For media: explicitly request generation and use an available tool.
- For repairs: supply the generated image or video, identify its main problem, and state what must stay.

For example: “Repair only the cap shape; keep the bottle, background, and composition.” Without seeing results, rule checks cannot count as image-quality or fidelity measurements.

## Choosing language and format

Request Chinese, English, or complete versions in both languages, and specify “prompt only” or “complete plan.” Documentation language does not force prompt language. A copyable card for complex tasks is in the [README](../README_EN.md#complete-input-card).
