---
Description: To provide text justification, an application can use one of two methods.
ms.assetid: 1190baed-5959-4f7a-8946-ac3b3da85821
title: Processing Complex Scripts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Processing Complex Scripts

To provide text justification, an application can use one of two methods. For a simple implementation of multilingual justification, the application should call [**ScriptJustify**](/windows/win32/Usp10/nf-usp10-scriptjustify?branch=master). It generates the delta dx array by considering kashida, then interword spacing, and then intercharacter spacing. For more sophisticated justification, the application can generate an updated delta dx array using its own language knowledge and the information retrieved by [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master) in the [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master) array.

Justification space or kashida should be inserted where identified by the **uJustification** member of [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master). When performing inter-character justification, the application should insert extra space only after glyphs marked with SCRIPT\_JUSTIFY\_CHARACTER.

The application does caret placement and hit testing by using [**ScriptXtoCP**](/windows/win32/Usp10/nf-usp10-scriptxtocp?branch=master) and [**ScriptCPtoX**](/windows/win32/Usp10/nf-usp10-scriptcptox?branch=master). For more information, see [Managing Caret Placement and Hit Testing](managing-caret-placement-and-hit-testing.md).

To get widths in a font-independent manner, the application calls [**ScriptGetLogicalWidths**](/windows/win32/Usp10/nf-usp10-scriptgetlogicalwidths?branch=master). By passing the logical widths to [**ScriptApplyLogicalWidth**](/windows/win32/Usp10/nf-usp10-scriptapplylogicalwidth?branch=master), a block of text can be redisplayed in the same boundaries with acceptable loss of quality even when the original font is not available. It generates an array of glyph widths ([advance widths](uniscribe-glossary.md#advance-width)) suitable for passing to [**ScriptTextOut**](/windows/win32/Usp10/nf-usp10-scripttextout?branch=master). Such recording and reapplying of advance width information in a font-independent manner can be useful in situations such as metafiling in an application defined format.

> [!Note]  
> Metafiles do not support glyph indexes. To write to an enhanced metafile, the application should use [**ExtTextOut**](gdi.exttextout) and write the logical characters directly. Using this mechanism, the glyph generation and placement does not occur until the text is played back.

 

To retrieve the specific glyphs that are used for the default, blanks, kashida, and so forth, for the current font, the application should call [**ScriptGetFontProperties**](/windows/win32/Usp10/nf-usp10-scriptgetfontproperties?branch=master). To determine which characters in a run are supported by the selected font, the application calls [**ScriptGetCMap**](/windows/win32/Usp10/nf-usp10-scriptgetcmap?branch=master). Characters that are not available have the default glyph in the glyph buffer. Note that this method fails if a font renders a character using a combination of glyphs instead of a single glyph. For example, 00C9; LATIN CAPITAL LETTER E WITH ACUTE can be rendered using a capital E glyph and an acute glyph. To determine the font support for a string that contains these kinds of code points, the application can call [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master). For more information, see [Using Shaping Engines](using-shaping-engines.md).

The [**ScriptCacheGetHeight**](/windows/win32/Usp10/nf-usp10-scriptcachegetheight?branch=master) function returns the height of the font from the font cache. [**ScriptGetProperties**](/windows/win32/Usp10/nf-usp10-scriptgetproperties?branch=master) provides information on the special processing required for all the scripts, indexed by script. For example, it includes the primary language associated with the script, data indicating if the script is numeric, and data indicating if the script is a complex script.

[**ScriptGetGlyphABCWidth**](/windows/win32/Usp10/nf-usp10-scriptgetglyphabcwidth?branch=master) returns the [ABC width](uniscribe-glossary.md#abc-width) of a given glyph, which might be useful for drawing glyph charts. However, it should not be used for normal complex script text formatting.

## Related Topics

[Using Uniscribe](using-uniscribe.md)


 

 



