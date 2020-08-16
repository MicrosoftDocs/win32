---
title: Bitmap objects
description: This topic describes the types of bitmap content that DirectComposition supports.
ms.assetid: BC32CF76-D5E4-4B25-AFD5-42E8DABFA0D0
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap objects

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

Microsoft DirectComposition is a bitmap compositing engine. It enables application developers to combine multiple bitmaps and manipulate them in various ways to achieve interesting visual effects and animations in an application UI. This topic describes the types of bitmap content that DirectComposition supports.

-   [Bitmap content](#bitmap-content)
    -   [Video memory bitmaps](#video-memory-bitmaps)
    -   [Window bitmaps](#window-bitmaps)
    -   [Associating bitmap content with a visual](#associating-bitmap-content-with-a-visual)
    -   [Alpha channel](#alpha-channel)
-   [Related topics](#related-topics)

## Bitmap content

Applications provide DirectComposition with the bitmap content to compose and animate by creating visual objects and then setting the [Content property](basic-concepts.md) of those objects. DirectComposition does not offer any rasterization services. An application must use some other software-based or hardware-accelerated rasterization library such as [Direct2D](../direct2d/direct2d-portal.md) or [Direct3D](/windows/desktop/direct3d11/atoc-dx-graphics-direct3d-11) to populate the bitmaps that are to be composed. After composing, DirectComposition passes composed bitmap content to [Desktop Window Manager (DWM)](/windows/desktop/dwm/dwm-overview) for rendering to the screen.

**Supported types of bitmap content** Microsoft DirectComposition supports the following kinds of bitmaps:

-   [Video memory bitmaps](#video-memory-bitmaps)
-   [Window bitmaps](#window-bitmaps)

### Video memory bitmaps

A video memory bitmap is rasterized in hardware by using Microsoft DirectX methods (including the DX-to-GDI interop model). It is backed by cross-process shared surfaces that are visible to the calling application and to DirectComposition. A video memory bitmap is not subject to tearing because the application can only read from the surfaces that DirectComposition textures from.

### Video content

Applications can use DirectComposition to compose video frames that use DirectX windowless swap chains that are bound to a DirectComposition surface. Conceptually, DirectComposition treats video content as a sequence of bitmaps. DirectComposition does not provide a means of presenting video frames.

DirectComposition supports DirectX windowless swap chains—that is, swap chains that are not bound to a particular window—and enables two different applications to share windowless swap chains across process boundaries. Sharing windowless swap chains enables video scenarios where the swap chain is created in one process and is used with DirectComposition in a second process. Windowless swap chains are created using the [**IDXGIFactory2::CreateSwapChainForCompositionSurface**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforcomposition) method.

For more information about DirectX swap chains, see [DXGI Overview](/windows/desktop/direct3ddxgi/d3d10-graphics-programming-guide-dxgi).

### Stereo content

Conceptually, a stereo swap chain consists of Microsoft DirectX Graphics Infrastructure (DXGI) surfaces that represent the left and right channels for stereo 3D content. When a stereo swap chain is used as the bitmap resource for a visual, DirectComposition composes in stereo. All non-stereo content (mono content) is considered to have identical left and right channel content; that is, the same bitmap content is used for both channels. DirectComposition composes all left content and all right content separately. If the display device is not stereo capable, DirectComposition treats the left or right stereo channel (depending on the application) as mono content and composes using only that data for the bitmap resource.

DirectComposition does not support creating or manipulating stereo content, and cannot promote a mono swap chain to a stereo pair. An application must perform these tasks before presenting DirectX stereo content to DirectComposition. Also, an application must provide the left and right channel offsets for depth perception; DirectComposition cannot adjust the left and right channel offsets to modify the perceived depth of DirectX stereo content.

DirectX stereo content is composed and persisted to DWM when stereo-capable hardware is available.

### Window bitmaps

A "window bitmap" is not a real bitmap, but is a placeholder that DirectComposition replaces in real time with rasterizations of layered top-level or child windows. A window bitmap is similar to a DWM thumbnail, except that a thumbnail can contain contributions from many windows, such as owned non-child windows, whereas a DirectComposition window bitmap is always a representation of just one window and its children.

Because DirectComposition has access to the redirection surfaces of all windows and all visual trees, it can reuse the content from one window in multiple visual trees. The window must be layered because a non-layered window does not have a dedicated redirection surface and, therefore, its rasterization is not always available to DirectComposition.

To use a window bitmap, an application associates a visual with a window handle (HWND). Afterward, DirectComposition re-composes the visual whenever the contents of the window change, including when the contents change as a result of changes to the visual trees associated with the window. In other words, like DWM thumbnails, DirectComposition window bitmaps are "live".

### Associating bitmap content with a visual

For all three kinds of bitmaps, an application can associate the same bitmap with multiple visuals, which means that a single memory allocation can be used to display the same content several times.

### Alpha channel

All bitmaps have a 32 bits per pixel (BPP) format, which includes eight bits for per-pixel transparency. However, an application can specify how DirectComposition should consume the alpha channel. In particular, DirectComposition can respect the alpha channel, or it can ignore alpha altogether, in which case the bitmap is considered to be fully opaque.

An additional alpha mode ignores the alpha channel, but treats the red, green, and blue values as per-channel alpha values instead of the normal interpretation of those channels as color intensities. This mode is useful for ClearType rendering, which requires sub-pixel coverage information. To use the per-channel alpha mode, an application must first use [Direct2D](../direct2d/direct2d-portal.md) and [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal) to write sub-pixel coverage data to a bitmap. Next the application must set the correct alpha mode and specify a text color when it associates the bitmap with a visual. DirectComposition blends the text color with the coverage data, which produces ClearType blending against the background.

In situations where the ClearType algorithm is not applicable, such as if the bitmap is not pixel-aligned and axis-aligned, or if it needs to be drawn to an intermediate surface, DirectComposition can use the subpixel coverage data in the bitmap to produce a grayscale rasterization instead, automatically and at no additional cost.

For more information, see the description of the *alphaMode* parameter of the [**IDCompositionDevice::CreateSurface**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-createsurface) or [**IDCompositionDevice::CreateVirtualSurface**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-createvirtualsurface) function.

## Related topics

<dl> <dt>

[DirectComposition Concepts](directcomposition-concepts.md)
</dt> </dl>

 

 