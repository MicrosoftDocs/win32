---
description: The UsingDifferentAllocators method determines whether the input and output pins are using different allocators.
ms.assetid: 75feaa6e-6395-4d47-ae92-10a857f8764b
title: CTransInPlaceFilter.UsingDifferentAllocators method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.UsingDifferentAllocators
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.UsingDifferentAllocators method

The `UsingDifferentAllocators` method determines whether the input and output pins are using different allocators.

## Syntax


```C++
BOOL UsingDifferentAllocators() const;
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the input and output pins are using different allocators, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




