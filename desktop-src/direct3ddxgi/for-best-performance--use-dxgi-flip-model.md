---
description: This topic provides developer guidance on how to maximize performance and efficiency in the presentation stack on modern versions of Windows.
ms.assetid: B6B92F4F-B1D0-40B9-987D-F0C0F2CC7AD1
title: For best performance, use DXGI flip model
ms.topic: article
ms.date: 05/31/2018
ms.custom: RS5
---

# For best performance, use DXGI flip model

This topic provides developer guidance on how to maximize performance and efficiency in the presentation stack on modern versions of Windows. It picks up where [DXGI flip model](dxgi-flip-model.md), [DirectX 12: Presentation Modes In Windows 10 (video)](https://www.youtube.com/watch?v=E3wTajGZOsA), and [Presentation Enhancements in Windows 10: An Early Look (video)](https://www.youtube.com/watch?v=nUZVV_mssWQ) left off.

## Call to action

If you are still using **DXGI\_SWAP\_EFFECT\_DISCARD** or **DXGI\_SWAP\_EFFECT\_SEQUENTIAL** (a.k.a. the "blt" present model), it's time to stop!

Switching to **DXGI\_SWAP\_EFFECT\_FLIP\_SEQUENTIAL** or **DXGI\_SWAP\_EFFECT\_FLIP\_DISCARD** (a.k.a. the flip model) will give better performance, lower power usage, and provide a richer set of features. (See [DXGI\_SWAP\_EFFECT enumeration](/windows/desktop/api/DXGI/ne-dxgi-dxgi_swap_effect) for more information about these values.)

Flip model presents go as far as making windowed mode effectively equivalent or better when compared to the classic "fullscreen exclusive" mode. In fact, you may want to reconsider whether your application actually needs a fullscreen exclusive mode, since the benefits of a flip model borderless window include faster Alt-Tab switching and better integration with modern display features.

Why now? Prior to the April 2018 Update, blt model presents could result in visible tearing when used on hybrid GPU configurations, often found in high-end laptops (see [KB 3158621](https://support.microsoft.com/help/3158621/hybrid-graphics-and-vsync-results-in-graphic-tearing-in-some-games-and)). In the April 2018 Update, this tearing has been fixed, at the cost of some additional work. If you are doing blt presents at high framerates across hybrid GPUs, especially at high resolutions such as 4K, this additional work may affect overall performance. To maintain best performance on these systems, switch from the blt to the flip present model. Additionally, consider reducing the resolution of your swapchain, especially if it isn’t the primary point of user interaction (as is often the case with VR preview windows).

## A brief history

What is the flip model? What is the alternative?

Prior to Windows 7, the only way to present content from D3D was to "blt" or copy it into a surface which was owned by the window or screen. Beginning with D3D9’s FLIPEX swap effect, and coming to DXGI through the FLIP\_SEQUENTIAL swap effect in Windows 8, we’ve developed a more efficient way to put content on screen by sharing it directly with the desktop compositor, with minimal copies. See [DXGI flip model](dxgi-flip-model.md) for a high level overview of the technology.

This optimization is possible thanks to the DWM (Desktop Window Manager), which is the compositor that drives the Windows desktop.

## When should I use the blt model?

There is one piece of functionality that the flip model does not provide: the ability to have multiple different APIs producing content, which all layer together into the same **HWND**, on a present-by-present basis. An example of this would be using D3D to draw a window background, and then [Windows GDI](/windows/desktop/gdi/windows-gdi) to draw something on top, or using two different graphics APIs, or two swapchains from the same API, to produce alternating frames. If you don’t require **HWND**-level interop between graphics components, then you don’t need blt model.

There is a second piece of functionality that was not provided in the original flip model design, but is available now, which is the ability to present at an unthrottled framerate. For an application using sync interval 0, we do not recommend switching to flip model unless the [IDXGIFactory5::CheckFeatureSupport](/windows/desktop/api/DXGI1_5/nf-dxgi1_5-idxgifactory5-checkfeaturesupport) API is available, and reports support for **DXGI\_FEATURE\_PRESENT\_ALLOW\_TEARING**. This feature is nearly ubiquitous on recent versions of Windows 10 and on modern hardware.

## DirectFlip

If you’ve watched [DirectX 12: Presentation Modes In Windows 10](https://www.youtube.com/watch?v=E3wTajGZOsA), you’ll see talk about "Direct Flip" and "Independent Flip." These are optimizations that are enabled for applications using flip model swapchains. Depending on window and buffer configuration, it is possible to bypass desktop composition entirely and directly send application frames to the screen, in the same way that exclusive fullscreen does.

These days, these optimizations can engage in one of 3 scenarios, in order of increasing functionality:

1.  **DirectFlip**: Your swapchain buffers match the screen dimensions, and your window client region covers the screen. Instead of using the DWM swapchain to display on the screen, the application swapchain is used.
2.  **DirectFlip with panel fitters**: Your window client region covers the screen, and your swapchain buffers are within some hardware-dependent scaling factor (for example, 0.25x to 4x) of the screen. The GPU scanout hardware is used to scale your buffer while sending it to the display.
3.  **DirectFlip with multi-plane overlay (MPO)**: Your swapchain buffers are within some hardware-dependent scaling factor of your window dimensions. The DWM is able to reserve a dedicated hardware scanout plane for your application, which is then scanned out and potentially stretched to an alpha-blended sub-region of the screen.

With the windowed flip model, the application can query hardware support for different DirectFlip scenarios and implement different types of dynamic scaling via the use of [IDXGIOutput6::CheckHardwareCompositionSupport](/windows/desktop/api/DXGI1_6/nf-dxgi1_6-idxgioutput6-checkhardwarecompositionsupport). One caveat to keep in mind is that if panel fitters are utilized, it’s possible for the cursor to suffer stretching side effects, which is indicated via **DXGI\_HARDWARE\_COMPOSITION\_SUPPORT\_FLAG\_CURSOR\_STRETCHED**.

Once your swapchain has been "DirectFlipped," then the DWM can go to sleep, and only wake up when something changes outside of your application. Your application frames are sent directly to the screen, independently, with the same efficiency as fullscreen exclusive. This is "Independent Flip," and can engage in all of the above scenarios. If other desktop contents come on top, the DWM can either seamlessly transition back to composed mode, efficiently "reverse compose" the contents on top of the application before flipping it, or leverage MPO to maintain the independent flip mode.

Check out the [PresentMon](https://github.com/GameTechDev/PresentMon) tool to get insight into which of the above was used.

## What else is new in the flip model?

In addition to the above improvements, which apply to standard swapchains without anything special, there are several features available for flip model applications to use:

-   Decreasing latency using **DXGI\_SWAP\_CHAIN\_FLAG\_FRAME\_LATENCY\_WAITABLE\_OBJECT**. When in Independent Flip mode, you can get down to 1 frame of latency on recent versions of Windows, with graceful fallback to the minimum possible when composed.
    -   Caveat: there was an issue that gave a minimum of two frames of latency in the Windows 10 Anniversary Update and earlier. See [this forum topic](https://www.gamedev.net/forums/topic/686507-windows-10-dx12-low-latency-tearing-free-rendering/) for more information. This is fixed in the Fall Creator’s Update.
-   **DXGI\_SWAP\_EFFECT\_FLIP\_DISCARD** enables a "reverse composition" mode of direct flip, which results in less overall work to display the desktop. The DWM can scribble on the application buffers and send those to the screen, instead of performing a full copy into their own swapchains.
-   **DXGI\_SWAP\_CHAIN\_FLAG\_ALLOW\_TEARING** can enable even lower latency than the waitable object, even in a window on systems with multi-plane overlay support.
-   Applications have control over content scaling that happens during window resize, using the [DXGI\_SCALING](/windows/desktop/api/DXGI1_2/ne-dxgi1_2-dxgi_scaling) property set during swapchain creation.
-   Content in HDR formats (R10G10B10A2\_UNORM or R16G16B16A16\_FLOAT) isn’t clamped unless it’s composed to an SDR desktop.
-   Present statistics are available in windowed mode.
-   There is greater compatibility with the UWP (Universal Windows Platform) application model and DX12 since these are only compatible with the flip model.

## What do I have to do to use the flip model?

Flip model swapchains have a few additional requirements on top of blt swapchains:

1.  The buffer count must be at least 2.
2.  After [Present](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-present) calls, the back buffer needs to explicitly be re-bound to the D3D11 immediate context before it can be used again.
3.  After calling [SetFullscreenState](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-setfullscreenstate), the application must call [ResizeBuffers](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-resizebuffers) before **Present**.
4.  MSAA (multisample anti-aliasing) swapchains are not directly supported in the flip model, so the application will need to do an MSAA resolve before issuing the **Present**.

## How to choose the right rendering and presentation resolutions

The traditional pattern for applications in the past has been to provide the user with a list of resolutions to choose from when the user selects exclusive fullscreen mode. With the ability of modern displays to seamlessly begin scaling content, consider providing users with the ability to choose a rendering resolution for performance scaling, independent from an output resolution, and even in windowed mode. Furthermore, applications should leverage **IDXGIOutput6::CheckHardwareCompositionSupport** to determine if they need to scale the content before presenting it, or if they should let the hardware do the scaling for them.

Your content may need to be migrated from one GPU to another as part of the present or composition operation. This is often true on multi-GPU laptops, or systems with external GPUs plugged in. As these configurations get more common, and as high-resolution displays become more common, the cost of presenting a full resolution swapchain increases. If the target of your swapchain isn’t the primary point of user interaction, as is often the case with VR titles that present a 2D preview of the VR scene into a secondary window, consider using a lower resolution swapchain to minimize the amount of bandwidth that needs to be transferred across different GPUs.

## Other considerations

The first time you ask the GPU to write to the swapchain back buffer is the time that the GPU will stall waiting for the buffer to become available. When possible, delay this point as far into the frame as possible.

 

 
