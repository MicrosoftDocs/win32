---
description: The CTransInPlaceInputPin class implements an input pin that is used by the CTransInPlaceFilter class.
ms.assetid: 8cd2f17d-64b4-4ee6-b31a-e841ada03ce6
title: CTransInPlaceInputPin class (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceInputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceInputPin class

![ctransinplaceinputpin class hierarchy](images/tsip01.png)

The `CTransInPlaceInputPin` class implements an input pin that is used by the [**CTransInPlaceFilter**](ctransinplacefilter.md) class.

Typically, you do not need to derive from this class. If you do, you must override the filter's [**CTransInPlaceFilter::GetPin**](ctransinplacefilter-getpin.md) method to create instances of your derived class.



| Protected Member Variables                                                          | Description                                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------|
| [**m\_bReadOnly**](ctransinplaceinputpin-m-breadonly.md)                           | Flag that specifies whether the input stream is read-only. |
| [**m\_pTIPFilter**](ctransinplaceinputpin-m-ptipfilter.md)                         | Pointer to the filter that created this pin.               |
| Public Methods                                                                      | Description                                                |
| [**CTransInPlaceInputPin**](ctransinplaceinputpin-ctransinplaceinputpin.md)        | Constructor method.                                        |
| [**CheckMediaType**](ctransinplaceinputpin-checkmediatype.md)                      | Determines if the pin accepts a specific media type.       |
| [**PeekAllocator**](ctransinplaceinputpin-peekallocator.md)                        | Retrieves a pointer to the pin's allocator.                |
| [**ReadOnly**](ctransinplaceinputpin-readonly.md)                                  | Indicates whether the input stream is read-only.           |
| IPin Methods                                                                        | Description                                                |
| [**EnumMediaTypes**](ctransinplaceinputpin-enummediatypes.md)                      | Enumerates the pin's preferred media types.                |
| IMemInputPin Methods                                                                | Description                                                |
| [**GetAllocator**](ctransinplaceinputpin-getallocator.md)                          | Retrieves the memory allocator proposed by this pin.       |
| [**NotifyAllocator**](ctransinplaceinputpin-notifyallocator.md)                    | Specifies an allocator for the connection.                 |
| [**GetAllocatorRequirements**](ctransinplaceinputpin--getallocatorrequirements.md) | Retrieves the allocator properties requested by the pin.   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




