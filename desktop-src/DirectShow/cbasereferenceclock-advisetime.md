---
description: The AdviseTime method creates a one-shot advise request. This method implements the IReferenceClock::AdviseTime method.
ms.assetid: 4849a04d-35f2-4a24-bf5d-f20e541f5e99
title: CBaseReferenceClock.AdviseTime method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.AdviseTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.AdviseTime method

The `AdviseTime` method creates a one-shot advise request. This method implements the [**IReferenceClock::AdviseTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-advisetime) method.

## Syntax


```C++
HRESULT AdviseTime(
   REFERENCE_TIME baseTime,
   REFERENCE_TIME streamTime,
   HEVENT         hEvent,
   DWORD_PTR      *pdwAdviseToken
);
```



## Parameters

<dl> <dt>

*baseTime* 
</dt> <dd>

Base reference time, in 100-nanosecond units.

</dd> <dt>

*streamTime* 
</dt> <dd>

Stream offset time, in 100-nanosecond units.

</dd> <dt>

*hEvent* 
</dt> <dd>

Handle to an event, created by the caller.

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

This method creates a one-shot advise request for the reference time *baseTime* + *streamTime*. The sum must be greater than zero and less than MAX\_TIME, or the method returns E\_INVALIDARG. At the requested time, the clock signals the event specified in the *hEvent* parameter.

To cancel the notification before the time is reached, call the [**CBaseReferenceClock::Unadvise**](cbasereferenceclock-unadvise.md) method and pass the *pdwAdviseToken* value returned from this call. After the notification has occurred, the clock automatically clears it, so it is not necessary to call **Unadvise**. However, it is not an error to do so.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




