---
description: The AdvisePeriodic method creates a periodic advise request. This method implements the IReferenceClock::AdvisePeriodic method.
ms.assetid: ddaf0861-df11-4008-8e9c-a0c53929cd3f
title: CBaseReferenceClock.AdvisePeriodic method (Refclock.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.AdvisePeriodic
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseReferenceClock.AdvisePeriodic method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `AdvisePeriodic` method creates a periodic advise request. This method implements the [**IReferenceClock::AdvisePeriodic**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-adviseperiodic) method.

## Syntax


```C++
HRESULT AdvisePeriodic(
   REFERENCE_TIME StartTime,
   REFERENCE_TIME PeriodTime,
   HSEMAPHORE     hSemaphore,
   DWORD_PTR      *pdwAdviseToken
);
```



## Parameters

<dl> <dt>

*StartTime* 
</dt> <dd>

Time of the first notification, in 100-nanosecond units. Must be greater than zero and less than MAX\_TIME.

</dd> <dt>

*PeriodTime* 
</dt> <dd>

Time between notifications, in 100-nanosecond units. Must be greater than zero.

</dd> <dt>

*hSemaphore* 
</dt> <dd>

Handle to a semaphore, created by the caller.

</dd> <dt>

*pdwAdviseToken* 
</dt> <dd>

Pointer to a variable that receives an identifier for the advise request.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                   | Description                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid time values<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Failure<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument<br/> |



 

## Remarks

At each notification time, the clock releases the semaphore specified in the *hSemaphore* parameter. When no further notifications are required, call the [**CBaseReferenceClock::Unadvise**](cbasereferenceclock-unadvise.md) method and pass the *pdwAdviseToken* value returned from this call.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




