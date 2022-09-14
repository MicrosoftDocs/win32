---
title: DirectWrite programming guide
description: View the articles in the DirectWrite API programming guide. DirectWrite enables Windows applications to enhance the text experience for UI and documents.
ms.assetid: ca80d130-0579-409f-9054-6e63af14ebe3
keywords:
- DirectWrite,about
- DirectWrite,programming guide
- programming guide for DirectWrite
ms.topic: article
ms.date: 05/31/2018
---

# DirectWrite programming guide

The following topics provide an overview of the [DirectWrite](direct-write-portal.md) API.

## In this section

| Topic | Description |
|-|-|
| [Introducing DirectWrite](introducing-directwrite.md) | |
| [Tutorial: Getting Started with DirectWrite](getting-started-with-directwrite.md) | This document shows you how to use [DirectWrite](direct-write-portal.md) and [Direct2D](rendering-by-using-direct2d.md) to create simple text that contains a single format, and then text that contains multiple formats.  |
| [Text Formatting and Layout](text-formatting-and-layout.md) | [DirectWrite](direct-write-portal.md) provides two interfaces for formatting text: [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) and [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout). **IDWriteTextFormat** describes only the format for text and is used in cases when an entire string is to be the same font size, style, weight and so on. On the other hand, **IDWriteTextLayout** encapsulates both a text string and the formatting for specified ranges of the string. This document describes each interface and their uses. For more information about the creation and methods of these interfaces, see the [**IDWriteTextFormat**](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) and [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) reference pages. |
| [Justification, Kerning, and Spacing](justification--kerning--and-spacing.md) | Starting with Windows 8, [DirectWrite](direct-write-portal.md) provides a number of features that allow you to control basic typographic, layout, and spacing features, such as character spacing, pair kerning, and justification. |
| [Vertical Text](vertical-text.md) | Starting with the Windows 8, [DirectWrite](direct-write-portal.md) has a number of new APIs that allow you to use vertical text in your apps.  |
| [Performance](performance.md) | Performance for [DirectWrite](direct-write-portal.md) depends largely on how you render it. See the [Improving the performance of Direct2D apps](../direct2d/improving-direct2d-performance.md) topic for info on rendering performance with [Direct2D](rendering-by-using-direct2d.md). |
| [Text Metrics](text-metrics.md) | In order to assist your layout, custom font selection, and other metric intensive operations, starting in Windows 8, [DirectWrite](direct-write-portal.md) has a number of new APIs to express all the info about fonts that you might require to develop rich text apps.  |
| [Color Fonts](color-fonts.md) | This topic describes color fonts, their support in DirectWrite and Direct2D, and how to use them in your app.  |
| [Rendering DirectWrite](rendering-directwrite.md) | |
| [How-to Topics](how-to-topics.md) | The following topics provide an overview of the [DirectWrite](direct-write-portal.md) API. |
| [Glyphs and Glyph Runs](glyphs-and-glyph-runs.md) | Glyphs and glyph runs are available at the lowest layer of functionality of the [DirectWrite](direct-write-portal.md) API, the glyph-rendering layer. |
| [Custom Font Sets](custom-font-sets-win10.md) | This topic describes various ways in which you can use custom fonts in your app. |
| [Custom Font Collections (Windows 7/8)](custom-font-collections.md) | [DirectWrite](direct-write-portal.md) provides access to the system font collection by using the [**IDWriteFactory::GetSystemFontCollection**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-getsystemfontcollection) method. This is the font collection that is most frequently used. However some applications have to use fonts that are not installed on the system, such as from included font files or font files embedded in the application.  If the fonts that you want are not in the system font collection, you can create a custom font collection derived from [**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection).  |
| [OpenType Variable Fonts](opentype-variable-fonts.md) | This topic describes OpenType variable fonts, their support in DirectWrite and Direct2D, and how to use them in your app.  |
| [Win32 Text API Comparison](appendix--win32-migration.md) | For those developers that are migrating their Win32 application code, the following table lists the Win32 Text APIs and the approximate equivalent in DirectWrite. |
| [Interoperating with GDI](interoperating-with-gdi.md) | [DirectWrite](direct-write-portal.md) provides a migration path from, and some interoperability with, GDI's font model, as well as interfaces for rendering text to a bitmap that can then be drawn on a window.  |
| [Font selection](font-selection.md) | The [**IDWriteFontSet4**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset4) interface exposes methods for selecting fonts from a font set. Those methods make it possible to transition to the *typographic font family model* while maintaining compatibility with existing applications, documents, and fonts. |
| [DirectWrite glossary](directwrite-glossary.md) | A glossary of DirectWrite terms. |
