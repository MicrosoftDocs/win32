---
Description: 'This section describes functions for typography and for complex script processing.'
ms.assetid: '876e36f5-a91c-490b-87bd-b7cb4993f8c4'
title: Uniscribe Functions
---

# Uniscribe Functions

This section describes functions for typography and for complex script processing.



| Function                                                               | Description                                                                                                                                                                       |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ScriptApplyDigitSubstitution**](scriptapplydigitsubstitution.md)   | Applies the specified digit substitution settings to the specified script control and script state structures.                                                                    |
| [**ScriptApplyLogicalWidth**](scriptapplylogicalwidth.md)             | Takes an array of advance widths for a run and generates an array of adjusted advance glyph widths.                                                                               |
| [**ScriptBreak**](scriptbreak.md)                                     | Retrieves information for determining line breaks.                                                                                                                                |
| [**ScriptCacheGetHeight**](scriptcachegetheight.md)                   | Retrieves the height of the currently cached font.                                                                                                                                |
| [**ScriptCPtoX**](scriptcptox.md)                                     | Generates the x offset from the left end or leading edge of a run to either the leading or trailing edge of a logical character cluster.                                          |
| [**ScriptFreeCache**](scriptfreecache.md)                             | Frees a script cache.                                                                                                                                                             |
| [**ScriptGetCMap**](scriptgetcmap.md)                                 | Retrieves the glyph indexes of the Unicode characters in a string according to either the TrueType cmap table or the standard cmap table implemented for old-style fonts.         |
| [**ScriptGetFontAlternateGlyphs**](scriptgetfontalternateglyphs.md)   | Retrieves a list of alternate glyphs for a specified character that can be accessed through a specified OpenType feature.                                                         |
| [**ScriptGetFontFeatureTags**](scriptgetfontfeaturetags.md)           | Retrieves a list of typographic features for the defined writing system for OpenType processing.                                                                                  |
| [**ScriptGetFontLanguageTags**](scriptgetfontlanguagetags.md)         | Retrieves a list of language tags that are available for the specified item and are supported by a specified script tag for OpenType processing.                                  |
| [**ScriptGetFontProperties**](scriptgetfontproperties.md)             | Retrieves information from the font cache on the special glyphs used by a font.                                                                                                   |
| [**ScriptGetFontScriptTags**](scriptgetfontscripttags.md)             | Retrieves a list of scripts available in the font for OpenType processing.                                                                                                        |
| [**ScriptGetGlyphABCWidth**](scriptgetglyphabcwidth.md)               | Retrieves the ABC width of a given glyph.                                                                                                                                         |
| [**ScriptGetLogicalWidths**](scriptgetlogicalwidths.md)               | Converts the glyph advance widths for a specific font into logical widths.                                                                                                        |
| [**ScriptGetProperties**](scriptgetproperties.md)                     | Retrieves information about the current scripts.                                                                                                                                  |
| [**ScriptIsComplex**](scriptiscomplex.md)                             | Determines whether a Unicode string requires complex script processing.                                                                                                           |
| [**ScriptItemize**](scriptitemize.md)                                 | Breaks a Unicode string into individually shapeable items.                                                                                                                        |
| [**ScriptItemizeOpenType**](scriptitemizeopentype.md)                 | Breaks a Unicode string into individually shapeable items and provides an array of feature tags for each shapeable item for OpenType processing.                                  |
| [**ScriptJustify**](scriptjustify.md)                                 | Creates an advance widths table to allow text justification when passed to the [**ScriptTextOut**](scripttextout.md) function.                                                   |
| [**ScriptLayout**](scriptlayout.md)                                   | Converts an array of run embedding levels to a map of visual-to-logical position and/or logical-to-visual position.                                                               |
| [**ScriptPlace**](scriptplace.md)                                     | Generates glyph advance width and two-dimensional offset information from the output of [**ScriptShape**](scriptshape.md).                                                       |
| [**ScriptPlaceOpenType**](scriptplaceopentype.md)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information from the output of [**ScriptShapeOpenType**](scriptshapeopentype.md).                         |
| [**ScriptPositionSingleGlyph**](scriptpositionsingleglyph.md)         | Positions a single glyph with a single adjustment using a specified feature provided in the font for OpenType processing.                                                         |
| [**ScriptRecordDigitSubstitution**](scriptrecorddigitsubstitution.md) | Reads the National Language Support (NLS) native digit and digit substitution settings and records them in a [**SCRIPT\_DIGITSUBSTITUTE**](script-digitsubstitute.md) structure. |
| [**ScriptShape**](scriptshape.md)                                     | Generates glyphs and visual attributes for a Unicode run.                                                                                                                         |
| [**ScriptShapeOpenType**](scriptshapeopentype.md)                     | Generates glyphs and visual attributes for a Unicode run with OpenType information.                                                                                               |
| [**ScriptStringAnalyse**](scriptstringanalyse.md)                     | Analyzes a plain text string.                                                                                                                                                     |
| [**ScriptStringCPtoX**](scriptstringcptox.md)                         | Retrieves the x coordinate for the leading or trailing edge of a character position.                                                                                              |
| [**ScriptStringFree**](scriptstringfree.md)                           | Frees a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure.                                                                                                     |
| [**ScriptStringGetLogicalWidths**](scriptstringgetlogicalwidths.md)   | Converts visual widths into logical widths.                                                                                                                                       |
| [**ScriptStringGetOrder**](scriptstringgetorder.md)                   | Creates an array that maps an original character position to a glyph position.                                                                                                    |
| [**ScriptStringOut**](scriptstringout.md)                             | Displays a string generated by a prior call to [**ScriptStringAnalyse**](scriptstringanalyse.md) and optionally adds highlighting.                                               |
| [**ScriptString\_pcOutChars**](scriptstring-pcoutchars.md)            | Returns a pointer to the length of a string after clipping.                                                                                                                       |
| [**ScriptString\_pLogAttr**](scriptstring-plogattr.md)                | Returns a pointer to a logical attributes buffer for an analyzed string.                                                                                                          |
| [**ScriptString\_pSize**](scriptstring-psize.md)                      | Returns a pointer to a [**SIZE**](gdi.size) structure for an analyzed string.                                                                                                     |
| [**ScriptStringValidate**](scriptstringvalidate.md)                   | Checks a [**SCRIPT\_STRING\_ANALYSIS**](script-string-analysis.md) structure for invalid sequences.                                                                              |
| [**ScriptStringXtoCP**](scriptstringxtocp.md)                         | Converts an x coordinate to a character position.                                                                                                                                 |
| [**ScriptSubstituteSingleGlyph**](scriptsubstitutesingleglyph.md)     | Enables substitution of a single glyph with one alternate form of the same glyph for OpenType processing.                                                                         |
| [**ScriptTextOut**](scripttextout.md)                                 | Displays text for the specified script shape and place information.                                                                                                               |
| [**ScriptXtoCP**](scriptxtocp.md)                                     | Generates the leading or trailing edge of a logical character cluster from the x offset of a run.                                                                                 |



 

 

 



