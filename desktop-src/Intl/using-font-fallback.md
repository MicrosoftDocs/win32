---
description: Using Font Fallback
ms.assetid: 952f33b6-ca52-40a2-b914-52c1c62ae0e0
title: Using Font Fallback
ms.topic: article
ms.date: 05/31/2018
---

# Using Font Fallback

> [!Note]  
> In this topic, all remarks about [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) apply equally to [**ScriptShapeOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptshapeopentype).

 

Your application must use font fallback during text display if some characters in a string are not supported in the font, or if the application uses a [complex script](uniscribe-glossary.md) not supported by the font. The requirement for font fallback is detected during the layout process for text, when the application calls the [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) function. For information about text display, see [Displaying Text with Uniscribe](displaying-text-with-uniscribe.md).

## Determine the Need for Font Fallback for Unsupported Characters

If some of the characters in a string are not supported in a requested font, an application call to [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) succeeds. However, the application must scan the glyph output buffer for the presence of missing glyphs. The glyph index of the missing glyph can be determined for a specific font by calling [**ScriptGetFontProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontproperties). If a particular glyph is unavailable, the application must either fall back to a different font for a glyph or render a graphic symbol that indicates that no glyph is available.

## Determine the Need for Font Fallback for Unsupported Complex Scripts

The font that an application prefers for display might not support a complex script that is required by the text. In this case, the application call to [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) fails with the error code E\_SCRIPT\_NOT\_IN\_FONT.

## Assign a Fallback Font

Once it has determined that font fallback is required, the application must assign a fallback font. The application can try the following techniques:

-   Call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) for each font in a font list until one call has an acceptable return.
-   Call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) with each font in a list until it can be determined that no font will succeed. If the error code is always E\_SCRIPT\_NOT\_IN\_FONT, a complex script is not supported by the fonts. Either render a graphic symbol that indicates that no glyph is available, or re-specify the script as undefined (no script processing) and start again. To set the script as undefined, set the **eScript** member of the [**SCRIPT\_ANALYSIS**](/windows/win32/api/usp10/ns-usp10-script_analysis) structure to SCRIPT\_UNDEFINED.
-   Call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) with each font in a list until it can be determined that no font will succeed. If the error code indicates that some of the characters are mapping to missing glyphs, break up the string into smaller ranges. Different fonts can be assigned to subranges so that more of the characters can be rendered.

## Generate Glyph Information

Once the application has assigned a font that succeeds in calls to [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape), it can make calls to [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace) to generate glyph advance width and two-dimensional offset information from the output of **ScriptShape**. The font should succeed in these calls. A font failure in a call to **ScriptPlace** after success in a **ScriptShape** call indicates a broken font.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



