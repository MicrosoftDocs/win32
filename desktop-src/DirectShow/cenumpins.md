---
description: The CEnumPins class implements an enumerator for pins.
ms.assetid: 8729f294-c76d-404f-9f51-7565470eced8
title: CEnumPins class (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumPins
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CEnumPins class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cenumpins class hierarchy](images/filter03.png)

The `CEnumPins` class implements an enumerator for pins.

This class implements the [**IEnumPins**](/windows/desktop/api/Strmif/nn-strmif-ienumpins) interface. It calls the following [**CBaseFilter**](cbasefilter.md) methods:

-   [**CBaseFilter::GetPin**](cbasefilter-getpin.md): Retrieves a pin on the filter, referenced by a zero-based index.
-   [**CBaseFilter::GetPinCount**](cbasefilter-getpincount.md): Retrieves the total number of pins on the filter.
-   [**CBaseFilter::GetPinVersion**](cbasefilter-getpinversion.md): Determines whether the pins have changed.

If the filter dynamically creates or destroys pins, it increments the pin version whenever the pins change. If the version number changes, the enumerator object is no longer synchronized with the filter. Once the enumerator is out of sync, the methods in `CEnumPins` return VFW\_E\_ENUM\_OUT\_OF\_SYNC. Call the [**CEnumPins::Reset**](cenumpins-reset.md) method to resynchronize the enumerator.



| Public Methods                             | Description                                                     |
|--------------------------------------------|-----------------------------------------------------------------|
| [**CEnumPins**](cenumpins-cenumpins.md)   | Constructor method.                                             |
| [**~CEnumPins**](cenumpins--cenumpins.md) | Destructor method. Virtual.                                     |
| IEnumPins Methods                          | Description                                                     |
| [**Clone**](cenumpins-clone.md)           | Makes a copy of the enumerator with the same enumeration state. |
| [**Next**](cenumpins-next.md)             | Retrieves a specified number of pins.                           |
| [**Reset**](cenumpins-reset.md)           | Resets the enumeration sequence to the beginning.               |
| [**Skip**](cenumpins-skip.md)             | Skips over a specified number of pins.                          |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




