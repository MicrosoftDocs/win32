---
description: To provide text justification, an application can use one of two methods.
ms.assetid: 1190baed-5959-4f7a-8946-ac3b3da85821
title: Processing Complex Scripts
ms.topic: article
ms.date: 05/31/2018
---

# Processing Complex Scripts

To provide text justification, an application can use one of two methods. For a simple implementation of multilingual justification, the application should call [**ScriptJustify**](/windows/desktop/api/Usp10/nf-usp10-scriptjustify). It generates the delta dx array by considering kashida, then interword spacing, and then intercharacter spacing. For more sophisticated justification, the application can generate an updated delta dx array using its own language knowledge and the information retrieved by [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) in the [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr) array.

Justification space or kashida should be inserted where identified by the **uJustification** member of [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr). When performing inter-character justification, the application should insert extra space only after glyphs marked with SCRIPT\_JUSTIFY\_CHARACTER.

The application does caret placement and hit testing by using [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) and [**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox). For more information, see [Managing Caret Placement and Hit Testing](managing-caret-placement-and-hit-testing.md).

To get widths in a font-independent manner, the application calls [**ScriptGetLogicalWidths**](/windows/desktop/api/Usp10/nf-usp10-scriptgetlogicalwidths). By passing the logical widths to [**ScriptApplyLogicalWidth**](/windows/desktop/api/Usp10/nf-usp10-scriptapplylogicalwidth), a block of text can be redisplayed in the same boundaries with acceptable loss of quality even when the original font is not available. It generates an array of glyph widths ([advance widths](uniscribe-glossary.md)) suitable for passing to [**ScriptTextOut**](/windows/desktop/api/Usp10/nf-usp10-scripttextout). Such recording and reapplying of advance width information in a font-independent manner can be useful in situations such as metafiling in an application defined format.

> [!Note]  
> Metafiles do not support glyph indexes. To write to an enhanced metafile, the application should use [**ExtTextOut**](/windows/win32/api/wingdi/nf-wingdi-exttextouta) and write the logical characters directly. Using this mechanism, the glyph generation and placement does not occur until the text is played back.

 

To retrieve the specific glyphs that are used for the default, blanks, kashida, and so forth, for the current font, the application should call [**ScriptGetFontProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontproperties). To determine which characters in a run are supported by the selected font, the application calls [**ScriptGetCMap**](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap). Characters that are not available have the default glyph in the glyph buffer. Note that this method fails if a font renders a character using a combination of glyphs instead of a single glyph. For example, 00C9; LATIN CAPITAL LETTER E WITH ACUTE can be rendered using a capital E glyph and an acute glyph. To determine the font support for a string that contains these kinds of code points, the application can call [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape). For more information, see [Using Shaping Engines](using-shaping-engines.md).

The [**ScriptCacheGetHeight**](/windows/desktop/api/Usp10/nf-usp10-scriptcachegetheight) function returns the height of the font from the font cache. [**ScriptGetProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetproperties) provides information on the special processing required for all the scripts, indexed by script. For example, it includes the primary language associated with the script, data indicating if the script is numeric, and data indicating if the script is a complex script.

[**ScriptGetGlyphABCWidth**](/windows/desktop/api/Usp10/nf-usp10-scriptgetglyphabcwidth) returns the [ABC width](uniscribe-glossary.md) of a given glyph, which might be useful for drawing glyph charts. However, it should not be used for normal complex script text formatting.

## Related Topics

[Using Uniscribe](using-uniscribe.md)


 

 
