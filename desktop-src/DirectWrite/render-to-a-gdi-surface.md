---
title: Render to a GDI Surface
description: Render to a GDI Surface
ms.assetid: 'a6096ff5-1e6e-4edb-b455-ea5d205072ff'
---

# Render to a GDI Surface

In some cases, you may want to be able to display [DirectWrite](direct-write-portal.md) text on a GDI surface. The [**IDWriteBitmapRenderTarget**](idwritebitmaprendertarget.md) interface encapsulates a bitmap and device context to render text onto. You create an **IDWriteBitmapRenderTarget** by using the [**IDWriteGdiInterop::CreateBitmapRenderTarget**](idwritegdiinterop-createbitmaprendertarget.md) method, as shown in the following code.


```C++
if (SUCCEEDED(hr))
{
    hr = g_pGdiInterop->CreateBitmapRenderTarget(hdc, r.right, r.bottom, &amp;g_pBitmapRenderTarget);
}
```



To render with an [**IDWriteBitmapRenderTarget**](idwritebitmaprendertarget.md), you must implement a custom text renderer callback interface derived from the [**IDWriteTextRenderer**](idwritetextrenderer.md) interface. You must implement methods for drawing a glyph run, underline, strikethrough, inline objects, and so on. For a complete list of the methods, see the [**IDWriteTextRenderer**](idwritetextrenderer.md) reference page. Not every method must be implemented, they can just return **E\_NOTIMPL**, and drawing will continue.

You can then draw the text by using the [**IDWriteTextLayout::Draw**](idwritetextlayout-draw.md) method and passing the callback interface that you implemented as a parameter. The **IDWriteTextLayout::Draw** method calls the methods of the custom renderer callback you provide. The [**DrawGlyphRun**](idwritetextrenderer-drawglyphrun.md), [**DrawUnderline**](idwritetextrenderer-drawunderline.md), [**DrawInlineObject**](idwritetextrenderer-drawinlineobject.md), and [**DrawStrikethrough**](idwritetextrenderer-drawstrikethrough.md) methods perform the drawing functions.

In your implementation of [**DrawGlyphRun**](idwritetextrenderer-drawglyphrun.md), call the [**IDWriteBitmapRenderTarget::DrawGlyphRun**](idwritebitmaprendertarget-drawglyphrun.md) method to draw the glyphs. The rendering of the underline, strikethrough and inline objects must be done by your custom renderer.

[**IDWriteBitmapRenderTarget::DrawGlyphRun**](idwritebitmaprendertarget-drawglyphrun.md) has an optional RECT out parameter that contains the bounds of the area where the text was drawn. You can use this information to set the bounding rectangle for the device context with the [**SetBoundsRect**](https://msdn.microsoft.com/library/windows/desktop/dd162966) function that is provided by GDI. The following code is an example implementation of the [**DrawGlyphRun**](idwritetextrenderer-drawglyphrun.md) method of a custom renderer.


```C++
STDMETHODIMP GdiTextRenderer::DrawGlyphRun(
    __maybenull void* clientDrawingContext,
    FLOAT baselineOriginX,
    FLOAT baselineOriginY,
    DWRITE_MEASURING_MODE measuringMode,
    __in DWRITE_GLYPH_RUN const* glyphRun,
    __in DWRITE_GLYPH_RUN_DESCRIPTION const* glyphRunDescription,
    IUnknown* clientDrawingEffect
    )
{
    HRESULT hr = S_OK;

    // Pass on the drawing call to the render target to do the real work.
    RECT dirtyRect = {0};

    hr = pRenderTarget_->DrawGlyphRun(
        baselineOriginX,
        baselineOriginY,
        measuringMode,
        glyphRun,
        pRenderingParams_,
        RGB(0,200,255),
        &amp;dirtyRect
        );
    

    return hr;
}
```



The [**IDWriteBitmapRenderTarget**](idwritebitmaprendertarget.md) interface renders to a device context (DC) in memory. You get a handle to this DC by using the [**IDWriteBitmapRenderTarget::GetMemoryDC**](idwritebitmaprendertarget-getmemorydc.md) method. As soon as the drawing has been performed, the memory DC of the **IDWriteBitmapRenderTarget** object must be copied to the destination GDI surface.

You can retrieve the bounding rectangle by using the [**GetBoundsRect**](https://msdn.microsoft.com/library/windows/desktop/dd144854) function, then use the bounding rectangle with the [**BitBlt**](https://msdn.microsoft.com/library/windows/desktop/dd183370) function to copy the rendered [DirectWrite](direct-write-portal.md) text from the memory DC to the GDI surface as shown in the following code.


```C++
// Transfer from DWrite's rendering target to the window.
BitBlt(
    hdc,
    0, 0,
    size.cx, size.cy,
    memoryHdc,
    0, 0, 
    SRCCOPY | NOMIRRORBITMAP
    );
```



 

 




