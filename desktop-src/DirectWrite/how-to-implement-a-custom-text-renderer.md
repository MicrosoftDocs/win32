---
title: Render Using a Custom Text Renderer
description: A DirectWrite \ 160;text layout can be drawn by a custom text renderer derived from IDWriteTextRenderer.
ms.assetid: a5b09733-24b2-408e-a1f9-cf7ad20c5c63
ms.topic: article
ms.date: 05/31/2018
---

# Render Using a Custom Text Renderer

A [DirectWrite](direct-write-portal.md) [**text layout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) can be drawn by a custom text renderer derived from [**IDWriteTextRenderer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer). A custom renderer is required to take advantage of some advanced features of DirectWrite, such as rendering to a bitmap or GDI surface, inline objects, and client drawing effects. This tutorial describes the methods of **IDWriteTextRenderer**, and provides an example implementation that uses [Direct2D](../direct2d/direct2d-portal.md) to render text with a bitmap fill.

This tutorial contains the following parts:

-   [The Constructor](#the-constructor)
-   [DrawGlyphRun()](#drawglyphrun)
-   [DrawUnderline() and DrawStrikethrough()](#drawunderline-and-drawstrikethrough)
-   [Pixel Snapping, Pixels per DIP, and Transform](#pixel-snapping-pixels-per-dip-and-transform)
    -   [IsPixelSnappingDisabled()](#ispixelsnappingdisabled)
    -   [GetCurrentTransform()](#getcurrenttransform)
    -   [GetPixelsPerDip()](#getpixelsperdip)
-   [DrawInlineObject()](#drawinlineobject)
-   [The Destructor](#the-destructor)
-   [Using the Custom Text Renderer](#using-the-custom-text-renderer)

Your custom text renderer must implement the methods inherited from IUnknown in addition to the methods listed on the [**IDWriteTextRenderer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer) reference page and below.

For the full source code for the custom text renderer, see the CustomTextRenderer.cpp and CustomTextRenderer.h files of the [DirectWrite Hello World Sample](/samples/browse/?redirectedfrom=MSDN-samples).

## The Constructor

Your custom text renderer will need a constructor. This example uses both solid and bitmap [Direct2D](../direct2d/direct2d-portal.md) brushes to render the text.

Because of this, the constructor takes the parameters found in the table below with descriptions.



| Parameter       | Description                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *pD2DFactory*   | A pointer to an [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) object that will be used to create any Direct2D resources that are needed.                                                                                                        |
| *pRT*           | A pointer to the [**ID2D1HwndRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1hwndrendertarget) object that the text will be rendered to. |
| *pOutlineBrush* | A pointer to the [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1solidcolorbrush) that will be use to draw outline of the text                                                                                                                     |
| *pFillBrush*    | A pointer to the [**ID2D1BitmapBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmapbrush) that will be used to fill the text.                                                                                                                                      |



 

These will be stored by the constructor as shown in the following code.


```C++
CustomTextRenderer::CustomTextRenderer(
    ID2D1Factory* pD2DFactory, 
    ID2D1HwndRenderTarget* pRT, 
    ID2D1SolidColorBrush* pOutlineBrush, 
    ID2D1BitmapBrush* pFillBrush
    )
:
cRefCount_(0), 
pD2DFactory_(pD2DFactory), 
pRT_(pRT), 
pOutlineBrush_(pOutlineBrush), 
pFillBrush_(pFillBrush)
{
    pD2DFactory_->AddRef();
    pRT_->AddRef();
    pOutlineBrush_->AddRef();
    pFillBrush_->AddRef();
}
```



## DrawGlyphRun()

The [**DrawGlyphRun**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawglyphrun) method is the main callback method of the text renderer. It is passed a run of glyphs to be rendered in addition to information such as the baseline origin and measuring mode. It also passes a client drawing effect object to be applied to the glyph run. For more information, see the [How to Add Client Drawing Effects to a Text Layout](how-to-add-custom-drawing-efffects-to-a-text-layout.md) topic.

This text renderer implementation renders glyph runs by converting them to [Direct2D](rendering-by-using-direct2d.md) geometries and then drawing and filling the geometries. This consists of the following steps.

1.  Create an [**ID2D1PathGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1pathgeometry) object, and then retrieve the [**ID2D1GeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrysink) object by using the [**ID2D1PathGeometry::Open**](/windows/win32/api/d2d1/nf-d2d1-id2d1pathgeometry-open) method.

    ```C++
    // Create the path geometry.
    ID2D1PathGeometry* pPathGeometry = NULL;
    hr = pD2DFactory_->CreatePathGeometry(
            &pPathGeometry
            );

    // Write to the path geometry using the geometry sink.
    ID2D1GeometrySink* pSink = NULL;
    if (SUCCEEDED(hr))
    {
        hr = pPathGeometry->Open(
            &pSink
            );
    }
    ```

    

2.  The [**DWRITE\_GLYPH\_RUN**](/windows/win32/api/dwrite/ns-dwrite-dwrite_glyph_run) that is passed to [**DrawGlyphRun**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawglyphrun) contains a [**IDWriteFontFace**](/windows/win32/api/dwrite/nn-dwrite-idwritefontface) object, named *fontFace*, that represents the font face for the whole glyph run. Put the outline of the glyph run into the geometry sink by using the [**IDWriteFontFace:: GetGlyphRunOutline**](/windows/win32/api/dwrite/nf-dwrite-idwritefontface-getglyphrunoutline) method, as shown in the following code.

    ```C++
    // Get the glyph run outline geometries back from DirectWrite and place them within the
    // geometry sink.
    if (SUCCEEDED(hr))
    {
        hr = glyphRun->fontFace->GetGlyphRunOutline(
            glyphRun->fontEmSize,
            glyphRun->glyphIndices,
            glyphRun->glyphAdvances,
            glyphRun->glyphOffsets,
            glyphRun->glyphCount,
            glyphRun->isSideways,
            glyphRun->bidiLevel%2,
            pSink
            );
    }
    ```

    

3.  After filling the geometry sink, close it.

    ```C++
    // Close the geometry sink
    if (SUCCEEDED(hr))
    {
        hr = pSink->Close();
    }
    ```

    

4.  The origin of the glyph run must be translated so that it is rendered from the correct baseline origin, as shown in the following code.

    ```C++
    // Initialize a matrix to translate the origin of the glyph run.
    D2D1::Matrix3x2F const matrix = D2D1::Matrix3x2F(
        1.0f, 0.0f,
        0.0f, 1.0f,
        baselineOriginX, baselineOriginY
        );
    ```

    

    The *baselineOriginX* and *baselineOriginY* are passed as parameters to the [**DrawGlyphRun**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawglyphrun) callback method.

5.  Create the transformed geometry by using the [**ID2D1Factory::CreateTransformedGeometry**](../direct2d/id2d1factory-createtransformedgeometry.md) method and passing the path geometry and the translation matrix.

    ```C++
    // Create the transformed geometry
    ID2D1TransformedGeometry* pTransformedGeometry = NULL;
    if (SUCCEEDED(hr))
    {
        hr = pD2DFactory_->CreateTransformedGeometry(
            pPathGeometry,
            &matrix,
            &pTransformedGeometry
            );
    }
    ```

    

6.  Finally, draw the outline of the transformed geometry, and fill it by using the [**ID2D1RenderTarget::DrawGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawgeometry) and [**ID2D1RenderTarget::FillGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillgeometry) methods and the [Direct2D](../direct2d/direct2d-portal.md) brushes stored as member variables.

    ```C++
        // Draw the outline of the glyph run
        pRT_->DrawGeometry(
            pTransformedGeometry,
            pOutlineBrush_
            );

        // Fill in the glyph run
        pRT_->FillGeometry(
            pTransformedGeometry,
            pFillBrush_
            );
    ```

    

7.  Now that you are finished drawing, do not forget to clean up the objects that were created in this method.

    ```C++
    SafeRelease(&pPathGeometry);
    SafeRelease(&pSink);
    SafeRelease(&pTransformedGeometry);
    ```

    

## DrawUnderline() and DrawStrikethrough()

[**IDWriteTextRenderer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer) also has callbacks for drawing the underline and strikethrough. This example draws a simple rectangle for an underline or strikethrough, but other shapes can be drawn.

Drawing an underline by using [Direct2D](../direct2d/direct2d-portal.md) consists of the following steps.

1.  First, create a [**D2D1\_RECT\_F**](../direct2d/d2d1-rect-f.md) structure of the size and shape of the underline. The [**DWRITE\_UNDERLINE**](/windows/win32/api/dwrite/ns-dwrite-dwrite_underline) structure that is passed to the [**DrawUnderline**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawunderline) callback method provides the offset, width, and thickness of the underline.

    ```C++
    D2D1_RECT_F rect = D2D1::RectF(
        0,
        underline->offset,
        underline->width,
        underline->offset + underline->thickness
        );
    ```

    

2.  Next, create an [**ID2D1RectangleGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1rectanglegeometry) object by using the [**ID2D1Factory::CreateRectangleGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createrectanglegeometry(constd2d1_rect_f_id2d1rectanglegeometry)) method and the initialized [**D2D1\_RECT\_F**](../direct2d/d2d1-rect-f.md) structure.

    ```C++
    ID2D1RectangleGeometry* pRectangleGeometry = NULL;
    hr = pD2DFactory_->CreateRectangleGeometry(
            &rect, 
            &pRectangleGeometry
            );
    ```

    

3.  As with the glyph run, the origin of the underline geometry must be translated, based on the baseline origin values, by using the [**CreateTransformedGeometry**](../direct2d/id2d1factory-createtransformedgeometry.md) method.

    ```C++
    // Initialize a matrix to translate the origin of the underline
    D2D1::Matrix3x2F const matrix = D2D1::Matrix3x2F(
        1.0f, 0.0f,
        0.0f, 1.0f,
        baselineOriginX, baselineOriginY
        );

    ID2D1TransformedGeometry* pTransformedGeometry = NULL;
    if (SUCCEEDED(hr))
    {
        hr = pD2DFactory_->CreateTransformedGeometry(
            pRectangleGeometry,
            &matrix,
            &pTransformedGeometry
            );
    }
    ```

    

4.  Finally, draw the outline of the transformed geometry, and fill it by using the [**ID2D1RenderTarget::DrawGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawgeometry) and [**ID2D1RenderTarget::FillGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillgeometry) methods and the [Direct2D](../direct2d/direct2d-portal.md) brushes stored as member variables.

    ```C++
        // Draw the outline of the glyph run
        pRT_->DrawGeometry(
            pTransformedGeometry,
            pOutlineBrush_
            );

        // Fill in the glyph run
        pRT_->FillGeometry(
            pTransformedGeometry,
            pFillBrush_
            );
    ```

    

5.  Now that you are finished drawing, do not forget to clean up the objects that were created in this method.

    ```C++
    SafeRelease(&pRectangleGeometry);
    SafeRelease(&pTransformedGeometry);
    ```

    

The process for drawing a strikethrough is the same. However, the strikethrough will have a different offset, and likely a different width and thickness.

## Pixel Snapping, Pixels per DIP, and Transform

### IsPixelSnappingDisabled()

This method is called to determine whether pixel snapping is disabled. The recommended default is **FALSE**, and that is the output of this example.


```C++
*isDisabled = FALSE;
```



### GetCurrentTransform()

This example renders to a Direct2D render target, so forward the transform from the render target using [**ID2D1RenderTarget::GetTransform**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-gettransform).


```C++
//forward the render target's transform
pRT_->GetTransform(reinterpret_cast<D2D1_MATRIX_3X2_F*>(transform));
```



### GetPixelsPerDip()

This method is called to get the number of pixels per Device Independent Pixel (DIP).


```C++
float x, yUnused;

pRT_->GetDpi(&x, &yUnused);
*pixelsPerDip = x / 96;
```



## DrawInlineObject()

A custom text renderer also has a callback for drawing inline objects. In this example, [**DrawInlineObject**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawinlineobject) returns E\_NOTIMPL. An explanation of how to draw inline objects is beyond the scope of this tutorial. For more information, see the [How to Add Inline Objects to a Text Layout](how-to-add-inline-objects-to-a-text-layout.md) topic.

## The Destructor

It is important to release any pointers that were used by the custom text renderer class.


```C++
CustomTextRenderer::~CustomTextRenderer()
{
    SafeRelease(&pD2DFactory_);
    SafeRelease(&pRT_);
    SafeRelease(&pOutlineBrush_);
    SafeRelease(&pFillBrush_);
}
```



## Using the Custom Text Renderer

You render with the custom renderer by using the [**IDWriteTextLayout::Draw**](/windows/win32/api/dwrite/nf-dwrite-idwritetextlayout-draw) method, which takes a callback interface derived from [**IDWriteTextRenderer**](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer) as an argument, as shown in the following code.


```C++
// Draw the text layout using DirectWrite and the CustomTextRenderer class.
hr = pTextLayout_->Draw(
        NULL,
        pTextRenderer_,  // Custom text renderer.
        origin.x,
        origin.y
        );

```



The [**IDWriteTextLayout::Draw**](/windows/win32/api/dwrite/nf-dwrite-idwritetextlayout-draw) method calls the methods of the custom renderer callback you provide. The [**DrawGlyphRun**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawglyphrun), [**DrawUnderline**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawunderline), [**DrawInlineObject**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawinlineobject), and [**DrawStrikethrough**](/windows/win32/api/dwrite/nf-dwrite-idwritetextrenderer-drawstrikethrough) methods described above perform the drawing functions.

 

 