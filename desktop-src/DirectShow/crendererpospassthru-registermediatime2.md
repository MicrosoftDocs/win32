---
description: The RegisterMediaTime method caches the time stamps from the current sample.
ms.assetid: 65755906-cf54-46d6-8149-5ad982be55f3
title: CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererPosPassThru.RegisterMediaTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererPosPassThru.RegisterMediaTime method (Ctlutil.h)

The [**RegisterMediaTime**](crendererpospassthru-registermediatime.md) method caches the time stamps from the current sample.

## Syntax


```C++
HRESULT RegisterMediaTime(
   LONGLONG StartTime,
   LONGLONG EndTime
);
```



## Parameters

<dl> <dt>

*StartTime* 
</dt> <dd>

Sample start time, in 100-nanosecond units.

</dd> <dt>

*EndTime* 
</dt> <dd>

Sample end time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                          | Description         |
|--------------------------------------------------------------------------------------|---------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Success.<br/> |



 

## Remarks

This method stores the time stamp values given in *StartTime* and *EndTime*. The [**CRendererPosPassThru::GetMediaTime**](crendererpospassthru-getmediatime.md) method retrieves the same values.

The filter should call this method for each sample that it receives. The method is overloaded to accept either a pointer to the sample, or the time stamp values themselves.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




