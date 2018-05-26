---
title: Text Metrics
description: In order to assist your layout, custom font selection, and other metric intensive operations, starting in Windows 8, DirectWrite has a number of new APIs to express all the info about fonts that you might require to develop rich text apps.
ms.assetid: 4524ace3-fca6-4daf-9ecb-516771e53fc9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Text Metrics

In order to assist your layout, custom font selection, and other metric intensive operations, starting in Windows 8, [DirectWrite](direct-write-portal.md) has a number of new APIs to express all the info about fonts that you might require to develop rich text apps.

## PANOSE

PANOSE is a visual classification system for identifying typefaces. The PANOSE classification contains info on the family, serif style, weight, proportion, contrast, stroke, arm style, X-height, etc. This info describes the visual style of the font. This info is important because fonts with similar PANOSE values look similar. This is very useful in situations where a font isn’t available and the app needs to fall back to a font that’s available. Comparing PANOSE values for fonts allows you to choose a font that’s similar visually to the original font.

In order to access the PANOSE info for a font, use the [**GetPanose**](/windows/win32/dwrite_1/?branch=master) method on the [**IDWriteFont1**](/windows/win32/dwrite_1/?branch=master) and [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) interfaces. This method returns a [**DWRITE\_PANOSE**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_panose?branch=master) enumeration that contains all of the PANOSE info for that font.

## Additional Metrics

Starting in Windows 8, the [DirectWrite](direct-write-portal.md) API also supports a number of new metrics in order to express useful info about the fonts to your app. These new metrics include this info.

-   Left, Right, Top, and Bottom glyph bounding box metrics.
-   X and Y positioning for superscript and subscript elements.
-   X and Y scaling info for superscript and subscript elements.
-   Whether or not the font has typographic metrics.

This info is all available through the new [**GetMetrics**](/windows/win32/dwrite_1/?branch=master) method on the [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) and [**IDWriteFont1**](/windows/win32/dwrite_1/?branch=master) interfaces. This method returns a [**DWRITE\_FONT\_METRICS1**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_font_metrics1?branch=master) structure that contains all this info.

## Caret Metrics

To create text editing apps you need access to info about how to draw the caret that navigates through the text. Starting in Windows 8, [DirectWrite](direct-write-portal.md) provides the [**GetCaretMetrics**](/windows/win32/dwrite_1/?branch=master) method on the [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) and [**IDWriteFont1**](/windows/win32/dwrite_1/?branch=master) interfaces for this scenario. **GetCaretMetrics** returns a [**DWRITE\_CARET\_METRICS**](/windows/win32/Dwrite_1/ns-dwrite_1-dwrite_caret_metrics?branch=master) enumeration which contains info about the slope and offset for the caret along the baseline.

This info is specifically helpful if you want to be able to have their caret slope appropriately with italic text.

## Monospaced Discoverability

Apps that allow your users to write computer code often use monospaced fonts in place of more traditional fonts. So you can have more control over font selection in apps related to development, [DirectWrite](direct-write-portal.md) expresses whether or not a font is monospaced through the API. The [**IsMonospacedFont**](/windows/win32/dwrite_1/?branch=master) method on the [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) interface returns a Boolean that indicates whether or not the font is monospaced.

## Font Name Matching

Rich text apps like PDF readers need to be able to match fonts in their content to fonts on the system, need access to the full names of fonts in multiple formats. So you can better match fonts, [DirectWrite](direct-write-portal.md) contains an enumeration that expresses full naming info about a font in many formats.

you use the [**DWRITE\_INFORMATIONAL\_STRING\_ID**](/windows/win32/dwrite/ne-dwrite-dwrite_informational_string_id?branch=master) enumeration to get the full name, PostScript name, and PostScript CID name of any font on the system. This info is valuable when you need to match fonts in your app to appropriate fonts on the local system.

## Glyph Advances

The **GetGlyphAdvances** method on the [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) and [**IDWriteFont1**](/windows/win32/dwrite_1/?branch=master) interfaces takes in the glyph count and indices that you need advances info about and then returns the advances for the glyphs in question.

## Unicode Ranges

Apps that want to handle their own font selection need access to the Unicode ranges that are supported by the font. This way, if a Unicode codepoint isn’t supported by the font, the app can choose an appropriate font that contains that glyph. Without this info, the app may use a font that doesn’t contain all the glyphs that are necessary to display the info present.

The [**GetUnicodeRanges**](/windows/win32/dwrite_1/?branch=master) method on the the [**IDWriteFontFace1**](/windows/win32/dwrite_1/?branch=master) and [**IDWriteFont1**](/windows/win32/dwrite_1/?branch=master) interfaces takes in the maximum number of ranges passed in from the client, and returns the actual ranges supported by the font.

## EUDC Font Collection

Use the [**GetEudcFontCollection**](/windows/win32/dwrite_1/?branch=master) method on the [**IDWriteFactory1**](/windows/win32/dwrite_1/?branch=master) interface access the EUDC font collection. This method works in the same way as [**GetSystemFontCollection**](/windows/win32/dwrite/?branch=master), but instead returns a pointer to an EUDC font collection.

 

 




