---
title: What's new in DirectWrite
description: Here are some of the new additions to DirectWrite.
ms.assetid: 2512D222-C6EB-4C2D-80A6-7978FED56F7A
ms.topic: article
ms.date: 09/23/2019
---

# What's new in DirectWrite

This topic describes what's new in [DirectWrite](direct-write-portal.md) for various releases of Windows 10.

## Project Reunion 0.1 Prerelease

[Project Reunion](/windows/apps/project-reunion/) introduces a new version of DirectWrite, called DWriteCore, that runs on versions of Windows down to Windows 8 and opens the door for you to use it cross-platform. For more details, see [DWriteCore overview](dwritecore-overview.md).

## Windows 10 May 2019 Update

No features or APIs were added nor updated for Windows 10, version 1903 (10.0; Build 18362)&mdash;also known as Windows 10 May 2019 Update.

## Windows 10 October 2018 Update

The following features and APIs were added or updated for Windows 10, version 1809 (10.0; Build 17763)&mdash;also known as Windows 10 October 2018 Update.

### New

- [**DWRITE_FONT_SOURCE_TYPE**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_source_type) enumeration
- [**IDWriteFontSet3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset3) interface, and its methods

## Windows 10 April 2018 Update

The following features and APIs were added or updated for Windows 10, version 1803 (10.0; Build 17134)&mdash;also known as Windows 10 April 2018 Update.

### New

- [**IDWriteFactory7**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory7) interface, and its methods
- [**IDWriteFontCollection3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection3) interface, and its methods
- [**IDWriteFontSet2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset2) interface, and its methods

## Windows 10 Fall Creators Update

The following features and APIs were added or updated for Windows 10, version 1709 (10.0; Build 16299)&mdash;also known as Windows 10 Fall Creators Update.

### New

- [**DWRITE_AUTOMATIC_FONT_AXES**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_automatic_font_axes) enumeration
- [**DWRITE_FONT_AXIS_ATTRIBUTES**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_axis_attributes) enumeration
- [**DWRITE_FONT_AXIS_TAG**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_axis_tag) enumeration
- [**DWRITE_FONT_FAMILY_MODEL**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_family_model) enumeration
- [**IDWriteFactory6**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory6) interface, and its methods
- [**IDWriteFontCollection2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection2) interface, and its methods
- [**IDWriteFontFace5**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface5) interface, and its methods
- [**IDWriteFontFaceReference1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference1) interface, and its methods
- [**IDWriteFontFallback1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfallback1) interface, and its methods
- [**IDWriteFontFamily2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfamily2) interface, and its methods
- [**IDWriteFontList2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontlist2) interface, and its methods
- [**IDWriteFontResource**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontresource) interface, and its methods
- [**IDWriteFontSet1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset1) interface, and its methods
- [**IDWriteFontSetBuilder2**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder2) interface, and its methods
- [**IDWriteTextFormat3**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextformat3) interface, and its methods
- [**IDWriteTextLayout4**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextlayout4) interface, and its methods
- [**DWRITE_MAKE_FONT_AXIS_TAG**](/windows/win32/api/dwrite_3/nf-dwrite_3-dwrite_make_font_axis_tag) macro
- [**DWRITE_FONT_AXIS_RANGE**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_axis_range) structure
- [**DWRITE_FONT_AXIS_VALUE**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_font_axis_value) structure

### Moved

The [**DWRITE_GLYPH_IMAGE_FORMATS**](/windows/win32/api/dcommon/ne-dcommon-dwrite_glyph_image_formats) enumeration moved from `dwrite_3.h` to `dcommon.h`.

## Windows 10 Creators Update

The following features and APIs were added or updated for Windows 10, version 1703 (10.0; Build 15063)&mdash;also known as Windows 10 Creators Update.

### Expanded API support for cloud fonts and custom font sets

Windows 10 included APIs that allow apps to easily access fonts from a Windows font service. In the Windows 10 Creators Update, APIs for remote fonts are extended to allow easy access to fonts from other sources on the Web that can be accessed using HTTP or HTTPS. 

The new remote-font APIs can be used with public or private Web services. In addition, they can be used to access raw, OpenType font files (.ttf, .otf., .ttc, .otc), or fonts packaged in [WOFF](https://www.w3.org/TR/WOFF/) or [WOFF2](https://www.w3.org/TR/WOFF2/) container formats. The new APIs are used in conjunction with existing APIs for queuing requests to download remote font data and for handling the actual download process.

Other new APIs make it easier for apps to work with custom fonts that are stored in the local file system or that are loaded into a memory buffer.

For more information on new APIs for working with remote fonts, custom font sets, or WOFF/WOFF2 container formats, see the following topic:

[Custom Font Sets](custom-font-sets-win10.md)

See also the links to API reference topics provided in that topic.  Use of new and existing APIs for working with custom fonts is also illustrated in the [DirectWrite Custom Font Sets sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/DirectWriteCustomFontSets/). This sample illustrates code implementation for several different scenarios, including local fonts on disk, remote fonts on the Web, in-memory font data, and fonts in packed WOFF or WOFF2 formats.

### Initial support for OpenType Font Variations

Version 1.8 of the OpenType font format specification introduced an exciting new extension to the format known as OpenType Font Variations. DirectWrite has been updated in the Windows 10 Creators Update to support named instances of variable fonts. For more information, see the following topic:

[OpenType Variable Fonts](opentype-variable-fonts.md)

## Windows 10 Anniversary Update

The following features and APIs were added or updated for Windows 10, version 1607 (10.0; Build 14393)&mdash;also known as Windows 10 Anniversary Update.

### Improved support for color fonts

Starting in Windows 10 Anniversary Update, DirectWrite provides built-in support for a wider variety of color font formats, allowing developers to use more types of fonts in their DirectWrite-powered apps than ever before. This includes support for:

-   The ‘COLR’ OpenType table, which enables compact vector content in fonts. (Supported since Windows 8.1.)
-   The ‘SVG ’ OpenType table, which enables SVG content in fonts.
-   The ‘CBDT’ OpenType table, which enables color bitmap content in fonts.
-   The ‘sbix’ OpenType table, which enables color bitmap content in fonts.

[Direct2D](../direct2d/direct2d-portal.md), which uses DirectWrite for text rendering, supports these color font formats automatically when the [**D2D1\_DRAW\_TEXT\_OPTIONS\_ENABLE\_COLOR\_FONT**](/windows/win32/api/d2d1/ne-d2d1-d2d1_draw_text_options) flag is enabled. For more information, see the following topics:

-   [Color Fonts](color-fonts.md)
-   [DirectWrite color glyph sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DWriteColorGlyph)

### Support for Adobe Typekit and other font-service clients

Some font services, such as Adobe Typekit, have client-side utilities that allow a user to load fonts from the service and use them in different applications on their Windows machine. These utilities typically work by making run-time calls to GDI to load additional fonts, rather than permanently installing fonts on the system. Because of that design, on earlier Windows versions, the fonts would be usable in GDI-based applications, but not in DirectWrite applications. Starting in the Windows 10 Anniversary Update, fonts that are loaded by such utilities will also be available in DirectWrite as well as in GDI.

Fonts loaded by a font-service utility are visible in the system font collection obtained by calling the [**IDWriteFactory::GetSystemFontCollection**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-getsystemfontcollection) method. Because font services typically follow a per-user licensing model, fonts loaded by these utilities are managed on a per-user basis. As a result, existing DirectWrite applications can utilize fonts that end-users have obtained using such services, without any code changes required in the application, providing a more seamless experience for users.

### Support for OpenType collections using CFF outlines

The OpenType and TrueType font formats have long supported the ability for multiple fonts to be packaged together in a single font file, known as a “font collection”. The OpenType specification has always allowed fonts to use either TrueType or CFF formats for glyph outline data. Until recently, however, the specification has only allowed for collections in which glyph outlines use the TrueType format. OpenType version 1.7 now allows for collections to use either TrueType or CFF formats for glyph outline data. Starting in the Windows 10 Anniversary Update, DirectWrite will support OpenType collections using CFF outline data.

## Windows 10

### Windows font service integration

Starting in Windows 10, fonts that are included with Windows are available in an online service and are accessible via DirectWrite on any Windows 10 device. This applies to all Windows 10 editions, including Windows 10 Mobile, Xbox and HoloLens as well as the desktop client. This allows applications to display content using any Windows font even if the font is not currently installed on the device.

Support for the DirectWrite font-service mechanisms has been implemented in the XAML framework, which means that any applications that use XAML require no code changes in order to take advantage of the font service. The [Downloadable fonts (XAML) code sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/XamlCloudFontIntegration) demonstrates this. Applications that call DirectWrite APIs directly will need to use new APIs to make use of the font-service mechanisms. For more information, see the following topics:

-   [**IDWriteFactory3::GetSystemFontCollection**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-getsystemfontcollection) method
-   [**IDWriteTextLayout3**](idwritetextlayout3.md) interface
-   [**IDWriteFontDownloadQueue**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) interface
-   [**IDWriteFontDownloadListener**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) interface

The [Downloadable fonts (DirectWrite) code sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DWriteTextLayoutCloudFont) illustrates the use of several of the new APIs.

### Font set APIs

DirectWrite's font collection interfaces provide a view to a collection of fonts that is organized by font families, using weight, stretch and style as sub-family attributes. Internally, DirectWrite implements the font collection interface using a flat list of fonts with various attributes. This approach is more flexible in that in can support enumeration of weight/stretch/style families, but can also support querying and filtering using other font attributes as well.

In Windows 10, this more flexible font-handling mechanism is made available to applications via the IDWriteFontSet and related APIs. The font set APIs can be used, for example, to create a customized font-picker user interface leveraging application-customized font properties in a custom font set.

For more information, see the following topics:

-   [**IDWriteFontSet**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset) interface
-   [**IDWriteFontSetBuilder**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) interface
-   [**DWRITE\_FONT\_PROPERTY\_ID**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_property_id) enumeration
-   [**IDWriteFontFactory3::GetSystemFontSet**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory3-getsystemfontset) method

### New text-layout line-spacing modes

DirectWrite’s text format and text layout interfaces support new line-spacing modes. In earlier versions, DirectWrite’s text layout implementation allowed for line spacing in which the height of each line was set automatically based on the tallest item within a line (the “default” mode), or line spacing with all lines set to a uniform height determined by the application (the “uniform” mode). In Windows 10, an additional “proportional” line-spacing mode is supported that gives applications more options for line-spacing behavior. For more information, see the following topics:

-   [**IDWriteTextLayout3**](idwritetextlayout3.md) interface
-   [**IDWriteTextLayout3::SetLineSpacing**](idwritetextlayout3-setlinespacing.md) method
-   [**DWRITE\_LINE\_SPACING**](/windows/win32/api/Dwrite_3/ns-dwrite_3-dwrite_line_spacing) structure
-   [**DWRITE\_LINE\_SPACING\_METHOD**](/windows/win32/api/dwrite/ne-dwrite-dwrite_line_spacing_method) enumeration
-   [**DWRITE\_FONT\_LINE\_GAP\_USAGE**](/windows/win32/api/dwrite_3/ne-dwrite_3-dwrite_font_line_gap_usage) enumeration
-   [**IDWriteTextLayout3::GetLineMetrics**](idwritetextlayout3-getlinemetrics.md) method
-   [**DWRITE\_LINE\_METRICS1**](/windows/win32/api/dwrite_3/ns-dwrite_3-dwrite_line_metrics1) structure

The [Line spacing (DirectWrite) code sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DWriteLineSpacingModes) illustrates use of several of the new APIs, and also provides a visualization of all of the different line-spacing modes that makes it much easier to understand the various line-spacing options that are available.

### GDI interop

Since its introduction in Windows 7, DirectWrite has provided a migration path for applications that were originally implemented using GDI’s font model, text layout and rendering. This was provided via the \[\[IDWriteGdiInterop\]\] interface. In Windows 10, additional APIs provide additional GDI-interop capabilities. For additional information, see the following topic:

-   [**IDWriteGdiInterop1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritegdiinterop1) interface

## Windows 8.1

### Rendering color fonts

Starting in Windows Windows 8.1, DirectWrite provides support for color fonts. [Direct2D](../direct2d/direct2d-portal.md), which uses DirectWrite for text rendering, has added the enum value D2D1\_DRAW\_TEXT\_OPTIONS\_ENABLE\_COLOR\_FONT to enable this feature when drawing text. For more information, see the following topics:

-   [**D2D1\_DRAW\_TEXT\_OPTIONS**](/windows/win32/api/d2d1/ne-d2d1-d2d1_draw_text_options) enumeration
-   [**IDWriteFactory2::TranslateColorGlyphRun**](/windows/win32/api/dwrite_2/nf-dwrite_2-idwritefactory2-translatecolorglyphrun) method

## Windows 8

A new factory interface, [**IDWriteFactory1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefactory1), for creating additional interfaces that are available.

Additional font properties, such as: super/subscript, caret slope, PANOSE, and Unicode ranges.

-   [**IDWriteFont1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefont1)
-   [**IDWriteFontFace1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefontface1)

Spacing improvements, such as: control character spacing, legacy kerning pairs, and justification. See the [Justification, Kerning, and Spacing](justification--kerning--and-spacing.md) topic for more info.

-   [**IDWriteTextLayout1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextlayout1)
-   [**IDWriteTextAnalyzer1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalyzer1)

Improved render targets and parameters.

-   [**IDWriteBitmapRenderTarget1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritebitmaprendertarget1)
-   [**IDWriteRenderingParams1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwriterenderingparams1)

Text complexity analysis improvements.

-   [**IDWriteTextAnalyzer1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalyzer1)

New script properties, new script support (Unicode 6), font fallback additions, paired parentheses, and bidi augmentation.

Font cache performance enhancements. Starting with Windows 8 the font cache is global and starts when your computer boots.

New rendering modes.

Starting with Windows 8, [DirectWrite](direct-write-portal.md) supports a number of features that help you make apps for the world market.

Here are several areas that help you implement rich text apps that can be tailored to customers across the globe.

### Chinese, Japanese, and Korean extensions C & D

Every few years, the Unicode Consortium releases a standardized list of additions to Chinese, Japanese, and Korean Unified Ideograph block. With the Unicode 6.0 revision, they have released extension blocks C and D. These blocks of ideographs can be found on the Unicode website [Extension C](https://www.unicode.org/charts/PDF/U2A700.pdf) and [Extension D](https://www.unicode.org/charts/PDF/U2B740.pdf).

Starting with Windows 8, [DirectWrite](direct-write-portal.md) supports the Unicode codepoints for these new blocks of standardized CJK Ideographs, so you can use them in DirectWrite apps.

### Indian rupee symbol

In March of 2005, the Indian government announced a competition to choose a symbol for the Indian rupee currency. After much competition, on the 15th of July, 2010, the Indian government chose the design created by D. Udaya Kumar, and [DirectWrite](direct-write-portal.md) includes support for the Unicode codepoint tied to the symbol. So, DirectWrite apps now support this currency symbol.

### Emoji

[DirectWrite](direct-write-portal.md) now supports the use of emoji in apps. Previous versions of DirectWrite, presented with a missing glyph box if you tried to render an emoji ideograph. Starting with Windows 8, DirectWrite supports the Unicode codeblock associated with emoji, so if your app uses the Unicode standard codepoints for emoji it displays the appropriate glyphs.

### Myanmar, Tiffinagh, and Old Hangul languages

Starting in Windows 8, [DirectWrite](direct-write-portal.md) supports the block of Unicode codepoints that correspond to the glyphs in the Myanmar, Tiffinagh, and Old Hangul languages, so you can create apps that include text from these three languages. In addition to supporting these characters, DirectWrite supports the unique way that Old Hangul handles line breaking.

### New scripts

Starting in Windows 8, the [**GetScriptProperties**](/windows/win32/api/dwrite_1/nf-dwrite_1-idwritetextanalyzer1-getscriptproperties) method returns info for a number of new scripts. Here is the list of scripts that [DirectWrite](direct-write-portal.md) supports in Windows 8 and after.

-   Avestan
-   Bamum
-   Batak
-   Brahmi
-   Egyptian hieroglyphics
-   Imperial Aramaic
-   Inscriptional Pahlavi
-   Inscriptional Parthian
-   Javanese
-   Kaithi
-   Lisu (Fraser)
-   Mandaic
-   Meetei Mayek
-   Old South Arabian
-   Old Turkish (Orkhon)
-   Samaritan
-   Tai Tham (Lanna)
-   Tai Viet
