---
title: Color font support
description: This topic describes color fonts, their support in DirectWrite and Direct2D, and how to use them in your app.
ms.assetid: 74e096c4-9d1c-8854-e9ee-f8b11ac1c71a
ms.topic: reference
ms.date: 09/18/2023
---

# Color font support

This topic describes color fonts, their support in DirectWrite and Direct2D (and some other frameworks), and how to use them in your app.

## What are color fonts?

By default, a glyph has a shape but no intrinsic color. Both DirectWrite and Direct2D have **DrawGlyphRun** methods that render glyph runs by filling the glyph shapes with a specified text color. For convenience, we'll refer to that as *monochrome* glyph rendering. All fonts have monochrome glyphs. A color font, on the other hand, also has color representations of some glyphs. And to render glyphs in color, your app must use different glyph-rendering APIs (as we'll discuss), instead of calling the monochrome **DrawGlyphRun** methods.

Color fonts are also referred to as multicolored fonts or chromatic fonts. They're a font technology that allows font designers to use multiple colors within each glyph. Color fonts enable multicolored text scenarios in apps and websites with less code and more robust operating system support than ad-hoc techniques implemented above the text rendering system.

The fonts that most of us are familiar with are *not* color fonts. Such fonts define only the shape of the glyphs that they contain; either with vector outlines or monochromatic bitmaps. At draw time, a text renderer fills the glyph shape using a single color (the font color) specified by the app or document being rendered. Color fonts, on the other hand, contain color information *in addition to* shape information. Some approaches allow font designers to offer multiple color palettes, giving the color font artistic flexibility.

Here's a glyph from the Segoe UI Emoji color font. The glyph is rendered in monochrome on the left, and in color on the right.

![Shows side-by-side glyphs, the left glyph rendered in monochrome, the right in Segoe U I Emoji color font.](images/color-font-cat.png)

Color fonts typically include fallback information for platforms that don't support them, or for scenarios in which color functionality has been disabled. On those platforms, color fonts are rendered as regular monochromatic fonts.

Because color font support is implemented at the glyph rendering level, it doesn't affect text layout. And that's true whether you use the [IDWriteTextLayout](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) interface, or whether you implement your own text layout algorithm. The mapping of characters to glyphs, and the positioning of those glyphs, all use monochrome glyph IDs and their associated metrics. The output of the text layout process is a sequence of monochrome glyph runs. And then color font support can be enabled by translating those monochrome *base* glyph runs to color glyphs runs at rendering time.

## Why use color fonts?

Historically, designers and developers have used a variety of techniques to achieve multicolored text. For example, websites often use raster images instead of text in order to display rich headers. That approach enables artistic flexibility, but raster graphics don't scale well to all display sizes, and nor do they provide the same accessibility features as real text. Another common technique is to overlay multiple monochromatic fonts in different font colors; but that typically requires extra layout code to manage.

Color fonts offer a way to achieve those visual effects with all the simplicity and functionality of regular fonts. Text rendered in a color font is the same as other text: it can be copied and pasted, it can be parsed by accessibility tools, and so on.

## What kinds of color fonts does Windows support?

The [OpenType specification](https://www.microsoft.com/Typography/OpenTypeSpecification.aspx) defines several ways to embed color information in a font. Starting in Windows 10, version 1607 (Anniversary Update), DirectWrite and Direct2D (and the Windows frameworks built on them) support all of these approaches:

| Technique | Description |
|-|-|
| [COLR](/typography/opentype/spec/colr)/[CPAL](/typography/opentype/spec/cpal) tables | Uses layers of colored vectors, whose shapes are defined in the same way as single-color glyph outlines. Support started in Windows 8.1. |
| [SVG](/typography/opentype/spec/svg) table | Uses vector images authored in the Scalable Vector Graphics (SVG) format. As of Windows 10, version 1607 (Anniversary Update), DirectWrite supports a subset of the full SVG spec. Not all SVG content is guaranteed to render in an OpenType SVG font. For more details, see [SVG support](../direct2d/svg-support.md). |
| [CBDT](/typography/opentype/spec/cbdt)/[CBLC](/typography/opentype/spec/cblc) tables | Uses embedded color bitmap images. |
| [sbix](/typography/opentype/spec/sbix) table | Uses embedded color bitmap images. |

## Using color fonts

From the user's perspective, color fonts are just fonts. For example, they can usually be installed and uninstalled from the system in the same way as monochromatic fonts can; and they're rendered as regular, selectable text.

From the developer's perspective too, color fonts are usually used the same way as monochromatic fonts are. In the XAML and Microsoft Edge frameworks, you can style your text with color fonts the same way you can with regular fonts, and by default your text will be rendered in color. However, if your app directly calls Direct2D APIs (or Win2D APIs) to render text, then it must explicitly request color font rendering.

## Using color fonts with DirectWrite and Direct2D

Your app can use Direct2D's higher-level text drawing methods ([**DrawText**](../direct2d/id2d1devicecontext4-drawtext-overload.md) and [**DrawTextLayout**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext4-drawtextlayout)), or it can use lower-level techniques to draw glyph runs directly. In either case, your app requires specific code in order to handle color glyphs correctly. Direct2D's **DrawText** and **DrawTextLayout** APIs don't render color glyphs by default. That's to avoid unexpected behavior changes in text rendering apps that were designed prior to color font support.

To opt in to color glyph rendering, pass the [**D2D1_DRAW_TEXT_OPTIONS_ENABLE_COLOR_FONT**](/windows/win32/api/d2d1/ne-d2d1-d2d1_draw_text_options) options flag to the drawing method. The following code example shows how to call Direct2D's **DrawText** method to render a string in a color font:

```cpp
// If m_textFormat points to a font with color glyphs, then the following
// call will render m_string using the color glyphs available in that font.
// Any monochromatic glyphs will be rendered with m_defaultFillBrush.
m_deviceContext->DrawText(
    m_string->Data(),
    m_string->Length(),
    m_textFormat.Get(),
    m_layoutRect,
    m_defaultFillBrush.Get(),
    D2D1_DRAW_TEXT_OPTIONS_ENABLE_COLOR_FONT
    );
```

If your app uses lower-level APIs to handle glyph runs directly, then it will continue to function in the presence of color fonts, but it won't be able to draw color glyphs without additional logic.

To correctly handle color glyphs, your app should:

1.  Pass the glyph run information to [**TranslateColorGlyphRun**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory4-translatecolorglyphrun), along with a [**DWRITE_GLYPH_IMAGE_FORMATS**](/windows/win32/api/dcommon/ne-dcommon-dwrite_glyph_image_formats) parameter that indicates which type(s) of color glyph the app is prepared to handle. If any color glyphs are present (based on the font and the requested **DWRITE_GLYPH_IMAGE_FORMATS**), then DirectWrite will split the primary glyph run into individual color glyph runs, which can be accessed through the returned [**IDWriteColorGlyphRunEnumerator1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritecolorglyphrunenumerator1) object in Step 4.
2.  Check the **HRESULT** returned by [**TranslateColorGlyphRun**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory4-translatecolorglyphrun) to determine whether any color glyph runs were detected. An **HRESULT** of **DWRITE_E_NOCOLOR** indicates that there isn't an applicable color glyph run.
3.  If [**TranslateColorGlyphRun**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory4-translatecolorglyphrun) reports no color glyph runs (by returning **DWRITE_E_NOCOLOR**), then the whole glyph run is treated as monochromatic, and your app should draw it as desired (for example, using [**ID2D1DeviceContext::DrawGlyphRun**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-drawglyphrun)).
4.  If [**TranslateColorGlyphRun**](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory4-translatecolorglyphrun) does report the presence of color glyph runs, then your app should ignore the primary glyph run, and instead use the color glyph run(s) returned by **TranslateColorGlyphRun**. To do that, iterate through the returned [**IDWriteColorGlyphRunEnumerator1**](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritecolorglyphrunenumerator1) object, retrieving each color glyph run, and drawing it as appropriate for its glyph image format (for example, you can use [**DrawColorBitmapGlyphRun**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext4-drawcolorbitmapglyphrun) and [**DrawSvgGlyphRun**](/windows/win32/api/d2d1_3/nf-d2d1_3-id2d1devicecontext4-drawsvgglyphrun) to draw color bitmap glyphs and SVG glyphs, respectively).

This code example shows the general structure of this procedure:

```cpp
// An example code snippet demonstrating how to use TranslateColorGlyphRun 
// to handle different kinds of color glyphs. This code does not make any 
// actual drawing calls. 
HRESULT DrawGlyphRun( 
    FLOAT baselineOriginX, 
    FLOAT baselineOriginY, 
    DWRITE_MEASURING_MODE measuringMode, 
    _In_ DWRITE_GLYPH_RUN const* glyphRun, 
    _In_ DWRITE_GLYPH_RUN_DESCRIPTION const* glyphRunDescription, 
) 
{ 
    // Specify the color glyph formats your app supports. In this example, 
    // the app requests only glyphs defined with PNG or SVG. 
    DWRITE_GLYPH_IMAGE_FORMATS requestedFormats = 
        DWRITE_GLYPH_IMAGE_FORMATS_PNG | DWRITE_GLYPH_IMAGE_FORMATS_SVG; 

    ComPtr<IDWriteColorGlyphRunEnumerator1> glyphRunEnumerator; 
    HRESULT hr = m_dwriteFactory->TranslateColorGlyphRun( 
        D2D1::Point2F(baselineOriginX, baselineOriginY), 
        glyphRun, 
        glyphRunDescription, 
        requestedFormats, // The glyph formats supported by this renderer.
        measuringMode, 
        nullptr, 
        0, 
        &glyphRunEnumerator // On return, may contain color glyph runs.
        ); 

    if (hr == DWRITE_E_NOCOLOR) 
    { 
        // The glyph run has no color glyphs. Draw it as a monochrome glyph 
        // run, for example using the DrawGlyphRun method on a Direct2D 
        // device context. 
    } 
    else 
    { 
        // The glyph run has one or more color glyphs. 
        DX::ThrowIfFailed(hr); 

        // Iterate through the color glyph runs, and draw them. 
        for (;;) 
        { 
            BOOL haveRun; 
            DX::ThrowIfFailed(glyphRunEnumerator->MoveNext(&haveRun)); 
            if (!haveRun) 
            { 
                break; 
            } 

            // Retrieve the color glyph run. 
            DWRITE_COLOR_GLYPH_RUN1 const* colorRun; 
            DX::ThrowIfFailed(glyphRunEnumerator->GetCurrentRun(&colorRun)); 

            // Draw the color glyph run depending on its format. 
            switch (colorRun->glyphImageFormat) 
            { 
            case DWRITE_GLYPH_IMAGE_FORMATS_PNG: 
                // Draw the PNG glyph, for example with 
                // ID2D1DeviceContext4::DrawColorBitmapGlyphRun. 
                break; 

            case DWRITE_GLYPH_IMAGE_FORMATS_SVG: 
                // Draw the SVG glyph, for example with 
                // ID2D1DeviceContext4::DrawSvgGlyphRun. 
                break; 

                // ...etc. 
            } 
        } 
    } 

    return hr; 
} 
```

## Using color fonts in a XAML app

Color fonts are support by default by the XAML platform's text elements&mdash;such as [TextBlock](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.textblock), [TextBox](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.textbox), [RichEditBox](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.richeditbox), [Glyphs](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.documents.glyphs), and [FontIcon](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.fonticon). You simply style your text with a color font, and any color glyphs will be rendered in color.

The following syntax shows one way to style a **TextBlock** with a color font that's packaged with your app. The same technique applies to regular fonts.

```xaml
<TextBlock FontFamily="Assets/TMyColorFont.otf#MyFontFamilyName">Here's some text.</TextBlock>
```

If you want your XAML text element to *never* render multicolored text, then set its [IsColorFontEnabledProperty](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.textblock.iscolorfontenabledproperty) property to `false`.

> [!TIP]
> The links above are to the WinUI 3 versions of those XAML controls. You can find the Universal Windows Platform (UWP) equivalents in the [Windows.UI.Xaml.Controls](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls) namespace.

## Using color fonts in Microsoft Edge

Color fonts are rendered by default in websites and web apps running on Microsoft Edge, including the XAML [WebView2](/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.webview2) control. Simply use HTML and CSS to style your text with a color font, and any color glyphs will be rendered in color.

## Using color fonts with Win2D

Similar to Direct2D, Win2D's text drawing APIs don't render color glyphs by default. To opt in to color glyph rendering, set the [EnableColorFont](https://microsoft.github.io/Win2D/WinUI2/html/T_Microsoft_Graphics_Canvas_Text_CanvasDrawTextOptions.htm) options flag in the text format object your app passes to the text drawing method. The following code example shows how to render a string in a color font using Win2D:

```cpp
// The text format that will be used to draw the text. (Declared elsewhere 
// and initialized elsewhere by the app to point to a color font.) 
CanvasTextFormat m_textFormat; 

// Set the EnableColorFont option. 
m_textFormat.Options = CanvasDrawTextOptions.EnableColorFont; 

// If m_textFormat points to a font with color glyphs, then the following
// call will render m_string using the color glyphs available in that font.
// Any monochromatic glyphs will be rendered with m_color.
args.DrawingSession.DrawText(
    m_string,
    m_point,
    m_color,
    m_textFormat
    );
```

## Related topics

* [ID2D1DeviceContext4::DrawText method](../direct2d/id2d1devicecontext4-drawtext-overload.md)
* [IDWriteFactory4::TranslateColorGlyphRun method](/windows/win32/api/dwrite_3/nf-dwrite_3-idwritefactory4-translatecolorglyphrun)
* [IDWriteFontFace4 interface](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface4)
* [DirectWrite colored glyph sample app](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DWriteColorGlyph)
