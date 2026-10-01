# Three complete teaching examples

[简体中文](examples.md) | **English**

[Home](../README_EN.md) · [Quick start](quick-start.en.md)

These inputs and outputs are fictional teaching examples, with no corresponding tested image or video results. Actual output depends on your references, request, and platform.

## Example 1: a product scene

### Input

```text
Please use $gubai-visual-foundry:
Write an ecommerce scene prompt for an unbranded matte light-gray insulated cup.
The cup stands on a light wooden table under natural window light. Aspect ratio: 4:5.
Preserve body proportions and lid structure. Add no text, logos, droplets, or decorative props.
Output only the English prompt. Do not generate an image yet.
```

### Sample prompt

```text
Vertical 4:5 product scene. An unbranded matte light-gray insulated cup stands on a light wooden table.
Show the body-to-lid connection clearly, keep the entire cup in frame, and leave moderate space around it.
Soft natural window light illuminates one side, with natural tonal falloff on the other.
The contact shadow on the table follows the source-light direction.
Keep the background simple and low-contrast, distinguishing the matte coating from the pale wood grain.
Preserve the specified body proportions, lid structure, and light-gray surface.
Add no text, logos, water droplets, or decorative props.
```

Check subject count, lid structure, color, and material. Text alone cannot guarantee reproduction of a real product for which no reference was provided.

## Example 2: identity and outfit from different references

### Input

```text
Please use $gubai-visual-foundry:
I have uploaded three images.
A defines identity; B supplies clothing and footwear only; C supplies composition and lighting only.
Write a full-body fashion prompt. Do not import people, clothing, text, or props from C.
Output in English. Do not generate an image yet.
```

### Sample prompt

```text
Reference roles: A = identity; B = clothing and footwear; C = composition and lighting.
Use the person from A, preserving their recognizable facial features.
Use B for outfit design, colors, layers, and shoes.
Create a full-body fashion image with the entire person visible; do not crop the head or footwear.
Adapt C's composition and light direction to the current person and outfit,
keeping identity recognizable and garment structure clear.
Do not import another identity from B or any people, clothes, text, or props from C.
Avoid extra limbs, malformed hands, mixed garments, and substituted footwear.
```

In actual use, analyze the uploaded images before adding specific, supported descriptions. This example demonstrates role assignment; it does not claim analysis of real images. Review identity, outfit, and full-body framing after generation.

## Example 3: continuous product shots

### Input

```text
Please use $gubai-visual-foundry:
Create a three-shot storyboard for a fictional unbranded white diffuser bottle.
Target 3 seconds per shot, with a 9:16 frame.
Keep bottle shape, cap, blank label, and light-beige background consistent.
Show the whole bottle, a cap detail, and a closing whole-product view.
Output a shot table and prompts. Do not generate video yet.
```

### Sample storyboard

| Shot | Target duration | Action | Visible end state |
|---|---|---|---|
| 1 | 3 seconds | Camera slowly moves toward the stationary bottle | The entire bottle remains visible |
| 2 | 3 seconds | Slight lateral camera movement in a cap close-up | The cap connection is clearly visible |
| 3 | 3 seconds | Camera slowly moves back | The whole bottle is in frame with surrounding space |

### Sample shot prompts

```text
Shot 1: 9:16 product video, targeting 3 seconds. An unbranded white diffuser bottle remains still
against a light-beige background as the camera slowly moves closer. Preserve bottle shape,
cap, blank label, and soft side light. End with the entire bottle still visible.

Shot 2: 9:16 product video, targeting 3 seconds. Use the same bottle, light-beige background,
and soft side light. In a close-up of the cap and its connection, move the camera slightly sideways
while the bottle remains still. End with the cap connection clearly visible.

Shot 3: 9:16 product video, targeting 3 seconds. Use the same bottle, background, and light.
Move the camera slowly back from a medium product view. End with the entire bottle visible
and simple space around it.
```

Split shots according to tool capabilities and use supported durations. After confirming generated stills, use the corresponding approved frames as anchors for individual shots. Storyboard text alone does not guarantee drift-free video.
