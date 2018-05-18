---
Description: 'This topic is step 5 of the tutorial Audio/Video Playback in DirectShow.'
ms.assetid: '9d7a40e0-4327-4ca3-b430-2be02f80c16f'
title: 'Step 5: Add Video Functionality'
---

# Step 5: Add Video Functionality

This topic is step 5 of the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md). The complete code is shown in the topic [DirectShow Playback Example](directshow-playback-example.md).

To ensure that video displays correctly, the application must respond to [**WM\_PAINT**](gdi.wm_paint), [**WM\_SIZE**](winui._win32_WM_SIZE), and [**WM\_DISPLAYCHANGE**](gdi.wm_displaychange) messages as follows.

### Handle WM\_PAINT Messages

When the application receives a [**WM\_PAINT**](gdi.wm_paint) message, the video renderer might need to redraw the last video frame. For the [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR) filter, call [**IMFVideoDisplayControl::RepaintVideo**](mf.imfvideodisplaycontrol_repaintvideo).


```C++
HRESULT CEVR::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pVideoDisplay)
    {
        return m_pVideoDisplay->RepaintVideo();
    }
    else
    {
        return S_OK;
    }
}
```



For the [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9), call [**IVMRWindowlessControl9::RepaintVideo**](ivmrwindowlesscontrol9-repaintvideo.md).


```C++
HRESULT CVMR9::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pWindowless)
    {
        return m_pWindowless->RepaintVideo(hwnd, hdc);
    }
    else
    {
        return S_OK;
    }
}
```



For the [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7), call [**IVMRWindowlessControl::RepaintVideo**](ivmrwindowlesscontrol-repaintvideo.md).


```C++
HRESULT CVMR7::Repaint(HWND hwnd, HDC hdc)
{
    if (m_pWindowless)
    {
        return m_pWindowless->RepaintVideo(hwnd, hdc);
    }
    else
    {
        return S_OK;
    }
}
```



### Handle WM\_SIZE Messages

If the size of the video window changes, notify the video renderer to resize the video. For the EVR, call [**IMFVideoDisplayControl::SetVideoPosition**](mf.imfvideodisplaycontrol_setvideoposition).


```C++
HRESULT CEVR::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pVideoDisplay == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pVideoDisplay->SetVideoPosition(NULL, prc);
    }
    else
    {

        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pVideoDisplay->SetVideoPosition(NULL, &amp;rc);
    }
}
```



For the VMR-9, call [**IVMRWindowlessControl9::SetVideoPosition**](ivmrwindowlesscontrol9-setvideoposition.md).


```C++
HRESULT CVMR9::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pWindowless == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pWindowless->SetVideoPosition(NULL, prc);
    }
    else
    {

        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pWindowless->SetVideoPosition(NULL, &amp;rc);
    }
}
```



For the VMR-7, call [**IVMRWindowlessControl::SetVideoPosition**](ivmrwindowlesscontrol-setvideoposition.md).


```C++
HRESULT CVMR7::UpdateVideoWindow(HWND hwnd, const LPRECT prc)
{
    if (m_pWindowless == NULL)
    {
        return S_OK; // no-op
    }

    if (prc)
    {
        return m_pWindowless->SetVideoPosition(NULL, prc);
    }
    else
    {
        RECT rc;
        GetClientRect(hwnd, &amp;rc);
        return m_pWindowless->SetVideoPosition(NULL, &amp;rc);
    }
}
```



### Handle WM\_DISPLAYCHANGE Messages

If the display mode changes, you must notify the VMR-9 or VMR-7 filter. For the VMR-9, call [**IVMRWindowlessControl9::DisplayModeChanged**](ivmrwindowlesscontrol9-displaymodechanged.md).


```C++
HRESULT CVMR9::DisplayModeChanged()
{
    if (m_pWindowless)
    {
        return m_pWindowless->DisplayModeChanged();
    }
    else
    {
        return S_OK;
    }
}
```



For the VMR-7, call [**IVMRWindowlessControl::DisplayModeChanged**](ivmrwindowlesscontrol-displaymodechanged.md).


```C++
HRESULT CVMR7::DisplayModeChanged()
{
    if (m_pWindowless)
    {
        return m_pWindowless->DisplayModeChanged();
    }
    else
    {
        return S_OK;
    }
}
```



The EVR does not need to be notified when the display mode changes.

Next: [Step 6: Handle Graph Events](step-6--handle-graph-events.md).

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md)
</dt> <dt>

[DirectShow Playback Example](directshow-playback-example.md)
</dt> <dt>

[Using the DirectShow EVR Filter](mf.using_the_directshow_evr_filter)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> </dl>

 

 



