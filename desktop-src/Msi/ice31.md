---
description: ICE31 validates any predefined font styles used in controls that display text. It also validates that the DefaultUIFont property refers to a valid font style.
ms.assetid: 07e60774-0e26-4a50-b818-a8f074512e3e
title: ICE31
ms.topic: article
ms.date: 05/31/2018
---

# ICE31

ICE31 validates any predefined font styles used in [controls](controls.md) that display text. It also validates that the [**DefaultUIFont**](defaultuifont.md) property refers to a valid font style.

Controls can have a predefined font style as described in [Adding Controls and Text](adding-controls-and-text.md). To set the font and font style of a text string, prefix the string of displayed characters with {\\style} or {&*style*}. Where style is an identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). If neither of these are present, but the [**DefaultUIFont**](defaultuifont.md) property is defined as a valid text style, that font will be used.

ICE31 checks the Text column for each control in the [Control Table](control-table.md) to verifies that a valid entry exist in the [TextStyle table](textstyle-table.md).

ICE31 ignores the [ScrollableText Control](scrollabletext-control.md).

## Results

ICE31 posts an error message for undefined styles, style names that are too long, a missing TextStyle table, and style tags with no closing brace.

ICE31 posts a warning if the style tag is not at the beginning of the line, or if a control has multiple style tags.

## Example

ICE31 posts the following errors for the example shown:

-   Control DialogB.Control1 uses undefined TextStyle BadStyle.
-   Control DialogB.Control2 uses undefined TextStyle BadStyle.
-   Control DialogB.Control6 is missing closing brace in text style.
-   Control DialogB.Control3 specifies a text style that is too long to be valid.

ICE31 posts the following warning for the example shown:

-   Text Style tag in DialogB.Control4 has no effect. Do you really want it to appear as text?

[Control Table](control-table.md) (partial)



| Dialog  | Control  | Text                                                                                                                                                                |
|---------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DialogA | Control0 | {\\OKStyle}This is the text to display.                                                                                                                             |
| DialogA | Control1 | {&OKStyle}This is the text to display.                                                                                                                              |
| DialogB | Control1 | {&BadStyle}This is the text to display.                                                                                                                             |
| DialogB | Control2 | {\\BadStyle}This is the text to display.                                                                                                                            |
| DialogB | Control3 | {&Style that is over 72 chars and therefore cannot possibly be a style even if somehow you did manage to get it in the TextStyle table}This is the text to display. |
| DialogB | Control4 | Warning {\\OKStyle}This is the text to display.                                                                                                                     |
| DialogB | Control5 | {\\OKStyle}{&OKStyle}This is the text to display.                                                                                                                   |
| DialogB | Control6 | {\\OKStyle This is the text to display.                                                                                                                             |



 

[TextStyle table](textstyle-table.md) (partial)



| TextStyle |
|-----------|
| OkStyle   |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



