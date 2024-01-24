---
description: Uniscribe uses multiple shaping engines that contain the layout knowledge for particular scripts.
ms.assetid: 3cdd18f3-51d3-4d1c-be31-f5709074cbe7
title: Using Shaping Engines
ms.topic: article
ms.date: 05/31/2018
---

# Using Shaping Engines

Uniscribe uses multiple shaping engines that contain the layout knowledge for particular scripts. It also takes advantage of the OpenType layout shaping engine for handling font-specific script features, such as glyph generation, extent measurement, and word-breaking support. Uniscribe manages bidirectional character reordering using the Unicode bidirectional algorithm, and understands non-OpenType layout font formats for Arabic, Hebrew, and Thai shaping.

Since the exact code point ranges assigned to each shaping engine might vary, script numbers are not published, with the exception of SCRIPT\_UNDEFINED. However, your application can test the attributes of scripts by calling the [**ScriptGetProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetproperties) function, which accesses the global script properties table. The application can use the global script properties to help combine its own layout rules with the required shaping engine divisions.

The application accesses a shaping engine with a call to the [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) function. All the complex script shaping engines, the digit shaping engines, and the ASCII shaping engines validate the font indicated in the device context handle before shaping. Complex scripts must be shaped using the script returned by the [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize) function in order to be legible. Other runs remain legible if shaped with SCRIPT\_UNDEFINED specified in the **eScript** member of the [**SCRIPT\_ANALYSIS**](/windows/win32/api/usp10/ns-usp10-script_analysis) structure, although they might lose typographic quality.

[**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) returns 0 if successful, or USP\_E\_SCRIPT\_NOT\_IN\_FONT if the font supplied by the application does not contain sufficient glyphs or shaping tables. If the application specifies SCRIPT\_UNDEFINED and some characters are not supported by the font, the function still succeeds. In this case, the application should scan the glyph output buffer for the presence of missing glyphs. For strategies to deal with missing glyphs, see [Using Font Fallback](using-font-fallback.md).

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



