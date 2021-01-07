---
description: Describes how to use hardware overlays in Direct3D 9.
ms.assetid: fa9d5bf5-4c0f-471a-b639-d329b0cd89a4
title: Hardware Overlay Support
ms.topic: article
ms.date: 05/31/2018
---

# Hardware Overlay Support

A hardware overlay is a dedicated area of video memory that can be overlayed on the primary surface. No copy is performed when the overlay is displayed. The overlay operation is performed in hardware, without modifying the data in the primary surface.

The use of hardware overlays for video playback was common in earlier versions of Windows, because overlays are efficient for video content with a high frame rate. Starting in Windows 7, Direct3D 9 supports hardware overlays. This support is intended primarily for video playback, and differs in some respects from earlier DirectDraw APIs:

-   The overlay cannot be shrunk, mirrored, or deinterlaced.
-   Source color keys and alpha blending are not supported.
-   Overlays can be stretched if the overlay hardware supports it. Otherwise, stretching is not supported. In practice, not all graphics drivers support stretching.
-   Each device supports at most one overlay.
-   Overlay is performed using a destination color key, but the Direct3D runtime automatically selects the color and draws the destination rectangle. Direct3D automatically tracks the position of the window and updates the overlay position whenever the **PresentEx** is called.

### Creating a Hardware Overlay Surface

To query for overlay support, call **IDirect3D9::GetDeviceCaps**. If the driver supports hardware overlay, the **D3DCAPS\_OVERLAY** flag is set in the **D3DCAPS9.Caps** member.

To find out whether a specific overlay format is supported for a given display mode, call [**IDirect3D9ExOverlayExtension::CheckDeviceOverlayType**](/windows/desktop/api/d3d9/nf-d3d9-idirect3d9exoverlayextension-checkdeviceoverlaytype).

To create the overlay, call **IDirect3D9Ex::CreateDeviceEx** and specify the **D3DSWAPEFFECT\_OVERLAY** swap effect. The back buffer can use a non-RGB format if the hardware supports it.

Overlay surfaces have the following limitations:

-   The application cannot create more than one overlay swap chain.
-   The overlay must be used in windowed mode. It cannot be used in fullscreen mode.
-   The overlay swap effect must be used with the **IDirect3DDevice9Ex** interface. It is not supported for **IDirect3DDevice9**.
-   Multisampling cannot be used.
-   The **D3DPRESENT\_DONOTFLIP** and **D3DPRESENT\_FLIPRESTART** flags are not supported.
-   Presentation statistics are not available for the overlay surface.

If the hardware does not support stretching, it is recommended to create a swap chain as large as the display mode, so that the window can be resized to any dimensions. Recreating the swap chain is not an optimal way to handle resizing the window, because it can cause severe rendering artifacts. Also, because of the way the GPU manages the overlay memory, recreating the swap chain can potentially cause an application to run out of video memory.

### New D3DPRESENT\_PARAMETERS Flags

The following **D3DPRESENT\_PARAMETERS** flags are defined for creating overlays.



| Flag                                      | Description                                                                                                                                                                        |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **D3DPRESENTFLAG\_OVERLAY\_LIMITEDRGB**   | The RGB range is 16–235. The default is 0–255. <br/> Requires the **D3DOVERLAYCAPS\_LIMITEDRANGERGB** capability.<br/>                                                 |
| **D3DPRESENTFLAG\_OVERLAY\_YCbCr\_BT709** | YUV colors use the BT.709 definition. The default is BT.601. <br/> Requires the **D3DOVERLAYCAPS\_YCbCr\_BT709** capability.<br/>                                      |
| **D3DPRESENTFLAG\_OVERLAY\_YCbCr\_xvYCC** | Output the data by using extended YCbCr (xvYCC).<br/> Requires the **D3DOVERLAYCAPS\_YCbCr\_BT601\_xvYCC** or **D3DOVERLAYCAPS\_YCbCr\_BT709\_xvYCC** capability.<br/> |



 

### Using Hardware Overlays

To display the overlay surface, the application calls **IDirect3DDevice9Ex::PresentEx**. The Direct3D runtime automatically draws the destination color key.

The following **PresentEx** flags are defined for overlays.



| Flag                              | Description                                                                                                                                                                                                                                                                           |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **D3DPRESENT\_UPDATECOLORKEY**    | Set this flag if Desktop Window Manager (DWM) composition is disabled. This flag causes Direct3D to redraw the color key.<br/> If DWM is enabled, this flag is not required, because Direct3D draws the color key once on the surface that DWM uses for redirection.<br/> |
| **D3DPRESENT\_HIDEOVERLAY**       | Hides the overlay.                                                                                                                                                                                                                                                                    |
| **D3DPRESENT\_UPDATEOVERLAYONLY** | Updates the overlay without changing the contents.<br/> This flag is useful if the window moves while the video is paused.<br/>                                                                                                                                           |



 

An application should be prepared to handle the following cases:

-   If another application is using the overlay, **PresentEx** returns **D3DERR\_NOTAVAILABLE**.
-   If the window is moved to another monitor, the application must recreate the swap chain. Otherwise, if the application calls **PresentEx** to display the overlay on a different monitor, **PresentEx** returns **D3DERR\_INVALIDDEVICE**.
-   If the display mode changes, Direct3D attempts to restore the overlay. If the new mode does not support the overlay, **PresentEx** returns **D3DERR\_UNSUPPORTEDOVERLAY**.

### Example Code

The following example shows how to create an overlay surface.


```C++
const UINT VIDEO_WIDTH = 256;
const UINT VIDEO_HEIGHT = 256;

HRESULT CreateHWOverlay(
    HWND hwnd, 
    IDirect3D9Ex *pD3D, 
    IDirect3DDevice9Ex **ppDevice
    )
{
    *ppDevice = NULL;

    D3DCAPS9                caps;
    ZeroMemory(&caps, sizeof(caps));

    HRESULT hr = pD3D->GetDeviceCaps(
        D3DADAPTER_DEFAULT,
        D3DDEVTYPE_HAL,
        &caps
        );

    if (FAILED(hr))
    {
        return hr;
    }

    // Check if overlay is supported.
    if (!(caps.Caps & D3DCAPS_OVERLAY))
    {
        return D3DERR_UNSUPPORTEDOVERLAY;
    }

    D3DOVERLAYCAPS          overlayCaps = { 0 };

    IDirect3DDevice9Ex           *pDevice = NULL;
    IDirect3D9ExOverlayExtension *pOverlay = NULL;

    // Check specific overlay capabilities.
    hr = pD3D->QueryInterface(IID_PPV_ARGS(&pOverlay));

    if (SUCCEEDED(hr))
    {
        hr = pOverlay->CheckDeviceOverlayType(
            D3DADAPTER_DEFAULT,
            D3DDEVTYPE_HAL,
            VIDEO_WIDTH,
            VIDEO_HEIGHT,
            D3DFMT_X8R8G8B8,
            NULL,
            D3DDISPLAYROTATION_IDENTITY,
            &overlayCaps
            );
    }

    // Create the overlay.
    if (SUCCEEDED(hr))
    {

        DWORD flags =   D3DCREATE_FPU_PRESERVE | 
                        D3DCREATE_MULTITHREADED | 
                        D3DCREATE_SOFTWARE_VERTEXPROCESSING;

        
        D3DPRESENT_PARAMETERS   pp = { 0 };

        pp.BackBufferWidth = overlayCaps.MaxOverlayDisplayWidth;
        pp.BackBufferHeight = overlayCaps.MaxOverlayDisplayHeight;
        pp.BackBufferFormat = D3DFMT_X8R8G8B8;
        pp.SwapEffect = D3DSWAPEFFECT_OVERLAY;
        pp.hDeviceWindow = hwnd;
        pp.Windowed = TRUE;
        pp.Flags = D3DPRESENTFLAG_VIDEO;
        pp.FullScreen_RefreshRateInHz = D3DPRESENT_RATE_DEFAULT;
        pp.PresentationInterval       = D3DPRESENT_INTERVAL_ONE;

        hr = pD3D->CreateDeviceEx(D3DADAPTER_DEFAULT, D3DDEVTYPE_HAL,
            NULL, flags, &pp, NULL, &pDevice);
    }

    if (SUCCEEDED(hr))
    {
        (*ppDevice) = pDevice;
        (*ppDevice)->AddRef();
    }

    SafeRelease(&pD3D);
    SafeRelease(&pDevice);
    SafeRelease(&pOverlay);
    return hr;
}
```



## Related topics

<dl> <dt>

[Direct3D Video APIs](direct3d-video-apis.md)
</dt> </dl>

 

 




