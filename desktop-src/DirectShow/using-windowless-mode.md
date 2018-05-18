---
Description: Using Windowless Mode
ms.assetid: 'f53cecaa-dee7-4b02-a4ac-ffbd917f73aa'
title: Using Windowless Mode
---

# Using Windowless Mode

Both the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7) and the [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9) support *windowless mode*, which represents a major improvement over the [**IVideoWindow**](ivideowindow.md) interface. This topic describes the differences between windowless mode and windowed mode, and how to use windowless mode.

To remain backward-compatible with existing applications, the VMR defaults to windowed mode. In windowed mode, the renderer creates its own window to display the video. Typically the application sets the video window to be a child of the application window. The existence of a separate video window causes some problems, however:

-   Most importantly, there is a potential for deadlocks if window messages are sent between threads.
-   The Filter Graph Manager must forward certain window messages, such as WM\_PAINT, to the Video Renderer. The application must use the Filter Graph Manager's implementation of [**IVideoWindow**](ivideowindow.md) (and not the Video Renderer's), so that the Filter Graph Manager maintains the correct internal state.
-   To receive mouse or keyboard events from the video window, the application must set a *message drain*, causing the video window to forward these messages to the application.
-   To prevent clipping problems, the video window must have the right window styles.

Windowless mode avoids these problems by having the VMR draw directly on the application window's client area, using DirectDraw to clip the video rectangle. Windowless mode significantly reduces the chance of deadlocks. Also, the application does not have to set the owner window or the window styles. In fact, when the VMR is in windowless mode, it does not even expose the [**IVideoWindow**](ivideowindow.md) interface, which is no longer needed.

To use windowless mode, you must explicitly configure the VMR. However, you will find that is more flexible and easier to use than windowed mode.

The VMR-7 filter and the VMR-9 filter expose different interfaces, but the steps are equivalent for each.

## Configure the VMR for Windowless Mode

To override the VMR's default behavior, configure the VMR before building the filter graph:

**VMR-7**

1.  Create the Filter Graph Manager.
2.  Create the VMR-7 and add it to the filter graph.
3.  Call [**IVMRFilterConfig::SetRenderingMode**](ivmrfilterconfig-setrenderingmode.md) on the VMR-7 with the **VMRMode\_Windowless** flag.
4.  Query the VMR-7 for the [**IVMRWindowlessControl**](ivmrwindowlesscontrol.md) interface.
5.  Call [**IVMRWindowlessControl::SetVideoClippingWindow**](ivmrwindowlesscontrol-setvideoclippingwindow.md) on the VMR-7. Specify a handle to the window where the video should appear.

**VMR-9**

1.  Create the Filter Graph Manager.
2.  Create the VMR-9 and add it to the filter graph.
3.  Call [**IVMRFilterConfig9::SetRenderingMode**](ivmrfilterconfig9-setrenderingmode.md) on the VMR-9 with the **VMR9Mode\_Windowless** flag.
4.  Query the VMR-9 for the [**IVMRWindowlessControl9**](ivmrwindowlesscontrol9.md) interface.
5.  Call [**IVMRWindowlessControl9::SetVideoClippingWindow**](ivmrwindowlesscontrol9-setvideoclippingwindow.md) on the VMR-9. Specify a handle to the window where the video should appear.

Now build the rest of the filter graph by calling [**IGraphBuilder::RenderFile**](igraphbuilder-renderfile.md) or other graph-building methods. The Filter Graph Manager automatically uses the instance of the VMR that you added to the graph. (For details on why this happens, see [Intelligent Connect](intelligent-connect.md).)

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
        CLSCTX_INPROC, IID_IBaseFilter, (void**)&amp;pVmr); 
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
    hr = pVmr->QueryInterface(IID_IVMRFilterConfig, (void**)&amp;pConfig); 
    if (SUCCEEDED(hr)) 
    { 
        hr = pConfig->SetRenderingMode(VMRMode_Windowless); 
        pConfig->Release(); 
    }
    if (SUCCEEDED(hr))
    {
        // Set the window. 
        hr = pVmr->QueryInterface(IID_IVMRWindowlessControl, (void**)&amp;pWc);
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
hr = InitWindowlessVMR(hwnd, pGraph, &amp;g_pWc);
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

1.  Call the [**IVMRWindowlessControl::SetVideoPosition**](ivmrwindowlesscontrol-setvideoposition.md) method to specify both rectangles.
2.  The source rectangle must be equal to or smaller than the native video size; you can use the [**IVMRWindowlessControl::GetNativeVideoSize**](ivmrwindowlesscontrol-getnativevideosize.md) method to get the native video size.

**VMR-9**

1.  Call the [**IVMRWindowlessControl9::SetVideoPosition**](ivmrwindowlesscontrol9-setvideoposition.md) method to specify both rectangles.
2.  The source rectangle must be equal to or smaller than the native video size; you can use the [**IVMRWindowlessControl9::GetNativeVideoSize**](ivmrwindowlesscontrol9-getnativevideosize.md) method to get the native video size.

For example, the following code sets the source and destination rectangles for the VMR-7. It sets the source rectangle equal to the entire video image, and the destination rectangle equal to the entire window client area:


```C++
// Find the native video size.
long lWidth, lHeight; 
HRESULT hr = g_pWc->GetNativeVideoSize(&amp;lWidth, &amp;lHeight, NULL, NULL); 
if (SUCCEEDED(hr))
{
    RECT rcSrc, rcDest; 
    // Set the source rectangle.
    SetRect(&amp;rcSrc, 0, 0, lWidth, lHeight); 
    
    // Get the window client area.
    GetClientRect(hwnd, &amp;rcDest); 
    // Set the destination rectangle.
    SetRect(&amp;rcDest, 0, 0, rcDest.right, rcDest.bottom); 
    
    // Set the video position.
    hr = g_pWc->SetVideoPosition(&amp;rcSrc, &amp;rcDest); 
}
```



If you want to video to occupy a smaller portion of the client area, modify the *rcDest* parameter. If you want to crop the video image, modify the *rcSrc* parameter.

## Handle Window Messages

Because the VMR does not have its own window, it must be notified if it need to repaint or resize the video. Respond to the following window messages by calling the VMR methods listed.

**VMR-7**

1.  [**WM\_PAINT**](gdi.wm_paint). Call [**IVMRWindowlessControl::RepaintVideo**](ivmrwindowlesscontrol-repaintvideo.md). This method causes the VMR-7 to repaint the most recent video frame.
2.  [**WM\_DISPLAYCHANGE**](gdi.wm_displaychange): Call [**IVMRWindowlessControl::DisplayModeChanged**](ivmrwindowlesscontrol-displaymodechanged.md). This method notifies the VMR-7 that the video must be shown at a new resolution or color depth.
3.  [**WM\_SIZE**](winui._win32_WM_SIZE) or [**WM\_WINDOWPOSCHANGED**](winui._win32_WM_WINDOWPOSCHANGED): Recalculate the position of the video and call [**IVMRWindowlessControl::SetVideoPosition**](ivmrwindowlesscontrol-setvideoposition.md) to update the position, if needed.

**VMR-9**

1.  [**WM\_PAINT**](gdi.wm_paint). Call [**IVMRWindowlessControl9::RepaintVideo**](ivmrwindowlesscontrol9-repaintvideo.md). This method causes the VMR-9 to repaint the most recent video frame.
2.  [**WM\_DISPLAYCHANGE**](gdi.wm_displaychange): Call [**IVMRWindowlessControl9::DisplayModeChanged**](ivmrwindowlesscontrol9-displaymodechanged.md). This method notifies the VMR-9 that the video must be shown at a new resolution or color depth.
3.  [**WM\_SIZE**](winui._win32_WM_SIZE) or [**WM\_WINDOWPOSCHANGED**](winui._win32_WM_WINDOWPOSCHANGED): Recalculate the position of the video and call [**IVMRWindowlessControl9::SetVideoPosition**](ivmrwindowlesscontrol9-setvideoposition.md) to update the position, if needed.

> [!Note]  
> The default handler for the [**WM\_WINDOWPOSCHANGED**](winui._win32_WM_WINDOWPOSCHANGED) message sends a [**WM\_SIZE**](winui._win32_WM_SIZE) message. But if your application intercepts **WM\_WINDOWPOSCHANGED** and does not pass it to [**DefWindowProc**](winui._win32_DefWindowProc), you should call **SetVideoPosition** in your **WM\_WINDOWPOSCHANGED** handler, in addition to your **WM\_SIZE** handler.

 

The following example shows a [**WM\_PAINT**](gdi.wm_paint) message handler. It paints a region defined by the client rectangle minus the video rectangle. Do not draw onto the video rectangle, because the VMR will paint over it, causing flickering. For the same reason, do not set a background brush in your window class.


```C++
void OnPaint(HWND hwnd) 
{ 
    PAINTSTRUCT ps; 
    HDC         hdc; 
    RECT        rcClient; 
    GetClientRect(hwnd, &amp;rcClient); 
    hdc = BeginPaint(hwnd, &amp;ps); 
    if (g_pWc != NULL) 
    { 
        // Find the region where the application can paint by subtracting 
        // the video destination rectangle from the client area.
        // (Assume that g_rcDest was calculated previously.)
        HRGN rgnClient = CreateRectRgnIndirect(&amp;rcClient); 
        HRGN rgnVideo  = CreateRectRgnIndirect(&amp;g_rcDest);  
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
        FillRect(hdc, &amp;rc2, (HBRUSH)(COLOR_BTNFACE + 1)); 
    } 
    EndPaint(hwnd, &amp;ps); 
} 
```



Although you must respond to [**WM\_PAINT**](gdi.wm_paint) messages, there is nothing you need to do between **WM\_PAINT** messages to update the video. As this example shows, windowless mode lets you treat the video image simply as a self-drawing region on the window.

## Related topics

<dl> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 



