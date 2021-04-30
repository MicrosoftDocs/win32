---
description: The CTransInPlaceOutputPin class implements an output pin that is used by the CTransInPlaceFilter class.
ms.assetid: 90d54807-85c1-43b9-8998-e1bcf7b54725
title: CTransInPlaceOutputPin class (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceOutputPin class

![ctransinplaceoutputpin class hierarchy](images/tsip02.png)

The `CTransInPlaceOutputPin` class implements an output pin that is used by the [**CTransInPlaceFilter**](ctransinplacefilter.md) class.

Typically, you do not need to derive from this class. If you do, you must override the filter's [**CTransInPlaceFilter::GetPin**](ctransinplacefilter-getpin.md) method to create instances of your derived class.



| Protected Member Variables                                                      | Description                                          |
|---------------------------------------------------------------------------------|------------------------------------------------------|
| [**m\_pTIPFilter**](ctransinplaceoutputpin-m-ptipfilter.md)                    | Pointer to the filter that created this pin.         |
| Public Methods                                                                  | Description                                          |
| [**CTransInPlaceOutputPin**](ctransinplaceoutputpin-ctransinplaceoutputpin.md) | Constructor method.                                  |
| [**CheckMediaType**](ctransinplaceoutputpin-checkmediatype.md)                 | Determines if the pin accepts a specific media type. |
| [**SetAllocator**](ctransinplaceoutputpin-setallocator.md)                     | Specifies an allocator for the connection.           |
| [**ConnectedIMemInputPin**](ctransinplaceoutputpin-connectedimeminputpin.md)   | Retrieves a pointer to the downstream input pin.     |
| [**PeekAllocator**](ctransinplaceoutputpin-peekallocator.md)                   | Retrieves a pointer to the pin's allocator.          |
| IPin Methods                                                                    | Description                                          |
| [**EnumMediaTypes**](ctransinplaceoutputpin-enummediatypes.md)                 | Enumerates the pin's preferred media types.          |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




