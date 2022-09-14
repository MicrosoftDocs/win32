---
description: This section describes functions for typography and for complex script processing.
ms.assetid: 876e36f5-a91c-490b-87bd-b7cb4993f8c4
title: Uniscribe Functions
ms.topic: article
ms.date: 05/31/2018
---

# Uniscribe Functions

This section describes functions for typography and for complex script processing.



| Function                                                               | Description                                                                                                                                                                       |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ScriptApplyDigitSubstitution**](/windows/desktop/api/Usp10/nf-usp10-scriptapplydigitsubstitution)   | Applies the specified digit substitution settings to the specified script control and script state structures.                                                                    |
| [**ScriptApplyLogicalWidth**](/windows/desktop/api/Usp10/nf-usp10-scriptapplylogicalwidth)             | Takes an array of advance widths for a run and generates an array of adjusted advance glyph widths.                                                                               |
| [**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak)                                     | Retrieves information for determining line breaks.                                                                                                                                |
| [**ScriptCacheGetHeight**](/windows/desktop/api/Usp10/nf-usp10-scriptcachegetheight)                   | Retrieves the height of the currently cached font.                                                                                                                                |
| [**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox)                                     | Generates the x offset from the left end or leading edge of a run to either the leading or trailing edge of a logical character cluster.                                          |
| [**ScriptFreeCache**](/windows/desktop/api/Usp10/nf-usp10-scriptfreecache)                             | Frees a script cache.                                                                                                                                                             |
| [**ScriptGetCMap**](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap)                                 | Retrieves the glyph indexes of the Unicode characters in a string according to either the TrueType cmap table or the standard cmap table implemented for old-style fonts.         |
| [**ScriptGetFontAlternateGlyphs**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontalternateglyphs)   | Retrieves a list of alternate glyphs for a specified character that can be accessed through a specified OpenType feature.                                                         |
| [**ScriptGetFontFeatureTags**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontfeaturetags)           | Retrieves a list of typographic features for the defined writing system for OpenType processing.                                                                                  |
| [**ScriptGetFontLanguageTags**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontlanguagetags)         | Retrieves a list of language tags that are available for the specified item and are supported by a specified script tag for OpenType processing.                                  |
| [**ScriptGetFontProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontproperties)             | Retrieves information from the font cache on the special glyphs used by a font.                                                                                                   |
| [**ScriptGetFontScriptTags**](/windows/desktop/api/Usp10/nf-usp10-scriptgetfontscripttags)             | Retrieves a list of scripts available in the font for OpenType processing.                                                                                                        |
| [**ScriptGetGlyphABCWidth**](/windows/desktop/api/Usp10/nf-usp10-scriptgetglyphabcwidth)               | Retrieves the ABC width of a given glyph.                                                                                                                                         |
| [**ScriptGetLogicalWidths**](/windows/desktop/api/Usp10/nf-usp10-scriptgetlogicalwidths)               | Converts the glyph advance widths for a specific font into logical widths.                                                                                                        |
| [**ScriptGetProperties**](/windows/desktop/api/Usp10/nf-usp10-scriptgetproperties)                     | Retrieves information about the current scripts.                                                                                                                                  |
| [**ScriptIsComplex**](/windows/desktop/api/Usp10/nf-usp10-scriptiscomplex)                             | Determines whether a Unicode string requires complex script processing.                                                                                                           |
| [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize)                                 | Breaks a Unicode string into individually shapeable items.                                                                                                                        |
| [**ScriptItemizeOpenType**](/windows/desktop/api/usp10/nf-usp10-scriptitemizeopentype)                 | Breaks a Unicode string into individually shapeable items and provides an array of feature tags for each shapeable item for OpenType processing.                                  |
| [**ScriptJustify**](/windows/desktop/api/Usp10/nf-usp10-scriptjustify)                                 | Creates an advance widths table to allow text justification when passed to the [**ScriptTextOut**](/windows/desktop/api/Usp10/nf-usp10-scripttextout) function.                                                   |
| [**ScriptLayout**](/windows/desktop/api/Usp10/nf-usp10-scriptlayout)                                   | Converts an array of run embedding levels to a map of visual-to-logical position and/or logical-to-visual position.                                                               |
| [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace)                                     | Generates glyph advance width and two-dimensional offset information from the output of [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape).                                                       |
| [**ScriptPlaceOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptplaceopentype)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information from the output of [**ScriptShapeOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptshapeopentype).                         |
| [**ScriptPositionSingleGlyph**](/windows/desktop/api/Usp10/nf-usp10-scriptpositionsingleglyph)         | Positions a single glyph with a single adjustment using a specified feature provided in the font for OpenType processing.                                                         |
| [**ScriptRecordDigitSubstitution**](/windows/desktop/api/Usp10/nf-usp10-scriptrecorddigitsubstitution) | Reads the National Language Support (NLS) native digit and digit substitution settings and records them in a [**SCRIPT\_DIGITSUBSTITUTE**](/windows/win32/api/usp10/ns-usp10-script_digitsubstitute) structure. |
| [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape)                                     | Generates glyphs and visual attributes for a Unicode run.                                                                                                                         |
| [**ScriptShapeOpenType**](/windows/desktop/api/Usp10/nf-usp10-scriptshapeopentype)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information.                                                                                               |
| [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse)                     | Analyzes a plain text string.                                                                                                                                                     |
| [**ScriptStringCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptstringcptox)                         | Retrieves the x coordinate for the leading or trailing edge of a character position.                                                                                              |
| [**ScriptStringFree**](/windows/desktop/api/Usp10/nf-usp10-scriptstringfree)                           | Frees a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure.                                                                                                     |
| [**ScriptStringGetLogicalWidths**](/windows/desktop/api/Usp10/nf-usp10-scriptstringgetlogicalwidths)   | Converts visual widths into logical widths.                                                                                                                                       |
| [**ScriptStringGetOrder**](/windows/desktop/api/Usp10/nf-usp10-scriptstringgetorder)                   | Creates an array that maps an original character position to a glyph position.                                                                                                    |
| [**ScriptStringOut**](/windows/desktop/api/Usp10/nf-usp10-scriptstringout)                             | Displays a string generated by a prior call to [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse) and optionally adds highlighting.                                               |
| [**ScriptString\_pcOutChars**](/windows/desktop/api/Usp10/nf-usp10-scriptstring_pcoutchars)            | Returns a pointer to the length of a string after clipping.                                                                                                                       |
| [**ScriptString\_pLogAttr**](/windows/desktop/api/Usp10/nf-usp10-scriptstring_plogattr)                | Returns a pointer to a logical attributes buffer for an analyzed string.                                                                                                          |
| [**ScriptString\_pSize**](/windows/desktop/api/Usp10/nf-usp10-scriptstring_psize)                      | Returns a pointer to a [**SIZE**](/previous-versions//dd145106(v=vs.85)) structure for an analyzed string.                                                                                                     |
| [**ScriptStringValidate**](/windows/desktop/api/Usp10/nf-usp10-scriptstringvalidate)                   | Checks a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure for invalid sequences.                                                                              |
| [**ScriptStringXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptstringxtocp)                         | Converts an x coordinate to a character position.                                                                                                                                 |
| [**ScriptSubstituteSingleGlyph**](/windows/desktop/api/Usp10/nf-usp10-scriptsubstitutesingleglyph)     | Enables substitution of a single glyph with one alternate form of the same glyph for OpenType processing.                                                                         |
| [**ScriptTextOut**](/windows/desktop/api/Usp10/nf-usp10-scripttextout)                                 | Displays text for the specified script shape and place information.                                                                                                               |
| [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp)                                     | Generates the leading or trailing edge of a logical character cluster from the x offset of a run.                                                                                 |



 

 

 
