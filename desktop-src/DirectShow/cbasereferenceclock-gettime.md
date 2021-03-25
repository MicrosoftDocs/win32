---
description: The GetTime method retrieves the current reference time. This method implements the IReferenceClock::GetTime method.
ms.assetid: 4e4e5954-b899-4741-8b7c-7bc98a3f0404
title: CBaseReferenceClock.GetTime method (Refclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.GetTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseReferenceClock.GetTime method

The `GetTime` method retrieves the current reference time. This method implements the [**IReferenceClock::GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) method.

## Syntax


```C++
HRESULT GetTime(
   REFERENCE_TIME *pTime
);
```



## Parameters

<dl> <dt>

*pTime* 
</dt> <dd>

Pointer to a variable that receives the current time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                               | Description                                                 |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>                       |
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Returned time is the same as the previous value.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                                         |



 

## Remarks

This method calls the [**CBaseReferenceClock::GetPrivateTime**](cbasereferenceclock-getprivatetime.md) method to determine the real clock time. If the clock time is strictly greater than the previous value, `GetTime` uses the clock time and returns S\_OK. Otherwise, `GetTime` uses the previous value and returns S\_FALSE. Therefore, the internal clock can run backward for a short period, without causing the reference time to run backward. Instead, the reference time will "stall" at the same value until the internal clock catches up.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




