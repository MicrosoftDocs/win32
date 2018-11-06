---
title: Rendering DirectWrite
description: Rendering DirectWrite
ms.assetid: e8099fac-b5d7-4fb1-b06d-a6e85da0d1dc
ms.topic: article
ms.date: 05/31/2018
---

# Rendering DirectWrite

## Rendering Options

Text with formatting described by only an [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) object can be rendered with [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx), however, there are a few more options for rendering an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object.

The string described by an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object can be rendered using the methods below.

## 1. Render using Direct2D

To render an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object using Direct2D, use the [**ID2D1RenderTarget::DrawTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd371913) method, as shown in the following code.


```C++
pRT_->DrawTextLayout(
    origin,
    pTextLayout_,
    pBlackBrush_
    );

```



For a more in depth look at drawing an [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/Dd316718(v=VS.85).aspx) object using [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx), see [Getting Started with DirectWrite](getting-started-with-directwrite.md).

## 2. Render using a custom text renderer.

You render with a custom renderer by using the [**IDWriteTextLayout::Draw**](https://msdn.microsoft.com/en-us/library/Dd316726(v=VS.85).aspx) method, which takes a callback interface derived from [**IDWriteTextRenderer**](https://msdn.microsoft.com/en-us/library/Dd371523(v=VS.85).aspx) as an argument, as shown in the following code.


```C++
// Draw the text layout using DirectWrite and the CustomTextRenderer class.
hr = pTextLayout_->Draw(
        NULL,
        pTextRenderer_,  // Custom text renderer.
        origin.x,
        origin.y
        );

```



The [**IDWriteTextLayout::Draw**](https://msdn.microsoft.com/en-us/library/Dd316726(v=VS.85).aspx) method calls the methods of the custom renderer callback you provide. The [**DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371526(v=VS.85).aspx), [**DrawUnderline**](https://msdn.microsoft.com/en-us/library/Dd371533(v=VS.85).aspx), [**DrawInlineObject**](https://msdn.microsoft.com/en-us/library/Dd371527(v=VS.85).aspx), and [**DrawStrikethrough**](https://msdn.microsoft.com/en-us/library/Dd371530(v=VS.85).aspx) methods perform the drawing functions.

[**IDWriteTextRenderer**](https://msdn.microsoft.com/en-us/library/Dd371523(v=VS.85).aspx) declares methods for drawing a glyph run, underline, strikethrough, and inline objects. It is up to the application to implement these methods. Creating a custom text renderer allows the application to apply additional effects when rendering text, such as a custom fill or outline. A sample custom text renderer is included in the [DirectWrite Hello World Sample](http://go.microsoft.com/fwlink/?LinkID=624680).

## 3. Render ClearType to a GDI surface.

Rendering to a GDI surface is actually an example of using a custom text renderer. However, some of the work is done for you in the form of the [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd368165(v=VS.85).aspx) interface.

To create this interface, use the [**IDWriteGdiInterop::CreateBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371182(v=VS.85).aspx) method.

The [**DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371526(v=VS.85).aspx) method of your custom text renderer calls the [**IDWriteBitmapRenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd368167(v=VS.85).aspx) method to draw the glyphs. The rendering of the underline, strikethrough, and inline objects must be done by your custom renderer.

The [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd368165(v=VS.85).aspx) interface renders to a device context (DC) in memory. You get a handle to this DC by using the [**IDWriteBitmapRenderTarget::GetMemoryDC**](https://msdn.microsoft.com/en-us/library/Dd368171(v=VS.85).aspx) method.


```C++
memoryHdc = g_pBitmapRenderTarget->GetMemoryDC();
```



Once the drawing has been performed, the memory DC of the [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd368165(v=VS.85).aspx) object must be copied to the destination GDI surface.

> [!Note]  
> You also have the option of transferring the bitmap to another type of surface, such as a GDI+ surface.

 


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



> [!Note]  
> Your app has the responsibility to render everything to the window in the end. This includes text and graphics. There is a performance penalty to this. Additionally, rendering to a memory DC is not GDI hardware accelerated.

 

For a more detailed overview of interoperating with GDI see [Interoperating with GDI](interoperating-with-gdi.md).

## 4. Render Grayscale Text Transparently to a GDI Surface. (Windows 8 and later)

Starting in Windows 8, you can render grayscale text transparently to a GDI surface for better performance. To do this you need to:

1.  Clear the memory DC to transparent.
2.  Render text to the memory HDC using grayscale antialiasing (DWRITE\_TEXT\_ANTIALIAS\_MODE\_GRAYSCALE).
3.  Use the [**AlphaBlend**](https://msdn.microsoft.com/library/windows/desktop/dd183351) function to render the memory HDC transparently on top of the final target HDC.
4.  Repeat as many times as necessary (say, once per glyph run) and in between other graphics may be rendered directly to the final target HDC without being overwritten by the [**AlphaBlend**](https://msdn.microsoft.com/library/windows/desktop/dd183351) function.


```C++
pRT_->SetTextAntialiasMode(DWRITE_TEXT_ANTIALIAS_MODE_GRAYSCALE);

pRT_->DrawTextLayout(
    origin,
    pTextLayout_,
    pBlackBrush_
    );

BLENDFUNCTION blendFunction = { 0 };  
blendFunction.BlendOp = AC_SRC_OVER;  
blendFunction.SourceConstantAlpha = 255;  
blendFunction.AlphaFormat = AC_SRC_ALPHA;

AlphaBlend(  
        hdc,  
        0, 0,  
        width, height,  
        pRT_->GetMemoryDC(),  
        0, 0,  
        width, height,  
        blendFunction  
        );

```



## Related topics

<dl> <dt>

[Render Using Direct2D](rendering-by-using-direct2d.md)
</dt> <dt>

[Render Using a Custom Text Renderer](how-to-implement-a-custom-text-renderer.md)
</dt> <dt>

[Render to a GDI surface](render-to-a-gdi-surface.md)
</dt> <dt>

[Interoperating with GDI](interoperating-with-gdi.md)
</dt> </dl>

 

 




