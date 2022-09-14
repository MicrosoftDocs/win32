---
title: Direct2D API overview
description: Provides an overview of the Direct2D object model.
ms.assetid: b1362ef6-40fc-4fa5-ba5b-22c622c39f04
keywords:
- Direct2D,about
- Direct2D,header files
- Direct2D,object model
- Direct2D,interfaces
- ID2D1Factory interface
- Direct2D,render targets
- render targets,about
- Direct2D,drawing commands
- render targets,drawing commands
- Direct2D,error handling
- render targets,error handling
- error handling
- brushes
- render targets,brushes
- geometries
- Direct2D,geometries
- bitmaps for Direct2D
- Direct2D,bitmaps
- primitives
- Direct2D,primitives
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D API overview

Direct2D provides an API, similar to Direct3D, for use with C or C++. The API exposes a variety of drawing-related functionality:

-   Render targets for display and off-screen rendering using Direct2D, Direct3D, or GDI.
-   Objects for managing drawing state such as coordinate space transforms and antialiasing modes.
-   Representations for geometric data, and functions for geometry processing.
-   Rendering functionality for bitmaps, geometries, and text.
-   Provisions for using graphical content created using GDI or Direct3D.

This topic provides an overview of the objects that make up the Direct2D API. It contains the following sections:

-   [Direct2D Header Files](#direct2d-header-files)
-   [Direct2D Interfaces](#direct2d-interfaces)
-   [The ID2D1Factory Interface](#the-id2d1factory-interface)
-   [Render Targets](#render-targets)
    -   [Render Target Features](#render-target-features)
    -   [Render Target Resources](#render-target-resources)
    -   [Drawing Commands](#drawing-commands)
    -   [Error Handling](#error-handling)
-   [Drawing Resources](#drawing-resources)
    -   [Brushes](#brushes)
    -   [Geometries](#geometries)
    -   [Bitmaps](#bitmaps)
-   [Drawing Text](#drawing-text)
-   [Direct2D Primitives](#direct2d-primitives)
-   [Related topics](#related-topics)

## Direct2D Header Files

The Direct2D API is defined by the following header files.

| Header file         | Description                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------|
| d2d1.h              | Defines C and C++ versions of the primary Direct2D API.                                                                      |
| d2d1helper.h        | Defines C++ helper functions, classes, and structures.                                                                       |
| d2dbasetypes.h      | Defines drawing primitives for Direct2D, such as points and rectangles. This header is included with d2d1.h.                 |
| d2derr.h            | Defines the error codes for Direct2D. This header is included with d2d1.h.                                                   |
| d2d1\_1.h           | Defines C and C++ versions of the primary Direct2D API for Windows 8 and later.                                              |
| d2d1\_1helper.h     | Defines C++ helper functions, classes, and structures for Windows 8 and later.                                               |
| d2d1effects.h       | Defines C and C++ versions of the image effects part of the Direct2D API for Windows 8 and later.                            |
| d2d1effecthelpers.h | Defines C++ helper functions, classes, and structures of the image effects part of the Direct2D API for Windows 8 and later. |



 

To use Direct2D, your application should include the d2d1.h header file.

To compile a Direct2D application, add d2d1.lib to the list of libraries. You can find d2d1.h and d2d1.lib in [Windows Software Development Kit (SDK) for Windows 7](https://msdn.microsoft.com/windows/bb980924.aspx).

The following sections describe some of the common interfaces provided by the Direct2D API.

## Direct2D Interfaces

At the root of the Direct2D API are the [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) and [**ID2D1Resource**](/windows/win32/api/d2d1/nn-d2d1-id2d1resource) interfaces. An **ID2D1Factory** object creates **ID2D1Resource** objects and serves as the starting point for using Direct2D. All other Direct2D objects inherit from the **ID2D1Resource** interface. There are two types of Direct2D resources: device-independent resources and device-dependent resources.

-   Device-independent resources are not associated with a particular rendering device and can persist for the life of an application.
-   Device-dependent resources are associated with a particular rendering device and cease to function if that device is removed.

(For more information about resources and resource sharing, see the [Resources Overview](resources-and-resource-domains.md).)

## The ID2D1Factory Interface

The [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) interface is the starting point for using Direct2D. You use an **ID2D1Factory** to instantiate Direct2D resources. To create an ID2D1Factory, you use one of the [**CreateFactory**](/windows/win32/api/d2d1/nf-d2d1-d2d1createfactory) methods.

A factory defines a set of Create*Resource* methods that can produce the following drawing resources:

-   Render targets are objects that render drawing commands.
-   Drawing state blocks are objects that store drawing state information, such as the current transformation and antialiasing mode.
-   Geometries are objects that represent simple and potentially complex shapes.

One of the most useful objects a factory can create is the [**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget), described in the following section.

## Render Targets

A render target is a resource that inherits from the [**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget) interface. A render target creates resources for drawing and performs drawing operations. There are several kinds of render targets that can be used to render graphics in the following ways:

-   [**ID2D1HwndRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1hwndrendertarget) objects render content to a window.
-   [**ID2D1DCRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1dcrendertarget) objects render to a GDI device context.
-   Bitmap render target objects render content to an off-screen bitmap.
-   DXGI render target objects render to a DXGI surface for use with Direct3D.

Because a render target is associated with a particular rendering device, it is a device-dependent resource and ceases to function if the device is removed.

### Render Target Features

You can specify whether a render target should use hardware acceleration and whether remote display should be rendered by the local or remote computer. Render targets can be set up for aliased or antialiased rendering. For rendering scenes with a large number of primitives, a developer can also render 2-D graphics in aliased mode and use D3D multisample antialiasing to achieve greater scalability.

Render targets can also group drawing operations into layers that are represented by the [**ID2D1Layer**](/windows/win32/api/d2d1/nn-d2d1-id2d1layer) interface. Layers are useful for collecting drawing operations to be composited together when rendering a frame. For some scenarios, this can be a useful alternative to rendering to a bitmap render target, and then reusing the bitmap contents, as allocation costs for layering are lower than for an [**ID2D1BitmapRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmaprendertarget).

Render targets can create new render targets that are compatible with themselves, which is useful for intermediate off-screen rendering while retaining the various render-target properties that were set on the original.

It is also possible to render using GDI on a Direct2D render target by calling [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on a render target for [**ID2D1GdiInteropRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1gdiinteroprendertarget), which has [**GetDC**](/windows/win32/api/d2d1/nf-d2d1-id2d1gdiinteroprendertarget-getdc) and [**ReleaseDC**](/windows/win32/api/d2d1/nf-d2d1-id2d1gdiinteroprendertarget-releasedc) methods on it that can be used to retrieve a GDI device context. Rendering via GDI is possible only if the render target was created with the [**D2D1\_RENDER\_TARGET\_USAGE\_GDI\_COMPATIBLE**](/windows/win32/api/d2d1/ne-d2d1-d2d1_render_target_usage) flag set. This is useful for applications that primarily render with Direct2D but have an extensibility model or other legacy content that requires the ability to render with GDI. For more information, see the [Direct2D and GDI Interoperability Overview](direct2d-and-gdi-interoperation-overview.md).

### Render Target Resources

Like a factory, a render target can create drawing resources. Any resources created by a render target are device-dependent resources (just like the render target). A render target can create the following types of resources:

-   Bitmaps
-   Brushes
-   Layers
-   Meshes

### Drawing Commands

To render content, you use the render target drawing methods. Before you begin drawing, you call the [**ID2D1RenderTarget::BeginDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) method. After you finished drawing, you call the [**ID2D1RenderTarget::EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method. In between these calls, you use Draw and Fill methods to render drawing resources. Most Draw and Fill methods take a shape (either a primitive or a geometry) and a brush for filling or outlining the shape.

Render targets also provide methods for clipping, applying opacity masks, and transforming the coordinate space.

Direct2D uses a left-handed coordinate system: positive x-axis values proceed to the right and positive y-axis values proceed downward.

### Error Handling

Render target drawing commands do not indicate whether the requested operation was successful. To find out whether there were drawing errors, call the render target [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) method or [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method to obtain an **HRESULT**.

## Drawing Resources

The following sections describe some of the resources that can be created by the render target and factory interfaces.

### Brushes

A brush, represented by the [**ID2D1Brush**](/windows/win32/api/d2d1/nn-d2d1-id2d1brush) interface, is a device-dependent resource, created by a render target, that paints an area with its output. Different brushes have different types of output. Some brushes paint an area with a solid color, others with a gradient or an image. Direct2D provides four types of brushes:

-   [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1solidcolorbrush) paints an area with a solid color.
-   [**ID2D1LinearGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) paints an area with a linear gradient that blends two or more colors across a line, the gradient axis.
-   [**ID2D1RadialGradientBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) paints an area with a radial gradient that blends two or more colors around an ellipse.
-   [**ID2D1BitmapBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmapbrush) paints an area with a bitmap.

To create a brush, you use one of the [**ID2D1RenderTarget::**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)Create*&lt;Type&gt;*Brush methods, such as [**CreateRadialGradientBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createradialgradientbrush(constd2d1_radial_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1radialgradientbrush)). Brushes can be used with a render target Draw and Fill methods, either to paint a shape stroke or outline, or as an opacity mask.

For more information about brushes, see the [Brushes Overview](direct2d-brushes-overview.md).

### Geometries

In addition to basic drawing primitives such as points, rectangles, and ellipses, Direct2D provides the [**ID2D1Geometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry) interface for describing simple and complex shapes. Interfaces that inherit from **ID2D1Geometry** define different types of shapes, such as [**ID2D1RectangleGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1rectanglegeometry) for representing rectangles, [**ID2D1RoundedRectangleGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1roundedrectanglegeometry) for representing rounded rectangles, and [**ID2D1EllipseGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1ellipsegeometry) for representing ellipses.

More complex shapes can be created by using the [**ID2D1GeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrysink) interface to specify a series of figures composed of lines, curves, and arcs. The **ID2D1GeometrySink** is passed to the Open method of an [**ID2D1PathGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1pathgeometry) to generate a complex geometry. [**ID2D1SimplifiedGeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) can also be used with the DirectWrite API to extract path outlines of formatted text for artistic rendering.

The geometry interfaces provide methods for manipulating shapes by widening or simplifying existing geometries, or by generating the intersection or union of multiple geometries. They also provide methods for determining whether geometries are intersecting or overlapping, retrieving bounds information, computing the area or length of a geometry, and interpolating locations along a geometry. Direct2D also provides the ability to create a mesh of triangles that is tessellated from a geometry.

To create a geometry, you use one of the [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory)::Create*&lt;Type&gt;*Geometry methods, such as [**CreatePathGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1factory-createpathgeometry). A geometry is a device-independent resource.

To render a geometry, you use the [**DrawGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawgeometry) and [**FillGeometry**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillgeometry) methods of a render target.

For more information about geometries, see the [Geometries Overview](direct2d-geometries-overview.md).

### Bitmaps

Direct2D does not provide methods for loading or storing bitmaps; rather, it enables you to create bitmaps using the [Windows Imaging Component (WIC)](../wic/-wic-about-windows-imaging-codec.md). Bitmap resources can be loaded using WIC and then used to create an [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) through the [**ID2D1RenderTarget::CreateBitmapFromWicBitmap**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createbitmapfromwicbitmap(iwicbitmapsource_constd2d1_bitmap_properties_id2d1bitmap)) method.

Bitmaps can also be created from in-memory data that was set up through other means. After a bitmap has been created, it can be drawn by the render target [**DrawBitmap**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawbitmap(id2d1bitmap_constd2d1_rect_f__float_d2d1_bitmap_interpolation_mode_constd2d1_rect_f_)) method or with a bitmap brush.

Because creating bitmap resources on hardware render targets is often an expensive operation, Direct2D can update the contents of a bitmap (or portion of the bitmap) by using the [**CopyFromBitmap**](/windows/win32/api/d2d1/nf-d2d1-id2d1bitmap-copyfrombitmap), [**CopyFromRenderTarget**](/windows/win32/api/d2d1/nf-d2d1-id2d1bitmap-copyfromrendertarget), and [**CopyFromMemory**](/windows/win32/api/d2d1/nf-d2d1-id2d1bitmap-copyfrommemory) methods. Using these methods can potentially save the costs associated with additional GPU texture allocations.

## Drawing Text

Direct2D was designed to work with the text operations of the new text API, DirectWrite. To make using the DirectWrite API simpler, render targets provide three methods for rendering DirectWrite text resources: [**DrawText**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)), [**DrawTextLayout**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtextlayout), and [**DrawGlyphRun**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawglyphrun). Because Direct2D uses the GPU for the ClearType text rendering process, Direct2D provides lower CPU usage than GDI for text operations and better scalability as more GPU processing power is available.

The [**ID2D1RenderTarget::DrawText**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode)) is designed for the simplest scenarios involving rendering a string of Unicode text with minimal formatting. More complex layout and typographic flexibility is provided through the [**ID2D1RenderTarget::DrawTextLayout**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtextlayout) method, which uses an [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) object to specify the content and formatting to be rendered. **IDWriteTextLayout** enables you to specify individual formatting for substrings of text and other advanced typography options.

For scenarios where precise control of glyph-level layout is required, the [**ID2D1RenderTarget::DrawGlyphRun**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawglyphrun) method can be used in conjunction with the measurement facilities provided by [DirectWrite](../directwrite/direct-write-portal.md).

To use the DirectWrite API, include the dwrite.h header. Like Direct2D, DirectWrite uses a factory, [**IDWriteFactory**](/windows/win32/api/dwrite/nn-dwrite-idwritefactory) to create text objects. Use the [**DWriteCreateFactory**](/windows/win32/api/dwrite/nf-dwrite-dwritecreatefactory) function to create a factory, and then use its Create methods to create DirectWrite resources (such as [**IDWriteTextFormat**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawtext(constwchar_uint32_idwritetextformat_constd2d1_rect_f__id2d1brush_d2d1_draw_text_options_dwrite_measuring_mode))).

For more information about DirectWrite, see the [Introducing DirectWrite](../directwrite/introducing-directwrite.md) topic.

## Direct2D Primitives

Direct2D defines a set of primitives that are similar to those provided by other drawing APIs. It provides a color structure, a matrix structure for performing transformations, and floating-point and integer versions of points, rectangles, ellipses, and size structures. Usually, you use the floating-point versions of these structures.

You do not use a factory or a render target to instantiate Direct2D primitives. You can create them directly, or use the helper methods defined in d2d1helper.h to create them.

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> <dt>

[DirectWrite Hello World Sample](/samples/browse/?redirectedfrom=MSDN-samples)
</dt> <dt>

[Introducing DirectWrite](../directwrite/introducing-directwrite.md)
</dt> <dt>

[Resources Overview](resources-and-resource-domains.md)
</dt> <dt>

[Windows Imaging Component (WIC)](../wic/-wic-about-windows-imaging-codec.md)
</dt> </dl>

 

 
