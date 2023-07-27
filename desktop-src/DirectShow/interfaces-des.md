---
description: Interfaces For DirectShow Editing Services
ms.assetid: e7fdb387-83b3-4fa2-9608-2f5dc95975bf
title: Interfaces For DirectShow Editing Services
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Interfaces For DirectShow Editing Services

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

This section contains reference topics for the [DirectShow Editing Services](directshow-editing-services.md) (DES) interfaces.



| Interface                                                  | Description                                                                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [**IAMErrorLog**](iamerrorlog.md)                         | Provides a callback method for error logging.                                                                                  |
| [**IAMSetErrorLog**](iamseterrorlog.md)                   | Sets or retrieves an error log.                                                                                                |
| [**IAMTimeline**](iamtimeline.md)                         | Provides methods for manipulating the timeline.                                                                                |
| [**IAMTimelineComp**](iamtimelinecomp.md)                 | Inserts or retrieves virtual tracks on a composition.                                                                          |
| [**IAMTimelineEffect**](iamtimelineeffect.md)             | Provides methods for manipulating timeline effects.                                                                            |
| [**IAMTimelineEffectable**](iamtimelineeffectable.md)     | Provides methods for adding effects to a timeline object.                                                                      |
| [**IAMTimelineGroup**](iamtimelinegroup.md)               | Sets and retrieves properties on groups.                                                                                       |
| [**IAMTimelineObj**](iamtimelineobj.md)                   | Provides methods for manipulating timeline objects.                                                                            |
| [**IAMTimelineSplittable**](iamtimelinesplittable.md)     | Splits a timeline object.                                                                                                      |
| [**IAMTimelineSrc**](iamtimelinesrc.md)                   | Provides methods for manipulating and setting properties on source objects.                                                    |
| [**IAMTimelineTrack**](iamtimelinetrack.md)               | Provides methods for manipulating track objects.                                                                               |
| [**IAMTimelineTrans**](iamtimelinetrans.md)               | Provides methods for manipulating transition objects.                                                                          |
| [**IAMTimelineTransable**](iamtimelinetransable.md)       | Adds transitions to an object.                                                                                                 |
| [**IAMTimelineVirtualTrack**](iamtimelinevirtualtrack.md) | Provides methods for working with virtual tracks.                                                                              |
| [**IDxtAlphaSetter**](idxtalphasetter.md)                 | Sets properties on the [Alpha Setter](alpha-setter-effect.md) effect.                                                         |
| [**IDxtCompositor**](idxtcompositor.md)                   | Sets properties on the [Compositor](compositor-transition.md) transition.                                                     |
| [**IDxtJpeg**](idxtjpeg.md)                               | Sets properties on the [SMPTE Wipe](smpte-wipe-transition.md) transition.                                                     |
| [**IDxtKey**](idxtkey.md)                                 | Sets properties on the [Key](key-transition.md) transition.                                                                   |
| [**IFindCompressorCB**](ifindcompressorcb.md)             | Not supported.                                                                                                                 |
| [**IGrfCache**](igrfcache.md)                             | Not supported.                                                                                                                 |
| [**IMediaDet**](imediadet.md)                             | Retrieves information about a media file, such as the number of streams and the type, duration, and frame rate of each stream. |
| [**IMediaLocator**](imedialocator.md)                     | Provides methods for validating file names.                                                                                    |
| [**IPropertySetter**](ipropertysetter.md)                 | Sets properties on an effect or transition.                                                                                    |
| [**IRenderEngine**](irenderengine.md)                     | Renders a DES project by constructing a filter graph from a timeline.                                                          |
| [**IRenderEngine2**](irenderengine2.md)                   | Enables the application to replace the default video resizing filter used by DES.                                              |
| [**IResize**](iresize.md)                                 | Must be supported by any custom video resizer filter.                                                                          |
| [**ISampleGrabber**](isamplegrabber.md)                   | Retrieves individual media samples as they move through the filter graph.                                                      |
| [**ISampleGrabberCB**](isamplegrabbercb.md)               | Callback interface for the [**ISampleGrabber**](isamplegrabber.md) interface.                                                 |
| [**ISmartRenderEngine**](ismartrenderengine.md)           | Provides methods that support smart recompression.                                                                             |
| [**IXml2Dex**](ixml2dex.md)                               | Saves and loads DES project files in Extensible Markup Language (XML).                                                         |



 

## Related topics

<dl> <dt>

[DirectShow Editing Services C++ Reference](directshow-editing-services-c---reference.md)
</dt> </dl>

 

 



