---
description: Handling Repaint Events in Video Capture
ms.assetid: 80739be7-fa38-409d-a827-d788d3044abe
title: Handling Repaint Events in Video Capture
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handling Repaint Events in Video Capture

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you build a video capture graph without using the [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) interface, and you preview the video using the old Video Renderer filter, then you should override the default handling for [**EC\_REPAINT**](ec-repaint.md) events. Query the Filter Graph Manager for the [**IMediaEvent**](/windows/desktop/api/Control/nn-control-imediaevent) interface and call the [**IMediaEvent::CancelDefaultHandling**](/windows/desktop/api/Control/nf-control-imediaevent-canceldefaulthandling) method with the value EC\_REPAINT:


```C++
IMediaEvent *pEvent = 0;
hr = pGraph->QueryInterface(IID_IMediaEvent, (void**)&pEvent);
if (SUCCEEDED(hr))
{
    pEvent->CancelDefaultHandling (EC_REPAINT);
    pEvent->Release();
}
```



This prevents a possible error that can corrupt your capture file. If the user covers and uncovers the preview window, the Video Renderer filter receives a WM\_PAINT message. By default, the Video Renderer requests a new frame, and the Filter Graph Manager pauses the graph in order to cue another video frame. If that happens while the graph is writing a file, it will corrupt the file. Overriding the default EC\_REPAINT behavior prevents the renderer from requesting a new frame.

You do not have to perform this step if you are using the **ICaptureGraphBuilder2** interface, because the Capture Graph Builder does it for you automatically. Also, it is not required if you are using the Video Mixing Renderer (VMR) for preview. The VMR always has the most recent frame available, so it does not send EC\_REPAINT events.

## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



