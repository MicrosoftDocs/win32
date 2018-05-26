---
Description: The SetControlVideoPin method sets the pin used by the filter.
ms.assetid: 4346f828-4380-4150-9ecb-74eb690bdcdf
title: CBaseControlVideo.SetControlVideoPin method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlVideo.SetControlVideoPin method

The `SetControlVideoPin` method sets the pin used by the filter.

## Syntax


```C++
void SetControlVideoPin(
   CBasePin *pPin
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the pin with which the interface is synchronized.

</dd> </dl>

## Return value

No return value.

## Remarks

The interface can be called only when the filter has been connected successfully. The object is passed through this method to the pin with which it is synchronized; in most cases it will determine if the pin is connected when it has an interface method called and will return VFW\_E\_NOT\_CONNECTED if it fails.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




