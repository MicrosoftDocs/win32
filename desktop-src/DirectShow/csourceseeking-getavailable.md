---
description: CSourceSeeking.GetAvailable method - The GetAvailable method retrieves the range of times in which seeking is efficient. This method implements the IMediaSeeking::GetAvailable method.
ms.assetid: 2a7b6cdb-47c3-4aeb-89ff-ea968c6a809b
title: CSourceSeeking.GetAvailable method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.GetAvailable
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.GetAvailable method

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

Pointer to a variable that receives the earliest time for efficient seeking. The variable is set to zero.

</dd> <dt>

*pLatest* 
</dt> <dd>

Pointer to a variable that receives the latest time for efficient seeking. The variable is set to the value of the [**CSourceSeeking::m\_rtDuration**](csourceseeking-m-rtduration.md) member variable.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




