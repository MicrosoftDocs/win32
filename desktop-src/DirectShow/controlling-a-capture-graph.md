---
description: Controlling a Capture Graph
ms.assetid: e7afafca-e993-4096-bad4-399ee6c67fe9
title: Controlling a Capture Graph
ms.topic: article
ms.date: 05/31/2018
---

# Controlling a Capture Graph

The Filter Graph Manager's [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) interface has methods for running, stopping, and pausing the entire graph. If the filter graph has capture and preview streams, however, you probably want to control the two streams independently. For example, you might want to preview the video without capturing it. You can do this through the [**ICaptureGraphBuilder2::ControlStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-controlstream) method.

> [!Note]  
> This method does not work when capturing to an Advanced Systems Format (ASF) file.

 

Controlling the Capture Stream

The following code sets the video capture stream to run for four seconds, starting one second after the graph runs:


```C++
// Control the video capture stream. 
REFERENCE_TIME rtStart = 10000000, rtStop = 50000000;
const WORD wStartCookie = 1, wStopCookie = 2;  // Arbitrary values.
hr = pBuild->ControlStream(
    &PIN_CATEGORY_CAPTURE, // Pin category.
    &MEDIATYPE_Video,      // Media type.
    pCap,                 // Capture filter.
    &rtStart, &rtStop,     // Start and stop times.
    wStartCookie, wStopCookie  // Values for the start and stop events.
);
pControl->Run();
```



The first parameter specifies which stream to control, as a pin category GUID. The second parameter gives the media type. The third parameter is a pointer to the capture filter. To control all the capture streams in the graph, set the second and third parameters to **NULL**.

The next two parameters define the times when the stream will start and stop, relative to the time when the graph starts running. Call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) to run the graph. Until you run the graph, the **ControlStream** method has no effect. If the graph is already running, the settings take effect immediately.

The last two parameters are used for getting event notifications when the stream starts and stops. For each stream that you control using this method, the filter graph sends a pair of events: [**EC\_STREAM\_CONTROL\_STARTED**](ec-stream-control-started.md) when the stream starts, and [**EC\_STREAM\_CONTROL\_STOPPED**](ec-stream-control-stopped.md) when the stream stops. The values of **wStartCookie** and **wStopCookie** are used as the second event parameter. Thus, *lParam2* in the start event equals **wStartCookie**, and *lParam2* in the stop event equals **wStopCookie**. The following code shows how to get these events:


```C++
while (hr = pEvent->GetEvent(&evCode, &param1, &param2, 0), SUCCEEDED(hr))
{
    switch (evCode)
    {
    case EC_STREAM_CONTROL_STARTED: 
    // param2 == wStartCookie
    break;

    case EC_STREAM_CONTROL_STOPPED: 
    // param2 == wStopCookie
    break;
    
    } 
    pEvent->FreeEventParams(evCode, param1, param2);
}
```



The **ControlStream** method defines some special values for the start and stop times.



| Label | Value |
|-------------|----------------------------------------|------------------------------------|
|             | Start                                  | Stop                               |
| MAXLONGLONG | Never start this stream.               | Do not stop until the graph stops. |
| **NULL**    | Start immediately when the graph runs. | Stop immediately.                  |



 

For example, the following code stops the capture stream immediately:


```C++
pBuild->ControlStream(&PIN_CATEGORY_CAPTURE, &MEDIATYPE_Video, pCap,
    0, 0,     // Start and stop times.
    wStartCookie, wStopCookie); 
```



Although you can stop the capture stream and restart it later, this will create a gap in the time stamps. On playback, the video will appear to stall during the gap (depending on the file format).

Controlling the Preview Stream

To control the preview pin, call **ControlStream** but set the first parameter to PIN\_CATEGORY\_PREVIEW. This works just like it does for PIN\_CATEGORY\_CAPTURE, except that you cannot use reference times to specify the start and stop, because the preview frames do not have time stamps. Therefore, you must use **NULL** or MAXLONGLONG. Use **NULL** to start the preview stream:


```C++
pBuild->ControlStream(&PIN_CATEGORY_PREVIEW, &MEDIATYPE_Video, pCap,
    NULL,    // Start now.
    0,       // (Don't care.)
    wStartCookie, wStopCookie); 
```



Use MAXLONGLONG to stop the preview stream:


```C++
pBuild->ControlStream(&PIN_CATEGORY_PREVIEW, &MEDIATYPE_Video, pCap,
    0,               // (Don't care.)
    MAXLONGLONG,     // Stop now.
    wStartCookie, wStopCookie); 
```



It does not matter whether the preview stream comes from a preview pin on the capture filter, or from the Smart Tee filter. The **ControlStream** method works either way.

For video port pins, however, the method will fail. In that case, another approach is to hide the video window. Query the graph for **IVideoWindow**, and use the [**IVideoWindow::put\_Visible**](/windows/desktop/api/Control/nf-control-ivideowindow-put_visible) method to show or hide the window.


```C++
// Hide the video window.
IVideoWindow *pVidWin = 0;
hr = pGraph->QueryInterface(IID_IVideoWindow, (void**)&pVidWin);
if (SUCCEEDED(hr))
{
    pVidWin->put_Visible(OAFALSE);
    pVidWin->Release();
}
```



Also, if you call [**IVideoWindow::put\_AutoShow**](/windows/desktop/api/Control/nf-control-ivideowindow-put_autoshow) with the value OAFALSE before you run the graph, the Video Renderer filter hides the window until you specify otherwise. By default, the Video Renderer shows the window when you run the graph.

Remarks about Stream Control

The default behavior for a pin is to deliver samples when the graph runs. For example, suppose that you call **ControlStream** with PIN\_CATEGORY\_CAPTURE but not with PIN\_CATEGORY\_PREVIEW. When you run the graph, the preview stream will run immediately, while the capture stream will run at whatever time you specified in **ControlStream**.

If you are capturing more than one stream and sending them to a mux filter — for example, if you are capturing audio and video to an AVI file — you should control both streams in tandem. Otherwise, the mux filter might block waiting for one stream, as it tries to interleave the two streams. Set the same start and stop times on all capture streams before running the graph:


```C++
pBuild->ControlStream(&PIN_CATEGORY_CAPTURE, 
    
NULL, NULL,       // All capture streams.
    &rtStart, rtStop, 
    wStartCookie, wStopCookie); 
```



Internally, the **ControlStream** method uses the [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol) interface, which is exposed on the pins of the capture filter, the Smart Tee filter (if present), and possibly the mux filter. You can use this interface directly, instead of calling **ControlStream**, although there is no particular advantage to doing so.

## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



