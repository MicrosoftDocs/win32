---
description: Introduction to the Filter Base Classes
ms.assetid: db6324d7-1914-44a8-a202-dff752b61c1a
title: Introduction to the Filter Base Classes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Introduction to the Filter Base Classes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes the Microsoft DirectShow base class library. This library is intended for filter developers, but application writers might find some of the helper classes and debugging utilities useful. The base class library is not required for DirectShow programming, however.

The following sections summarize the most important base classes in the library.

**COM Object Classes**

The following classes support the creation of COM objects:



| Class                              | Description                            |
|------------------------------------|----------------------------------------|
| [**CBaseObject**](cbaseobject.md) | Base object class.                     |
| [**CUnknown**](cunknown.md)       | Implements the **IUnknown** interface. |



 

Most of the DirectShow classes derive from **CBaseObject**. This class provides debugging assistance by keeping a count of all the active objects in the DLL at run time. In debug builds, the DLL asserts if it is unloaded while the object count is greater than zero. This makes it easier to track down leaks caused by reference-counting problems.

All of the base classes that support COM interfaces derive from **CUnknown**, which inherits **CBaseObject**. The **CUnknown** class supports reference counting, **QueryInterface**, and aggregration. For more information, see [How to Implement IUnknown](how-to-implement-iunknown.md).

**Filter and Pin Classes**

The following classes support the creation of DirectShow filter and pin objects:



| Class                                    | Description                                                                                                                                                     |
|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CBaseFilter**](cbasefilter.md)       | Base class for filters. Implements the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface.                                                                            |
| [**CBasePin**](cbasepin.md)             | Base class for pins. Implements the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) and [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) interfaces.                                             |
| [**CBaseInputPin**](cbaseinputpin.md)   | Base class for input pins that use local memory transport. Implements the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface. This class derives from **CBasePin**. |
| [**CBaseOutputPin**](cbaseoutputpin.md) | Base class for output pins that use **IMemInputPin** connections. This class derives from **CBasePin**.                                                         |



 

The following classes are useful for creating more specialized types of filters:



| Class                                                  | Description                                                                                                                                                                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CSource**](csource.md)                             | Base class for source filters. This class is designed for creating push sources. It is not suitable for pull sources, such as file readers. To create output pins for this class, use the [**CSourceStream**](csourcestream.md) class.                                                                   |
| [**CTransformFilter**](ctransformfilter.md)           | Base class for transform filters. This class performs a copy on the data. The pins for this class are [**CTransformInputPin**](ctransforminputpin.md) and [**CTransformOutputPin**](ctransformoutputpin.md).                                                                                            |
| [**CTransInPlaceFilter**](ctransinplacefilter.md)     | Base class for transform filters that do not copy data. This class performs the data processing directly on the input data before passing it downstream. The pins for this class are [**CTransInPlaceInputPin**](ctransinplaceinputpin.md) and [**CTransInPlaceOutputPin**](ctransinplaceoutputpin.md). |
| [**CVideoTransformFilter**](cvideotransformfilter.md) | Base class for video transform filters. This class derives from **CTransformFilter** and adds support for quality control.                                                                                                                                                                                |
| [**CBaseRenderer**](cbaserenderer.md)                 | Base class for renderer filters. The input pin for this class is [**CRendererInputPin**](crendererinputpin.md).                                                                                                                                                                                          |
| [**CBaseVideoRenderer**](cbasevideorenderer.md)       | Base class for video renderers. This class derives from **CBaseRenderer**.                                                                                                                                                                                                                                |



 

To use these classes, you must derive your own class and write code to support the functionality that is specific to your filter. The more specialized the base class, the less code you will need to write in your derived class.

**Helper Objects**

The following classes implement helper objects that are used by filters and pins. Most of these classes can be used without deriving new classes from them:



| Class                                              | Description                                                                                                                                                        |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CPullPin**](cpullpin.md)                       | Helper object for input pins on parser filters. Supports [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) connections with pull sources.                                       |
| [**COutputQueue**](coutputqueue.md)               | Helper object for output pins that queue samples for delivery on a worker thread.                                                                                  |
| [**CSourceSeeking**](csourceseeking.md)           | Help object for implementing seeking on a source filter with exactly one output pin. (This class is not designed for filters with multiple pins, such as parsers.) |
| [**CEnumPins**](cenumpins.md)                     | Enumerator object for enumerating pins on a filter. Implements the [**IEnumPins**](/windows/desktop/api/Strmif/nn-strmif-ienumpins) interface.                                                       |
| [**CEnumMediaTypes**](cenummediatypes.md)         | Enumerator object for enumerating preferred media types on a pin. Implements the [**IEnumMediaTypes**](/windows/desktop/api/Strmif/nn-strmif-ienummediatypes) interface.                             |
| [**CMemAllocator**](cmemallocator.md)             | Memory allocator object. Implements the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.                                                                          |
| [**CMediaSample**](cmediasample.md)               | Media sample object. Implements the [**IMediaSample2**](/windows/desktop/api/Strmif/nn-strmif-imediasample2) interface.                                                                              |
| [**CBaseReferenceClock**](cbasereferenceclock.md) | Base class for reference clocks. Implements the [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) interface.                                                              |
| [**CMediaType**](cmediatype.md)                   | Helper object for manipulating [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structures.                                                                                |



 

 

 



