---
description: Video Port Pins in File Capture
ms.assetid: 0fa6d88e-3c64-487f-b007-8c65bf47211d
title: Video Port Pins in File Capture
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Port Pins in File Capture

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If the capture device has a video port, the video port pin must be connected to a video renderer, even if you only want to capture to a file.

If you call [**ICaptureGraphBuilder2::RenderStream**](/windows/desktop/api/Strmif/nf-strmif-icapturegraphbuilder2-renderstream) with the value **PIN\_CATEGORY\_CAPTURE** and the device has a video port pin, the Capture Graph Builder automatically connects the video port pin to the [Overlay Mixer](overlay-mixer-filter.md) filter and connects the Overlay Mixer to the Video Renderer. The Capture Graph Builder hides the video window by calling [**IVideoWindow::put\_AutoShow**](/windows/desktop/api/Control/nf-control-ivideowindow-put_autoshow) with the value **OAFALSE**. If the application later calls **RenderStream** with **PIN\_CATEGORY\_PREVIEW**, the Capture Graph Builder calls **put\_AutoShow** with the value **OATRUE**, in order to show the video window.

After you call **RenderStream** with **PIN\_CATEGORY\_CAPTURE**, you can check whether it has added the Video Renderer by querying the Filter Graph Manager for the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface.

## Related topics

<dl> <dt>

[Capturing Video to a File](capturing-video-to-a-file.md)
</dt> </dl>

 

 



