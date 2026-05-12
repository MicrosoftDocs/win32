---
title: Color font support (preview)
description: This topic describes color fonts, their support in DirectWrite and Direct2D, and how to use them in your app (preview).
ms.topic: reference
ms.date: 09/20/2023
---

# Color font support (preview)

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

This topic describes color fonts, their support in DirectWrite and Direct2D, and how to use them in your app. For an introductory topic, also see [Color font support](color-fonts.md).

## Using color fonts with DirectWrite and Direct2D

The easiest way to enable color is to call the **DrawGlyphRunWithColorSupport** method instead of
**DrawGlyphRun**. Direct2D exposes this method through the **ID2D1DeviceContext7** interface.
DirectWrite exposes it through the **IDWriteBitmapRenderTarget3** interface.

At a lower level, enabling color involves translating the monochrome *base glyph run* to a sequence
of *color glyph runs*. Each color glyph run must then be rendered using the appropriate method,
depending on its *glyph image format*. The translation is performed by the factory object's
*TranslateColorGlyphRun* method. It and related APIs are described in the following sections.

### Using TranslateColorGlyphRun

The **TranslateColorGlyphRun** factory method translates a monochrome _base glyph run_ into a sequence
of _color glyph runs_. There are multiple ways of representing color glyphs, known as _glyph image
formats_ and identified by the **DWRITE_GLYPH_IMAGE_FORMATS** enumeration. When calling
**TranslateColorGlyphRun**, you specify the combination of glyph image formats that you support.
The **TranslateColorGlyphRun** returns a _glyph run enumerator_ object
(**IDWriteColorGlyphRunEnumerator1** interface), which you use to iterate over the sequence of
color glyph runs, represented by the **DWRITE_COLOR_GLYPH_RUN1** structure. Each color glyph run has a
glyph image format. You branch on the color run's glyph image format to determine how to
render the color run.

If the base glyph run doesn't have color glyphs in any of the requested glyph image formats, then the
**TranslateColorGlyphRun** method returns **DWRITE_E_NOCOLOR**, in which case you should render
the base glyph run as a monochrome glyph run.

Otherwise, the base glyph run might contain a mix of color glyphs in different glyph image formats as
well as monochrome glyphs. For each base glyph, the **TranslateColorGlyphRun** method determines the
available glyph image format (if any) that best matches the requested formats. The base glyph run is
split into subranges based on the matching glyph image format. Glyphs that don't support any of the
requested formats are treated as monochrome glyphs.

The glyph image formats fall into four general categories:

* Monochrome glyphs (**DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE** or **DWRITE_GLYPH_IMAGE_FORMATS_CFF**)
* Layers of solid-color glyphs (**DWRITE_GLYPH_IMAGE_FORMATS_COLR**)
* Color bitmaps embedded in the font (**DWRITE_GLYPH_IMAGE_FORMATS_PNG**,
    **DWRITE_GLYPH_IMAGE_FORMATS_JPEG**, **DWRITE_GLYPH_IMAGE_FORMATS_TIFF**, and
    **DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8**)
* Vector graphics encoded in the font as SVG (**DWRITE_GLYPH_IMAGE_FORMATS_SVG**)
* Vector graphics as a tree of *paint* elements (**DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE**)

The following subsections describe each of these approaches.

### Monochrome glyphs

The **DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE** and **DWRITE_GLYPH_IMAGE_FORMATS_CFF** glyph image formats
represent monochrome glyphs, which you can render using the **DrawGlyphRun** method. The two formats
correspond to different ways of representing glyph outlines in the font. An enumerated
**DWRITE_COLOR_GLYPH_RUN1** structure can specify these formats for one of two reasons:

* One or more of the base glyphs don't support any of the requested glyph image formats, and so
    should be rendered as monochrome glyphs.
* The best matching glyph image format for a glyph was **DWRITE_GLYPH_IMAGE_FORMATS_COLR**. Glyphs
    in this image format are rendered by enumerating a monochrome run in a specified color for each
    layer, as described in the next section.

In the first case, you should render the enumerated glyph run by using the app-defined
foreground brush. That's indicated by setting the *paletteIndex* member of the
**DWRITE_COLOR_GLYPH_RUN** structure to **DWRITE_NO_PALETTE_INDEX** (0xFFFF). If the *paletteIndex*
member has any other value, then you should render the text in the specified color.

### Layers of solid color glyphs

The **DWRITE_GLYPH_IMAGE_FORMATS_COLR** value specifies a color format that supports version 0 of the
OpenType COLR table. In that format, a color glyph is rendered by drawing multiple monochrome glyphs
on top of each other, each in a specified color.

The calling pattern used with this image format is different than with all other glyph image
formats. That's because what gets rendered finally is just a series of ordinary,
monochrome glyph runs&mdash;just with different glyph IDs and different colors than were specified initially. 
Because the enumerated color glyph runs are rendered as ordinary monochrome glyph runs,
their glyph image formats are either **DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE** or
**DWRITE_GLYPH_IMAGE_FORMATS_CFF**.

For example, suppose the base glyph run specifies a smiley face glyph. If we were to render the base glyph
run using **DrawGlyphRun**, then the visual result would be a monochrome representation of a smiley face
(the base glyph ID). The COLR table in the font maps this base glyph ID to an array of _layer
records_, each of which specifies a _replacement glyph ID_ and an index into a font-defined color
palette. The **IDWriteColorGlyphRunEnumerator** object returned by **TranslateColorGlyphRun** enumerates
one color glyph run for each of those layer records. Each color glyph run has a position, and a single
glyph ID (the replacement glyph ID for the layer), and a color (derived from the palette entry
index). You would draw the enumerated color glyph runs in the specified colors at the specified
coordinates to produce the desired visual result. In the smiley face example, that might comprise a
filled-circle glyph rendered in yellow followed by an eyes-and-mouth glyph rendered in black.

### Color bitmaps embedded in the font

The **DWRITE_GLYPH_IMAGE_FORMATS** enumeration includes values for several bitmap formats: PNG, JPEG,
TIFF, and premultiplied BGRA32 format. A font might represent color glyphs by embedding bitmaps in any
of those formats in the font. A font might include bitmaps or multiple sizes to support different font
sizes and DPI scales; though that comes at an obvious cost in terms of file size.

If your app requests bitmap image formats, then **TranslateColorGlyphRun** checks whether the font has
color bitmaps for the specified input glyphs in the specified formats. If it does, then the enumerated
color glyph runs specify the base glyph IDs and the matching image format. There are no
replacement glyph IDs in this case, like there are with **DWRITE_GLYPH_IMAGE_FORMATS_COLR**. However,
the base glyph run might still be split into multiple color runs if different input glyphs have color
bitmaps in different image formats; or if some glyphs have color representations, and others are
monochrome only.

An app using Direct2D can render the enumerated color glyph runs in these formats by calling the
**ID2DDeviceContext3::DrawColorBitmapGlyphRun** method.

A lower-level app can call **IDWriteFontFace3::GetGlyphImageData** to get the raw bitmap data
for each glyph in the returned image format. The app is then responsible itself for decoding and
rendering the bitmaps. Direct2D's internal implementation of **DrawColorBitmapGlyphRun** calls
**GetGlyphImageData** to get the bitmaps for each glyph.

### Vector graphics encoded in the font as SVG

The **DWRITE_GLYPH_IMAGE_FORMATS_SVG** value specifies a glyph image format in which color glyphs are
represented as vector graphics embedded in the font in Scaled Vector Graphics (SVG) format. The
embedded SVG might be stored with gzip compression.

The calling pattern used with SVG is similar to that with the bitmap formats, and unlike the calling
pattern for **DWRITE_GLYPH_IMAGE_FORMATS_COLR**. If the app requests SVG format, and specified
glyph IDs have SVG representations, then the enumerated color glyph runs specify the base glyph IDs
and the SVG image format.

An app using Direct2D can render enumerated color glyph runs in this format by calling the
**ID2DDeviceContext3::DrawSvgGlyphRun** method.

A lower-level app can call **IDWriteFontFace3::GetGlyphImageData** to get the raw SVG data for
each glyph. The app is then responsible for parsing and rendering the SVG itself. Direct2D's
internal implementation of **DrawSvgGlyphRun** calls **GetGlyphImageData** to get the SVG data for each
glyph.

### Vector graphics as a tree of "paint" elements

In version 1 of the OpenType COLR table, color glyphs are represented by a tree of _paint elements_.
There are different types of paint elements for geometries (represented as glyphs), transforms,
solid and gradient fills, and composition. The **DWRITE_GLYPH_IMAGE_FORMATS_COLR** format
supports layering only solid-color glyphs on top of each other. So a different glyph image format is
required to support COLR version 1 and greater, and that's **DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE**. When
using this glyph image format, the app must also specify the maximum _paint feature level_
(**DWRITE_PAINT_FEATURE_LEVEL**) that it supports. That enables future versions of the COLR table to be
supported without having to define additional glyph image formats.

The calling pattern used with this glyph image format is similar to that used with SVG. If the
app requests the COLR-paint format, and the specified glyph IDs have COLR representations, then
the enumerated color glyph runs specify the base glyph IDs and the COLR-paint image format.

An app using Direct2D can render enumerated color glyph runs in this format by calling the
**ID2DDeviceContext7::DrawPaintGlyphRun** method. An app using DirectWrite's bitmap render target
API can call **IDWriteBitmapRenderTarget3::DrawPaintGlyphRun**.

A lower-level app can use the color paint APIs described in the next section to get the tree of
paint elements for each glyph, and render it. Direct2D's and DirectWrite's implementations of
**DrawPaintGlyphRun** internally use these lower-level APIs.

### Color paint APIs

A glyph in the **DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE** image format is represented as a tree of
_paint elements_. The OpenType COLR table spec describes a directed acyclic graph of paint records,
but the subgraph for a specific glyph is always a tree. An app can use a _paint reader_ object
(**IDWritePaintReader** interface) to read the tree of paint elements for a glyph.

Each paint element has a _paint type_ (**DWRITE_PAINT_TYPE** enumeration). There are different paint
types for graphical elements such as geometries (represented as glyphs), transforms, and solid and
gradient fills. Paint reader methods return information about a paint element by filling in a
**DWRITE_PAINT_ELEMENT** structure, which comprises a paint type and a union.

Additional paint types might be added in future versions of the COLR specification. To allow for that,
an app must specify the maximum _paint feature level_ (**DWRITE_PAINT_FEATURE_LEVEL**) that it supports
when creating a paint reader object, or when calling **TranslateColorGlyphRun**. Only paint elements of
types supported by the specified feature level are returned by paint reader methods. In addition,
methods that take an output parameter of type **DWRITE_PAINT_ELEMENT** also take a size parameter,
since the structure size might change if/when additional paint types are defined.

The algorithm for rendering a color glyph is to recursively render the paint elements, each
according to its type. The following paint types are defined:

| Paint Type                            | Rendering Action                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------------------- |
| **DWRITE_PAINT_TYPE_NONE**            | No action                                                                                |
| **DWRITE_PAINT_TYPE_LAYERS**          | Render the child paint elements in bottom-up order.                                      |
| **DWRITE_PAINT_TYPE_SOLID_GLYPH**     | Fill the specified glyph shape with the specified color.                                 |
| **DWRITE_PAINT_TYPE_SOLID**           | Fill the current clip with the specified color.                                          |
| **DWRITE_PAINT_TYPE_LINEAR_GRADIENT** | Fill the current clip with the specified gradient.                                       |
| **DWRITE_PAINT_TYPE_RADIAL_GRADIENT** | Fill the current clip with the specified gradient.                                       |
| **DWRITE_PAINT_TYPE_SWEEP_GRADIENT**  | Fill the current clip with the specified gradient.                                       |
| **DWRITE_PAINT_TYPE_GLYPH**           | Fill the specified glyph shape with child paint element.                                 |
| **DWRITE_PAINT_TYPE_COLOR_GLYPH**     | Render the child paint element.                                                          |
| **DWRITE_PAINT_TYPE_TRANSFORM**       | Render the child paint element with the specified transform.                             |
| **DWRITE_PAINT_TYPE_COMPOSITE**       | Render the two child paint elements and compose them using the specified composite mode. |

For more information about paint types, see the
[OpenType COLR Table](/typography/opentype/spec/colr) specification. 
Some paint types in the DirectWrite API correspond to multiple paint formats in the COLR table.
That's because the API hides some complexities, such as differences in how some paint elements are
encoded in variable versus non-variable fonts.

## Code examples

Some of the code examples below use types (such as **ComPtr**) from the [Windows Runtime C++ Template Library (WRL)](/cpp/windows/windows-runtime-cpp-template-library-wrl). [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/) is Microsoft's recommended replacement for WRL.

Other code examples use the [Windows Implementation Libraries (WIL)](https://github.com/Microsoft/wil). A convenient way to install WIL is to go to Visual Studio, click **Project** \> **Manage NuGet Packages...** \> **Browse**, type or paste **Microsoft.Windows.ImplementationLibrary** in the search box, select the item in search results, and then click **Install** to install the package for that project.

### Rendering color glyph runs using Direct2D

This section shows a sample **TextRenderer::DrawGlyphRun** method that implements the **DrawGlyphRun**
method of the **IDWriteTextRenderer** interface. The **IDWriteTextRenderer** callback interface is used
by **IDWriteTextLayout::Draw** to render glyph runs, underlines, and so on. The use of a callback
interface enables the text layout API to be decoupled from the specific graphics engine. For
example, it's possible to implement **IDWriteTextRenderer** in terms of Direct2D, or in terms of
**IDWriteBitmapRenderTarget**, or in some other way. This example uses Direct2D.

The example includes only the **DrawGlyphRun** method. The rest of the **TextRenderer** class is omitted
for brevity, but the example assumes that the class implements the **IDWriteTextRenderer** interface, and
has the following member variables:

```cpp
wil::com_ptr<IDWriteFactory4> m_dwriteFactory;
wil::com_ptr<ID2D1DeviceContext4> m_deviceContext;
wil::com_ptr<ID2D1Brush> m_foregroundBrush;
```

The example method renders color glyphs in one of two ways. The easy way is to call
**ID2D1DeviceContext7::DrawGlyphRunWithColorSupport**. However, the example also includes a fallback
code path in case the available version of Direct2D doesn't implement the **ID2D1DeviceContext7**
interface. The fallback code path uses **TranslateColorGlyphRun**.

```cpp
// Implementation of IDWriteTextRenderer::DrawGlyphRun.
HRESULT STDMETHODCALLTYPE TextRenderer::DrawGlyphRun(
    _In_opt_ void* clientDrawingContext,
    FLOAT baselineOriginX,
    FLOAT baselineOriginY,
    DWRITE_MEASURING_MODE measuringMode,
    _In_ DWRITE_GLYPH_RUN const* glyphRun,
    _In_ DWRITE_GLYPH_RUN_DESCRIPTION const* glyphRunDescription,
    _In_opt_ IUnknown* clientDrawingEffect
) noexcept
{
    D2D_POINT_2F baselineOrigin{ baselineOriginX, baselineOriginY };

    // If a brush is specified via the clientDrawingEffect parameter, then use it as
    // the foreground brush for this glyph run. Otherwise, use the brush specified
    // by the m_foregroundBrush member.
    wil::com_ptr<ID2D1Brush> foregroundBrush;
    if (clientDrawingEffect != nullptr)
    {
        foregroundBrush = wil::try_com_query<ID2D1Brush>(clientDrawingEffect);
    }
    if (foregroundBrush == nullptr)
    {
        foregroundBrush = m_foregroundBrush;
    }

    // If available, use the ID2D1DeviceContext7 interface to draw
    // the glyph run with color the "easy" way.
    if (auto deviceContext7 = m_deviceContext.try_query<ID2D1DeviceContext7>())
    {
        // Note: Direct2D drawing methods return void. If a drawing
        // operation fails, then an error is returned by EndDraw.
        deviceContext7->DrawGlyphRunWithColorSupport(
            baselineOrigin,
            glyphRun,
            foregroundBrush.get(),
            measuringMode,
            /*colorPaletteIndex*/ 0
        );
        return S_OK;
    }

    // If we fall through to here, then we're using an older version of
    // Direct2D that doesn't implement the ID2D1DeviceContext7 interface.
    // We'll need to call TranslateColorGlyphRun. First determine the
    // world to device transform.
    D2D_MATRIX_3X2_F transform;
    m_deviceContext->GetTransform(&transform);
    float dpiX, dpiY;
    m_deviceContext->GetDpi(&dpiX, &dpiY);
    transform = transform * D2D1::Matrix3x2F::Scale(dpiX, dpiY);

    // Combination of image formats we support. Do *not* include
    // DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE, because this code
    // path is for an older version of Direct2D which doesn't support
    // the ID2D1DeviceContext7 interface.
    constexpr DWRITE_GLYPH_IMAGE_FORMATS desiredGlyphImageFormats =
        DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE |
        DWRITE_GLYPH_IMAGE_FORMATS_CFF |
        DWRITE_GLYPH_IMAGE_FORMATS_COLR |
        DWRITE_GLYPH_IMAGE_FORMATS_SVG |
        DWRITE_GLYPH_IMAGE_FORMATS_PNG |
        DWRITE_GLYPH_IMAGE_FORMATS_JPEG |
        DWRITE_GLYPH_IMAGE_FORMATS_TIFF |
        DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8;

    // Perform color translation.
    wil::com_ptr<IDWriteColorGlyphRunEnumerator1> colorRunEnumerator;
    HRESULT hr = m_dwriteFactory->TranslateColorGlyphRun(
        baselineOrigin,
        glyphRun,
        glyphRunDescription,
        desiredGlyphImageFormats,
        measuringMode,
        reinterpret_cast<DWRITE_MATRIX const*>(&transform),
        /*colorPaletteIndex*/ 0,
        /*out*/ & colorRunEnumerator
    );

    // Handle DWRITE_E_NOCOLOR, which is returned if the base glyph run doesn't
    // have any color glyphs in the desired glyph image formats. In that case,
    // just render the base glyph run as a monochrome glyph run.
    if (hr == DWRITE_E_NOCOLOR)
    {
        // Note: Direct2D drawing methods return void. If a drawing
        // operation fails, then an error is returned by EndDraw.
        m_deviceContext->DrawGlyphRun(
            baselineOrigin,
            glyphRun,
            foregroundBrush.get(),
            measuringMode
        );
        return S_OK;
    }

    // Any other failure HRESULT from TranslateColorGlyphRun is an error.
    RETURN_IF_FAILED(hr);

    // Solid color brush to be lazily created if needed.
    wil::com_ptr<ID2D1SolidColorBrush> solidBrush;

    // Use the returned enumerator object to iterate over the color glyph runs.
    for (;;)
    {
        // Advanced to the first or next run.
        BOOL haveRun;
        RETURN_IF_FAILED(colorRunEnumerator->MoveNext(&haveRun));
        if (!haveRun)
            break;

        // Retrieve a pointer to the color glyph run structure.
        DWRITE_COLOR_GLYPH_RUN1 const* colorGlyphRun;
        RETURN_IF_FAILED(colorRunEnumerator->GetCurrentRun(&colorGlyphRun));

        // Determine the brush to use for this color glyph run.
        wil::com_ptr<ID2D1Brush> runBrush;
        if (colorGlyphRun->paletteIndex == DWRITE_NO_PALETTE_INDEX)
        {
            // Special palette index meaning use the text foreground brush.
            runBrush = foregroundBrush;
        }
        else
        {
            // Use the specified color from the font's color palette.
            // Lazily create the solid color brush, or set its color if already created.
            if (solidBrush == nullptr)
            {
                RETURN_IF_FAILED(m_deviceContext->CreateSolidColorBrush(
                    colorGlyphRun->runColor,
                    &solidBrush
                    ));
            }
            else
            {
                solidBrush->SetColor(colorGlyphRun->runColor);
            }

            // Use the solid color brush as the current run's brush.
            runBrush = solidBrush;
        }

        // Branch depending on the run's glyph image format.
        switch (colorGlyphRun->glyphImageFormat)
        {
        case DWRITE_GLYPH_IMAGE_FORMATS_NONE:
            // do nothing
            break;

        case DWRITE_GLYPH_IMAGE_FORMATS_PNG:
        case DWRITE_GLYPH_IMAGE_FORMATS_JPEG:
        case DWRITE_GLYPH_IMAGE_FORMATS_TIFF:
        case DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8:
            // Note: Direct2D drawing methods return void. If a drawing
            // operation fails, then an error is returned by EndDraw.
            m_deviceContext->DrawColorBitmapGlyphRun(
                colorGlyphRun->glyphImageFormat,
                baselineOrigin,
                &colorGlyphRun->glyphRun,
                colorGlyphRun->measuringMode,
                D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_DEFAULT
            );
            break;

        case DWRITE_GLYPH_IMAGE_FORMATS_SVG:
            // Note: Direct2D drawing methods return void. If a drawing
            // operation fails, then an error is returned by EndDraw.
            m_deviceContext->DrawSvgGlyphRun(
                baselineOrigin,
                &colorGlyphRun->glyphRun,
                runBrush.get(),
                /*SVG style*/ nullptr,
                /*colorPaletteIndex*/ 0,
                colorGlyphRun->measuringMode
            );
            break;

        default:
            // Treat any other format as a monochrome glyph run.
            // This is used for monochrome glyphs, or for each layer
            // of a glyph in DWRITE_GLYPH_IMAGE_FORMATS_COLR.
            m_deviceContext->DrawGlyphRun(
                baselineOrigin,
                &colorGlyphRun->glyphRun,
                colorGlyphRun->glyphRunDescription,
                runBrush.get(),
                colorGlyphRun->measuringMode
            );
            break;
        }
    }
    return S_OK;
}
```

### Using Color Paint APIs

A color glyph in the **DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE** format is represented as a visual
tree of graphical elements called _paint elements_. The example in this section demonstrates how to
use the **IDWritePaintReader** interface to traverse the tree of paint elements for a glyph.

The **DumpPaintTree** sample function in this section doesn't render a color glyph, but outputs a
textual representation of its paint tree. Following is an example of the output:

```console
  - glyphIndex: 35
  - clipBox: { 0, -1, 0.5, -0.5 }
  - attributes: DWRITE_PAINT_ATTRIBUTES_USES_PALETTE
  - paintTree:
    DWRITE_PAINT_TYPE_COMPOSITE:
      - mode: DWRITE_COLOR_COMPOSITE_SRC_OVER
      - children (source, destination):
        DWRITE_PAINT_TYPE_SOLID_GLYPH:
          - glyphIndex: 84
          - color: { 0.501961, 0.501961, 0.501961, 0.400024 }
        DWRITE_PAINT_TYPE_COLOR_GLYPH:
          - glyphIndex: 88
          - clipBox: { 0.1, -0.9, 0.9, -0.1 }
          - child:
            DWRITE_PAINT_TYPE_COLOR_GLYPH:
              - glyphIndex: 20
              - clipBox: { 0, -1, 1, -0 }
              - child:
                DWRITE_PAINT_TYPE_GLYPH:
                  - glyphIndex: 82
                  - child:
                    DWRITE_PAINT_TYPE_RADIAL_GRADIENT:
                      - center0: (0.166, -0.768)
                      - radius0: 0
                      - center1: (0.166, -0.768)
                      - radius1: 0.256
                      - extendMode: D2D1_EXTEND_MODE_MIRROR (2)
                      - gradientStops:
                        D2D1_GRADIENT_STOP:
                          - position: 0
                          - color: { 0, 0.501961, 0, 1 }
                        D2D1_GRADIENT_STOP:
                          - position: 0.5
                          - color: { 1, 1, 1, 1 }
                        D2D1_GRADIENT_STOP:
                          - position: 1
                          - color: { 1, 0, 0, 1 }
```

For convenience, the sample defines **Indent** and **PropName** helper types with associated stream
output operators. It also defines stream output operators for various API types. These helper types
and operators are shown at the end of this section.

The **DumpPaintTree** function creates an **IDWritePaintReader** object, sets the current glyph, outputs
the glyph properties, and then calls the recursive **DumpPaintElement** function to output the tree of
paint elements.

```cpp
void DumpPaintTree(std::ostream& out, IDWriteFontFace7* fontFace, uint32_t glyphIndex)
{
    wil::com_ptr<IDWritePaintReader> paintReader;
    THROW_IF_FAILED(fontFace->CreatePaintReader(
        DWRITE_GLYPH_IMAGE_FORMATS_COLR_PAINT_TREE,
        DWRITE_PAINT_FEATURE_LEVEL_COLR_V1,
        &paintReader
    ));

    DWRITE_PAINT_ELEMENT paintElement;
    D2D_RECT_F clipBox;
    DWRITE_PAINT_ATTRIBUTES attributes;
    THROW_IF_FAILED(paintReader->SetCurrentGlyph(glyphIndex, &paintElement, &clipBox, &attributes));

    out << PropName{ "glyphIndex" } << glyphIndex << '\n'
        << PropName{ "clipBox" } << clipBox << '\n'
        << PropName{ "attributes" } << attributes << '\n'
        << PropName{ "paintTree" } << '\n';
    DumpPaintElement(out, Indent{ 1 }, paintReader.get(), paintElement);
}
```

The recursive **DumpPaintElement** function outputs a description of the specified paint element and
its children. The **DWRITE_PAINT_ELEMENT** structure is a tagged union. The **DumpPaintElement**
branches on its **paintType** member to determine what to write.

```cpp
void DumpPaintElement(std::ostream& out, Indent indent, IDWritePaintReader* reader, DWRITE_PAINT_ELEMENT& element)
{
    // Helper to write gradient information, for gradient paint types.
    auto WriteGradient = [&](D2D1_EXTEND_MODE extendMode, uint32_t gradientStopCount)
    {
        out << indent << PropName{ "extendMode" } << extendMode << '\n';
        out << indent << PropName{ "gradientStops" } << '\n';
        DumpGradientStops(out, indent + 1, reader, gradientStopCount);
    };

    // Helper to recursively call DumpPaintElement for a child paint element.
    auto Recurse = [&]()
    {
        DumpPaintElement(out, indent + 1, reader, element);
    };

    // Helper to write the specified number of children.
    // The number of children is specified by the caller, because it depends on
    // the paint type. See the documentation for the DWRITE_PAINT_ELEMENT structure
    // for more information.
    auto WriteChildren = [&](uint32_t childCount)
    {
        if (childCount != 0)
        {
            HR(reader->MoveToFirstChild(&element));
            Recurse();

            for (uint32_t i = 1; i < childCount; i++)
            {
                HR(reader->MoveToNextSibling(&element));
                Recurse();
            }

            HR(reader->MoveToParent());
        }
    };

    // Write information about the paint element, depending on its type.
    switch (element.paintType)
    {
    case DWRITE_PAINT_TYPE_NONE:
        out << indent << "DWRITE_PAINT_TYPE_NONE\n";
        break;

    case DWRITE_PAINT_TYPE_LAYERS:
    {
        out << indent << "DWRITE_PAINT_TYPE_LAYERS:\n";
        auto const& paint = element.paint.layers;
        // Write the children.
        // A layers paint element has a variable number of children.
        WriteChildren(paint.childCount);
        break;
    }

    case DWRITE_PAINT_TYPE_SOLID_GLYPH:
    {
        auto const& paint = element.paint.solidGlyph;
        // Write the properties.
        // A solid glyph paint element has no children.
        out << indent << "DWRITE_PAINT_TYPE_SOLID_GLYPH:\n"
            << indent << PropName{ "glyphIndex" } << paint.glyphIndex << '\n'
            << indent << PropName{ "color" } << paint.color.value << '\n';
        break;
    }

    case DWRITE_PAINT_TYPE_SOLID:
    {
        auto const& paint = element.paint.solid;
        // Write the properties.
        // A solid paint element has no children.
        out << indent << "DWRITE_PAINT_TYPE_SOLID:\n"
            << indent << PropName{ "color" } << paint.value << '\n';
        break;
    }

    case DWRITE_PAINT_TYPE_LINEAR_GRADIENT:
    {
        auto const& paint = element.paint.linearGradient;
        // Write the properties, including gradient stops.
        // A linear gradient paint element has no children.
        out << indent << "DWRITE_PAINT_TYPE_LINEAR_GRADIENT:\n"
            << indent << PropName{ "p0" } << D2D_POINT_2F{ paint.x0, paint.y0 } << '\n'
            << indent << PropName{ "p1" } << D2D_POINT_2F{ paint.x1, paint.y1 } << '\n'
            << indent << PropName{ "p2" } << D2D_POINT_2F{ paint.x2, paint.y2 } << '\n';
        WriteGradient(static_cast<D2D1_EXTEND_MODE>(paint.extendMode), paint.gradientStopCount);
        break;
    }

    case DWRITE_PAINT_TYPE_RADIAL_GRADIENT:
    {
        auto const& paint = element.paint.radialGradient;
        // Write the properties, including gradient stops.
        // A radial gradient paint element has no children.
        out << indent << "DWRITE_PAINT_TYPE_RADIAL_GRADIENT:\n"
            << indent << PropName{ "center0" } << D2D_POINT_2F{ paint.x0, paint.y0 } << '\n'
            << indent << PropName{ "radius0" } << paint.radius0 << '\n'
            << indent << PropName{ "center1" } << D2D_POINT_2F{ paint.x1, paint.y1 } << '\n'
            << indent << PropName{ "radius1" } << paint.radius1 << '\n';
        WriteGradient(static_cast<D2D1_EXTEND_MODE>(paint.extendMode), paint.gradientStopCount);
        break;
    }

    case DWRITE_PAINT_TYPE_SWEEP_GRADIENT:
    {
        auto const& paint = element.paint.sweepGradient;
        // Write the properties, including gradient stops.
        // A sweep gradient paint element has no children.
        out << indent << "DWRITE_PAINT_TYPE_SWEEP_GRADIENT:\n"
            << indent << PropName{ "center" } << D2D_POINT_2F{ paint.centerX, paint.centerY } << '\n'
            << indent << PropName{ "startAngle" } << paint.startAngle << '\n'
            << indent << PropName{ "endAngle" } << paint.endAngle << '\n';
        WriteGradient(static_cast<D2D1_EXTEND_MODE>(paint.extendMode), paint.gradientStopCount);
        break;
    }

    case DWRITE_PAINT_TYPE_GLYPH:
    {
        auto const& paint = element.paint.glyph;
        // Write the properties and the child element.
        // A glyph paint element always has one child, which represents the fill
        // for the glyph shape.
        out << indent << "DWRITE_PAINT_TYPE_GLYPH:\n"
            << indent << PropName{ "glyphIndex" } << paint.glyphIndex << '\n'
            << indent << PropName{ "child" } << '\n';
        WriteChildren(1);
        break;
    }

    case DWRITE_PAINT_TYPE_COLOR_GLYPH:
    {
        auto const& paint = element.paint.colorGlyph;
        // Write the properties and the child element.
        // A color glyph paint element always has one child, which is the root
        // of the paint tree for the glyph specified by glyphIndex.
        out << indent << "DWRITE_PAINT_TYPE_COLOR_GLYPH:\n"
            << indent << PropName{ "glyphIndex" } << paint.glyphIndex << '\n'
            << indent << PropName{ "clipBox" } << paint.clipBox << '\n'
            << indent << PropName{ "child" } << '\n';
        WriteChildren(1);
        break;
    }

    case DWRITE_PAINT_TYPE_TRANSFORM:
    {
        DWRITE_MATRIX const& paint = element.paint.transform;
        // Write the properties and the child element.
        // A transform paint element always has one child, which represents the
        // transformed content.
        out << indent << "DWRITE_PAINT_TYPE_TRANSFORM:\n"
            << indent << PropName{ "transform" } << paint << '\n'
            << indent << PropName{ "child" } << '\n';
        WriteChildren(1);
        break;
    }

    case DWRITE_PAINT_TYPE_COMPOSITE:
    {
        auto const& paint = element.paint.composite;
        // Write the properties and the child elements.
        // A composite paint element always has two children, which represent
        // the source and destination of the composite operation.
        out << indent << "DWRITE_PAINT_TYPE_COMPOSITE:\n"
            << indent << PropName{ "mode" } << paint.mode << '\n'
            << indent << PropName{ "children (source, destination)" } << '\n';
        WriteChildren(2);
        break;
    }

    default:
        out << indent << "Unknown paint type: " << element.paintType << '\n';
        break;
    }
}
```

The **DumpPaintElement** function calls the following **DumpGradientStops** function to output the array
of gradient stops for a paint element:

```cpp
void DumpGradientStops(std::ostream& out, Indent indent, IDWritePaintReader* reader, uint32_t gradientStopCount)
{
    std::vector<D2D1_GRADIENT_STOP> stops;
    stops.resize(gradientStopCount);
    HR(reader->GetGradientStops(0, gradientStopCount, /*out*/ stops.data()));

    for (auto& stop : stops)
    {
        out << indent << "D2D1_GRADIENT_STOP:\n"
            << indent << PropName{ "position" } << stop.position << '\n'
            << indent << PropName{ "color" } << stop.color << '\n';
    }
}
```

The **Indent** helper type represents the indent level. Its associated stream operator outputs four
spaces for each level of indent:

```cpp
struct Indent { int value; };
std::ostream& operator<<(std::ostream& out, Indent const& indent)
{
    for (int i = 0; i < indent.value; i++)
    {
        out << "    ";
    }
    return out;
}
Indent operator+(Indent lhs, int rhs)
{
    return Indent{ lhs.value + rhs };
}
```

The **PropName** helper type represents a property name:

```cpp
struct PropName { char const* name; };
std::ostream& operator<<(std::ostream& out, PropName const& value)
{
    return out << "  - " << value.name << ": ";
}
```

For convenience, the sample uses the following stream output operators:

```cpp
std::ostream& operator<<(std::ostream& out, DWRITE_COLOR_F const& value)
{
    return out << "{ " << value.r << ", " << value.g << ", " << value.b << ", " << value.a << " }";
}

std::ostream& operator<<(std::ostream& out, D2D_POINT_2F const& value)
{
    return out << '(' << value.x << ", " << value.y << ')';
}

std::ostream& operator<<(std::ostream& out, D2D_RECT_F const& value)
{
    return out << "{ "
        << value.left << ", "
        << value.top << ", "
        << value.right << ", "
        << value.bottom
        << " }";
}

std::ostream& operator<<(std::ostream& out, DWRITE_MATRIX const& value)
{
    return out << "{ "
        << value.m11 << ", "
        << value.m12 << ", "
        << value.m21 << ", "
        << value.m22 << ", "
        << value.dx << ", "
        << value.dy << " }";
}

std::ostream& operator<<(std::ostream& out, D2D1_EXTEND_MODE value)
{
    switch (value)
    {
    case D2D1_EXTEND_MODE_CLAMP: return out << "D2D1_EXTEND_MODE_CLAMP (0)";
    case D2D1_EXTEND_MODE_WRAP: return out << "D2D1_EXTEND_MODE_WRAP (1)";
    case D2D1_EXTEND_MODE_MIRROR: return out << "D2D1_EXTEND_MODE_MIRROR (2)";
    default: return out << (int)value;
    }
}

std::ostream& operator<<(std::ostream& out, DWRITE_PAINT_ATTRIBUTES value)
{
    switch (value)
    {
    case DWRITE_PAINT_ATTRIBUTES_USES_PALETTE:
        return out << "DWRITE_PAINT_ATTRIBUTES_USES_PALETTE";

    case DWRITE_PAINT_ATTRIBUTES_USES_TEXT_COLOR:
        return out << "DWRITE_PAINT_ATTRIBUTES_USES_TEXT_COLOR";

    case DWRITE_PAINT_ATTRIBUTES_USES_PALETTE | DWRITE_PAINT_ATTRIBUTES_USES_TEXT_COLOR:
        return out << "DWRITE_PAINT_ATTRIBUTES_USES_PALETTE | DWRITE_PAINT_ATTRIBUTES_USES_TEXT_COLOR";

    default:
        return out << (int)value;
    }
}

std::ostream& operator<<(std::ostream& out, DWRITE_COLOR_COMPOSITE_MODE value)
{
    switch (value)
    {
    case DWRITE_COLOR_COMPOSITE_CLEAR: return out << "DWRITE_COLOR_COMPOSITE_CLEAR";
    case DWRITE_COLOR_COMPOSITE_SRC: return out << "DWRITE_COLOR_COMPOSITE_SRC";
    case DWRITE_COLOR_COMPOSITE_DEST: return out << "DWRITE_COLOR_COMPOSITE_DEST";
    case DWRITE_COLOR_COMPOSITE_SRC_OVER: return out << "DWRITE_COLOR_COMPOSITE_SRC_OVER";
    case DWRITE_COLOR_COMPOSITE_DEST_OVER: return out << "DWRITE_COLOR_COMPOSITE_DEST_OVER";
    case DWRITE_COLOR_COMPOSITE_SRC_IN: return out << "DWRITE_COLOR_COMPOSITE_SRC_IN";
    case DWRITE_COLOR_COMPOSITE_DEST_IN: return out << "DWRITE_COLOR_COMPOSITE_DEST_IN";
    case DWRITE_COLOR_COMPOSITE_SRC_OUT: return out << "DWRITE_COLOR_COMPOSITE_SRC_OUT";
    case DWRITE_COLOR_COMPOSITE_DEST_OUT: return out << "DWRITE_COLOR_COMPOSITE_DEST_OUT";
    case DWRITE_COLOR_COMPOSITE_SRC_ATOP: return out << "DWRITE_COLOR_COMPOSITE_SRC_ATOP";
    case DWRITE_COLOR_COMPOSITE_DEST_ATOP: return out << "DWRITE_COLOR_COMPOSITE_DEST_ATOP";
    case DWRITE_COLOR_COMPOSITE_XOR: return out << "DWRITE_COLOR_COMPOSITE_XOR";
    case DWRITE_COLOR_COMPOSITE_PLUS: return out << "DWRITE_COLOR_COMPOSITE_PLUS";

    case DWRITE_COLOR_COMPOSITE_SCREEN: return out << "DWRITE_COLOR_COMPOSITE_SCREEN";
    case DWRITE_COLOR_COMPOSITE_OVERLAY: return out << "DWRITE_COLOR_COMPOSITE_OVERLAY";
    case DWRITE_COLOR_COMPOSITE_DARKEN: return out << "DWRITE_COLOR_COMPOSITE_DARKEN";
    case DWRITE_COLOR_COMPOSITE_LIGHTEN: return out << "DWRITE_COLOR_COMPOSITE_LIGHTEN";
    case DWRITE_COLOR_COMPOSITE_COLOR_DODGE: return out << "DWRITE_COLOR_COMPOSITE_COLOR_DODGE";
    case DWRITE_COLOR_COMPOSITE_COLOR_BURN: return out << "DWRITE_COLOR_COMPOSITE_COLOR_BURN";
    case DWRITE_COLOR_COMPOSITE_HARD_LIGHT: return out << "DWRITE_COLOR_COMPOSITE_HARD_LIGHT";
    case DWRITE_COLOR_COMPOSITE_SOFT_LIGHT: return out << "DWRITE_COLOR_COMPOSITE_SOFT_LIGHT";
    case DWRITE_COLOR_COMPOSITE_DIFFERENCE: return out << "DWRITE_COLOR_COMPOSITE_DIFFERENCE";
    case DWRITE_COLOR_COMPOSITE_EXCLUSION: return out << "DWRITE_COLOR_COMPOSITE_EXCLUSION";
    case DWRITE_COLOR_COMPOSITE_MULTIPLY: return out << "DWRITE_COLOR_COMPOSITE_MULTIPLY";

    case DWRITE_COLOR_COMPOSITE_HSL_HUE: return out << "DWRITE_COLOR_COMPOSITE_HSL_HUE";
    case DWRITE_COLOR_COMPOSITE_HSL_SATURATION: return out << "DWRITE_COLOR_COMPOSITE_HSL_SATURATION";
    case DWRITE_COLOR_COMPOSITE_HSL_COLOR: return out << "DWRITE_COLOR_COMPOSITE_HSL_COLOR";
    case DWRITE_COLOR_COMPOSITE_HSL_LUMINOSITY: return out << "DWRITE_COLOR_COMPOSITE_HSL_LUMINOSITY";
    default: return out << (int)value;
    }
}
```

## Related topics

[Color font support](color-fonts.md)
