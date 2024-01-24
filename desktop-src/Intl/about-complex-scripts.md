---
description: A complex script is a script for which the fComplex member of SCRIPT\_PROPERTIES is set to TRUE. This topic details the properties that a complex script might have.
ms.assetid: bceeb0d6-bda3-43bf-984e-87fbfb327578
title: About Complex Scripts
ms.topic: article
ms.date: 05/31/2018
---

# About Complex Scripts

A [complex script](uniscribe-glossary.md) is a script for which the **fComplex** member of [**SCRIPT\_PROPERTIES**](/windows/desktop/api/Usp10/ns-usp10-script_properties) is set to **TRUE**. This topic details the properties that a complex script might have.

## Bidirectional Rendering

Bidirectional rendering is handling of text that reads both left-to-right and right-to-left. For example, in the bidirectional rendering of Arabic, the default reading direction for text is right-to-left, but it is left-to-right for some numbers. Processing a complex script must account for the difference between the logical (keystroke) order and the visual order of the glyphs. In addition, processing must properly deal with caret movement and hit testing. The mapping between screen position and a character index requires an understanding of the layout algorithms for the particular display, for example, selection of text or caret display.

## Contextual Shaping

In contextual shaping, script characters change shape depending on the characters that surround them. Such shaping occurs in English cursive writing when a lowercase "l" changes shape depending on the character that precedes it, such as an "a" (connects low to the "l") or an "o" (connects high). For example, Arabic is a script that exhibits contextual shaping.

## Combining Characters

Combining characters, also called "ligatures," are characters that join into one character when placed together. Arabic is a script that has many combining characters. One example of the use of combining characters is the "a" followed by "combining grave", for which the rendered representation is "à". The Unicode stream "U+0061 U+0300" requires some processing to make sure the "combining grave" is correctly positioned above the "a".

## Specialized Word Break and Justification

Some scripts, for example, Thai, have complex rules for dividing words between lines or justifying text on a line.

## Filtering for Illegal Character Combinations

A complex script, for example, Thai, can filter out illegal character combinations when a language does not allow certain character combinations.

## Font Fallback

Font fallback is the automated selection of a font other than the font selected by the user. In Uniscribe, font fallback is applied by the [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse) function when all or part of the text is in a script that the user-selected font does not support. For more information, see [Using Font Fallback](using-font-fallback.md).

## Related topics

<dl> <dt>

[About Uniscribe](about-uniscribe.md)
</dt> </dl>

 

 



