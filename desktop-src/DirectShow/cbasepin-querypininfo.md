---
Description: The QueryPinInfo method retrieves information about the pin. This method implements the IPinQueryPinInfo method.
ms.assetid: 9de41f61-9f03-4594-a320-2f7f0ed734fd
title: CBasePin.QueryPinInfo method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.QueryPinInfo method

The `QueryPinInfo` method retrieves information about the pin. This method implements the [**IPin::QueryPinInfo**](/windows/win32/Strmif/nf-strmif-ipin-querypininfo?branch=master) method.

## Syntax


```C++
HRESULT QueryPinInfo(
   PIN_INFO *pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* 
</dt> <dd>

Pointer to a [**PIN\_INFO**](/windows/win32/strmif/ns-strmif-_pininfo?branch=master) structure that receives the pin information.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Remarks

This method uses the [**CBasePin::m\_pName**](cbasepin-m-pname.md) member variable for the **achName** member of the PIN\_INFO structure.

When the method returns, if the **pFilter** member of the PIN\_INFO structure is non-**NULL**, it has an outstanding reference count. Be sure to release the interface when you are done.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




