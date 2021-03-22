---
description: The CEnumMediaTypes class implements an enumerator for preferred media types.
ms.assetid: 50a90926-0bc7-4204-8000-81894bd154ac
title: CEnumMediaTypes class (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CEnumMediaTypes
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CEnumMediaTypes class

![cenummediatypes class hierarchy](images/filter04.png)

The `CEnumMediaTypes` class implements an enumerator for preferred media types.

This class implements the [**IEnumMediaTypes**](/windows/desktop/api/Strmif/nn-strmif-ienummediatypes) interface. It calls the following [**CBasePin**](cbasepin.md) methods:

-   [**CBasePin::GetMediaType**](cbasepin-getmediatype.md):Retrieves a media type, referenced by a zero-based index.
-   [**CBasePin::GetMediaTypeVersion**](cbasepin-getmediatypeversion.md): Determines whether the set of preferred types has changed.

Whenever a pin alters its list of preferred media types, the pin increments the media-type version number. When this happens, the enumerator object is no longer synchronized with the pin, and the class methods return VFW\_E\_ENUM\_OUT\_OF\_SYNC. Call the [**CEnumMediaTypes::Reset**](cenummediatypes-reset.md) method to resynchronize the enumerator.



| Public Methods                                               | Description                                                     |
|--------------------------------------------------------------|-----------------------------------------------------------------|
| [**CEnumMediaTypes**](cenummediatypes-cenummediatypes.md)   | Constructor method.                                             |
| [**~CEnumMediaTypes**](cenummediatypes--cenummediatypes.md) | Destructor method. Virtual.                                     |
| IEnumMediaTypes Methods                                      | Description                                                     |
| [**Clone**](cenummediatypes-clone.md)                       | Makes a copy of the enumerator with the same enumeration state. |
| [**Next**](cenummediatypes-next.md)                         | Retrieves a specified number of media types.                    |
| [**Reset**](cenummediatypes-reset.md)                       | Resets the enumeration sequence to the beginning.               |
| [**Skip**](cenummediatypes-skip.md)                         | Skips over a specified number of media types.                   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




