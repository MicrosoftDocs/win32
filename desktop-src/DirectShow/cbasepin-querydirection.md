---
Description: The QueryDirection method retrieves the direction of the pin (input or output). This method implements the IPinQueryDirection method.
ms.assetid: c28332dc-5ac4-4c89-98b4-281424f36ba9
title: CBasePin.QueryDirection method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.QueryDirection method

The `QueryDirection` method retrieves the direction of the pin (input or output). This method implements the [**IPin::QueryDirection**](/windows/win32/Strmif/nf-strmif-ipin-querydirection?branch=master) method.

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

Pointer to a variable that receives a member of the [**PIN\_DIRECTION**](/windows/win32/strmif/ne-strmif-_pindirection?branch=master) enumerated type.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




