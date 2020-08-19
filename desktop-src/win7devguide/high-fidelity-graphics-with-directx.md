---
title: High Fidelity Graphics with DirectX
description: Windows application developers have long used Microsoft DirectX to provide high-quality, hardware-accelerated, 3D graphics.
ms.assetid: db555657-90b9-4db2-a0c2-bfaa526a8dd5
ms.topic: article
ms.date: 05/31/2018
---

# High Fidelity Graphics with DirectX

Windows application developers have long used Microsoft DirectX to provide high-quality, hardware-accelerated, 3D graphics. When the technology debuted in 1995, developers could provide high-quality 3D graphics for games and engineering applications for gamers and professionals willing to pay extra for a 3D graphics board. Now, even the most inexpensive PCs include capable 3D-graphics hardware.

To take advantage of these graphics capabilities, Windows Vista introduced the Windows Display Driver Model (WDDM) infrastructure for DirectX that enabled multiple applications and services to share the resources of the graphics processing unit (GPU). The Desktop Window Manager (DWM) uses this technology to animate task switching in 3D, provide dynamic thumbnail images of application windows, and to provide Windows Aero glass effects for desktop applications.

Windows 7 puts even more graphics capability into the hands of application developers. Through a new set of DirectXAPIs, Microsoft Win32 developers can take advantage of the latest innovations in GPUs to add fast, scalable, high-quality, 2D and 3D graphics, text, and images to their applications. On the latest *LCD* displays, DirectXAPIs can display desktop and window content using color depth greater than 8 bits per color component.

With DirectX, Win32 developers can also use the GPU's parallelism for general-purpose computation such as image processing, and can render to DirectX 10 hardware, DirectX 9 hardware, the CPU, or to a remote Windows computer. These technologies were designed to interoperate with Windows Graphics Device Interface (GDI) and Windows GDI+, ensuring that developers can easily preserve their existing investments in Win32 code. (See [What's New in the March 2009 DirectX SDK](/previous-versions//bb173043(v=vs.85)).)

These enhanced graphics capabilities are provided by the following *COM*-based APIs:

-   [Direct2D](../direct2d/direct2d-portal.md) for drawing 2D graphics.
-   [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal) for arranging and rendering text.
-   [Windows Imaging Component](/windows/desktop/wic/-wic-lh) for processing and displaying images.
-   [Direct3D 10](/windows/desktop/direct3d10/d3d10-graphics) for drawing 3D graphics.
-   [Direct3D 11](/windows/desktop/direct3d11/atoc-dx-graphics-direct3d-11) for drawing 3D graphics, and providing access to next-generation GPU technologies, such as tessellation, limited support for texture streaming, and general purpose computing.
-   [DirectX Graphics Infrastructure (DXGI)](/windows/desktop/direct3ddxgi/dx-graphics-dxgi) for managing local and remote display devices and GPU resources, and providing interoperability between DirectX and GDI.

## Direct2D

Built on Microsoft Direct3D 10, [Direct2D](../direct2d/direct2d-portal.md) offers Win32 developers immediate-mode, resolution-independent, 2D APIs that use the power of next-generation graphics hardware, yet interoperate well with today's GDI/GDI+ applications and Direct3D 10 applications. Direct2D provides high-quality 2D rendering with performance superior to GDI and GDI+. It provides Win32 developers finer control over resources and their management. (See [Direct2D](../direct2d/direct2d-portal.md).)

## DirectWrite

Many of today's applications need to support high-quality text rendering, resolution-independent outline fonts, and full Unicode text and layout support. [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal), a new DirectX component, provides these features and more:

-   A device-independent text layout system that improves text readability in documents and in UI.
-   High-quality, sub-pixel, *ClearType* text rendering that can use GDI, [Direct2D](../direct2d/direct2d-portal.md), or application-specific rendering technology.
-   Hardware-accelerated text, when used with [Direct2D](../direct2d/direct2d-portal.md).
-   Support for multi-format text.
-   Support for the advanced typography features of *OpenType* fonts.
-   Support for the layout and rendering of text in all supported languages.
-   GDI-compatible layout and rendering.

The [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal) font system enables "any font anywhere" font usage, where users don't have to perform a separate installation step just to use a font, and an improved structural hierarchy of font grouping to help with manual or programmatic font discovery. The APIs support measuring, drawing, and hit-testing of multi-format text. DirectWrite handles text in all supported languages for global and localized applications, building on the key language infrastructure found in Windows 7. DirectWrite also provides low-level glyph rendering APIs for developers who want to perform their own layout and Unicode-to-glyph processing. (See [DirectWrite](../directwrite/direct-write-portal.md).)

## Windows Imaging Component

In Windows Vista, the [Windows Imaging Component](/windows/desktop/wic/-wic-lh) introduced an extensible framework for working with images and image metadata. The image formats supported by Windows Imaging Component include *JPEG*, *PNG*, and *TIFF*, and the supported metadata formats include *XMP* and *EXIF*. With Windows 7, Windows Imaging Component broadens its standards compliance by providing support for progressive image decoding, expanded *PNG* features, *GIF* metadata, and metadata that spans *APPn* segments. (See [What's New for WIC in Windows 7](/previous-versions//ee720061(v=vs.85)).)

## Direct3D 11

Microsoft Direct3D 11 extends the functionality of the Direct3D 10 pipeline and provides Windows 7 games and high-end 3D applications with efficient, robust, scalable access to the upcoming generation of GPUs and multi-core CPUs. In addition to the functionality found in Direct3D 10, Direct3D 11 introduces several new features.

Geometry and high-order surfaces can now be tessellated to support scalable, dynamic content in patch and subdivision surface representations.

To make good use of the parallel processing power available from multiple CPU cores, multithreading increases the number of potential rendering calls per frame by distributing the application, runtime, and driver calls across multiple cores. In addition, resource creation and management has been optimized for multithreaded use, enabling more efficient dynamic texture management for streaming.

New general-purpose compute shaders have been created for Direct3D 11. Unlike existing shaders, these are extensions to the programmable pipeline that enable your application to do more work completely on the GPU, independent of the CPU. [**DrawAuto**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-drawauto), which was introduced in Direct3D 10, has been extended to interact with a compute shader.

Several improvements have been made to the high-level shading language ([HLSL](/windows/desktop/direct3dhlsl/dx-graphics-hlsl)), such as a limited form of dynamic linkage in shaders to improve specialization complexity, and object-oriented programming constructs like classes and interfaces. (See [What's New in the March 2009 DirectX SDK](/previous-versions//bb173043(v=vs.85)).)

## Direct3D 10 Improvements

Direct3D 10 includes a redesigned graphics pipeline with programmable shader stages and immutable state objects for initializing the fixed-function stages. The state objects simplify the pipeline and improve performance by minimizing the number of state changes required. Programmability of shader stages now offers high-level shading language extensions to support unlimited shader instructions, generalized shader resources, and integer and bitwise calculations.

The pipeline also introduces the geometry shader stage, which offloads work entirely from the CPU to the GPU. This new stage enables you to create geometry, stream the data to memory, and render the geometry with no CPU interaction.

Several other improvements are designed specifically for faster performance. Predicated rendering performs occlusion culling to reduce the amount of geometry that is rendered. Instancing APIs can dramatically reduce the amount of geometry that needs to be transferred to the GPU by drawing multiple-instances of similar objects. Texture arrays enable the GPU to do texture swapping without CPU intervention.

Several additions have been made to Direct3D 10 and Direct3D 11 to extend the gamut of configurations that can be targeted with these APIs. The [Windows Advanced Rasterization Platform (WARP)](/windows/desktop/direct3darticles/directx-warp) implements fast, multi-core scalable CPU rendering for Direct3D 10, enabling full-featured graphics rendering on systems without graphics hardware. The addition of new "Feature Levels," specifically called [Direct3D 10 Level 9](/windows/desktop/direct3d11/d3d11-graphics-reference-10level9), allow the Direct3D 10 and Direct3D 11APIs to drive Microsoft Direct3D 9-class hardware, expanding the number of configurations a Direct3D 10 or Direct3D 11 application can target to nearly every computer system on the market. (See [Direct3D 10 Graphics](../direct3d10/d3d10-graphics.md).)

## DirectX/GDI Interoperability

In Windows Vista, the behavior of an application that uses both DirectX and GDI to render to a shared surface is different depending on whether DWM is on or off. In addition, when DWM is on, applications that use both DirectX and GDI behave differently on Windows Vista than on Windows XP. This caused many ISVs to disable DWM when running their applications on Windows Vista to ensure consistent behavior. With the improvements to DirectX in Windows 7, an application can now freely mix DirectX and GDI without disabling DWM. Windows 7 also features improved performance for scenarios that require interoperation between DirectX and GDI by utilizing the more efficient Direct3D 10 APIs. (See [Direct2D and GDI Interoperation Overview](../direct2d/direct2d-and-gdi-interoperation-overview.md).)

 

 