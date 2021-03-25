---
description: The AbortPlayback method is used to signal a streaming error. It sends an EC\_ERRORABORT event to the Filter Graph Manager, and sends an end-of-stream notification downstream.
ms.assetid: b48ec72f-d220-4b27-98fc-88eaa4f663eb
title: CVideoTransformFilter.AbortPlayback method (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.AbortPlayback
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter.AbortPlayback method

The `AbortPlayback` method is used to signal a streaming error. It sends an [**EC\_ERRORABORT**](ec-errorabort.md) event to the Filter Graph Manager, and sends an end-of-stream notification downstream.

## Syntax


```C++
HRESULT AbortPlayback(
   HRESULT hr
);
```



## Parameters

<dl> <dt>

*hr* 
</dt> <dd>

**HRESULT** value of the operation that failed. This value is used as the first event parameter for the EC\_ERRORABORT event.

</dd> </dl>

## Return value

Returns the value of the *hr* parameter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




