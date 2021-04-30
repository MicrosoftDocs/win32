---
description: CPosPassThru.GetMediaTime method - The GetMediaTime method retrieves the time stamps on the current sample.
ms.assetid: 36f3b6d3-b884-4168-94f3-f334a5056c7d
title: CPosPassThru.GetMediaTime method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetMediaTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.GetMediaTime method

The `GetMediaTime` method retrieves the time stamps on the current sample.

## Syntax


```C++
virtual HRESULT GetMediaTime(
   LONGLONG *pStartTime,
   LONGLONG *pEndTime
);
```



## Parameters

<dl> <dt>

*pStartTime* 
</dt> <dd>

Pointer to a variable that receives the start time, in units of the current time format.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to a variable that receives the end time, in units of the current time format.

</dd> </dl>

## Return value

Returns E\_FAIL.

## Remarks

Override this method if your filter caches the time stamps on the samples it receives.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




