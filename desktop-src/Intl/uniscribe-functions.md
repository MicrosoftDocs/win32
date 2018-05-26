---
Description: This section describes functions for typography and for complex script processing.
ms.assetid: 876e36f5-a91c-490b-87bd-b7cb4993f8c4
title: Uniscribe Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Uniscribe Functions

This section describes functions for typography and for complex script processing.



| Function                                                               | Description                                                                                                                                                                       |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ScriptApplyDigitSubstitution**](/windows/win32/Usp10/nf-usp10-scriptapplydigitsubstitution?branch=master)   | Applies the specified digit substitution settings to the specified script control and script state structures.                                                                    |
| [**ScriptApplyLogicalWidth**](/windows/win32/Usp10/nf-usp10-scriptapplylogicalwidth?branch=master)             | Takes an array of advance widths for a run and generates an array of adjusted advance glyph widths.                                                                               |
| [**ScriptBreak**](/windows/win32/Usp10/nf-usp10-scriptbreak?branch=master)                                     | Retrieves information for determining line breaks.                                                                                                                                |
| [**ScriptCacheGetHeight**](/windows/win32/Usp10/nf-usp10-scriptcachegetheight?branch=master)                   | Retrieves the height of the currently cached font.                                                                                                                                |
| [**ScriptCPtoX**](/windows/win32/Usp10/nf-usp10-scriptcptox?branch=master)                                     | Generates the x offset from the left end or leading edge of a run to either the leading or trailing edge of a logical character cluster.                                          |
| [**ScriptFreeCache**](/windows/win32/Usp10/nf-usp10-scriptfreecache?branch=master)                             | Frees a script cache.                                                                                                                                                             |
| [**ScriptGetCMap**](/windows/win32/Usp10/nf-usp10-scriptgetcmap?branch=master)                                 | Retrieves the glyph indexes of the Unicode characters in a string according to either the TrueType cmap table or the standard cmap table implemented for old-style fonts.         |
| [**ScriptGetFontAlternateGlyphs**](/windows/win32/Usp10/nf-usp10-scriptgetfontalternateglyphs?branch=master)   | Retrieves a list of alternate glyphs for a specified character that can be accessed through a specified OpenType feature.                                                         |
| [**ScriptGetFontFeatureTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontfeaturetags?branch=master)           | Retrieves a list of typographic features for the defined writing system for OpenType processing.                                                                                  |
| [**ScriptGetFontLanguageTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontlanguagetags?branch=master)         | Retrieves a list of language tags that are available for the specified item and are supported by a specified script tag for OpenType processing.                                  |
| [**ScriptGetFontProperties**](/windows/win32/Usp10/nf-usp10-scriptgetfontproperties?branch=master)             | Retrieves information from the font cache on the special glyphs used by a font.                                                                                                   |
| [**ScriptGetFontScriptTags**](/windows/win32/Usp10/nf-usp10-scriptgetfontscripttags?branch=master)             | Retrieves a list of scripts available in the font for OpenType processing.                                                                                                        |
| [**ScriptGetGlyphABCWidth**](/windows/win32/Usp10/nf-usp10-scriptgetglyphabcwidth?branch=master)               | Retrieves the ABC width of a given glyph.                                                                                                                                         |
| [**ScriptGetLogicalWidths**](/windows/win32/Usp10/nf-usp10-scriptgetlogicalwidths?branch=master)               | Converts the glyph advance widths for a specific font into logical widths.                                                                                                        |
| [**ScriptGetProperties**](/windows/win32/Usp10/nf-usp10-scriptgetproperties?branch=master)                     | Retrieves information about the current scripts.                                                                                                                                  |
| [**ScriptIsComplex**](/windows/win32/Usp10/nf-usp10-scriptiscomplex?branch=master)                             | Determines whether a Unicode string requires complex script processing.                                                                                                           |
| [**ScriptItemize**](/windows/win32/Usp10/nf-usp10-scriptitemize?branch=master)                                 | Breaks a Unicode string into individually shapeable items.                                                                                                                        |
| [**ScriptItemizeOpenType**](/windows/win32/usp10/nf-usp10-scriptitemizeopentype?branch=master)                 | Breaks a Unicode string into individually shapeable items and provides an array of feature tags for each shapeable item for OpenType processing.                                  |
| [**ScriptJustify**](/windows/win32/Usp10/nf-usp10-scriptjustify?branch=master)                                 | Creates an advance widths table to allow text justification when passed to the [**ScriptTextOut**](/windows/win32/Usp10/nf-usp10-scripttextout?branch=master) function.                                                   |
| [**ScriptLayout**](/windows/win32/Usp10/nf-usp10-scriptlayout?branch=master)                                   | Converts an array of run embedding levels to a map of visual-to-logical position and/or logical-to-visual position.                                                               |
| [**ScriptPlace**](/windows/win32/Usp10/nf-usp10-scriptplace?branch=master)                                     | Generates glyph advance width and two-dimensional offset information from the output of [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master).                                                       |
| [**ScriptPlaceOpenType**](/windows/win32/Usp10/nf-usp10-scriptplaceopentype?branch=master)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information from the output of [**ScriptShapeOpenType**](/windows/win32/Usp10/nf-usp10-scriptshapeopentype?branch=master).                         |
| [**ScriptPositionSingleGlyph**](/windows/win32/Usp10/nf-usp10-scriptpositionsingleglyph?branch=master)         | Positions a single glyph with a single adjustment using a specified feature provided in the font for OpenType processing.                                                         |
| [**ScriptRecordDigitSubstitution**](/windows/win32/Usp10/nf-usp10-scriptrecorddigitsubstitution?branch=master) | Reads the National Language Support (NLS) native digit and digit substitution settings and records them in a [**SCRIPT\_DIGITSUBSTITUTE**](/windows/win32/Usp10/ns-usp10-tag_script_digitsubstitute?branch=master) structure. |
| [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master)                                     | Generates glyphs and visual attributes for a Unicode run.                                                                                                                         |
| [**ScriptShapeOpenType**](/windows/win32/Usp10/nf-usp10-scriptshapeopentype?branch=master)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information.                                                                                               |
| [**ScriptStringAnalyse**](/windows/win32/Usp10/nf-usp10-scriptstringanalyse?branch=master)                     | Analyzes a plain text string.                                                                                                                                                     |
| [**ScriptStringCPtoX**](/windows/win32/Usp10/nf-usp10-scriptstringcptox?branch=master)                         | Retrieves the x coordinate for the leading or trailing edge of a character position.                                                                                              |
| [**ScriptStringFree**](/windows/win32/Usp10/nf-usp10-scriptstringfree?branch=master)                           | Frees a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure.                                                                                                     |
| [**ScriptStringGetLogicalWidths**](/windows/win32/Usp10/nf-usp10-scriptstringgetlogicalwidths?branch=master)   | Converts visual widths into logical widths.                                                                                                                                       |
| [**ScriptStringGetOrder**](/windows/win32/Usp10/nf-usp10-scriptstringgetorder?branch=master)                   | Creates an array that maps an original character position to a glyph position.                                                                                                    |
| [**ScriptStringOut**](/windows/win32/Usp10/nf-usp10-scriptstringout?branch=master)                             | Displays a string generated by a prior call to [**ScriptStringAnalyse**](/windows/win32/Usp10/nf-usp10-scriptstringanalyse?branch=master) and optionally adds highlighting.                                               |
| [**ScriptString\_pcOutChars**](/windows/win32/Usp10/nf-usp10-scriptstring_pcoutchars?branch=master)            | Returns a pointer to the length of a string after clipping.                                                                                                                       |
| [**ScriptString\_pLogAttr**](/windows/win32/Usp10/nf-usp10-scriptstring_plogattr?branch=master)                | Returns a pointer to a logical attributes buffer for an analyzed string.                                                                                                          |
| [**ScriptString\_pSize**](/windows/win32/Usp10/nf-usp10-scriptstring_psize?branch=master)                      | Returns a pointer to a [**SIZE**](gdi.size) structure for an analyzed string.                                                                                                     |
| [**ScriptStringValidate**](/windows/win32/Usp10/nf-usp10-scriptstringvalidate?branch=master)                   | Checks a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure for invalid sequences.                                                                              |
| [**ScriptStringXtoCP**](/windows/win32/Usp10/nf-usp10-scriptstringxtocp?branch=master)                         | Converts an x coordinate to a character position.                                                                                                                                 |
| [**ScriptSubstituteSingleGlyph**](/windows/win32/Usp10/nf-usp10-scriptsubstitutesingleglyph?branch=master)     | Enables substitution of a single glyph with one alternate form of the same glyph for OpenType processing.                                                                         |
| [**ScriptTextOut**](/windows/win32/Usp10/nf-usp10-scripttextout?branch=master)                                 | Displays text for the specified script shape and place information.                                                                                                               |
| [**ScriptXtoCP**](/windows/win32/Usp10/nf-usp10-scriptxtocp?branch=master)                                     | Generates the leading or trailing edge of a logical character cluster from the x offset of a run.                                                                                 |



 

 

 



