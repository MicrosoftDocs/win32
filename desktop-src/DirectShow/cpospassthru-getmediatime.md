---
Description: The GetMediaTime method retrieves the time stamps on the current sample.
ms.assetid: 36f3b6d3-b884-4168-94f3-f334a5056c7d
title: CPosPassThru.GetMediaTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




