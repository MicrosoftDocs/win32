---
description: Using Windowless Mode
ms.assetid: f53cecaa-dee7-4b02-a4ac-ffbd917f73aa
title: Using Windowless Mode
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Windowless Mode

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Both the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7) and the [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9) support *windowless mode*, which represents a major improvement over the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface. This topic describes the differences between windowless mode and windowed mode, and how to use windowless mode.

To remain backward-compatible with existing applications, the VMR defaults to windowed mode. In windowed mode, the renderer creates its own window to display the video. Typically the application sets the video window to be a child of the application window. The existence of a separate video window causes some problems, however:

-   Most importantly, there is a potential for deadlocks if window messages are sent between threads.
-   The Filter Graph Manager must forward certain window messages, such as WM\_PAINT, to the Video Renderer. The application must use the Filter Graph Manager's implementation of [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) (and not the Video Renderer's), so that the Filter Graph Manager maintains the correct internal state.
-   To receive mouse or keyboard events from the video window, the application must set a *message drain*, causing the video window to forward these messages to the application.
-   To prevent clipping problems, the video window must have the right window styles.

Windowless mode avoids these problems by having the VMR draw directly on the application window's client area, using DirectDraw to clip the video rectangle. Windowless mode significantly reduces the chance of deadlocks. Also, the application does not have to set the owner window or the window styles. In fact, when the VMR is in windowless mode, it does not even expose the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface, which is no longer needed.

To use windowless mode, you must explicitly configure the VMR. However, you will find that is more flexible and easier to use than windowed mode.

The VMR-7 filter and the VMR-9 filter expose different interfaces, but the steps are equivalent for each.

## Configure the VMR for Windowless Mode

To override the VMR's default behavior, configure the VMR before building the filter graph:

**VMR-7**

1.  Create the Filter Graph Manager.
2.  Create the VMR-7 and add it to the filter graph.
3.  Call [**IVMRFilterConfig::SetRenderingMode**](/windows/desktop/api/Strmif/nf-strmif-ivmrfilterconfig-setrenderingmode) on the VMR-7 with the **VMRMode\_Windowless** flag.
4.  Query the VMR-7 for the [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol) interface.
5.  Call [**IVMRWindowlessControl::SetVideoClippingWindow**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-setvideoclippingwindow) on the VMR-7. Specify a handle to the window where the video should appear.

**VMR-9**

1.  Create the Filter Graph Manager.
2.  Create the VMR-9 and add it to the filter graph.
3.  Call [**IVMRFilterConfig9::SetRenderingMode**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrfilterconfig9-setrenderingmode) on the VMR-9 with the **VMR9Mode\_Windowless** flag.
4.  Query the VMR-9 for the [**IVMRWindowlessControl9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9) interface.
5.  Call [**IVMRWindowlessControl9::SetVideoClippingWindow**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-setvideoclippingwindow) on the VMR-9. Specify a handle to the window where the video should appear.

Now build the rest of the filter graph by calling [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) or other graph-building methods. The Filter Graph Manager automatically uses the instance of the VMR that you added to the graph. (For details on why this happens, see [Intelligent Connect](intelligent-connect.md).)

The following code shows a helper function that creates the VMR-7, adds it to the graph, and sets up windowless mode.


```C++
HRESULT InitWindowlessVMR( 
    HWND hwndApp,                  // Window to hold the video. 
    IGraphBuilder* pGraph,         // Pointer to the Filter Graph Manager. 
    IVMRWindowlessControl** ppWc   // Receives a pointer to the VMR.
    ) 
{ 
    if (!pGraph || !ppWc) 
    {
        return E_POINTER;
    }
    IBaseFilter* pVmr = NULL; 
    IVMRWindowlessControl* pWc = NULL; 
    // Create the VMR. 
    HRESULT hr = CoCreateInstance(CLSID_VideoMixingRenderer, NULL, 
        CLSCTX_INPROC, IID_IBaseFilter, (void**)&pVmr); 
    if (FAILED(hr))
    {
        return hr;
    }
    
    // Add the VMR to the filter graph.
    hr = pGraph->AddFilter(pVmr, L"Video Mixing Renderer"); 
    if (FAILED(hr)) 
    {
        pVmr->Release();
        return hr;
    }
    // Set the rendering mode.  
    IVMRFilterConfig* pConfig; 
    hr = pVmr->QueryInterface(IID_IVMRFilterConfig, (void**)&pConfig); 
    if (SUCCEEDED(hr)) 
    { 
        hr = pConfig->SetRenderingMode(VMRMode_Windowless); 
        pConfig->Release(); 
    }
    if (SUCCEEDED(hr))
    {
        // Set the window. 
        hr = pVmr->QueryInterface(IID_IVMRWindowlessControl, (void**)&pWc);
        if( SUCCEEDED(hr)) 
        { 
            hr = pWc->SetVideoClippingWindow(hwndApp); 
            if (SUCCEEDED(hr))
            {
                *ppWc = pWc; // Return this as an AddRef'd pointer. 
            }
            else
            {
                // An error occurred, so release the interface.
                pWc->Release();
            }
        } 
    } 
    pVmr->Release(); 
    return hr; 
} 
```



This function assumes that are displaying only one video stream and are not mixing a static bitmap over the video. For details, see [VMR Windowless Mode](vmr-windowless-mode.md). You would call this function as follows:


```C++
IVMRWindowlessControl *pWc = NULL;
hr = InitWindowlessVMR(hwnd, pGraph, &g_pWc);
if (SUCCEEDED(hr))
{
    // Build the graph. For example:
    pGraph->RenderFile(wszMyFileName, 0);
    // Release the VMR interface when you are done.
    pWc->Release();
}
```



## Position the Video

After configuring the VMR, the next step is to set the position of the video. There are two rectangles to consider, the *source* rectangle and the *destination* rectangle. The source rectangle defines which portion of the video to display. The destination rectangle specifies the region in the window's client area that will contain the video. The VMR crops the video image to the source rectangle and stretches the cropped image to fit the destination rectangle.

**VMR-7**

1.  Call the [**IVMRWindowlessControl::SetVideoPosition**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-setvideoposition) method to specify both rectangles.
2.  The source rectangle must be equal to or smaller than the native video size; you can use the [**IVMRWindowlessControl::GetNativeVideoSize**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-getnativevideosize) method to get the native video size.

**VMR-9**

1.  Call the [**IVMRWindowlessControl9::SetVideoPosition**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-setvideoposition) method to specify both rectangles.
2.  The source rectangle must be equal to or smaller than the native video size; you can use the [**IVMRWindowlessControl9::GetNativeVideoSize**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-getnativevideosize) method to get the native video size.

For example, the following code sets the source and destination rectangles for the VMR-7. It sets the source rectangle equal to the entire video image, and the destination rectangle equal to the entire window client area:


```C++
// Find the native video size.
long lWidth, lHeight; 
HRESULT hr = g_pWc->GetNativeVideoSize(&lWidth, &lHeight, NULL, NULL); 
if (SUCCEEDED(hr))
{
    RECT rcSrc, rcDest; 
    // Set the source rectangle.
    SetRect(&rcSrc, 0, 0, lWidth, lHeight); 
    
    // Get the window client area.
    GetClientRect(hwnd, &rcDest); 
    // Set the destination rectangle.
    SetRect(&rcDest, 0, 0, rcDest.right, rcDest.bottom); 
    
    // Set the video position.
    hr = g_pWc->SetVideoPosition(&rcSrc, &rcDest); 
}
```



If you want to video to occupy a smaller portion of the client area, modify the *rcDest* parameter. If you want to crop the video image, modify the *rcSrc* parameter.

## Handle Window Messages

Because the VMR does not have its own window, it must be notified if it need to repaint or resize the video. Respond to the following window messages by calling the VMR methods listed.

**VMR-7**

1.  [**WM\_PAINT**](../gdi/wm-paint.md). Call [**IVMRWindowlessControl::RepaintVideo**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-repaintvideo). This method causes the VMR-7 to repaint the most recent video frame.
2.  [**WM\_DISPLAYCHANGE**](../gdi/wm-displaychange.md): Call [**IVMRWindowlessControl::DisplayModeChanged**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-displaymodechanged). This method notifies the VMR-7 that the video must be shown at a new resolution or color depth.
3.  [**WM\_SIZE**](../winmsg/wm-size.md) or [**WM\_WINDOWPOSCHANGED**](../winmsg/wm-windowposchanged.md): Recalculate the position of the video and call [**IVMRWindowlessControl::SetVideoPosition**](/windows/desktop/api/Strmif/nf-strmif-ivmrwindowlesscontrol-setvideoposition) to update the position, if needed.

**VMR-9**

1.  [**WM\_PAINT**](../gdi/wm-paint.md). Call [**IVMRWindowlessControl9::RepaintVideo**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-repaintvideo). This method causes the VMR-9 to repaint the most recent video frame.
2.  [**WM\_DISPLAYCHANGE**](../gdi/wm-displaychange.md): Call [**IVMRWindowlessControl9::DisplayModeChanged**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-displaymodechanged). This method notifies the VMR-9 that the video must be shown at a new resolution or color depth.
3.  [**WM\_SIZE**](../winmsg/wm-size.md) or [**WM\_WINDOWPOSCHANGED**](../winmsg/wm-windowposchanged.md): Recalculate the position of the video and call [**IVMRWindowlessControl9::SetVideoPosition**](/previous-versions/windows/desktop/api/Vmr9/nf-vmr9-ivmrwindowlesscontrol9-setvideoposition) to update the position, if needed.

> [!Note]  
> The default handler for the [**WM\_WINDOWPOSCHANGED**](../winmsg/wm-windowposchanged.md) message sends a [**WM\_SIZE**](../winmsg/wm-size.md) message. But if your application intercepts **WM\_WINDOWPOSCHANGED** and does not pass it to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), you should call **SetVideoPosition** in your **WM\_WINDOWPOSCHANGED** handler, in addition to your **WM\_SIZE** handler.

 

The following example shows a [**WM\_PAINT**](../gdi/wm-paint.md) message handler. It paints a region defined by the client rectangle minus the video rectangle. Do not draw onto the video rectangle, because the VMR will paint over it, causing flickering. For the same reason, do not set a background brush in your window class.


```C++
void OnPaint(HWND hwnd) 
{ 
    PAINTSTRUCT ps; 
    HDC         hdc; 
    RECT        rcClient; 
    GetClientRect(hwnd, &rcClient); 
    hdc = BeginPaint(hwnd, &ps); 
    if (g_pWc != NULL) 
    { 
        // Find the region where the application can paint by subtracting 
        // the video destination rectangle from the client area.
        // (Assume that g_rcDest was calculated previously.)
        HRGN rgnClient = CreateRectRgnIndirect(&rcClient); 
        HRGN rgnVideo  = CreateRectRgnIndirect(&g_rcDest);  
        CombineRgn(rgnClient, rgnClient, rgnVideo, RGN_DIFF);  
        
        // Paint on window.
        HBRUSH hbr = GetSysColorBrush(COLOR_BTNFACE); 
        FillRgn(hdc, rgnClient, hbr); 

        // Clean up.
        DeleteObject(hbr); 
        DeleteObject(rgnClient); 
        DeleteObject(rgnVideo); 

        // Request the VMR to paint the video.
        HRESULT hr = g_pWc->RepaintVideo(hwnd, hdc);  
    } 
    else  // There is no video, so paint the whole client area. 
    { 
        FillRect(hdc, &rc2, (HBRUSH)(COLOR_BTNFACE + 1)); 
    } 
    EndPaint(hwnd, &ps); 
} 
```



Although you must respond to [**WM\_PAINT**](../gdi/wm-paint.md) messages, there is nothing you need to do between **WM\_PAINT** messages to update the video. As this example shows, windowless mode lets you treat the video image simply as a self-drawing region on the window.

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 
