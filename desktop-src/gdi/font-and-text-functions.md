---
description: The following functions are used with fonts and text.
ms.assetid: 69c04ed7-52da-4cb6-9fd2-f2a8c044df8b
title: Font and Text Functions (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Font and Text Functions (Windows GDI)

The following functions are used with fonts and text.



| Function                                                   | Description                                                                                                          |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**AddFontMemResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-addfontmemresourceex)       | Adds an embedded font to the system font table.                                                                      |
| [**AddFontResource**](/windows/desktop/api/Wingdi/nf-wingdi-addfontresourcea)                 | Adds a font resource to the system font table.                                                                       |
| [**AddFontResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-addfontresourceexa)             | Adds a private or non-enumerable font to the system font table.                                                      |
| [**CreateFont**](/windows/desktop/api/Wingdi/nf-wingdi-createfonta)                           | Creates a logical font.                                                                                              |
| [**CreateFontIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createfontindirecta)           | Creates a logical font from a structure.                                                                             |
| [**CreateFontIndirectEx**](/windows/desktop/api/Wingdi/nf-wingdi-createfontindirectexa)       | Creates a logical font from a structure.                                                                             |
| [**DrawText**](/windows/desktop/api/Winuser/nf-winuser-drawtext)                               | Draws formatted text in a rectangle.                                                                                 |
| [**DrawTextEx**](/windows/desktop/api/Winuser/nf-winuser-drawtextexa)                           | Draws formatted text in rectangle.                                                                                   |
| [**EnumFontFamExProc**](/previous-versions//dd162618(v=vs.85))             | An application definedcallback function used with [**EnumFontFamiliesEx**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesexa) to process fonts. |
| [**EnumFontFamiliesEx**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesexa)           | Enumerates all fonts in the system with certain characteristics.                                                     |
| [**ExtTextOut**](/windows/desktop/api/Wingdi/nf-wingdi-exttextouta)                           | Draws a character string.                                                                                            |
| [**GetAspectRatioFilterEx**](/windows/desktop/api/Wingdi/nf-wingdi-getaspectratiofilterex)   | Gets the setting for the aspect-ratio filter.                                                                        |
| [**GetCharABCWidths**](/windows/desktop/api/Wingdi/nf-wingdi-getcharabcwidthsa)               | Gets the widths of consecutive characters from the TrueType font.                                                    |
| [**GetCharABCWidthsFloat**](/windows/desktop/api/Wingdi/nf-wingdi-getcharabcwidthsfloata)     | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharABCWidthsI**](/windows/desktop/api/Wingdi/nf-wingdi-getcharabcwidthsi)             | Gets the widths of consecutive glyph indices or from an array of glyph indices from the TrueType font.               |
| [**GetCharacterPlacement**](/windows/desktop/api/Wingdi/nf-wingdi-getcharacterplacementa)     | Gets information about a character string.                                                                           |
| [**GetCharWidth32**](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidth32a)                   | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharWidthFloat**](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidthfloata)             | Gets the fractional widths of consecutive characters from the current font.                                          |
| [**GetCharWidthI**](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidthi)                     | Gets the widths of consecutive glyph indices or an array of glyph indices from the current font.                     |
| [**GetFontData**](/windows/desktop/api/Wingdi/nf-wingdi-getfontdata)                         | Gets metric data for a TrueType font.                                                                                |
| [**GetFontLanguageInfo**](/windows/desktop/api/Wingdi/nf-wingdi-getfontlanguageinfo)         | Returns information about the selected font for a display context.                                                   |
| [**GetFontUnicodeRanges**](/windows/desktop/api/Wingdi/nf-wingdi-getfontunicoderanges)       | Tells which Unicode characters are supported by a font.                                                              |
| [**GetGlyphIndices**](/windows/desktop/api/Wingdi/nf-wingdi-getglyphindicesa)                 | Translates a string into an array of glyph indices.                                                                  |
| [**GetGlyphOutline**](/windows/desktop/api/Wingdi/nf-wingdi-getglyphoutlinea)                 | Gets the outline or bitmap for a character in the TrueType font.                                                     |
| [**GetKerningPairs**](/windows/desktop/api/WinGdi/nf-wingdi-getkerningpairsa)                 | Gets the character-kerning pairs for a font.                                                                         |
| [**GetOutlineTextMetrics**](/windows/desktop/api/Wingdi/nf-wingdi-getoutlinetextmetricsa)     | Gets text metrics for TrueType fonts.                                                                                |
| [**GetRasterizerCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getrasterizercaps)             | Tells whether TrueType fonts are installed.                                                                          |
| [**GetTabbedTextExtent**](/windows/desktop/api/Winuser/nf-winuser-gettabbedtextextenta)         | Computes the width and height of a character string, including tabs.                                                 |
| [**GetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-gettextalign)                       | Gets the text-alignment setting for a device context.                                                                |
| [**GetTextCharacterExtra**](/windows/desktop/api/Wingdi/nf-wingdi-gettextcharacterextra)     | Gets the current intercharacter spacing for a device context.                                                        |
| [**GetTextColor**](/windows/desktop/api/Wingdi/nf-wingdi-gettextcolor)                       | Gets the text color for a device context.                                                                            |
| [**GetTextExtentExPoint**](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentexpointa)       | Gets the number of characters in a string that will fit within a space.                                              |
| [**GetTextExtentExPointI**](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentexpointi)     | Gets the number of glyph indices that will fit within a space.                                                       |
| [**GetTextExtentPoint32**](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentpoint32a)       | Computes the width and height of a string of text.                                                                   |
| [**GetTextExtentPointI**](/windows/desktop/api/Wingdi/nf-wingdi-gettextextentpointi)         | Computes the width and height of an array of glyph indices.                                                          |
| [**GetTextFace**](/windows/desktop/api/Wingdi/nf-wingdi-gettextfacea)                         | Gets the name of the font that is selected into a device context.                                                    |
| [**GetTextMetrics**](/windows/desktop/api/Wingdi/nf-wingdi-gettextmetrics)                   | Fills a buffer with the metrics for a font.                                                                          |
| [**PolyTextOut**](/windows/desktop/api/Wingdi/nf-wingdi-polytextouta)                         | Draws several strings using the font and text colors in a device context.                                            |
| [**RemoveFontMemResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-removefontmemresourceex) | Removes a font whose source was embedded in a document from the system font table.                                   |
| [**RemoveFontResource**](/windows/desktop/api/Wingdi/nf-wingdi-removefontresourcea)           | Removes the fonts in a file from the system font table.                                                              |
| [**RemoveFontResourceEx**](/windows/desktop/api/Wingdi/nf-wingdi-removefontresourceexa)       | Removes a private or non-enumerable font from the system font table.                                                 |
| [**SetMapperFlags**](/windows/desktop/api/Wingdi/nf-wingdi-setmapperflags)                   | Alters the algorithm used to map logical fonts to physical fonts.                                                    |
| [**SetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-settextalign)                       | Sets the text-alignment flags for a device context.                                                                  |
| [**SetTextCharacterExtra**](/windows/desktop/api/Wingdi/nf-wingdi-settextcharacterextra)     | Sets the intercharacter spacing.                                                                                     |
| [**SetTextColor**](/windows/desktop/api/Wingdi/nf-wingdi-settextcolor)                       | Sets the text color for a device context.                                                                            |
| [**SetTextJustification**](/windows/desktop/api/Wingdi/nf-wingdi-settextjustification)       | Specifies the amount of space the system should add to the break characters in a string.                             |
| [**TabbedTextOut**](/windows/desktop/api/Winuser/nf-winuser-tabbedtextouta)                     | Writes a character string at a location, expanding tabs to specified values.                                         |
| [**TextOut**](/windows/desktop/api/Wingdi/nf-wingdi-textouta)                                 | Writes a character string at a location.                                                                             |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows.

-   [**CreateScalableFontResource**](/windows/desktop/api/Wingdi/nf-wingdi-createscalablefontresourcea)
-   [**EnumFontFamilies**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa)
-   [**EnumFontFamProc**](/previous-versions//dd162621(v=vs.85))
-   [**EnumFonts**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontsa)
-   [**EnumFontsProc**](/previous-versions//dd162623(v=vs.85))
-   [**GetCharWidth**](/windows/desktop/api/Wingdi/nf-wingdi-getcharwidtha)
-   [**GetTextExtentPoint**](/windows/desktop/api/WinGdi/nf-wingdi-gettextextentpointa)

 

 
