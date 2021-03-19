---
description: The CEnumPins class implements an enumerator for pins.
ms.assetid: 8729f294-c76d-404f-9f51-7565470eced8
title: CEnumPins class (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CEnumPins class

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



 

 




