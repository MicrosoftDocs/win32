---
Description: The GetStopPosition method retrieves the time when playback will stop, relative to the duration of the stream. This method implements the IMediaSeekingGetStopPosition method.
ms.assetid: 83928f62-7acc-43b9-9537-49131ed0b0d4
title: CSourceSeeking.GetStopPosition method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourceSeeking.GetStopPosition method

The `GetStopPosition` method retrieves the time when playback will stop, relative to the duration of the stream. This method implements the [**IMediaSeeking::GetStopPosition**](/windows/win32/Strmif/nf-strmif-imediaseeking-getstopposition?branch=master) method.

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

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer value<br/> |



 

## Remarks

The stop time is specified by the [**CSourceSeeking::m\_rtStop**](csourceseeking-m-rtstop.md) member variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




