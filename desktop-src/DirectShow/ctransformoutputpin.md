---
description: The CTransformOutputPin class implements an output pin that is used by the CTransformFilter class.
ms.assetid: 76f9a981-8f0d-45d4-b901-c5ec5b5ac9ee
title: CTransformOutputPin class (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformOutputPin class

![ctransformoutputpin class hierarchy](images/tfrm02.png)

The `CTransformOutputPin` class implements an output pin that is used by the [**CTransformFilter**](ctransformfilter.md) class.

Typically, you do not need to derive from this class. Most of the methods in this class call corresponding methods on the **CTransformFilter** class, which you can override. If you derive from this class, you must override the filter's [**CTransformFilter::GetPin**](ctransformfilter-getpin.md) method to create instances of your derived class.

This class exposes the **IMediaSeeking** and **IMediaPosition** interfaces through the [**CPosPassThru**](cpospassthru.md) object. It passes all seek requests to the next filter upstream.



| Protected Member Variables                                               | Description                                              |
|--------------------------------------------------------------------------|----------------------------------------------------------|
| [**m\_pTransformFilter**](ctransformoutputpin-m-ptransformfilter.md)    | Pointer to the owning filter.                            |
| Public Member Variables                                                  | Description                                              |
| [**m\_pPosition**](ctransformoutputpin-m-pposition.md)                  | Helper object to pass seek commands upstream.            |
| Public Methods                                                           | Description                                              |
| [**CTransformOutputPin**](ctransformoutputpin-ctransformoutputpin.md)   | Constructor method.                                      |
| [**~CTransformOutputPin**](ctransformoutputpin--ctransformoutputpin.md) | Destructor method.                                       |
| [**CheckConnect**](ctransformoutputpin-checkconnect.md)                 | Determines whether a pin connection is suitable.         |
| [**BreakConnect**](ctransformoutputpin-breakconnect.md)                 | Releases the pin from a connection.                      |
| [**CompleteConnect**](ctransformoutputpin-completeconnect.md)           | Completes a connection to another pin.                   |
| [**CheckMediaType**](ctransformoutputpin-checkmediatype.md)             | Determines if the pin accepts a specific media type.     |
| [**SetMediaType**](ctransformoutputpin-setmediatype.md)                 | Sets the media type for the connection.                  |
| [**DecideBufferSize**](ctransformoutputpin-decidebuffersize.md)         | Sets the buffer requirements.                            |
| [**GetMediaType**](ctransformoutputpin-getmediatype.md)                 | Retrieves a preferred media type, by index value.        |
| [**CurrentMediaType**](ctransformoutputpin-currentmediatype.md)         | Retrieves the media type for the current pin connection. |
| IPin Methods                                                             | Description                                              |
| [**QueryId**](ctransformoutputpin-queryid.md)                           | Retrieves an identifier for the pin.                     |
| IQualityControl Methods                                                  | Description                                              |
| [**Notify**](ctransformoutputpin-notify.md)                             | Notifies the pin that a quality change is requested.     |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




