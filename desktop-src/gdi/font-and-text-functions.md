---
Description: 'The following functions are used with fonts and text.'
ms.assetid: '69c04ed7-52da-4cb6-9fd2-f2a8c044df8b'
title: Font and Text Functions
---

# Font and Text Functions

The following functions are used with fonts and text.



| Function                                                   | Description                                                                                                          |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**AddFontMemResourceEx**](addfontmemresourceex.md)       | Adds an embedded font to the system font table.                                                                      |
| [**AddFontResource**](addfontresource.md)                 | Adds a font resource to the system font table.                                                                       |
| [**AddFontResourceEx**](addfontresourceex.md)             | Adds a private or non-enumerable font to the system font table.                                                      |
| [**CreateFont**](createfont.md)                           | Creates a logical font.                                                                                              |
| [**CreateFontIndirect**](createfontindirect.md)           | Creates a logical font from a structure.                                                                             |
| [**CreateFontIndirectEx**](createfontindirectex.md)       | Creates a logical font from a structure.                                                                             |
| [**DrawText**](drawtext.md)                               | Draws formatted text in a rectangle.                                                                                 |
| [**DrawTextEx**](drawtextex.md)                           | Draws formatted text in rectangle.                                                                                   |
| [**EnumFontFamExProc**](enumfontfamexproc.md)             | An application definedcallback function used with [**EnumFontFamiliesEx**](enumfontfamiliesex.md) to process fonts. |
| [**EnumFontFamiliesEx**](enumfontfamiliesex.md)           | Enumerates all fonts in the system with certain characteristics.                                                     |
| [**ExtTextOut**](exttextout.md)                           | Draws a character string.                                                                                            |
| [**GetAspectRatioFilterEx**](getaspectratiofilterex.md)   | Gets the setting for the aspect-ratio filter.                                                                        |
| [**GetCharABCWidths**](getcharabcwidths.md)               | Gets the widths of consecutive characters from the TrueType font.                                                    |
| [**GetCharABCWidthsFloat**](getcharabcwidthsfloat.md)     | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharABCWidthsI**](getcharabcwidthsi.md)             | Gets the widths of consecutive glyph indices or from an array of glyph indices from the TrueType font.               |
| [**GetCharacterPlacement**](getcharacterplacement.md)     | Gets information about a character string.                                                                           |
| [**GetCharWidth32**](getcharwidth32.md)                   | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharWidthFloat**](getcharwidthfloat.md)             | Gets the fractional widths of consecutive characters from the current font.                                          |
| [**GetCharWidthI**](getcharwidthi.md)                     | Gets the widths of consecutive glyph indices or an array of glyph indices from the current font.                     |
| [**GetFontData**](getfontdata.md)                         | Gets metric data for a TrueType font.                                                                                |
| [**GetFontLanguageInfo**](getfontlanguageinfo.md)         | Returns information about the selected font for a display context.                                                   |
| [**GetFontUnicodeRanges**](getfontunicoderanges.md)       | Tells which Unicode characters are supported by a font.                                                              |
| [**GetGlyphIndices**](getglyphindices.md)                 | Translates a string into an array of glyph indices.                                                                  |
| [**GetGlyphOutline**](getglyphoutline.md)                 | Gets the outline or bitmap for a character in the TrueType font.                                                     |
| [**GetKerningPairs**](getkerningpairs.md)                 | Gets the character-kerning pairs for a font.                                                                         |
| [**GetOutlineTextMetrics**](getoutlinetextmetrics.md)     | Gets text metrics for TrueType fonts.                                                                                |
| [**GetRasterizerCaps**](getrasterizercaps.md)             | Tells whether TrueType fonts are installed.                                                                          |
| [**GetTabbedTextExtent**](gettabbedtextextent.md)         | Computes the width and height of a character string, including tabs.                                                 |
| [**GetTextAlign**](gettextalign.md)                       | Gets the text-alignment setting for a device context.                                                                |
| [**GetTextCharacterExtra**](gettextcharacterextra.md)     | Gets the current intercharacter spacing for a device context.                                                        |
| [**GetTextColor**](gettextcolor.md)                       | Gets the text color for a device context.                                                                            |
| [**GetTextExtentExPoint**](gettextextentexpoint.md)       | Gets the number of characters in a string that will fit within a space.                                              |
| [**GetTextExtentExPointI**](gettextextentexpointi.md)     | Gets the number of glyph indices that will fit within a space.                                                       |
| [**GetTextExtentPoint32**](gettextextentpoint32.md)       | Computes the width and height of a string of text.                                                                   |
| [**GetTextExtentPointI**](gettextextentpointi.md)         | Computes the width and height of an array of glyph indices.                                                          |
| [**GetTextFace**](gettextface.md)                         | Gets the name of the font that is selected into a device context.                                                    |
| [**GetTextMetrics**](gettextmetrics.md)                   | Fills a buffer with the metrics for a font.                                                                          |
| [**PolyTextOut**](polytextout.md)                         | Draws several strings using the font and text colors in a device context.                                            |
| [**RemoveFontMemResourceEx**](removefontmemresourceex.md) | Removes a font whose source was embedded in a document from the system font table.                                   |
| [**RemoveFontResource**](removefontresource.md)           | Removes the fonts in a file from the system font table.                                                              |
| [**RemoveFontResourceEx**](removefontresourceex.md)       | Removes a private or non-enumerable font from the system font table.                                                 |
| [**SetMapperFlags**](setmapperflags.md)                   | Alters the algorithm used to map logical fonts to physical fonts.                                                    |
| [**SetTextAlign**](settextalign.md)                       | Sets the text-alignment flags for a device context.                                                                  |
| [**SetTextCharacterExtra**](settextcharacterextra.md)     | Sets the intercharacter spacing.                                                                                     |
| [**SetTextColor**](settextcolor.md)                       | Sets the text color for a device context.                                                                            |
| [**SetTextJustification**](settextjustification.md)       | Specifies the amount of space the system should add to the break characters in a string.                             |
| [**TabbedTextOut**](tabbedtextout.md)                     | Writes a character string at a location, expanding tabs to specified values.                                         |
| [**TextOut**](textout.md)                                 | Writes a character string at a location.                                                                             |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows.

-   [**CreateScalableFontResource**](createscalablefontresource.md)
-   [**EnumFontFamilies**](enumfontfamilies.md)
-   [**EnumFontFamProc**](enumfontfamproc.md)
-   [**EnumFonts**](enumfonts.md)
-   [**EnumFontsProc**](enumfontsproc.md)
-   [**GetCharWidth**](getcharwidth.md)
-   [**GetTextExtentPoint**](gettextextentpoint.md)

 

 



