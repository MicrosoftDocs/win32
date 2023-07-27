---
description: Event Notification Codes
ms.assetid: 339ffcd9-7724-4c92-b241-afbed81d9380
title: Event Notification Codes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Event Notification Codes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This sections lists the DirectShow events that are not specific to DVD. For events specific to DVD, see [DVD Event Notification Codes](dvd-notification-codes.md).

Filters send events to the Filter Graph Manager by calling the [**IMediaEventSink::Notify**](/windows/desktop/api/Strmif/nf-strmif-imediaeventsink-notify) method. The Filter Graph Manager handles some events and queues others for the application. The application retrieves them by calling the [**IMediaEvent::GetEvent**](/windows/desktop/api/Control/nf-control-imediaevent-getevent) method.

In the sections that follow, each entry lists the event code, the meaning of the event parameters, and the Filter Graph Manager's default action for the event, if any. To override the default action, call [**IMediaEvent::CancelDefaultHandling**](/windows/desktop/api/Control/nf-control-imediaevent-canceldefaulthandling). Event codes are defined in the header files Evcode.h and Audevcod.h. If there is no default action, the Filter Graph Manager automatically forwards the event to the application (through the event queue).

**Custom Events**

Filters can define custom events with event codes in the range EC\_USER and higher. The Filter Graph Manager will place these directly in the event queue. However, the following caveats apply:

-   The Filter Graph Manager cannot free the event parameters using the normal [**IMediaEvent::FreeEventParams**](/windows/desktop/api/Control/nf-control-imediaevent-freeeventparams) method. The application must free any memory or reference counts associated with the event parameters.
-   The filter should only send the event from within an application that is prepared to handle the event. (Possibly the application can set a custom property on the filter to indicate that it is safe to send the event.)



| Event notification code                                                 | Description                                                                                                               |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**EC\_ACTIVATE**](ec-activate.md)                                     | A video window is being activated or deactivated.                                                                         |
| [**EC\_BANDWIDTHCHANGE**](ec-bandwidthchange.md)                       | Not supported.                                                                                                            |
| [**EC\_BUFFERING\_DATA**](ec-buffering-data.md)                        | The graph is buffering data, or has stopped buffering data.                                                               |
| [**EC\_BUILT**](ec-built.md)                                           | Send by the Video Control when a graph has been built. Not forwarded to applications.                                     |
| [**EC\_CLOCK\_CHANGED**](ec-clock-changed.md)                          | The reference clock has changed.                                                                                          |
| [**EC\_CLOCK\_UNSET**](ec-clock-unset.md)                              | The clock provider was disconnected.                                                                                      |
| [**EC\_CODECAPI\_EVENT**](ec-codecapi-event.md)                        | Sent by an encoder to signal an encoding event.                                                                           |
| [**EC\_COMPLETE**](ec-complete.md)                                     | All data from a particular stream has been rendered.                                                                      |
| [**EC\_CONTENTPROPERTY\_CHANGED**](ec-contentproperty-changed.md)      | Not supported.                                                                                                            |
| [**EC\_DEVICE\_LOST**](ec-device-lost.md)                              | A Plug and Play device was removed or has become available again.                                                         |
| [**EC\_DISPLAY\_CHANGED**](ec-display-changed.md)                      | The display mode has changed.                                                                                             |
| [**EC\_END\_OF\_SEGMENT**](ec-end-of-segment.md)                       | The end of a segment has been reached.                                                                                    |
| [**EC\_EOS\_SOON**](ec-eos-soon.md)                                    | Not supported.                                                                                                            |
| [**EC\_ERROR\_STILLPLAYING**](ec-error-stillplaying.md)                | An asynchronous command to run the graph has failed.                                                                      |
| [**EC\_ERRORABORT**](ec-errorabort.md)                                 | An operation was aborted because of an error.                                                                             |
| [**EC\_ERRORABORTEX**](ec-errorabortex.md)                             | An operation was aborted because of an error.                                                                             |
| [**EC\_EXTDEVICE\_MODE\_CHANGE**](ec-extdevice-mode-change.md)         | Not supported.                                                                                                            |
| [**EC\_FILE\_CLOSED**](ec-file-closed.md)                              | The source file was closed because of an unexpected event.                                                                |
| [**EC\_FULLSCREEN\_LOST**](ec-fullscreen-lost.md)                      | The video renderer is switching out of full-screen mode.                                                                  |
| [**EC\_GRAPH\_CHANGED**](ec-graph-changed.md)                          | The filter graph has changed.                                                                                             |
| [**EC\_LENGTH\_CHANGED**](ec-length-changed.md)                        | The length of a source has changed.                                                                                       |
| [**EC\_LOADSTATUS**](ec-loadstatus.md)                                 | Notifies the application of progress when opening a network file.                                                         |
| [**EC\_MARKER\_HIT**](ec-marker-hit.md)                                | Not supported.                                                                                                            |
| [**EC\_NEED\_RESTART**](ec-need-restart.md)                            | A filter is requesting that the graph be restarted.                                                                       |
| [**EC\_NEW\_PIN**](ec-new-pin.md)                                      | Not supported.                                                                                                            |
| [**EC\_NOTIFY\_WINDOW**](ec-notify-window.md)                          | Notifies a filter of the video renderer's window.                                                                         |
| [**EC\_OLE\_EVENT**](ec-ole-event.md)                                  | A filter is passing a text string to the application.                                                                     |
| [**EC\_OPENING\_FILE**](ec-opening-file.md)                            | The graph is opening a file, or has finished opening a file.                                                              |
| [**EC\_PALETTE\_CHANGED**](ec-palette-changed.md)                      | The video palette has changed.                                                                                            |
| [**EC\_PAUSED**](ec-paused.md)                                         | A pause request has completed.                                                                                            |
| [**EC\_PLEASE\_REOPEN**](ec-please-reopen.md)                          | The source file has changed.                                                                                              |
| [**EC\_PREPROCESS\_COMPLETE**](ec-preprocess-complete.md)              | Sent by the [WM ASF Writer](wm-asf-writer-filter.md) filter when it completes the pre-processing for multipass encoding. |
| [**EC\_PROCESSING\_LATENCY**](ec-processing-latency.md)                | Indicates the amount of time that a component is taking to process each sample.                                           |
| [**EC\_QUALITY\_CHANGE**](ec-quality-change.md)                        | The graph is dropping samples, for quality control.                                                                       |
| [**EC\_RENDER\_FINISHED**](ec-render-finished.md)                      | Not supported.                                                                                                            |
| [**EC\_REPAINT**](ec-repaint.md)                                       | A video renderer requires a repaint.                                                                                      |
| [**EC\_SAMPLE\_LATENCY**](ec-sample-latency.md)                        | Specifies how far behind schedule a component is for processing samples.                                                  |
| [**EC\_SAMPLE\_NEEDED**](ec-sample-needed.md)                          | Requests a new input sample from the Enhanced Video Renderer (EVR) filter.                                                |
| [**EC\_SCRUB\_TIME**](ec-scrub-time.md)                                | Specifies the time stamp for the most recent frame step.                                                                  |
| [**EC\_SEGMENT\_STARTED**](ec-segment-started.md)                      | A new segment has started.                                                                                                |
| [**EC\_SHUTTING\_DOWN**](ec-shutting-down.md)                          | The filter graph is shutting down, prior to being destroyed.                                                              |
| [**EC\_SNDDEV\_IN\_ERROR**](ec-snddev-in-error.md)                     | A device error has occurred in an audio capture filter.                                                                   |
| [**EC\_SNDDEV\_OUT\_ERROR**](ec-snddev-out-error.md)                   | A device error has occurred in an audio renderer filter.                                                                  |
| [**EC\_STARVATION**](ec-starvation.md)                                 | A filter is not receiving enough data.                                                                                    |
| [**EC\_STATE\_CHANGE**](ec-state-change.md)                            | The filter graph has changed state.                                                                                       |
| [**EC\_STATUS**](ec-status.md)                                         | Contains two arbitrary status strings.                                                                                    |
| [**EC\_STEP\_COMPLETE**](ec-step-complete.md)                          | A filter performing frame stepping has stepped the specified number of frames.                                            |
| [**EC\_STREAM\_CONTROL\_STARTED**](ec-stream-control-started.md)       | A stream-control start command has taken effect.                                                                          |
| [**EC\_STREAM\_CONTROL\_STOPPED**](ec-stream-control-stopped.md)       | A stream-control stop command has taken effect.                                                                           |
| [**EC\_STREAM\_ERROR\_STILLPLAYING**](ec-stream-error-stillplaying.md) | An error has occurred in a stream. The stream is still playing.                                                           |
| [**EC\_STREAM\_ERROR\_STOPPED**](ec-stream-error-stopped.md)           | A stream has stopped because of an error.                                                                                 |
| [**EC\_TIMECODE\_AVAILABLE**](ec-timecode-available.md)                | Not supported.                                                                                                            |
| [**EC\_UNBUILT**](ec-unbuilt.md)                                       | Send by the Video Control when a graph has been torn down. Not forwarded to applications.                                 |
| [**EC\_USERABORT**](ec-userabort.md)                                   | The user has terminated playback.                                                                                         |
| [**EC\_VIDEO\_SIZE\_CHANGED**](ec-video-size-changed.md)               | The native video size has changed.                                                                                        |
| [**EC\_VIDEOFRAMEREADY**](ec-videoframeready.md)                       | A video frame is ready for display.                                                                                       |
| [**EC\_VMR\_RECONNECTION\_FAILED**](ec-vmr-reconnection-failed.md)     | Sent by the VMR-7 and the VMR-9 when it was unable to accept a dynamic format change request from the upstream decoder.   |
| [**EC\_VMR\_RENDERDEVICE\_SET**](ec-vmr-renderdevice-set.md)           | Sent when the VMR has selected its rendering mechanism.                                                                   |
| [**EC\_VMR\_SURFACE\_FLIPPED**](ec-vmr-surface-flipped.md)             | Sent when the VMR-7's allocator presenter has called the DirectDraw Flip method on the surface being presented.           |
| [**EC\_WINDOW\_DESTROYED**](ec-window-destroyed.md)                    | The video renderer was destroyed or removed from the graph.                                                               |
| [**EC\_WMT\_EVENT**](ec-wmt-event.md)                                  | Sent by the WM ASF Reader filter when it reads ASF files protected by digital rights management (DRM).                    |
| [**EC\_WMT\_INDEX\_EVENT**](ec-wmt-index-event.md)                     | Sent when an application uses the WM ASF Writer to index Windows Media Video files.                                       |



 

## Related topics

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



