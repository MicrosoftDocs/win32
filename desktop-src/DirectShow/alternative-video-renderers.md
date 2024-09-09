---
description: This topic describes how to write a custom video renderer for DirectShow.
ms.assetid: abba5113-125f-4dac-b566-99c0d9b5978c
title: Alternative Video Renderers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Alternative Video Renderers

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to write a custom video renderer for DirectShow.

> [!Note]  
> Instead of writing a custom video renderer, it is recommended that you write a plug-in allocator-presenter for the Video Mixing Renderer (VMR) or [**Enhanced Video Renderer**](enhanced-video-renderer-filter.md) (EVR). This approach will give you all of the benefits of the VMR/EVR, including support for DirectX Video Acceleration (DXVA), hardware deinterlacing, and frame stepping, and is likely to be more robust than a custom video renderer. For more information, see the following topics:
>
> -   [VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
> -   [How to Write an EVR Presenter](/windows/desktop/medfound/how-to-write-an-evr-presenter)

 

## Writing an Alternative Renderer

Microsoft DirectShow provides a window-based video renderer; it also provides a full-screen renderer in the run-time installation. You can use the DirectShow base classes to write alternative video renderers. For alternative renderers to interact correctly with DirectShow-based applications, the renderers must adhere to the guidelines outlined in this article. You can use the [**CBaseRenderer**](cbaserenderer.md) and [**CBaseVideoRenderer**](cbasevideorenderer.md) classes to help follow these guidelines when implementing an alternative video render. Because of the ongoing development of DirectShow, review your implementation periodically to ensure that the renderers are compatible with the most recent version of DirectShow.

This topic discusses many notifications that a renderer is responsible for handling. A brief review of DirectShow notifications might help to set the stage. There are essentially three kinds of notifications that occur in DirectShow:

-   *Stream notifications*, which are events that occur in the media stream and are passed from one filter to the next. These can be begin-flushing, end-flushing or end-of-stream notifications and are sent by calling the appropriate method on the downstream filter's input pin (for example [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush)).
-   *Filter graph notifications*, which are events sent from a filter to the Filter Graph Manager such as [**EC\_COMPLETE**](ec-complete.md). This is accomplished by calling the [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify) method on the Filter Graph Manager.
-   *Application notifications*, which are retrieved from the Filter Graph Manager by the controlling application. An application calls the [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) method on the Filter Graph Manager to retrieve these events. Often, the Filter Graph Manager passes through the events it receives to the application.

This topic discusses the responsibility of the renderer filter in handling stream notifications it receives and in sending appropriate filter graph notifications.

## Handling End-of-stream and Flushing Notifications

An end-of-stream notification begins at an upstream filter (such as the source filter) when that filter detects that it can send no more data. It is passed through every filter in the graph and eventually ends at the renderer, which is responsible for subsequently sending an [**EC\_COMPLETE**](ec-complete.md) notification to the Filter Graph Manager. Renderers have special responsibilities when it comes to handling these notifications.

A renderer receives an end-of-stream notification when its input pin's [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method is called by the upstream filter. A renderer should note this notification and continue to render any data it has already received. Once all remaining data has been received, the renderer should send an [**EC\_COMPLETE**](ec-complete.md) notification to the Filter Graph Manager. The **EC\_COMPLETE** notification should be sent only once by a renderer each time it reaches the end of a stream. Furthermore, **EC\_COMPLETE** notifications must never be sent except when the filter graph is running. Therefore, if the filter graph is paused when a source filter sends an end-of-stream notification, then **EC\_COMPLETE** should not be sent until the filter graph is finally run.

Any calls to the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) or [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple) methods after an end-of-stream notification is signaled should be rejected. **E\_UNEXPECTED** is the most appropriate error message to return in this case.

When a filter graph is stopped, any cached end-of-stream notification should be cleared and not resent when next started. This is because the Filter Graph Manager always pauses all filters just before running them so that proper flushing occurs. So, for example, if the filter graph is paused and an end-of-stream notification is received, and then the filter graph is stopped, the renderer should not send an [**EC\_COMPLETE**](ec-complete.md) notification when it is subsequently run. If no seeks have occurred, the source filter will automatically send another end-of-stream notification during the pause state that precedes a run state. If, on the other hand, a seek has occurred while the filter graph is stopped, then the source filter might have data to send, so it won't send an end-of-stream notification.

Video renderers often depend on end-of-stream notifications for more than the sending of [**EC\_COMPLETE**](ec-complete.md) notifications. For example, if a stream has finished playing (that is, an end-of-stream notification is sent) and another window is dragged over a video renderer window, a number of [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) window messages will be generated. The typical practice for running video renderers is to refrain from repainting the current frame upon receipt of **WM\_PAINT** messages (based on the assumption that another frame to be drawn will be received). However, when the end-of-stream notification has been sent, the renderer is in a waiting state; it is still running but is aware that it will not receive any additional data. Under these circumstances, the renderer customarily draws the playback area black.

Handling flushing is an additional complication for renderers. Flushing is carried out through a pair of [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) methods called [**BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) and [**EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush). Flushing is essentially an additional state that the renderer must handle. It is illegal for a source filter to call **BeginFlush** without calling **EndFlush**, so hopefully the state is short and discrete; however, the renderer must correctly handle data or notifications it receives during the flush transition.

Any data received after calling [**BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) should be rejected immediately by returning **S\_FALSE**. Furthermore, any cached end-of-stream notification should also be cleared when a renderer is flushed. A renderer will typically be flushed in response to a seek. The flush ensures that old data is cleared from the filter graph before fresh samples are sent. (Typically, the playing of two sections of a stream, one after another, is best handled through deferred commands rather than waiting for one section to finish and then issuing a seek command.)

## Handling State Changes and Pause Completion

A renderer filter behaves the same as any other filter in the filter graph when its state is changed, with the following exception. After being paused, the renderer will have some data queued, ready to be rendered when subsequently run. When the video renderer is stopped, it holds on to this queued data. This is an exception to the DirectShow rule that no resources should be held by filters while the filter graph is stopped.

The reason for this exception is that by holding resources, the renderer will always have an image with which to repaint the window if it receives a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message. It also has an image to satisfy methods, such as [**CBaseControlVideo::GetStaticImage**](cbasecontrolvideo-getstaticimage.md), that request a copy of the current image. Another effect of holding resources is that holding on to the image stops the allocator from being decommitted, which in turn makes the next state change occur much faster because the image buffers are already allocated.

A video renderer should render and release samples only while running. While paused, the filter might render them (for example, when drawing a static poster image in a window), but should not release them. Audio renderers will do no rendering while paused (although they can perform other activities, such as preparing the wave device, for example). The time at which the samples should be rendered is obtained by combining the stream time in the sample with the reference time passed as a parameter to the [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) method. Renderers should reject samples with start times less than or equal to end times.

When an application pauses a filter graph, the filter graph does not return from its [**IMediaControl::Pause**](/windows/desktop/api/Control/nf-control-imediacontrol-pause) method until there is data queued at the renderers. In order to ensure this, when a renderer is paused, it should return S\_FALSE if there is no data waiting to be rendered. If it has data queued, then it can return **S\_OK**.

The Filter Graph Manager checks all return values when pausing a filter graph, to ensure that the renderers have data queued. If one or more filters are not ready, then the Filter Graph Manager polls the filters in the graph by calling [**IMediaFilter::GetState**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getstate). The **GetState** method takes a time-out parameter. A filter (typically a renderer) that is still waiting for data to arrive before completing the state change returns **VFW\_S\_STATE\_INTERMEDIATE** if the **GetState** method expires. Once data arrives at the renderer, **GetState** should be returned immediately with **S\_OK**.

In both the intermediate and completed state, the reported filter state will be State\_Paused. Only the return value indicates whether the filter is really ready or not. If, while a renderer is waiting for data to arrive, its source filter sends an end-of-stream notification, then that should also complete the state change.

Once all filters actually have data waiting to be rendered, the filter graph will complete its pause state change.

## Handling Termination

Video renderers must correctly handle termination events from the user. This implies correctly hiding the window and knowing what to do if a window is subsequently forced to be displayed. Also, video renderers must notify the Filter Graph Manager when its window is destroyed (or more accurately, when the renderer is removed from the filter graph) to free resources.

If the user closes the video window (for instance by pressing ALT+F4), the convention is to hide the window immediately and send an [**EC\_USERABORT**](ec-userabort.md) notification to the Filter Graph Manager. This notification is passed through to the application, which will stop the graph playing. After sending **EC\_USERABORT**, a video renderer should reject any additional samples delivered to it.

The graph-stopped flag should be left on by the renderer until it is subsequently stopped, at which point it should be reset so that an application can override the user action and continue playing the graph if it desires. If ALT+F4 is pressed while the video is running, the window will be hidden and all further samples delivered will be rejected. If the window is subsequently shown (perhaps through [**IVideoWindow::put\_Visible**](/windows/desktop/api/Control/nf-control-ivideowindow-put_visible)), then no [**EC\_REPAINT**](ec-repaint.md) notifications should be generated.

The video renderer should also send the [**EC\_WINDOW\_DESTROYED**](ec-window-destroyed.md) notification to the filter graph when the video renderer is terminating. In fact, it is best to handle this when the renderer's [**IBaseFilter::JoinFilterGraph**](/windows/desktop/api/Strmif/nf-strmif-ibasefilter-joinfiltergraph) method is called with a null parameter (indicating that the renderer is about to be removed from the filter graph), rather than waiting until the actual video window is destroyed. Sending this notification enables the plug-in distributor in the Filter Graph Manager to pass on resources that depend on window focus to other filters, such as audio devices.

## Handling Dynamic Format Changes

In some cases, the renderer's upstream filter might try to change the video format while the video is playing. It is most often the video decompressor that initiates a dynamic format change.

An upstream filter attempting to change formats dynamically should always call the [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) method on the renderer input pin. A video renderer has some leeway as to what kinds of dynamic format changes it should support. At a minimum, it should allow the upstream filter to change palettes. When an upstream filter changes media types, it attaches the media type to the first sample delivered in the new format. If the renderer holds samples in a queue for rendering, it should not change the format until it renders the sample with the type change.

A video renderer can also request a format change from the decoder. For example, it might ask the decoder to provide a DirectDraw-compatible format with a negative **biHeight**. When the renderer is paused, it should call [**QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) on the upstream pin to see which formats the decoder can provide. The decoder might not enumerate all of the types that it can accept, however, so the renderer should offer some types even if the decoder does not advertise them.

If the decoder can switch to the requested format, it returns **S\_OK** from [**QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept). The renderer then attaches the new media type to the next media sample on the upstream allocator. For this to work, the renderer must provide a custom allocator that implements a private method for attaching the media type to the next sample. (Within this private method, call [**IMediaSample::SetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setmediatype) to set the type.)

The renderer's input pin should return the renderer's custom allocator in the [**IMemInputPin::GetAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-getallocator) method. Override [**IMemInputPin::NotifyAllocator**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-notifyallocator) so that it fails if the upstream filter does not use the renderer's allocator.

With some decoders, setting **biHeight** to a positive number on YUV types causes the decoder to draw the image upside down. (This is incorrect, and should be considered a bug in the decoder.)

Whenever a format change is detected by the video renderer, it should send an [**EC\_DISPLAY\_CHANGED**](ec-display-changed.md) notification. Most video renderers pick a format during connection so that the format can be drawn efficiently through GDI. If the user changes the current display mode without restarting the computer, a renderer might find itself with a bad image format connection and should send this notification. The first parameter should be the pin that needs reconnecting. The Filter Graph Manager will arrange for the filter graph to be stopped and the pin reconnected. During the subsequent reconnection, the renderer can accept a more appropriate format.

Whenever a video renderer detects a palette change in the stream it should send the [**EC\_PALETTE\_CHANGED**](ec-palette-changed.md) notification to the Filter Graph Manager. The DirectShow video renderers detect whether a palette has really changed in dynamic format or not. The video renderers do this not only to filter out the number of **EC\_PALETTE\_CHANGED** notifications sent but also to reduce the amount of palette creation, installation, and deletion required.

Finally, the video renderer might also detect that the size of the video has changed, in which case, it should send the [**EC\_VIDEO\_SIZE\_CHANGED**](ec-video-size-changed.md) notification. An application might use this notification to negotiate space in a compound document. The actual video dimensions are available through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) control interface. The DirectShow renderers detect whether the video has actually changed size or not prior to sending these events.

## Handling Persistent Properties

All properties set through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) and [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interfaces are meant to be persistent across connections. Therefore, disconnecting and reconnecting a renderer should show no effects on the window size, position, or styles. However, if the video dimensions change between connections, the renderer should reset the source and destination rectangles to their defaults. The source and destination positions are set through the **IBasicVideo** interface.

Both [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) and [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) provide enough access to properties to allow an application to save and restore all the data in the interface in a persistent format. This will be useful to applications that must save the exact configuration and properties of filter graphs during an editing session and restore them later.

## Handling EC\_REPAINT Notifications

The [**EC\_REPAINT**](ec-repaint.md) notification is sent only when the renderer is either paused or stopped. This notification signals to the Filter Graph Manager that the renderer needs data. If the filter graph is stopped when it receives one of these notifications, it will pause the filter graph, wait for all filters to receive data (by calling [**GetState**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-getstate)), and then stop it again. When stopped, a video renderer should hold on to the image so that subsequent [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) messages can be handled.

Therefore, if a video renderer receives a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message when stopped or paused, and it has nothing with which to paint its window, then it should send [**EC\_REPAINT**](ec-repaint.md) to the Filter Graph Manager. If an **EC\_REPAINT** notification is received while paused, then the Filter Graph Manager calls [**IMediaPosition::put\_CurrentPosition**](/windows/desktop/api/Control/nf-control-imediaposition-put_currentposition) with the current position (that is, seeks to the current position). This causes the source filters to flush the filter graph and causes new data to be sent through the filter graph.

A renderer must send only one of these notifications at a time. Therefore, once the renderer sends a notification, it should ensure no more are sent until some samples are delivered. The conventional way to do this is to have a flag to signify that a repaint can be sent, which is turned off after an [**EC\_REPAINT**](ec-repaint.md) notification is sent. This flag should be reset once data is delivered or when the input pin is flushed, but not if end-of-stream is signaled on the input pin.

If the renderer does not monitor its [**EC\_REPAINT**](ec-repaint.md) notifications, it will flood the Filter Graph Manager with **EC\_REPAINT** requests (which are relatively expensive to process). For example, if a renderer has no image to draw, and another window is dragged across the window of the renderer in a full-drag operation, the renderer receives multiple [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) messages. Only the first of these should generate an **EC\_REPAINT** event notification from the renderer to the Filter Graph Manager.

A renderer should send its input pin as the first parameter to the [**EC\_REPAINT**](ec-repaint.md) notification. By doing this, the attached output pin will be queried for [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink), and if supported, the **EC\_REPAINT** notification will be sent there first. This enables output pins to handle repaints before the filter graph must be touched. This will not be done if the filter graph is stopped, because no buffers would be available from the decommitted renderer allocator.

If the output pin cannot handle the request and the filter graph is running, then the [**EC\_REPAINT**](ec-repaint.md) notification is ignored. An output pin must return **S\_OK** from [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify) to signal that it processed the repaint request successfully. The output pin will be called on the Filter Graph Manager worker thread, which avoids having the renderer call the output pin directly, and so sidesteps any deadlock issues. If the filter graph is stopped or paused and the output doesn't handle the request, then the default processing is done.

## Handling Notifications in Full-Screen Mode

The [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) plug-in distributor (PID) in the filter graph manages full-screen playback. It will swap a video renderer out for a specialist full-screen renderer, stretch a window of a renderer to full screen, or have the renderer implement full-screen playback directly. To interact in full-screen protocols, a video renderer should send an [**EC\_ACTIVATE**](ec-activate.md) notification whenever its window is either activated or deactivated. In other words, an **EC\_ACTIVATE** notification should be sent for each WM\_ACTIVATEAPP message a renderer receives.

When a renderer is being used in full-screen mode, these notifications manage the switching into and out of that full-screen mode. Window deactivation typically occurs when a user presses ALT+TAB to switch to another window, which the DirectShow full-screen renderer uses as a cue to return to typical rendering mode.

When the [**EC\_ACTIVATE**](ec-activate.md) notification is sent to the Filter Graph Manager upon switching out of full-screen mode, the Filter Graph Manager sends an [**EC\_FULLSCREEN\_LOST**](ec-fullscreen-lost.md) notification to the controlling application. The application might use this notification to restore the state of a full-screen button, for example. The **EC\_ACTIVATE** notifications are used internally by DirectShow to manage full-screen switching on cues from the video renderers.

## Summary of Notifications

This section lists the filter graph notifications that a renderer can send.



| Event notification                                        | Description                                                                                                                                                                                       |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EC\_ACTIVATE**](ec-activate.md)                       | Sent by video renderers in full-screen rendering mode for each WM\_ACTIVATEAPP message received.                                                                                                  |
| [**EC\_COMPLETE**](ec-complete.md)                       | Sent by renderers after all data has been rendered.                                                                                                                                               |
| [**EC\_DISPLAY\_CHANGED**](ec-display-changed.md)        | Sent by video renderers when a display format changes.                                                                                                                                            |
| [**EC\_PALETTE\_CHANGED**](ec-palette-changed.md)        | Sent whenever a video renderer detects a palette change in the stream.                                                                                                                            |
| [**EC\_REPAINT**](ec-repaint.md)                         | Sent by stopped or paused video renderers when a WM\_PAINT message is received and there is no data to display. This causes the Filter Graph Manager to generate a frame to paint to the display. |
| [**EC\_USERABORT**](ec-userabort.md)                     | Sent by video renderers to signal a closure that the user requested (for example, a user closing the video window).                                                                               |
| [**EC\_VIDEO\_SIZE\_CHANGED**](ec-video-size-changed.md) | Sent by video renderers whenever a change in native video size is detected.                                                                                                                       |
| [**EC\_WINDOW\_DESTROYED**](ec-window-destroyed.md)      | Sent by video renderers when the filter is removed or destroyed so that resources that depend on window focus can be passed to other filters.                                                     |



 

## Related topics

<dl> <dt>

[Writing Video Renderers](writing-video-renderers.md)
</dt> </dl>

 

 
