---
description: The EndFlush method ends a flush operation. This method overrides the CTransformFilter::EndFlush method.
ms.assetid: e7dfc6f9-1630-426b-95b2-9814331b5e61
title: CVideoTransformFilter.EndFlush method (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter.EndFlush method

The `EndFlush` method ends a flush operation. This method overrides the [**CTransformFilter::EndFlush**](ctransformfilter-endflush.md) method.

## Syntax


```C++
HRESULT EndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an error code.

## Remarks

This method resets all of the filter's internal performance measurements.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




