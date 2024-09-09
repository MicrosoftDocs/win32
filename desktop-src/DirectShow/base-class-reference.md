---
description: DirectShow Base Class Reference
ms.assetid: 56f3685f-3df8-4358-b04e-3efc04b58008
title: DirectShow Base Class Reference
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectShow Base Class Reference

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains reference entries for all the Microsoft [DirectShow Base Classes](directshow-base-classes.md), their data members, and their functions.



| Class                                                                  | Description                                                                                                                       |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**CAggDirectDraw**](caggdirectdraw.md)                               | Deprecated.                                                                                                                       |
| [**CAggDrawSurface**](caggdrawsurface.md)                             | Deprecated.                                                                                                                       |
| [**CAMEvent**](camevent.md)                                           | Wrapper class for manual- and auto-reset events.                                                                                  |
| [**CAMMsgEvent**](cammsgevent.md)                                     | Wrapper class for event objects that perform message processing.                                                                  |
| [**CAMSchedule**](camschedule.md)                                     | Scheduler for reference clocks.                                                                                                   |
| [**CAMThread**](camthread.md)                                         | Bass class for managing worker threads.                                                                                           |
| [**CAutoLock**](cautolock.md)                                         | Holds a critical section for the scope of a block.                                                                                |
| [**CAutoUsingOutputPin**](cautousingoutputpin-cautousingoutputpin.md) | Obtains and releases access to a [**CDynamicOutputPin**](cdynamicoutputpin.md) object.                                           |
| [**CBaseAllocator**](cbaseallocator.md)                               | Bass class for allocators.                                                                                                        |
| [**CBaseBasicVideo**](cbasebasicvideo.md)                             | Handles the IDispatch component of the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface.                                              |
| [**CBaseControlVideo**](cbasecontrolvideo.md)                         | Implements the IBasicVideo interface for a generic video window.                                                                  |
| [**CBaseControlWindow**](cbasecontrolwindow.md)                       | Implements the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface.                                                                    |
| [**CBaseDispatch**](cbasedispatch.md)                                 | Base class for implementing the IDispatch interface.                                                                              |
| [**CBaseFilter**](cbasefilter.md)                                     | Base class for filters.                                                                                                           |
| [**CBaseInputPin**](cbaseinputpin.md)                                 | Base class for input pins.                                                                                                        |
| [**CBaseList**](cbaselist.md)                                         | Base class for generic lists.                                                                                                     |
| [**CBaseMediaFilter**](cbasemediafilter.md)                           | Implements the [**IMediaFilter**](/windows/desktop/api/Strmif/nn-strmif-imediafilter) interface.                                                                    |
| [**CBaseObject**](cbaseobject.md)                                     | Base class for implementing DirectShow objects.                                                                                   |
| [**CBaseOutputPin**](cbaseoutputpin.md)                               | Base class for output pins.                                                                                                       |
| [**CBasePin**](cbasepin.md)                                           | Base class for pins.                                                                                                              |
| [**CBasePropertyPage**](cbasepropertypage.md)                         | Base class for implementing property pages.                                                                                       |
| [**CBaseReferenceClock**](cbasereferenceclock.md)                     | Implements a reference clock.                                                                                                     |
| [**CBaseRenderer**](cbaserenderer.md)                                 | Base class for implementing renderer filters.                                                                                     |
| [**CBaseStreamControl**](cbasestreamcontrol.md)                       | Implements the [**IAMStreamControl**](/windows/desktop/api/Strmif/nn-strmif-iamstreamcontrol) interface.                                                            |
| [**CBaseVideoRenderer**](cbasevideorenderer.md)                       | Base class for video renderers.                                                                                                   |
| [**CBaseVideoWindow**](cbasevideowindow.md)                           | Handles the IDispatch component of the [**IVideoWindow**](/windows/desktop/api/Control/nn-control-ivideowindow) interface.                                            |
| [**CBaseWindow**](cbasewindow.md)                                     | Base class for managing windows.                                                                                                  |
| [**CBasicAudio**](cbasicaudio.md)                                     | Handles the IDispatch interface component of the [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio) interface.                                    |
| [**CCmdQueue**](ccmdqueue.md)                                         | Helper class for implementing the [**IQueueCommand**](/windows/desktop/api/Control/nn-control-iqueuecommand) interface.                                               |
| [**CCritSec**](ccritsec.md)                                           | Provides a thread lock.                                                                                                           |
| [**CDeferredCommand**](cdeferredcommand.md)                           | Implements the [**IDeferredCommand**](/windows/desktop/api/Control/nn-control-ideferredcommand) interface.                                                            |
| [**CDispParams**](cdispparams.md)                                     | Wrapper class for the DISPPARAMS structure.                                                                                       |
| [**CDrawImage**](cdrawimage.md)                                       | Helper class for drawing to a window.                                                                                             |
| [**CDynamicOutputPin**](cdynamicoutputpin.md)                         | Output pin that supports dyanamic reconnections and format changes.                                                               |
| [**CEnumMediaTypes**](cenummediatypes.md)                             | Enumerator for preferred media types.                                                                                             |
| [**CEnumPins**](cenumpins.md)                                         | Enumerator for pins.                                                                                                              |
| [**CFactoryTemplate**](cfactorytemplate.md)                           | Class that provides information for a class factory.                                                                              |
| [**CGenericList**](cgenericlist.md)                                   | Class template that implements a type-specific list.                                                                              |
| [**CImageAllocator**](cimageallocator.md)                             | Allocator for DIB sections.                                                                                                       |
| [**CImageDisplay**](cimagedisplay.md)                                 | Helper class for managing image display formats.                                                                                  |
| [**CImagePalette**](cimagepalette.md)                                 | Helper class for managing palettes.                                                                                               |
| [**CImageSample**](cimagesample.md)                                   | Media sample that uses DIB sections.                                                                                              |
| [**CLoadDirectDraw**](cloaddirectdraw.md)                             | Deprecated.                                                                                                                       |
| [**CMediaControl**](cmediacontrol.md)                                 | Handles the IDispatch methods of the [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol) interface.                                            |
| [**CMediaEvent**](cmediaevent.md)                                     | Handles the IDispatch methods of the [**IMediaEvent**](/windows/desktop/api/Control/nn-control-imediaevent) interface.                                                |
| [**CMediaPosition**](cmediaposition.md)                               | Handles the IDispatch methods of the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) interface.                                          |
| [**CMediaSample**](cmediasample.md)                                   | Media sample.                                                                                                                     |
| [**CMediaType**](cmediatype.md)                                       | Class for managing media types.                                                                                                   |
| [**CMemAllocator**](cmemallocator.md)                                 | Memory allocator.                                                                                                                 |
| [**CMsg**](cmsg.md)                                                   | Helper class for managing requests made to a [**CMsgThread**](cmsgthread.md) object.                                             |
| [**CMsgThread**](cmsgthread.md)                                       | Worker thread that queues requests to the queuing thread for asynchronous completion.                                             |
| [**COARefTime**](coareftime.md)                                       | Converts reference times between seconds and 100-nanosecond units.                                                                |
| [**COutputQueue**](coutputqueue.md)                                   | Object that queues media samples for delivery.                                                                                    |
| [**CPersistStream**](cpersiststream.md)                               | Base class for implementing the IPersistStream interface.                                                                         |
| [**CPosPassThru**](cpospassthru.md)                                   | Handles seek commands for filters with one input pin.                                                                             |
| [**CPullPin**](cpullpin.md)                                           | Helper class that pulls data from an output pin that supports the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface.                 |
| [**CQueue**](cqueue.md)                                               | Class template that implements a simple, statically sized queue.                                                                  |
| [**CRefTime**](creftime.md)                                           | Helper class to manage reference times.                                                                                           |
| [**CRenderedInputPin**](crenderedinputpin.md)                         | Input pin for renderer filters that support multiple inputs.                                                                      |
| [**CRendererInputPin**](crendererinputpin.md)                         | Input pin for the [**CBaseRenderer**](cbaserenderer.md) class.                                                                   |
| [**CRendererPosPassThru**](crendererpospassthru.md)                   | Handles seek commands for renderer filters.                                                                                       |
| [**CSeekingPassThru**](cseekingpassthru.md)                           | Helper object that creates [**CPosPassThru**](cpospassthru.md) and [**CRendererPosPassThru**](crendererpospassthru.md) objects. |
| [**CSource**](csource.md)                                             | Base class for implementing source filters.                                                                                       |
| [**CSourcePosition**](csourceposition.md)                             | Abstract class for implementing the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) interface. Obsolete.                                 |
| [**CSourceSeeking**](csourceseeking.md)                               | Abstract class for implementing seeking in source filters with one output pin.                                                    |
| [**CSourceStream**](csourcestream.md)                                 | Output pin for the [**CSource**](csource.md) class.                                                                              |
| [**CSystemClock**](csystemclock.md)                                   | System clock.                                                                                                                     |
| [**CTransformFilter**](ctransformfilter.md)                           | Base class for implementing transform filters.                                                                                    |
| [**CTransformInputPin**](ctransforminputpin.md)                       | Input pin used by the CTransformFilter class.                                                                                     |
| [**CTransformOutputPin**](ctransformoutputpin.md)                     | Output pin used by the CTransformFilter class.                                                                                    |
| [**CTransInPlaceFilter**](ctransinplacefilter.md)                     | Class for implementing transform filters that do not copy data.                                                                   |
| [**CTransInPlaceInputPin**](ctransinplaceinputpin.md)                 | Input pin for the CTransInPlaceFilter class.                                                                                      |
| [**CTransInPlaceOutputPin**](ctransinplaceoutputpin.md)               | Output pin for the CTransInPlaceFilter class.                                                                                     |
| [**CUnknown**](cunknown.md)                                           | Implements the IUnknown interface.                                                                                                |
| [**CVideoTransformFilter**](cvideotransformfilter.md)                 | Base class for video transform filters.                                                                                           |
| [**FOURCCMap**](fourccmap.md)                                         | Helper class for converting between GUIDs and FOURCCs.                                                                            |



 

## Related topics

<dl> <dt>

[DirectShow Base Classes](directshow-base-classes.md)
</dt> </dl>

 

 



