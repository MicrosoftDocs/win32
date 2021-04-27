---
description: CPosPassThru.GetDuration method - The GetDuration method retrieves the duration of the stream. This method implements the IMediaSeeking::GetDuration method.
ms.assetid: 0552e7bb-4d7e-40a8-a8ad-89ae6fff8ccb
title: CPosPassThru.GetDuration method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetDuration
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.GetDuration method

The `GetDuration` method retrieves the duration of the stream. This method implements the [**IMediaSeeking::GetDuration**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getduration) method.

## Syntax


```C++
HRESULT GetDuration(
   LONGLONG *pDuration
);
```



## Parameters

<dl> <dt>

*pDuration* 
</dt> <dd>

Pointer to a variable that receives the duration, in units of the current time format.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




