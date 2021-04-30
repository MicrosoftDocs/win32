---
description: Using the Video Display Controls
ms.assetid: 09501d67-effb-41ce-a7b7-d2415acdf3ac
title: Using the Video Display Controls
ms.topic: article
ms.date: 05/31/2018
---

# Using the Video Display Controls

The [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface controls how the enhanced video renderer (EVR) displays video inside an application window. This interface can be used in either DirectShow or Media Foundation. Internally, the video display controls are provided by the EVR's default presenter. If you write a custom presenter, you can provide the same interface or define a custom interface.

The correct way to get a pointer to the [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface depends on whether you are using the DirectShow version of the EVR or the Media Foundation version. For the Media Foundation EVR, it also depends on whether you are using the EVR directly or using it through the Media Session (which is more typical).

To get a pointer to the [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface, do the following:

1.  Get a pointer to the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface.

    -   If you are using the DirectShow EVR filter, call **QueryInterface** on the filter.

    -   If you are using the EVR media sink directly, call **QueryInterface** on the media sink.

    -   If you are using the Media Session, call **QueryInterface** on the Media Session.

2.  If you are using the Media Session, wait for the Media Session to send the [MESessionTopologyStatus](mesessiontopologystatus.md) event with a status value of MF\_TOPOSTATUS\_READY. (Skip this step otherwise.)

3.  Call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) to get the [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface. The service identifier is MR\_VIDEO\_RENDER\_SERVICE.

You can use the [**IMFVideoDisplayControl**](/windows/desktop/api/evr/nn-evr-imfvideodisplaycontrol) interface to perform the following tasks:

-   Set the clipping window.

-   Set the source and destination rectangles.

-   Update the video window in response to window messages.

-   Enable or disable full-screen mode.

## Clipping Window

The application must provide a window where the EVR draws the video. To set the clipping window, call [**IMFVideoDisplayControl::SetVideoWindow**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setvideowindow) with a handle to the application window.

If you create the EVR media sink through its activation object, this step is not required. The activation object automatically calls [**SetVideoWindow**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setvideowindow), using the window handle that you provided in the [**MFCreateVideoRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatevideorendereractivate) function.

## Source and Destination Rectangles

During playback, the presenter takes a portion of the composited video image and draws it onto an area of the video window. The portion of the composited image is the *source rectangle*, and the area of the video window is the *destination rectangle*.

The source rectangle is defined using normalized coordinates where the point (0.0, 0.0) corresponds to the upper left corner of the video, and (1.0, 1.0) corresponds to the lower right corner of the video. The source rectangle can be any region within this rectangle. The destination rectangle is specified in pixels, relative to the client area of the window. The default source rectangle is the entire image, and the default destination rectangle is an empty rectangle.

To set the source and destination rectangles, call [**IMFVideoDisplayControl::SetVideoPosition**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setvideoposition).

If you create the EVR media sink through its activation object, this step is not required. The activation object automatically sets the destination rectangle equal to the entire client area of the window. However, you should call [**SetVideoPosition**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setvideoposition) if you want to change the source rectangle or set a different destination rectangle.

## Window Messages

During playback, your application should respond to certain window messages, as follows:

-   WM\_PAINT: Call [**IMFVideoDisplayControl::RepaintVideo**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-repaintvideo) to repaint the video. Also, avoid painting over the destination rectangle while video is playing, because this can cause flickering.

-   WM\_SIZE: You might need to call [**SetVideoPosition**](/windows/desktop/api/evr/nf-evr-imfvideodisplaycontrol-setvideoposition) to resize the destination rectangle.

Unlike the Video Mixing Renderer (VMR) filter in DirectShow, you do not have to notify the EVR when you receive a WM\_DISPLAYCHANGE message.

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



