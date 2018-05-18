---
title: Text Formatting and Layout
description: DirectWrite provides two interfaces for formatting text IDWriteTextFormat and IDWriteTextLayout.
ms.assetid: 'a68963a6-e486-4881-8ad6-873173396fca'
keywords: ["DirectWrite,text formatting", "DirectWrite,layout", "DirectWrite,IDWriteTextFormat interface", "DirectWrite,IDWriteTextLayout interface", "IDWriteTextFormat interface", "IDWriteTextLayout interface"]
---

# Text Formatting and Layout

[DirectWrite](direct-write-portal.md) provides two interfaces for formatting text: [**IDWriteTextFormat**](idwritetextformat.md) and [**IDWriteTextLayout**](idwritetextlayout.md). **IDWriteTextFormat** describes only the format for text and is used in cases when an entire string is to be the same font size, style, weight and so on. On the other hand, **IDWriteTextLayout** encapsulates both a text string and the formatting for specified ranges of the string. This document describes each interface and their uses. For more information about the creation and methods of these interfaces, see the [**IDWriteTextFormat**](idwritetextformat.md) and [**IDWriteTextLayout**](idwritetextlayout.md) reference pages.

This document contains the following parts:

-   [IDWriteTextFormat](#modifying-an-idwritetextformat)
    -   [Modifying an IDWriteTextFormat](#modifying-an-idwritetextformat)
-   [IDWriteTextLayout](#idwritetextlayout)
    -   [Formatting a range of text](#formatting-a-range-of-text)
    -   [Rendering Options](#rendering-options)

## IDWriteTextFormat

An [**IDWriteTextFormat**](idwritetextformat.md) object is used to:

-   Describe the format for an entire string when rendering. To render a string with multiple formats, use an [**IDWriteTextLayout**](idwritetextlayout.md) object.
-   Specify the default text format when creating an [**IDWriteTextLayout**](idwritetextlayout.md) object.

To create an [**IDWriteTextFormat**](idwritetextformat.md) object, you use the [**IDWriteFactory::CreateTextFormat**](idwritefactory-createtextformat.md) method and specify the font family, font collection, font weight, font size (in DIPs), locale name.

### Modifying an IDWriteTextFormat

Once an [**IDWriteTextFormat**](idwritetextformat.md) interface is created, some values cannot be changed: the font family, collection, weight, and size, as well the locale name. To change these values, a new **IDWriteTextFormat** object must be created.

[**IDWriteTextLayout**](idwritetextlayout.md) enables you to change the properties above without recreating anthing. [**IDWriteTextFormat**](idwritetextformat.md) enables you to make format changes that apply to the entire text, such as text alignment. If you want to apply formatting to specific character ranges, you should do so by using a **IDWriteTextLayout**.

[**IDWriteTextFormat**](idwritetextformat.md) provides methods to set the text alignment, flow direction, incremental tab stop, line spacing, paragraph alignment, trimming, and word wrapping. These properties can be changed at any time after the creation of the **IDWriteTextFormat** object.

## IDWriteTextLayout

The [**IDWriteTextLayout**](idwritetextlayout.md) interface, unlike [**IDWriteTextFormat**](idwritetextformat.md), represents both a block of text and the associated formatting. **IDWriteTextFormat** represents initial formatting information. The following example shows how to create an **IDWriteTextLayout** object using [**IDWriteFactory::CreateTextLayout**](idwritefactory-createtextlayout.md).


```C++
// Create a text layout using the text format.
if (SUCCEEDED(hr))
{
    RECT rect;
    GetClientRect(hwnd_, &amp;rect); 
    float width  = rect.right  / dpiScaleX_;
    float height = rect.bottom / dpiScaleY_;

    hr = pDWriteFactory_->CreateTextLayout(
        wszText_,      // The string to be laid out and formatted.
        cTextLength_,  // The length of the string.
        pTextFormat_,  // The text format to apply to the string (contains font information, etc).
        width,         // The width of the layout box.
        height,        // The height of the layout box.
        &amp;pTextLayout_  // The IDWriteTextLayout interface pointer.
        );
}

```



The text in an [**IDWriteTextLayout**](idwritetextlayout.md) object cannot be changed once the object is created. To change the text you must delete the existing object and create a new **IDWriteTextLayout** object.

You can use an [**IDWriteTextLayout**](idwritetextlayout.md) to format specified ranges of text. **IDWriteTextLayout** also provides methods for changing font style and weight, and adding OpenType font features and hit testing. For more information and a complete list of methods see the [**IDWriteTextLayout**](idwritetextlayout.md) reference page.

### Formatting a range of text

[**IDWriteTextLayout**](idwritetextlayout.md) provides several methods to format ranges of text. Each of these methods takes a [**DWRITE\_TEXT\_RANGE**](dwrite-text-range.md) structure as a parameter to specify the starting text position within the string and the length of the range to format. The following example shows how to set the font weight of a range of text to bold.


```C++
// Set the font weight to bold for the first 5 letters.
DWRITE_TEXT_RANGE textRange = {0, 4};

if (SUCCEEDED(hr))
{
    hr = pTextLayout_->SetFontWeight(DWRITE_FONT_WEIGHT_BOLD, textRange);
}

```



### Rendering Options

Text with formatting described by only a [**IDWriteTextFormat**](idwritetextformat.md) object can be rendered with [Direct2D](direct2d.direct2d_portal.xml), however, there are a few more options for rendering an [**IDWriteTextLayout**](idwritetextlayout.md) object.

The string described by an [**IDWriteTextLayout**](idwritetextlayout.md) object can be rendered using the methods below.

1.  [Render using Direct2D](rendering-by-using-direct2d.md).
2.  [Render using a custom text renderer](how-to-implement-a-custom-text-renderer.md).
3.  [Render to a GDI surface](render-to-a-gdi-surface.md).

 

 




