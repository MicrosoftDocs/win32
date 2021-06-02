---
description: Flag that indicates whether a run-time error has occurred.
ms.assetid: 917bcb21-a11e-4ac5-af96-565f61c155cd
title: CBasePin::m_bRunTimeError member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bRunTimeError
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin::m\_bRunTimeError member

Flag that indicates whether a run-time error has occurred.

## Syntax


```C++
bool m_bRunTimeError;
```



## Remarks

This flag defaults to **FALSE**. Set the flag to **TRUE** if a run-time error occurs during streaming. The [**CBasePin::Inactive**](cbasepin-inactive.md) method resets the flag to **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




