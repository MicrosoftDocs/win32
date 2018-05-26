---
Description: The SetTime method sets the stream times when this sample should begin and finish. This method implements the IMediaSampleSetTime method.
ms.assetid: cab4907f-eb6f-4444-9b41-1f95a6ecffed
title: CMediaSample.SetTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaSample.SetTime method

The `SetTime` method sets the stream times when this sample should begin and finish. This method implements the [**IMediaSample::SetTime**](/windows/win32/Strmif/nf-strmif-imediasample-settime?branch=master) method.

## Syntax


```C++
HRESULT SetTime(
   REFERENCE_TIME *pTimeStart,
   REFERENCE_TIME *pTimeEnd
);
```



## Parameters

<dl> <dt>

*pTimeStart* 
</dt> <dd>

Pointer to the stream time at which the sample begins, in 100-nanosecond units, or **NULL**.

</dd> <dt>

*pTimeEnd* 
</dt> <dd>

Pointer to the stream time at which the sample ends, in 100-nanosecond units, or **NULL**.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CMediaSample::m\_Start**](cmediasample-m-start.md) and [**CMediaSample::m\_End**](cmediasample-m-end.md) member variables, which specify the time stamps. It also updates the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable, which specifies whether the time stamps are valid.

For information about time stamps, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




