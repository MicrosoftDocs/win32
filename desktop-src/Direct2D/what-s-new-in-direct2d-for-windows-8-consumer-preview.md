---
title: Whats new in Direct2D
description: Here are some of the new additions to Direct2D.
ms.assetid: BA459FF0-9457-4652-A97C-BD4EC57EC8E2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's new in Direct2D

Here are some of the new additions to Direct2D.

## What’s new for Windows 10 Creators Update

The following features and APIs were added or updated for Windows 10 Creators Update.

### Support for SVG image rendering

Starting in Windows 10 Creators Update, Direct2D provides support for parsing and drawing SVG images, allowing developers to render assets produced in their favorite vector art tools without converting them to raster images first. Use this feature to improve the disk footprint and scaling behavior of your in-app iconography, and use Direct2D’s new SVG object model APIs to make programmatic changes to your app’s SVG. Note that Direct2D only supports a limited subset of SVG suitable for images and does not support all SVG drawing features. If you need browser-grade SVG compatibility or SVG’s web-oriented features, consider using the [XAML WebView control](https://docs.microsoft.com/uwp/api/Windows.UI.Xaml.Controls.WebView) instead. For more information, see the following topics:

-   [Direct2D SVG image rendering sample](http://go.microsoft.com/fwlink/p/?LinkId=848071)
-   [SVG Support](svg-support.md)
-   [**ID2D1DeviceContext5::CreateSvgDocument**](/windows/win32/d2d1_3/?branch=master) method
-   [**ID2D1DeviceContext5::DrawSvgDocument**](/windows/win32/d2d1_3/?branch=master) method
-   [**ID2D1SvgElement**](/windows/win32/d2d1svg/?branch=master) interface

### Improved support for color management

Starting in Windows 10 Creators Update, Direct2D provides improved color management capabilities. Developers no longer need an ICC profile to use Direct2D’s color management effect; they can now use DXGI color spaces or construct their own parameterized color space definition. For more information, see the following topics:

-   [Color management effect](color-management.md)
-   [**ID2D1DeviceContext5::CreateColorContextFromDxgiColorSpace**](/windows/win32/d2d1_3/?branch=master)
-   [**ID2D1DeviceContext5::CreateColorContextFromSimpleColorProfile**](/windows/win32/d2d1_3/?branch=master)

## What's new for Windows 10 Anniversary Update

The following features and APIs were added or updated for Windows 10 Anniversary Update.

### Improved support for color fonts

Starting in Windows 10 Anniversary Update, Direct2D now supports rendering a wider variety of color font formats, allowing developers to use more types of fonts in their Direct2D-powered apps than ever before. This includes support for:

-   The ‘COLR’ OpenType table, which enables compact vector content in fonts. (Supported since Windows 8.1.)
-   The ‘SVG ’ OpenType table, which enables SVG content in fonts.
-   The ‘CBDT’ OpenType table, which enables color bitmap content in fonts.
-   The ‘sbix’ OpenType table, which enables color bitmap content in fonts.

Direct2D supports these color font formats automatically when the [**D2D1\_DRAW\_TEXT\_OPTIONS\_ENABLE\_COLOR\_FONT**](/windows/win32/d2d1/ne-d2d1-d2d1_draw_text_options?branch=master) flag is enabled. For more information, see the following topics:

-   [Color Fonts](https://msdn.microsoft.com/library/windows/desktop/mt765165)
-   [DirectWrite color glyph sample](http://go.microsoft.com/fwlink/p/?LinkId=832476)

### New image effects

Starting in Windows 10 Anniversary Update, Direct2D includes the AlphaMask, CrossFade, Opacity, and Tint effects. This functionality was previously available from specific configurations of Composite, ArithmeticComposite, and ColorMatrix effects, but the new built-in effects make it easier to do these common operations.

## What's new for Windows 10

The following features and APIs were added or updated for Windows 10.

### Sprite batches

Starting in Windows 10, Direct2D provides support for creating and rendering sprite batches. Compared to the general-purpose [**DrawImage**](id2d1devicecontext-drawimage-overload.md) method, sprite batches incur dramatically less per-image CPU overhead. This makes them ideal for scenarios involving hundreds or thousands of concurrent images, such as game sprites or particle systems. For more information, see the following topics:

-   [**ID2D1DeviceContext3::CreateSpriteBatch**](/windows/win32/d2d1_3/?branch=master) method
-   [**ID2D1DeviceContext3::DrawSpriteBatch**](/windows/win32/d2d1_3/nf-d2d1_3-drawspritebatch?branch=master) methods
-   [**ID2D1SpriteBatch**](/windows/win32/d2d1_3/?branch=master) interface

### Gradient meshes

Starting in Windows 10, Direct2D provides a new primitive for gradient meshes. Gradient meshes are often used by professional illustrators in graphic design software, and they allow artists to render complex (even photo-realistic) multicolored shapes with all the memory and scalability benefits of vectors. For more information, see the follow topics:

-   [Direct2D gradient mesh sample](http://go.microsoft.com/fwlink/p/?LinkId=620532)
-   [**D2D1\_GRADIENT\_MESH\_PATCH**](/windows/win32/d2d1_3/ns-d2d1_3-d2d1_gradient_mesh_patch?branch=master) structure
-   [**ID2D1DeviceContext2::DrawGradientMesh**](/windows/win32/D2d1_3/?branch=master) method

### Improved image loading APIs

Starting with Windows 10, Direct2D offers a new API for loading images, ID2D1ImageSource. The image source improves upon existing image loading APIs including CreateBitmapFromWicBitmap, the Bitmap Source effect, and the YCbCr effect. The Direct2D image source combines the capabilities of these APIs with support for arbitrarily large images, easy integration with printing and effects, and numerous optimizations including YCbCr JPEG and indexed JPEG. For more information, see these topics:

-   [Direct2D Photo Adjustment SDK sample](http://go.microsoft.com/fwlink/p/?LinkId=620533)
-   [**ID2D1ImageSource**](/windows/win32/D2d1_3/?branch=master)
-   [**ID2D1ImageSourceFromWic**](/windows/win32/d2d1_3/?branch=master)
-   [IWICJpegFrameDecode::SetIndexing](https://msdn.microsoft.com/library/windows/desktop/dn903861.aspx)

### Improved support for ink rendering

Starting in Windows 10, Direct2D provides a new primitive to represent ink strokes. Direct2D ink strokes are defined by Bezier curves, support different nib shapes and transforms, and may have fixed or variable thickness. Direct2D’s built-in support for ink strokes allows apps to easily render faster, more beautiful ink than previous approaches, which typically required apps to manage ink themselves, as a series of ellipses and quadrilaterals. For more information, see the following topics:

-   [**ID2D1Ink interface**](/windows/win32/d2d1_3/?branch=master)
-   [**ID2D1DeviceContext2::DrawInk method**](/windows/win32/D2d1_3/?branch=master)
-   [**ID2D1InkStyle interface**](/windows/win32/d2d1_3/?branch=master)

### Effect shader linking

Direct2D effects are implemented using HLSL pixel, vertex, and/or compute shaders. Starting with Windows 10, Direct2D now automatically analyzes effect graphs for opportunities to combine and execute individual shaders together. This can provide a significant increase in effect throughput. Consumers of built-in effects do not need to do anything to benefit from effect shader linking, but developers who build their own custom effects should follow updated best practices for leveraging effect shader linking. For more information, see the following topics:

-   [Effect Shader Linking](effect-shader-linking.md)
-   [Direct2D HLSL Helpers](hlsl-helpers.md)
-   [Direct2D custom effects SDK sample](http://go.microsoft.com/fwlink/p/?LinkId=620531)

Effect shader linking is designed to not affect the visual output of effects. However, this is not always possible due to specific behavior around effect precision and numerical clipping. For more information on how to control for these behaviors, see:

-   [Controlling Precision and Numerical Clipping in Effect Graphs](precision-and-clipping-in-effect-graphs.md)

### New built-in effects

Starting with Windows 10, Direct2D includes a rich set of new built-in effects which address top developer requests and enable new kinds of visual scenarios. The new effects are:

### Color:

-   [RGB to Hue effect](rgb-to-hue-effect.md)
-   [Hue to RGB effect](hue-to-rgb-effect.md)
-   [3D lookup table effect](3d-lookup-table-effect.md)

### Photo:

-   [Contrast effect](contrast-effect.md)
-   [Exposure effect](exposure-effect.md)
-   [Grayscale effect](grayscale-effect.md)
-   [Highlights and shadows effect](highlights-and-shadows-effect.md)
-   [Invert effect](invert-effect.md)
-   [Sepia effect](sepia-effect.md)
-   [Sharpen effect](sharpen-effect.md)
-   [Straighten effect](straighten-effect.md)
-   [Temperature and tint effect](temperature-and-tint-effect.md)
-   [Vignette effect](vignette-effect.md)

### Filter:

-   [Edge detection effect](edge-detection-effect.md)

### Stylize:

-   [Emboss effect](emboss-effect.md)
-   [Posterize effect](posterize-effect.md)

### Transparency:

-   [Chroma-key effect](chromakey-effect.md)

The straighten, saturation, contrast, highlights and shadows, and temperature and tint effects are demonstrated in the [Direct2D Photo Adjustment SDK sample](http://go.microsoft.com/fwlink/p/?LinkId=620533).

## What's new for Windows 8.1

The following features and APIs were added or updated for Windows 8.1.

Starting with Windows 8.1, Direct2D is built on top of Direct3D 11.2.

### Geometry realizations

Starting in Windows 8.1, Direct2D offers geometry realizations. Geometry realizations allow applications to improve geometry rendering performance in certain situations, without some of the drawbacks of rasterizing geometry to a bitmap. For more information, see the following topics:

-   [**ID2D1Device1**](/windows/win32/D2d1_2/?branch=master) interface
-   [**ID2D1DeviceContext1::DrawGeometryRealization**](/windows/win32/D2d1_2/?branch=master) method

### Support for JPEG YCbCr images

Starting in Windows 8.1, Direct2D provides support for rendering image data in the JPEG Y’CbCr format. Apps can render JPEG content in its native Y’CbCr representation instead of decompressing to BGRA. This can significantly reduce graphics memory consumption and resource creation time. For more information, see the following topics:

-   Direct2D [YCbCr effect](ycbcr-effect.md)
-   [**IWICPlanarBitmapSourceTransform**](https://msdn.microsoft.com/library/windows/desktop/dn302093) interface

### Support for block compressed formats (DDS files)

Starting in Windows 8.1, Direct2D provides support for bitmaps that contain DXGI\_FORMAT\_BC1\_UNORM, DXGI\_FORMAT\_BC2\_UNORM, and DXGI\_FORMAT\_BC3\_UNORM pixel data. Apps can replace their image assets with block compressed DDS images. This can significantly reduce graphics memory consumption and resource creation time. For more information, see the following topics:

-   [**ID2D1DeviceContext::CreateBitmapFromWicBitmap**](id2d1devicecontext-createbitmapfromwicbitmap-overload.md) method
-   [**IWICDdsFrameDecode**](https://msdn.microsoft.com/library/windows/desktop/dn302086) interface

### Rendering priority

Starting in Windows 8.1, Direct2D provides support for per-device rendering priority. This new feature allows apps to switch a device between normal rendering priority (the default) and low rendering priority (in which the device will not block other rendering tasks on the system). It is recommended that apps use low rendering priority for tasks that are not critical to user-responsiveness, such as pre-rendering content, rendering while minimized, and other operations that are typically performed in the background. For more information, see the following topics:

-   [**ID2D1Device1::SetRenderingPriority**](/windows/win32/D2d1_2/?branch=master) method
-   [**D2D1\_RENDERING\_PRIORITY**](/windows/win32/D2D1_2/ne-d2d1_2-d2d1_rendering_priority?branch=master) enumeration

## What's new for Windows 8

The following features and APIs were added or updated for Windows 8.

The new Direct2D interfaces are supported on Windows 7 with the [Platform Update for Windows 7](https://msdn.microsoft.com/library/windows/desktop/jj863687) installed.

Direct2D's semantics for devices and device contexts have been updated to more closely resemble the semantics used by Direct3D, and to provide concise operation on Windows Store apps. See [Devices and device contexts](devices-and-device-contexts.md) for more info.

Selected related APIs:

-   [**ID2D1Device**](/windows/win32/D2d1_1/?branch=master)
-   [**ID2D1DeviceContext**](/windows/win32/D2d1_1/?branch=master)

The command list API allows you to share the rendering path for on screen rendering and printing. It also allows you to use primitives to create an image brush for filling primitives.

Selected related APIs:

-   [**ID2D1CommandList**](/windows/win32/D2d1_1/?branch=master)
-   [**ID2D1PrintControl**](/windows/win32/D2d1_1/?branch=master)
-   [**ID2D1ImageBrush**](/windows/win32/d2d1_1/?branch=master)

[Direct2D effects](effects-overview.md) is a set of APIs, new in Windows 8, for applying high quality effects to images. It also includes APIs that allow you to make your own custom effects.

Selected related APIs:

-   [**ID2D1Effect**](/windows/win32/D2d1_1/?branch=master)
-   [**ID2D1EffectImpl**](/windows/win32/d2d1effectauthor/?branch=master)
-   [**ID2D1EffectContext**](/windows/win32/D2D1EffectAuthor/?branch=master)

Starting with Windows 8, Direct2D includes additional APIs for building multithreaded apps. See [Multithreaded Direct2D Apps](multi-threaded-direct2d-apps.md) for more info.

Selected related APIs:

-   [**ID2D1MultiThread**](/windows/win32/D2d1_1/?branch=master)
-   [**D2D1\_FACTORY\_TYPE\_MULTI\_THREADED**](/windows/win32/d2d1/ne-d2d1-d2d1_factory_type?branch=master)

 

 




