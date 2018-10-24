---
title: Text Rendering with Direct2D and DirectWrite
description: Unlike other APIs, such as GDI, GDI+ or WPF, Direct2D interoperates with another API, DirectWrite, to manipulate and render text. This topic describes the benefits and interoperation of these separate components.
ms.assetid: 1d5b8deb-34e2-433c-8de3-4ef66fb4e49d
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Text Rendering with Direct2D and DirectWrite

Unlike other APIs, such as [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203), GDI+ or WPF, [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) interoperates with another API, [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038), to manipulate and render text. This topic describes the benefits and interoperation of these separate components.

This topic contains the following sections.

-   [Direct2D Enables Incremental Adoption](#direct2d-enables-incremental-adoption)
-   [Text Services versus Text Rendering](#text-services-versus-text-rendering)
-   [Glyphs versus Text](#glyphs-versus-text)
-   [DirectWrite and Direct2D](#directwrite-and-direct2d)
    -   [DrawText](#drawtextlayout)
    -   [DrawTextLayout](#drawtextlayout)
    -   [DrawGlyphRun](#drawglyphrun)
-   [Glyph Rendering](#glyph-rendering)
-   [Conclusion](#conclusion)

## Direct2D Enables Incremental Adoption

Moving an application from one graphics API to another can be difficult or not what you want for various reasons. This might be because you have to support plug-ins that still take the older interfaces, because the application itself is too large to port over to a new API in one release or because some part of the newer API is desirable but the older API is working well enough for other parts of the application.

Because [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) and [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) are implemented as separate components, you can upgrade your whole 2D graphics system or just the text part of it. For example, you could update an application to use DirectWrite for text but still use [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203) or GDI+ for rendering.

## Text Services versus Text Rendering

As applications have evolved, their text processing requirements have grown increasingly complex. At first, text was generally confined to statically laid-out UI, and the text was rendered in a well-defined box, such as a button. As applications began to be available in a growing number of languages, this approach became more difficult to sustain because both the width and height of the translated text can vary significantly between languages. To adapt, applications started to dynamically lay out their UI to depend on the actual rendered size of the text, instead of the other way around.

To help applications complete this task, [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) provides the [**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718) interface. This API enables an application to specify a piece of text with complex characteristics such as different fonts and font sizes, underlines, strikethroughs, bi-directional text, effects, ellipsis and even embedded non-glyph characters (such as a bitmap emoticon or an icon). The application can then change various characteristics of the text as it iteratively determines its UI layout. The [DirectWrite Hello World Sample](http://go.microsoft.com/fwlink/?LinkID=624680), which is shown in the following illustration and in the [Tutorial: Getting Started with DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368152) topic, shows many of these effects.

![screen shot of the "hello world" sample.](images/dwrite-hello-world.png)

The layout can either position the glyphs ideally based on their widths (as WPF does), or it can snap the glyphs to the nearest pixel positions (as [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203) does).

In addition to obtaining text measurements, the application can hit test various parts of the text. For example, it might want to know that a hyperlink in the text is clicked. (For more information about hit testing, see the [How to Perform Hit Testing on a Text Layout](https://msdn.microsoft.com/library/windows/desktop/dd756613) topic.)

The text layout interface is decoupled from the rendering API that the application uses, as the following diagram shows:

![text layout and graphics api diagram.](images/direct2d-directwrite1.png)

This separation is possible because DirectWrite provides a rendering interface ([**IDWriteTextRenderer**](https://msdn.microsoft.com/library/windows/desktop/dd371523)) that applications can implement to render text by using whatever graphics API you want. The application implemented [**IDWriteTextRenderer::DrawGlyphRun**](https://msdn.microsoft.com/library/windows/desktop/dd371526) callback method is called by DirectWrite when rendering a text layout. It is the responsibility of this method to perform the drawing operations or pass them along.

For drawing glyphs, [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) provides [**ID2D1RenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371893(v=VS.85).aspx) for drawing to a Direct2D surface and [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) provides [**IDWriteBitmapRenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/library/windows/desktop/dd368167) for drawing to a GDI surface that can then be transferred to a window by using GDI. Conveniently, **DrawGlyphRun** in both Direct2D and DirectWrite have exactly compatible parameters to the [**DrawGlyphRun**](https://msdn.microsoft.com/library/windows/desktop/dd371526) method that the application implements on [**IDWriteTextRenderer**](https://msdn.microsoft.com/library/windows/desktop/dd371523).

Following a similar separation, text-specific features (such as font enumeration and management, glyph analysis, and so on) are handled by [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) instead of [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx). The DirectWrite objects are accepted directly by Direct2D. To help existing GDI applications to take advantage of DirectWrite, it provides the [**IDWriteGdiInterop**](https://msdn.microsoft.com/library/windows/desktop/dd371172) method interface with methods to do the following:

-   Create a [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) Font from a [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203) Logical Font ([**CreateFontFromLOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd371187)).
-   Convert from a [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) Font Face to a [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203) Logical Font ([**ConvertFontFaceToLOGFONT**](https://msdn.microsoft.com/library/windows/desktop/dd371175)).
-   Retrieve the [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) Font Face from the one that is selected into an HDC. ([**CreateFontFaceFromHdc**](https://msdn.microsoft.com/library/windows/desktop/dd371185))
-   Create a [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) [**bitmap render target**](https://msdn.microsoft.com/library/windows/desktop/dd368165) in system memory ([**CreateBitmapRenderTarget**](https://msdn.microsoft.com/library/windows/desktop/dd371182)).

## Glyphs versus Text

Text is a set of Unicode code points (characters), with various stylistic modifiers (fonts, weights, underlines, strikethroughs, and so on) that is laid out in a rectangle. A glyph, in contrast, is a particular index into a particular font file. A glyph defines a set of curves which can be rendered, but, it doesn't have any textual meaning. There is potentially a many-to-many mapping between glyphs and characters. A sequence of glyphs that come from the same Font Face and that are laid-out sequentially on a baseline is called a [GlyphRun](https://msdn.microsoft.com/library/windows/desktop/dd941785). Both [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) and [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) call their most precise glyph rendering API [**DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371893(v=VS.85).aspx) and they have very similar signatures. The following is from [**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371766(v=VS.85).aspx) in Direct2D:


```
STDMETHOD_(void, DrawGlyphRun)(
        D2D1_POINT_2F baselineOrigin,
        __in CONST DWRITE_GLYPH_RUN *glyphRun,
        __in ID2D1Brush *foregroundBrush,
        DWRITE_MEASURING_MODE measuringMode = DWRITE_MEASURING_MODE_NATURAL 
        ) PURE;
```



And this method is from [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/library/windows/desktop/dd368165) in [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038):


```
STDMETHOD(DrawGlyphRun)(
        FLOAT baselineOriginX,
        FLOAT baselineOriginY,
        DWRITE_MEASURING_MODE measuringMode,
        __in DWRITE_GLYPH_RUN const* glyphRun,
        IDWriteRenderingParams* renderingParams,
        COLORREF textColor,
        __out_opt RECT* blackBoxRect = NULL
        ) PURE;
```



The [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) version keeps the baseline origin, measuring mode and the glyph run parameters and includes additional parameters.

[DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) also enables you to use a custom renderer for glyphs by implementing the [**IDWriteTextRenderer**](https://msdn.microsoft.com/library/windows/desktop/dd371523) interface. This interface also has a **DrawGlyphRun** method, as the following code example shows.


```
STDMETHOD(DrawGlyphRun)(
        __maybenull void* clientDrawingContext,
        FLOAT baselineOriginX,
        FLOAT baselineOriginY,
        DWRITE_MEASURING_MODE measuringMode,
        __in DWRITE_GLYPH_RUN const* glyphRun,
        __in DWRITE_GLYPH_RUN_DESCRIPTION const* glyphRunDescription,
        __maybenull IUnknown* clientDrawingEffect
        ) PURE;
```



This version includes more parameters that are useful when you implement a [custom text renderer](https://msdn.microsoft.com/library/windows/desktop/dd941787). The final parameter is used for application-implemented custom drawing effects. (For more information about client drawing effects see [How to Add Client Drawing Effects to a Text Layout](https://msdn.microsoft.com/library/windows/desktop/dd941786).

Each glyph run starts at an origin and is put on a line starting from this origin. The glyphs are changed by the current world transform and the selected text rendering settings on the associated render target. This API is generally called directly only by applications that do their own layout (For example a Word Processor) or by an application that has implemented the [**IDWriteTextRenderer**](https://msdn.microsoft.com/library/windows/desktop/dd371523) interface.

## DirectWrite and Direct2D

[Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) provides glyph level rendering services through [**DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371893(v=VS.85).aspx). However, this requires the application to implement the details of rendering, which basically reproduces the functionality of the [**DrawText**](https://msdn.microsoft.com/library/windows/desktop/dd162498) API from GDI on its own.

Therefore, [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) provides APIs that accept text instead of glyphs: [**ID2D1RenderTarget::DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) and [**ID2D1RenderTarget::DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx). Both methods render to a Direct2D surface. To render to a GDI surface, [**IDWriteBitmapRenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/library/windows/desktop/dd368167) is provided. But this method requires a custom text renderer to be implemented by the application. (For more information, see the [Render to a GDI Surface](https://msdn.microsoft.com/library/windows/desktop/ff485856) topic.)

An application's usage of text typically starts simple: put **OK** or **Cancel** on a fixed-layout button, for example. However, over time, it becomes more complex as internationalization and other features are added. Eventually many applications will have to use [DirectWrite's](https://msdn.microsoft.com/library/windows/desktop/dd368038) text layout objects and implement the text renderer.

Therefore, [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) provides layered APIs that enable an application to start simply and grow more sophisticated without having to back-track or abandon their working code. A simplified view is shown in the following diagram:

![directwrite and direct2d application diagram.](images/direct2d-directwrite2.png)

### DrawText

[**DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx) is the simplest of the APIs to use. It takes a Unicode string, a foreground brush, a single format object and a destination rectangle. It will lay out and render the whole string within the layout rectangle, and optionally clip it. This is useful when you put a simple piece of text in a piece of fixed-layout UI.

### DrawTextLayout

By creating an [**IDWriteTextLayout**](https://msdn.microsoft.com/library/windows/desktop/dd316718) object, an application can start measuring and arranging the text and other UI elements, and support multiple fonts, styles, underlines and strikethroughs. [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) provides the [**DrawTextLayout**](https://msdn.microsoft.com/en-us/library/Dd371913(v=VS.85).aspx) API that directly accepts this object and renders the text at a given point. (The width and height are provided by the layout object). In addition to implementing all the expected text layout features, Direct2D will interpret any effect object as a brush and apply that brush to the selected range of glyphs. It will also call any inline objects. An application can then insert non-glyph characters (icons) into the text if it wishes. Another advantage of using a text layout object is that the glyph positions are cached in it. Therefore, a large performance gain is possible by reusing the same layout object for multiple draw calls and avoiding recalculating the glyph positions for each call. This capability is not present for GDI's [**DrawText**](https://msdn.microsoft.com/en-us/library/Dd371919(v=VS.85).aspx).

### DrawGlyphRun

Finally, the application can implement the [**IDWriteTextRenderer**](https://msdn.microsoft.com/library/windows/desktop/dd371523) interface itself and call [**DrawGlyphRun**](https://msdn.microsoft.com/en-us/library/Dd371893(v=VS.85).aspx) and [**FillRectangle**](https://msdn.microsoft.com/en-us/library/Dd742851(v=VS.85).aspx) itself, or any other rendering API. All the existing interaction with the Text Layout object will remain unchanged.

For an example of how to implement a custom text renderer see the [Render Using a Custom Text Renderer](https://msdn.microsoft.com/library/windows/desktop/dd941787) topic.

## Glyph Rendering

Adding [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) to an existing GDI application enables the application to use the [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/library/windows/desktop/dd368165) API to render glyphs. The [**IDWriteBitmapRenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/library/windows/desktop/dd368167) method that DirectWrite provides will render in solid color to a memory DC without requiring any additional APIs, such as [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx).

This enables the application to obtain advanced text rendering features such as the following:

-   Sub-pixel ClearType enables an application to put glyphs on sub-pixel positions to allow for both sharp glyph rendering and glyph layout.
-   Y-direction antialiasing enables smoother rendering of curves on larger glyphs.

An application moving to [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) will also obtain the following features:

-   Hardware acceleration.
-   The ability to fill text with an arbitrary [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) brush, such as radial gradients, linear gradients, and bitmaps.
-   More support for layering and clipping through the [**PushAxisAlignedClip**](https://msdn.microsoft.com/en-us/library/Dd316860(v=VS.85).aspx), [**PushLayer**](https://msdn.microsoft.com/en-us/library/Dd316869(v=VS.85).aspx) and [**CreateCompatibleRenderTarget**](https://msdn.microsoft.com/library/windows/desktop/dd371825) APIs.
-   The ability to support Grayscale text rendering. This correctly populates the destination alpha channel according to both the text brush opacity and the antialiasing of the text.

To efficiently support hardware acceleration, [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) uses a slightly different approximation to Gamma correction called *alpha correction*. This does not require Direct2D to inspect the render target color pixel when rendering text.

## Conclusion

This topic explains the differences and similarities between [Direct2D](https://msdn.microsoft.com/en-us/library/Dd370990(v=VS.85).aspx) and [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038) and the architectural motivations for providing them as separate, cooperative APIs.

 

 




