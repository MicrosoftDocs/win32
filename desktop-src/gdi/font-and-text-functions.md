---
Description: The following functions are used with fonts and text.
ms.assetid: 69c04ed7-52da-4cb6-9fd2-f2a8c044df8b
title: Font and Text Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Font and Text Functions

The following functions are used with fonts and text.



| Function                                                   | Description                                                                                                          |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**AddFontMemResourceEx**](/windows/win32/Wingdi/nf-wingdi-addfontmemresourceex?branch=master)       | Adds an embedded font to the system font table.                                                                      |
| [**AddFontResource**](/windows/win32/Wingdi/nf-wingdi-addfontresourcea?branch=master)                 | Adds a font resource to the system font table.                                                                       |
| [**AddFontResourceEx**](/windows/win32/Wingdi/nf-wingdi-addfontresourceexa?branch=master)             | Adds a private or non-enumerable font to the system font table.                                                      |
| [**CreateFont**](/windows/win32/Wingdi/nf-wingdi-createfonta?branch=master)                           | Creates a logical font.                                                                                              |
| [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master)           | Creates a logical font from a structure.                                                                             |
| [**CreateFontIndirectEx**](/windows/win32/Wingdi/nf-wingdi-createfontindirectexa?branch=master)       | Creates a logical font from a structure.                                                                             |
| [**DrawText**](/windows/win32/Winuser/nf-winuser-drawtext?branch=master)                               | Draws formatted text in a rectangle.                                                                                 |
| [**DrawTextEx**](/windows/win32/Winuser/nf-winuser-drawtextexa?branch=master)                           | Draws formatted text in rectangle.                                                                                   |
| [**EnumFontFamExProc**](/windows/win32/Wingdi/?branch=master)             | An application definedcallback function used with [**EnumFontFamiliesEx**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesexa?branch=master) to process fonts. |
| [**EnumFontFamiliesEx**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesexa?branch=master)           | Enumerates all fonts in the system with certain characteristics.                                                     |
| [**ExtTextOut**](/windows/win32/Wingdi/nf-wingdi-exttextouta?branch=master)                           | Draws a character string.                                                                                            |
| [**GetAspectRatioFilterEx**](/windows/win32/Wingdi/nf-wingdi-getaspectratiofilterex?branch=master)   | Gets the setting for the aspect-ratio filter.                                                                        |
| [**GetCharABCWidths**](/windows/win32/Wingdi/nf-wingdi-getcharabcwidthsa?branch=master)               | Gets the widths of consecutive characters from the TrueType font.                                                    |
| [**GetCharABCWidthsFloat**](/windows/win32/Wingdi/nf-wingdi-getcharabcwidthsfloata?branch=master)     | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharABCWidthsI**](/windows/win32/Wingdi/nf-wingdi-getcharabcwidthsi?branch=master)             | Gets the widths of consecutive glyph indices or from an array of glyph indices from the TrueType font.               |
| [**GetCharacterPlacement**](/windows/win32/Wingdi/nf-wingdi-getcharacterplacementa?branch=master)     | Gets information about a character string.                                                                           |
| [**GetCharWidth32**](/windows/win32/Wingdi/nf-wingdi-getcharwidth32a?branch=master)                   | Gets the widths of consecutive characters from the current font.                                                     |
| [**GetCharWidthFloat**](/windows/win32/Wingdi/nf-wingdi-getcharwidthfloata?branch=master)             | Gets the fractional widths of consecutive characters from the current font.                                          |
| [**GetCharWidthI**](/windows/win32/Wingdi/nf-wingdi-getcharwidthi?branch=master)                     | Gets the widths of consecutive glyph indices or an array of glyph indices from the current font.                     |
| [**GetFontData**](/windows/win32/Wingdi/nf-wingdi-getfontdata?branch=master)                         | Gets metric data for a TrueType font.                                                                                |
| [**GetFontLanguageInfo**](/windows/win32/Wingdi/nf-wingdi-getfontlanguageinfo?branch=master)         | Returns information about the selected font for a display context.                                                   |
| [**GetFontUnicodeRanges**](/windows/win32/Wingdi/nf-wingdi-getfontunicoderanges?branch=master)       | Tells which Unicode characters are supported by a font.                                                              |
| [**GetGlyphIndices**](/windows/win32/Wingdi/nf-wingdi-getglyphindicesa?branch=master)                 | Translates a string into an array of glyph indices.                                                                  |
| [**GetGlyphOutline**](/windows/win32/Wingdi/nf-wingdi-getglyphoutlinea?branch=master)                 | Gets the outline or bitmap for a character in the TrueType font.                                                     |
| [**GetKerningPairs**](/windows/win32/WinGdi/nf-wingdi-getkerningpairsa?branch=master)                 | Gets the character-kerning pairs for a font.                                                                         |
| [**GetOutlineTextMetrics**](/windows/win32/Wingdi/nf-wingdi-getoutlinetextmetricsa?branch=master)     | Gets text metrics for TrueType fonts.                                                                                |
| [**GetRasterizerCaps**](/windows/win32/Wingdi/nf-wingdi-getrasterizercaps?branch=master)             | Tells whether TrueType fonts are installed.                                                                          |
| [**GetTabbedTextExtent**](/windows/win32/Winuser/nf-winuser-gettabbedtextextenta?branch=master)         | Computes the width and height of a character string, including tabs.                                                 |
| [**GetTextAlign**](/windows/win32/Wingdi/nf-wingdi-gettextalign?branch=master)                       | Gets the text-alignment setting for a device context.                                                                |
| [**GetTextCharacterExtra**](/windows/win32/Wingdi/nf-wingdi-gettextcharacterextra?branch=master)     | Gets the current intercharacter spacing for a device context.                                                        |
| [**GetTextColor**](/windows/win32/Wingdi/nf-wingdi-gettextcolor?branch=master)                       | Gets the text color for a device context.                                                                            |
| [**GetTextExtentExPoint**](/windows/win32/Wingdi/nf-wingdi-gettextextentexpointa?branch=master)       | Gets the number of characters in a string that will fit within a space.                                              |
| [**GetTextExtentExPointI**](/windows/win32/Wingdi/nf-wingdi-gettextextentexpointi?branch=master)     | Gets the number of glyph indices that will fit within a space.                                                       |
| [**GetTextExtentPoint32**](/windows/win32/Wingdi/nf-wingdi-gettextextentpoint32a?branch=master)       | Computes the width and height of a string of text.                                                                   |
| [**GetTextExtentPointI**](/windows/win32/Wingdi/nf-wingdi-gettextextentpointi?branch=master)         | Computes the width and height of an array of glyph indices.                                                          |
| [**GetTextFace**](/windows/win32/Wingdi/nf-wingdi-gettextfacea?branch=master)                         | Gets the name of the font that is selected into a device context.                                                    |
| [**GetTextMetrics**](/windows/win32/Wingdi/nf-wingdi-gettextmetrics?branch=master)                   | Fills a buffer with the metrics for a font.                                                                          |
| [**PolyTextOut**](/windows/win32/Wingdi/nf-wingdi-polytextouta?branch=master)                         | Draws several strings using the font and text colors in a device context.                                            |
| [**RemoveFontMemResourceEx**](/windows/win32/Wingdi/nf-wingdi-removefontmemresourceex?branch=master) | Removes a font whose source was embedded in a document from the system font table.                                   |
| [**RemoveFontResource**](/windows/win32/Wingdi/nf-wingdi-removefontresourcea?branch=master)           | Removes the fonts in a file from the system font table.                                                              |
| [**RemoveFontResourceEx**](/windows/win32/Wingdi/nf-wingdi-removefontresourceexa?branch=master)       | Removes a private or non-enumerable font from the system font table.                                                 |
| [**SetMapperFlags**](/windows/win32/Wingdi/nf-wingdi-setmapperflags?branch=master)                   | Alters the algorithm used to map logical fonts to physical fonts.                                                    |
| [**SetTextAlign**](/windows/win32/Wingdi/nf-wingdi-settextalign?branch=master)                       | Sets the text-alignment flags for a device context.                                                                  |
| [**SetTextCharacterExtra**](/windows/win32/Wingdi/nf-wingdi-settextcharacterextra?branch=master)     | Sets the intercharacter spacing.                                                                                     |
| [**SetTextColor**](/windows/win32/Wingdi/nf-wingdi-settextcolor?branch=master)                       | Sets the text color for a device context.                                                                            |
| [**SetTextJustification**](/windows/win32/Wingdi/nf-wingdi-settextjustification?branch=master)       | Specifies the amount of space the system should add to the break characters in a string.                             |
| [**TabbedTextOut**](/windows/win32/Winuser/nf-winuser-tabbedtextouta?branch=master)                     | Writes a character string at a location, expanding tabs to specified values.                                         |
| [**TextOut**](/windows/win32/Wingdi/nf-wingdi-textouta?branch=master)                                 | Writes a character string at a location.                                                                             |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows.

-   [**CreateScalableFontResource**](/windows/win32/Wingdi/nf-wingdi-createscalablefontresourcea?branch=master)
-   [**EnumFontFamilies**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesa?branch=master)
-   [**EnumFontFamProc**](/windows/win32/Wingdi/?branch=master)
-   [**EnumFonts**](/windows/win32/Wingdi/nf-wingdi-enumfontsa?branch=master)
-   [**EnumFontsProc**](/windows/win32/Wingdi/?branch=master)
-   [**GetCharWidth**](/windows/win32/Wingdi/nf-wingdi-getcharwidtha?branch=master)
-   [**GetTextExtentPoint**](/windows/win32/WinGdi/nf-wingdi-gettextextentpointa?branch=master)

 

 



