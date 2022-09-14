---
description: The GetStopPosition method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the IMediaSeeking::GetStopPosition method.
ms.assetid: 11486371-da0a-4b83-956b-ef6b92721e74
title: CPosPassThru.GetStopPosition method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetStopPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.GetStopPosition method

The `GetStopPosition` method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the [**IMediaSeeking::GetStopPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getstopposition) method.

## Syntax


```C++
HRESULT GetStopPosition(
   LONGLONG *pStop
);
```



## Parameters

<dl> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that receives the stop time, in units of the current time format.

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

 

 




