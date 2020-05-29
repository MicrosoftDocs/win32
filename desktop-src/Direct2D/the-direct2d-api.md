---
title: Direct2D API Overview
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

# Direct2D API Overview

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

At the root of the Direct2D API are the [**ID2D1Factory**](https://msdn.microsoft.com/library/Dd371246(v=VS.85).aspx) and [**ID2D1Resource**](https://msdn.microsoft.com/library/Dd316908(v=VS.85).aspx) interfaces. An **ID2D1Factory** object creates **ID2D1Resource** objects and serves as the starting point for using Direct2D. All other Direct2D objects inherit from the **ID2D1Resource** interface. There are two types of Direct2D resources: device-independent resources and device-dependent resources.

-   Device-independent resources are not associated with a particular rendering device and can persist for the life of an application.
-   Device-dependent resources are associated with a particular rendering device and cease to function if that device is removed.

(For more information about resources and resource sharing, see the [Resources Overview](resources-and-resource-domains.md).)

## The ID2D1Factory Interface

The [**ID2D1Factory**](https://msdn.microsoft.com/library/Dd371246(v=VS.85).aspx) interface is the starting point for using Direct2D. You use an **ID2D1Factory** to instantiate Direct2D resources. To create an ID2D1Factory, you use one of the [**CreateFactory**](/windows/win32/api/d2d1/nf-d2d1-d2d1createfactory) methods.

A factory defines a set of Create*Resource* methods that can produce the following drawing resources:

-   Render targets are objects that render drawing commands.
-   Drawing state blocks are objects that store drawing state information, such as the current transformation and antialiasing mode.
-   Geometries are objects that represent simple and potentially complex shapes.

One of the most useful objects a factory can create is the [**ID2D1RenderTarget**](https://msdn.microsoft.com/library/Dd371766(v=VS.85).aspx), described in the following section.

## Render Targets

A render target is a resource that inherits from the [**ID2D1RenderTarget**](https://msdn.microsoft.com/library/Dd371766(v=VS.85).aspx) interface. A render target creates resources for drawing and performs drawing operations. There are several kinds of render targets that can be used to render graphics in the following ways:

-   [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/library/Dd371461(v=VS.85).aspx) objects render content to a window.
-   [**ID2D1DCRenderTarget**](https://msdn.microsoft.com/library/Dd371213(v=VS.85).aspx) objects render to a GDI device context.
-   Bitmap render target objects render content to an off-screen bitmap.
-   DXGI render target objects render to a DXGI surface for use with Direct3D.

Because a render target is associated with a particular rendering device, it is a device-dependent resource and ceases to function if the device is removed.

### Render Target Features

You can specify whether a render target should use hardware acceleration and whether remote display should be rendered by the local or remote computer. Render targets can be set up for aliased or antialiased rendering. For rendering scenes with a large number of primitives, a developer can also render 2-D graphics in aliased mode and use D3D multisample antialiasing to achieve greater scalability.

Render targets can also group drawing operations into layers that are represented by the [**ID2D1Layer**](https://msdn.microsoft.com/library/Dd371483(v=VS.85).aspx) interface. Layers are useful for collecting drawing operations to be composited together when rendering a frame. For some scenarios, this can be a useful alternative to rendering to a bitmap render target, and then reusing the bitmap contents, as allocation costs for layering are lower than for an [**ID2D1BitmapRenderTarget**](https://msdn.microsoft.com/library/Dd371146(v=VS.85).aspx).

Render targets can create new render targets that are compatible with themselves, which is useful for intermediate off-screen rendering while retaining the various render-target properties that were set on the original.

It is also possible to render using GDI on a Direct2D render target by calling [**QueryInterface**](https://msdn.microsoft.com/library/ms682521(v=VS.85).aspx) on a render target for [**ID2D1GdiInteropRenderTarget**](https://msdn.microsoft.com/library/Dd371321(v=VS.85).aspx), which has [**GetDC**](https://msdn.microsoft.com/library/Dd371323(v=VS.85).aspx) and [**ReleaseDC**](https://msdn.microsoft.com/library/Dd371327(v=VS.85).aspx) methods on it that can be used to retrieve a GDI device context. Rendering via GDI is possible only if the render target was created with the [**D2D1\_RENDER\_TARGET\_USAGE\_GDI\_COMPATIBLE**](/windows/win32/api/d2d1/ne-d2d1-d2d1_render_target_usage) flag set. This is useful for applications that primarily render with Direct2D but have an extensibility model or other legacy content that requires the ability to render with GDI. For more information, see the [Direct2D and GDI Interoperability Overview](direct2d-and-gdi-interoperation-overview.md).

### Render Target Resources

Like a factory, a render target can create drawing resources. Any resources created by a render target are device-dependent resources (just like the render target). A render target can create the following types of resources:

-   Bitmaps
-   Brushes
-   Layers
-   Meshes

### Drawing Commands

To render content, you use the render target drawing methods. Before you begin drawing, you call the [**ID2D1RenderTarget::BeginDraw**](https://msdn.microsoft.com/library/Dd371768(v=VS.85).aspx) method. After you finished drawing, you call the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/library/Dd371924(v=VS.85).aspx) method. In between these calls, you use Draw and Fill methods to render drawing resources. Most Draw and Fill methods take a shape (either a primitive or a geometry) and a brush for filling or outlining the shape.

Render targets also provide methods for clipping, applying opacity masks, and transforming the coordinate space.

Direct2D uses a left-handed coordinate system: positive x-axis values proceed to the right and positive y-axis values proceed downward.

### Error Handling

Render target drawing commands do not indicate whether the requested operation was successful. To find out whether there were drawing errors, call the render target [**Flush**](https://msdn.microsoft.com/library/Dd316801(v=VS.85).aspx) method or [**EndDraw**](https://msdn.microsoft.com/library/Dd371924(v=VS.85).aspx) method to obtain an **HRESULT**.

## Drawing Resources

The following sections describe some of the resources that can be created by the render target and factory interfaces.

### Brushes

A brush, represented by the [**ID2D1Brush**](https://msdn.microsoft.com/library/Dd371173(v=VS.85).aspx) interface, is a device-dependent resource, created by a render target, that paints an area with its output. Different brushes have different types of output. Some brushes paint an area with a solid color, others with a gradient or an image. Direct2D provides four types of brushes:

-   [**ID2D1SolidColorBrush**](https://msdn.microsoft.com/library/Dd372207(v=VS.85).aspx) paints an area with a solid color.
-   [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/library/Dd371488(v=VS.85).aspx) paints an area with a linear gradient that blends two or more colors across a line, the gradient axis.
-   [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/library/Dd371529(v=VS.85).aspx) paints an area with a radial gradient that blends two or more colors around an ellipse.
-   [**ID2D1BitmapBrush**](https://msdn.microsoft.com/library/Dd371122(v=VS.85).aspx) paints an area with a bitmap.

To create a brush, you use one of the [**ID2D1RenderTarget::**](https://msdn.microsoft.com/library/Dd371766(v=VS.85).aspx)Create*<Type>*Brush methods, such as [**CreateRadialGradientBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createradialgradientbrush(constd2d1_radial_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1radialgradientbrush)). Brushes can be used with a render target Draw and Fill methods, either to paint a shape stroke or outline, or as an opacity mask.

For more information about brushes, see the [Brushes Overview](direct2d-brushes-overview.md).

### Geometries

In addition to basic drawing primitives such as points, rectangles, and ellipses, Direct2D provides the [**ID2D1Geometry**](https://msdn.microsoft.com/library/Dd316578(v=VS.85).aspx) interface for describing simple and complex shapes. Interfaces that inherit from **ID2D1Geometry** define different types of shapes, such as [**ID2D1RectangleGeometry**](https://msdn.microsoft.com/library/Dd371561(v=VS.85).aspx) for representing rectangles, [**ID2D1RoundedRectangleGeometry**](https://msdn.microsoft.com/library/Dd316914(v=VS.85).aspx) for representing rounded rectangles, and [**ID2D1EllipseGeometry**](https://msdn.microsoft.com/library/Dd371239(v=VS.85).aspx) for representing ellipses.

More complex shapes can be created by using the [**ID2D1GeometrySink**](https://msdn.microsoft.com/library/Dd316592(v=VS.85).aspx) interface to specify a series of figures composed of lines, curves, and arcs. The **ID2D1GeometrySink** is passed to the Open method of an [**ID2D1PathGeometry**](https://msdn.microsoft.com/library/Dd371512(v=VS.85).aspx) to generate a complex geometry. [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/library/Dd316919(v=VS.85).aspx) can also be used with the DirectWrite API to extract path outlines of formatted text for artistic rendering.

The geometry interfaces provide methods for manipulating shapes by widening or simplifying existing geometries, or by generating the intersection or union of multiple geometries. They also provide methods for determining whether geometries are intersecting or overlapping, retrieving bounds information, computing the area or length of a geometry, and interpolating locations along a geometry. Direct2D also provides the ability to create a mesh of triangles that is tessellated from a geometry.

To create a geometry, you use one of the [**ID2D1Factory**](https://msdn.microsoft.com/library/Dd371246(v=VS.85).aspx)::Create*<Type>*Geometry methods, such as [**CreatePathGeometry**](https://msdn.microsoft.com/library/Dd371282(v=VS.85).aspx). A geometry is a device-independent resource.

To render a geometry, you use the [**DrawGeometry**](https://msdn.microsoft.com/library/Dd371890(v=VS.85).aspx) and [**FillGeometry**](https://msdn.microsoft.com/library/Dd371933(v=VS.85).aspx) methods of a render target.

For more information about geometries, see the [Geometries Overview](direct2d-geometries-overview.md).

### Bitmaps

Direct2D does not provide methods for loading or storing bitmaps; rather, it enables you to create bitmaps using the [Windows Imaging Component (WIC)](https://msdn.microsoft.com/library/Ee719654(v=VS.85).aspx). Bitmap resources can be loaded using WIC and then used to create an [**ID2D1Bitmap**](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) through the [**ID2D1RenderTarget::CreateBitmapFromWicBitmap**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createbitmapfromwicbitmap(iwicbitmapsource_constd2d1_bitmap_properties_id2d1bitmap)) method.

Bitmaps can also be created from in-memory data that was set up through other means. After a bitmap has been created, it can be drawn by the render target [**DrawBitmap**](https://msdn.microsoft.com/library/Dd371880(v=VS.85).aspx) method or with a bitmap brush.

Because creating bitmap resources on hardware render targets is often an expensive operation, Direct2D can update the contents of a bitmap (or portion of the bitmap) by using the [**CopyFromBitmap**](https://msdn.microsoft.com/library/Dd371152(v=VS.85).aspx), [**CopyFromRenderTarget**](https://msdn.microsoft.com/library/Dd371158(v=VS.85).aspx), and [**CopyFromMemory**](https://msdn.microsoft.com/library/Dd371155(v=VS.85).aspx) methods. Using these methods can potentially save the costs associated with additional GPU texture allocations.

## Drawing Text

Direct2D was designed to work with the text operations of the new text API, DirectWrite. To make using the DirectWrite API simpler, render targets provide three methods for rendering DirectWrite text resources: [**DrawText**](https://msdn.microsoft.com/library/Dd371919(v=VS.85).aspx), [**DrawTextLayout**](https://msdn.microsoft.com/library/Dd371913(v=VS.85).aspx), and [**DrawGlyphRun**](https://msdn.microsoft.com/library/Dd371893(v=VS.85).aspx). Because Direct2D uses the GPU for the ClearType text rendering process, Direct2D provides lower CPU usage than GDI for text operations and better scalability as more GPU processing power is available.

The [**ID2D1RenderTarget::DrawText**](https://msdn.microsoft.com/library/Dd371919(v=VS.85).aspx) is designed for the simplest scenarios involving rendering a string of Unicode text with minimal formatting. More complex layout and typographic flexibility is provided through the [**ID2D1RenderTarget::DrawTextLayout**](https://msdn.microsoft.com/library/Dd371913(v=VS.85).aspx) method, which uses an [**IDWriteTextLayout**](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) object to specify the content and formatting to be rendered. **IDWriteTextLayout** enables you to specify individual formatting for substrings of text and other advanced typography options.

For scenarios where precise control of glyph-level layout is required, the [**ID2D1RenderTarget::DrawGlyphRun**](https://msdn.microsoft.com/library/Dd371893(v=VS.85).aspx) method can be used in conjunction with the measurement facilities provided by [DirectWrite](/windows/win32/DirectWrite/direct-write-portal).

To use the DirectWrite API, include the dwrite.h header. Like Direct2D, DirectWrite uses a factory, [**IDWriteFactory**](/windows/win32/api/dwrite/nn-dwrite-idwritefactory) to create text objects. Use the [**DWriteCreateFactory**](/windows/win32/api/dwrite/nf-dwrite-dwritecreatefactory) function to create a factory, and then use its Create methods to create DirectWrite resources (such as [**IDWriteTextFormat**](https://msdn.microsoft.com/library/Dd371919(v=VS.85).aspx)).

For more information about DirectWrite, see the [Introducing DirectWrite](/windows/win32/DirectWrite/introducing-directwrite) topic.

## Direct2D Primitives

Direct2D defines a set of primitives that are similar to those provided by other drawing APIs. It provides a color structure, a matrix structure for performing transformations, and floating-point and integer versions of points, rectangles, ellipses, and size structures. Usually, you use the floating-point versions of these structures.

You do not use a factory or a render target to instantiate Direct2D primitives. You can create them directly, or use the helper methods defined in d2d1helper.h to create them.

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> <dt>

[DirectWrite Hello World Sample](https://docs.microsoft.com/samples/browse/?redirectedfrom=MSDN-samples)
</dt> <dt>

[Introducing DirectWrite](/windows/win32/DirectWrite/introducing-directwrite)
</dt> <dt>

[Resources Overview](resources-and-resource-domains.md)
</dt> <dt>

[Windows Imaging Component (WIC)](https://msdn.microsoft.com/library/Ee719654(v=VS.85).aspx)
</dt> </dl>

 

 




