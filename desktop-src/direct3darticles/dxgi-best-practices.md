---
title: DirectX Graphics Infrastructure (DXGI) Best Practices
description: This article discusses key porting issues.
ms.assetid: 2df92ffe-1bfc-d682-2770-20cf0c831c9b
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Graphics Infrastructure (DXGI): Best Practices

Microsoft DirectX Graphics Infrastructure (DXGI) is a new subsystem that was introduced with Windows Vista that encapsulates some of the low-level tasks that are needed by Direct3D 10, 10.1, 11, and 11.1. From the perspective of a Direct3D 9 programmer, DXGI encompasses most of the code for enumeration, swap-chain creation, and presentation that previously was packed into the Direct3D 9 APIs. When you port an app to DXGI and Direct3D 10.x and Direct3D 11.x, you need to take some considerations into account to ensure that the process runs smoothly.

This article discusses key porting issues.

-   [Full-Screen Issues](#full-screen-issues)
-   [Multiple Monitors](#multiple-monitors)
-   [Window Styles and DXGI](#window-styles-and-dxgi)
-   [Multithreading and DXGI](#multithreading-and-dxgi)
-   [Gamma and DXGI](#gamma-and-dxgi)
-   [DXGI 1.1](#dxgi-11)
-   [DXGI 1.2](#dxgi-12)

## Full-Screen Issues

In porting from Direct3D 9 to DXGI and to Direct3D 10.x or Direct3D 11.x, issues associated with moving from windowing to full-screen mode often may cause headaches for developers. The main problems arise because Direct3D 9 applications, unlike DXGI applications, require a more hands-on approach to tracking window styles and window states. When the mode-changing code is ported to run on DXGI, it often causes unexpected behavior.

Often, Direct3D 9 applications handled the transition into full-screen mode by setting the resolution of the front buffer, forcing the device into full-screen exclusive mode, and then setting the back buffer resolutions to match. A separate path was used for changes to window size because they had to be managed from the window process whenever the application received a WM\_SIZE message.

DXGI attempts to simplify this approach by combining the two cases. For example, when the window border is dragged in windowed mode, the application receives a WM\_SIZE message. DXGI intercepts this message and automatically resizes the front buffer. All that the application needs to do is call [**IDXGISwapChain::ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) to resize the back buffer to the size that was passed as parameters in WM\_SIZE. Similarly, when the application needs to switch between full-screen and windowed mode, the application can simply call [**IDXGISwapChain::SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate). DXGI resizes the front buffer to match the newly selected full-screen mode, and it sends a WM\_SIZE message to the application. The application again calls **ResizeBuffers**, just as it would if the window border was dragged.

The methodology of the preceding explanation follows a very particular path. DXGI set the full-screen resolution to the desktop resolution by default. Many applications, however, switch to a preferred full-screen resolution. In such a case, DXGI provides [**IDXGISwapChain::ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget). This should be called before calling [**SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate). Although these methods can be called in the opposite order (**SetFullscreenState** first, followed by **ResizeTarget**), doing so causes an extra WM\_SIZE message to be sent to the application. (Doing so can also cause flickering, since DXGI could be forced to perform two mode changes.) After calling **SetFullscreenState**, it is advisable to call **ResizeTarget** again with the **RefreshRate** member of [**DXGI\_MODE\_DESC**](/previous-versions/windows/desktop/legacy/bb173064(v=vs.85)) zeroed out. This amounts to a no-operation instruction in DXGI, but it can avoid issues with the refresh rate, which are discussed next.

When in full-screen mode, the Desktop Window Manager (DWM) is disabled. DXGI can perform a flip to present the back buffer contents instead of doing a blit, which it would do in windowed mode. This performance gain can be undone, however, if certain requirements are not met. To ensure that DXGI does a flip instead of a blit, the front buffer and back buffer must be sized identically. If the application correctly handles its WM\_SIZE messages, this should not be a problem. Also, the formats must be identical.

The problem for most applications is the refresh rate. The refresh rate that is specified in the call to [**ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget) must be a refresh rate that is enumerated by the [**IDXGIOutput**](/windows/desktop/api/dxgi/nn-dxgi-idxgioutput) object that the swap chain is using. DXGI can automatically calculate this value if the application zeroes out the **RefreshRate** member of [**DXGI\_MODE\_DESC**](/previous-versions/windows/desktop/legacy/bb173064(v=vs.85)) that is passed into **ResizeTarget**. It is important not to assume that certain refresh rates will always be supported and to simply hard-code a value. Often, developers choose 60 Hz as the refresh rate, not knowing that the enumerated refresh rate from the monitor is approximately 60,000 / 1,001 Hz from the monitor. If the refresh rate does not match the expected refresh rate of 60, DXGI is forced to perform a blit in full-screen mode instead of a flip.

The last issue that developers often face is how to change full-screen resolutions while remaining in full-screen mode. Calling [**ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget) and [**SetFullscreenState**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-setfullscreenstate) sometimes succeeds, but the full-screen resolution remains the desktop resolution. Also, developers may create a full-screen swap chain and give a specific resolution, only to find that DXGI defaults to the desktop resolution regardless of the numbers passed in. Unless otherwise instructed, DXGI defaults to the desktop resolution for full-screen swap chains. When creating a full-screen swap chain, the **Flags** member of the [**DXGI\_SWAP\_CHAIN\_DESC**](/windows/desktop/api/dxgi/ns-dxgi-dxgi_swap_chain_desc) structure must be set to [**DXGI\_SWAP\_CHAIN\_FLAG\_ALLOW\_MODE\_SWITCH**](/windows/desktop/api/dxgi/ne-dxgi-dxgi_swap_chain_flag) to override DXGI's default behavior. This flag also can be passed to **ResizeTarget** to enable or disable this functionality dynamically.

## Multiple Monitors

When using DXGI with multiple monitors, there are two rules to follow.

The first rule applies to the creation of two or more full-screen swap chains on multiple monitors. When creating such swap chains, it is best to create all swap chains as windowed, and then to set them to full-screen. If swap chains are created in full-screen mode, the creation of a second swap chain causes a mode change to be sent to the first swap chain, which could cause termination of full-screen mode.

The second rule applies to outputs. Be watchful of outputs used when creating swap chains. With DXGI, the [**IDXGIOutput**](/windows/desktop/api/dxgi/nn-dxgi-idxgioutput) object controls which monitor the swap chain uses when becoming full-screen. Unlike DXGI, Direct3D 9 had no concept of outputs.

## Window Styles and DXGI

Direct3D 9 applications had a lot of work to do when switching between full-screen and windowed modes. Much of this work involved changing window styles to add and remove borders, to add scrollbars, and so on. When applications are ported to DXGI and Direct3D 10.x or Direct3D 11.x, this code often is left in place. Depending on the changes being made, switching between modes can cause unexpected behavior. For example, when switching to windowed mode, the application might no longer have a window frame or window border despite having code that specifically sets these styles. This occurs because DXGI now handles much of this style changing on its own. Manual setting of window styles can interfere with DXGI, and this can cause unexpected behavior.

The recommended behavior is to do as little work as possible, and to let DXGI handle most of the interaction with the windows. However, if the application needs to handle its own windowing behavior, [**IDXGIFactory::MakeWindowAssociation**](/windows/desktop/api/dxgi/nf-dxgi-idxgifactory-makewindowassociation) can be used to tell DXGI to disable some of its automatic window handling.

## Multithreading and DXGI

Special care must be taken when using DXGI in a multithreaded application to ensure that deadlocks do not occur. Because of DXGI's close interaction with windowing, it occasionally sends window messages to the associated application window. DXGI needs the windowing changes to occur before it can continue, so it will use [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage), which is a synchronous call. The application must process the window message before **SendMessage** returns.

In an application where DXGI calls and the message pump are on the same thread (or a single-threaded application), little needs to be done. When the DXGI call is on the same thread as the message pump, [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) calls the window's [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)). This bypasses the message pump, and allows execution to continue after the call to **SendMessage**. Remember that [**IDXGISwapChain**](/windows/desktop/api/dxgi/nn-dxgi-idxgiswapchain) calls, such as [**IDXGISwapChain::Present**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-present), are also considered DXGI calls; DXGI may defer work from [**ResizeBuffers**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizebuffers) or [**ResizeTarget**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-resizetarget) until **Present** is called.

If the DXGI call and message pump are on different threads, care must be taken to avoid deadlocks. When the message pump and SendMessage are on different threads, [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) adds a message to the window's message queue, and waits for the window to process that message. If the window procedure is busy or is not called by the message pump, the message may never get processed and DXGI will wait indefinitely.

For example, if an application that has its message pump on one thread and its rendering on another, it may want to change modes. The message pump thread tells the rendering thread to change modes, and waits until the mode change is complete. However, the rendering thread calls DXGI functions, which in turn call [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage), which blocks until the message pump processes the message. A deadlock occurs because both threads now are blocked, and are waiting on each other. To avoid this, never block the message pump. If a block is unavoidable, then all DXGI interaction should occur on the same thread as the message pump.

## Gamma and DXGI

Although gamma may be best handled in Direct3D 10.x or Direct3D 11.x by using SRGB textures, the gamma ramp still can be useful to developers who want a different gamma value than 2.2 or who are using a render target format that does not support SRGB. Be aware of two issues when setting the gamma ramp through DXGI. The first issue is that the ramp values passed into [**IDXGIOutput::SetGammaControl**](/windows/desktop/api/dxgi/nf-dxgi-idxgioutput-setgammacontrol) are float values, not **WORD** values. Also, ensure that code ported from Direct3D 9 does not try to convert to **WORD** values before passing these to **SetGammaControl**.

The second issue is that, after changing to full-screen mode, [**SetGammaControl**](/windows/desktop/api/dxgi/nf-dxgi-idxgioutput-setgammacontrol) may not appear to work, dependent on the [**IDXGIOutput**](/windows/desktop/api/dxgi/nn-dxgi-idxgioutput) object being used. When changing to full-screen mode, DXGI creates a new output object, and uses the object for all subsequent operations on the output. If calling **SetGammaControl** on an output that is enumerated before a full-screen mode switch, the call is not directed toward the output that DXGI is using currently. To avoid this, call [**IDXGISwapChain::GetContainingOutput**](/windows/desktop/api/dxgi/nf-dxgi-idxgiswapchain-getcontainingoutput) to get the current output, and then call **SetGammaControl** off this output to get the correct behavior.

For info about using gamma correction, see [Using gamma correction](/windows/desktop/direct3ddxgi/using-gamma-correction).

## DXGI 1.1

The Direct3D 11 runtime included in Windows 7 and installed onto Windows Vista includes version 1.1 of DXGI. This update adds definitions for a number of new formats (particularly BGRA, 10-bit X2 bias, and Direct3D 11's BC6H and BC7 texture compression), as well as a new version of the DXGI factory and adapter interfaces ([**CreateDXGIFactory1**](/windows/desktop/api/dxgi/nf-dxgi-createdxgifactory1), [**IDXGIFactory1**](/windows/desktop/api/dxgi/nn-dxgi-idxgifactory1), [**IDXGIAdapter1**](/windows/desktop/api/dxgi/nn-dxgi-idxgiadapter1)) for enumerating remote desktop connections.

When you use Direct3D 11, the runtime will use DXGI 1.1 by default when calling [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice) or [**D3D11CreateDeviceAndSwapChain**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdeviceandswapchain) with a NULL [**IDXGIAdapter**](/windows/desktop/api/dxgi/nn-dxgi-idxgiadapter) pointer. Mixing use of DXGI 1.0 and DXGI 1.1 in the same process is not supported. Mixing DXGI object instances from different factories in the same process also is not supported. Therefore, when you use DirectX 11, any explicit use of the DXGI interfaces uses a [**IDXGIFactory1**](/windows/desktop/api/dxgi/nn-dxgi-idxgifactory1) created by the [**CreateDXGIFactory1**](/windows/desktop/api/dxgi/nf-dxgi-createdxgifactory1) entry-point in “DXGI.DLL” to ensure the application is always using DXGI 1.1.

## DXGI 1.2

The Direct3D 11.1 runtime that is included in Windows 8 also includes version 1.2 of DXGI.

DXGI 1.2 enables these features:

-   stereo rendering
-   16 bit-per-pixel formats

    -   DXGI\_FORMAT\_B5G6R5\_UNORM and DXGI\_FORMAT\_B5G5R5A1\_UNORM are now fully supported
    -   a new DXGI\_FORMAT\_B5G5R5A1\_UNORM format was added

-   video formats
-   new DXGI interfaces

For more info about DXGI 1.2 features, see [DXGI 1.2 Improvements](/windows/desktop/direct3ddxgi/dxgi-1-2-improvements).

 

 
