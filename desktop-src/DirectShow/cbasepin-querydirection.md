---
description: The QueryDirection method retrieves the direction of the pin (input or output). This method implements the IPin::QueryDirection method.
ms.assetid: c28332dc-5ac4-4c89-98b4-281424f36ba9
title: CBasePin.QueryDirection method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.QueryDirection
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.QueryDirection method

The `QueryDirection` method retrieves the direction of the pin (input or output). This method implements the [**IPin::QueryDirection**](/windows/desktop/api/Strmif/nf-strmif-ipin-querydirection) method.

## Syntax


```C++
HRESULT QueryDirection(
   PIN_DIRECTION *pPinDir
);
```



## Parameters

<dl> <dt>

*pPinDir* 
</dt> <dd>

Pointer to a variable that receives a member of the [**PIN\_DIRECTION**](/windows/win32/api/strmif/ne-strmif-pin_direction) enumerated type.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




