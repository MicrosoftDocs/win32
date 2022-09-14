---
title: Fonts and text metrics
description: This topic discusses the outline fonts provided by Windows, font metric values that may change between versions of Windows, and guidance for how to use font metrics in your desktop apps.
ms.assetid: B195154D-0168-4C5E-9CFB-AE7EF63D5F42
ms.topic: article
ms.date: 05/31/2018
---

# Fonts and text metrics

This topic discusses the outline fonts provided by Windows, font metric values that may change between versions of Windows, and guidance for how to use font metrics in your desktop apps.

-   For info specific to font metrics in DirectWrite, see [Text Metrics](/windows/desktop/DirectWrite/text-metrics).
-   For details on managing text in apps using GDI, see the topics in [Fonts and Text](/windows/desktop/gdi/fonts-and-text).

For more detailed information on font usage and type specifications, see the [Microsoft typography site](https://www.microsoft.com/typography/default.mspx).

## Available fonts

The outline fonts supplied with Windows are delivered as OpenType fonts with TrueType outlines (Windows also supports OpenType fonts in the CFF format). For lists of all fonts supplied by Windows, see [Microsoft typography: fonts by product or family](https://www.microsoft.com/typography/fonts/default.aspx). All Windows outline fonts conform to the latest version of the [OpenType specification](https://www.microsoft.com/typography/otspec/).

For a list of all the current and legacy UI fonts, see [Locked font metrics](#locked-font-metrics) below.

## Font modifications

To assure backwards compatibility, fonts are rarely removed from Windows. However, fonts are often modified. Modifications may include adding characters, redrawing existing characters, modifying hints, or adding or modifying support for advanced OpenType features and complex script shaping.

### Locked font metrics

Note that some values associated with UI fonts and default fonts used in Microsoft apps are locked. UI fonts are used to render UI elements like captions, dialogs, and menus. Very few changes are made to these fonts, given their high visibility and frequent use. However, because the reported values associated with these fonts are locked, there may be discrepancies between reported and actual font values.

The following reported values are locked for UI and default fonts, and may be inaccurately reported:

-   These values from the font’s [OS/2 table](https://www.microsoft.com/typography/otspec/os2.htm):
    -   xAvgCharWidth
    -   sTypoLineGap
    -   sTypoAscender
    -   sTypoDescender
    -   usWinAscent
    -   usWinDescent
-   The [unitsPerEm](https://www.microsoft.com/typography/otspec/head.htm) value set in the font’s header
-   Values from the [Vertical Device metrics table (VDMX)](https://www.microsoft.com/typography/otspec/vdmx.htm)
-   The advance widths for individual glyphs

Here's a list of the UI fonts shipped with Windows 8.1 (affected by locked values):

| Script name                   | UI font               |
|-------------------------------|-----------------------|
| Arabic                        | Segoe UI              |
| Armenian                      | Segoe UI              |
| Bangla (formerly Bengali)     | Nirmala UI            |
| Bopomofo                      | Microsoft JhengHei UI |
| Braille                       | Segoe UI Symbol       |
| Buginese                      | Leelawadee UI         |
| Canadian Aboriginal Syllabics | Gadugi                |
| Cherokee                      | Gadugi                |
| Coptic                        | Segoe UI Symbol       |
| Chinese (Simplified)          | Microsoft YaHei UI    |
| Chinese (Traditional)         | Microsoft JhengHei UI |
| Cyrillic                      | Segoe UI              |
| Devanagari                    | Nirmala UI            |
| Deseret                       | Segoe UI Symbol       |
| Ethiopic                      | Ebrima                |
| Georgian                      | Segoe UI              |
| Glagolitic                    | Segoe UI Symbol       |
| Gothic                        | Segoe UI Symbol       |
| Greek                         | Segoe UI              |
| Gujarati                      | Nirmala UI            |
| Gurmukhi                      | Nirmala UI            |
| Hebrew                        | Segoe UI              |
| Old Italic                    | Segoe UI Symbol       |
| Javanese                      | Javanese Text         |
| Japanese                      | Meiryo UI             |
| Kannada                       | Mirmala UI            |
| Khmer                         | Leelawadee UI         |
| Korean                        | Malgun Gothic         |
| Lao                           | Leelawadee UI         |
| Latin                         | Segoe UI              |
| Malayalam                     | Nirmala UI            |
| Mongolian                     | Mongolian Baiti       |
| Myanmar                       | Myanmar Text          |
| N'Ko                          | Ebrima                |
| Ogham                         | Segoe UI Symbol       |
| Ol Chiki                      | Nirmala UI            |
| Old Turkic                    | Segoe UI Symbol       |
| Odia (formerly Oriya)         | Nirmala UI            |
| Osmanya                       | Ebrima                |
| Phags-pa                      | Microsoft PhagsPa     |
| Runic                         | Segoe UI Symbol       |
| Sora Sompeng                  | Nirmala UI            |
| Sinhala                       | Nirmala UI            |
| Syriac                        | Estrangelo Edessa     |
| Tai Le                        | Microsoft Tai Le      |
| New Tai Lue                   | Microsoft New Tai Lue |
| Tamil                         | Nirmala UI            |
| Telugu                        | Nirmala UI            |
| Tifinagh                      | Ebrima                |
| Thaana                        | MV Boli               |
| Thai                          | Leelawadee UI         |
| Tibetan                       | Microsoft Himalaya    |
| Vai                           | Ebrima                |
| Yi                            | Microsoft Yi Baiti    |



 

Here's a list of the legacy UI fonts which are also affected by locked values:

| Script name (legacy)          | UI font (legacy)               |
|-------------------------------|--------------------------------|
| Bangla (formerly Bengali)     | Vrinda                         |
| Canadian Aboriginal Syllabics | Euphemia                       |
| Cherokee                      | Plantagenet                    |
| Chinese (Simplified)          | Microsoft YaHei and SimSun     |
| Chinese (Traditional)         | MingLiU and Microsoft JhengHei |
| Devanagari                    | Mangal                         |
| European languages            | Tahoma                         |
| Gujarati                      | Shruti                         |
| Gurmukhi                      | Raavi                          |
| Japanese                      | Meiryo and MS Gothic UI        |
| Kannada                       | Tunga                          |
| Khmer                         | Khmer                          |
| Korean                        | Gulim                          |
| Lao                           | Lao UI                         |
| Malayalam                     | Kartika                        |
| Middle Eastern languages      | Tahoma                         |
| Odia (formerly Oriya)         | Kalinga                        |
| Sinhalese                     | Iskoola Pota                   |
| Tamil                         | Latha and Vijaya               |
| Telugu                        | Gautami                        |
| Thai                          | Leelawadee and Tahoma          |



 

These fonts are used as defaults in Microsoft apps and are also affected by locked values:

-   Arial
-   Calibri
-   Cambria
-   Consolas
-   Courier New
-   MS Mincho
-   Times New Roman
-   Verdana

### Dynamic font metrics

Other than the locked metrics listed above, font values are accurately reported. If a font is changed in a new version of Windows, dynamic font values will differ between the new and old. For example, when a glyph is added to a font, values in the font’s header may change. Clipping could result if these values (which include xMin, xMax, yMin, and yMax, and report the minimum and maximum bounding box for glyphs in the font) were locked and didn't report true values.

> [!IMPORTANT]
> If you use dynamic font values in your app (like those in [**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica)), these values will change if fonts are modified in future versions of Windows. Don't use these actual values in situations where text must stay static.

 

## Guidelines for using font metrics

-   Compute screen metrics and font metrics (e.g., average width) when an app is launched, and use these values to lay out your app. This will provide consistently accurate rendering, and your layout will respond to changes in fonts or accommodate font fallback. For an overview of font fallback and font linking, see [Globalization Step by Step: Fonts](https://msdn.microsoft.com/goglobal/bb688134.aspx). See [Using Font Fallback](/windows/desktop/Intl/using-font-fallback) for Uniscribe-specific info.
    -   To compute a base metric, render representative text for your intended language/script.
    -   For controls that just contain a single line of unwrapped text, lay them out to fit the full width of the untrimmed text.
    -   For controls with multiple lines, get the total length, divide by the character length, and you’ve got a solid width to work with. Note that this is trickier for complex scripts where a single ‘character’ to the reader may be multiple code points.
-   Use sTypoAscender, sTypoDescender, and unitsPerEm (from the [OS/2 table](https://www.microsoft.com/typography/otspec/os2.htm)) to calculate vertical spacing. sTypoAscender is used to determine the optimum offset from the top of a text frame to the first baseline and sTypoDescender determines the optimum offset from the bottom of a text frame to the last baseline.
-   If you’re using DirectWrite, create a layout using [**IDWriteTextLayout**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextlayout). **IDWriteTextLayout** provides **ascender** + **descender** + **lineGap** in natural layout. You can access these specific values with [**DWRITE\_FONT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_metrics). For info on this interface, see [Text Formatting and Layout](/windows/desktop/DirectWrite/text-formatting-and-layout).
-   If you’re using GDI, render off screen, then inspect the layout (for example, the line length or characters per line) and recalculate the final layout parameters used in actual rendering.
-   Don’t build layouts statically based on particular values for particular versions of fonts. Actual values may change from release to release.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IDWriteTextLayout**](/windows/desktop/api/dwrite/nn-dwrite-idwritetextlayout)
</dt> <dt>

[**DWRITE\_FONT\_METRICS**](/windows/desktop/api/dwrite/ns-dwrite-dwrite_font_metrics)
</dt> <dt>

[**TEXTMETRIC**](/windows/win32/api/wingdi/ns-wingdi-textmetrica)
</dt> <dt>

[unitsPerEm](https://www.microsoft.com/typography/otspec/head.htm)
</dt> <dt>

[OS/2 table](https://www.microsoft.com/typography/otspec/os2.htm)
</dt> <dt>

[Vertical Device metrics table (VDMX)](https://www.microsoft.com/typography/otspec/vdmx.htm)
</dt> <dt>

[Microsoft typography: fonts by product or family](https://www.microsoft.com/typography/fonts/default.aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Text Metrics (DirectWrite)](/windows/desktop/DirectWrite/text-metrics)
</dt> <dt>

[Fonts and Text (GDI)](/windows/desktop/gdi/fonts-and-text)
</dt> <dt>

[Microsoft Typography](https://www.microsoft.com/typography/default.mspx)
</dt> </dl>

 

 