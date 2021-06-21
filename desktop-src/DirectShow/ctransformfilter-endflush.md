---
description: CTransformFilter.EndFlush method - The EndFlush method ends a flush operation.
ms.assetid: ebb6beec-84e2-49a7-9771-bbd191faada7
title: CTransformFilter.EndFlush method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.EndFlush method

The `EndFlush` method ends a flush operation.

## Syntax


```C++
virtual HRESULT EndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

At the end of a flush operation, the input pin's [**CTransformInputPin::EndFlush**](ctransforminputpin-endflush.md) method calls this method. This method passes the `EndFlush` call downstream.

If the derived class uses a worker thread to deliver samples, it must discard any queued data before sending the `EndFlush` call downstream. For more information, see [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




