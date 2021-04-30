---
description: CPosPassThru.GetAvailable method - The GetAvailable method retrieves the range of times in which seeking is efficient. This method implements the IMediaSeeking::GetAvailable method.
ms.assetid: 5f4af41a-eb7b-4caa-97e0-aaed78467723
title: CPosPassThru.GetAvailable method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetAvailable
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.GetAvailable method

The `GetAvailable` method retrieves the range of times in which seeking is efficient. This method implements the [**IMediaSeeking::GetAvailable**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getavailable) method.

## Syntax


```C++
HRESULT GetAvailable(
   LONGLONG *pEarliest,
   LONGLONG *pLatest
);
```



## Parameters

<dl> <dt>

*pEarliest* 
</dt> <dd>

Pointer to a variable that receives the earliest time for efficient seeking.

</dd> <dt>

*pLatest* 
</dt> <dd>

Pointer to a variable that receives the latest time for efficient seeking.

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

 

 




