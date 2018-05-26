---
Description: The get\_PrerollTime method retrieves the amount of data that will be queued before the start position. This method implements the IMediaPositionget\_PrerollTime method.
ms.assetid: 37c12798-eb0d-4859-8b2e-52d6ae147863
title: CPosPassThru.get\_PrerollTime method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.get\_PrerollTime method

The `get_PrerollTime` method retrieves the amount of data that will be queued before the start position. This method implements the [**IMediaPosition::get\_PrerollTime**](/windows/win32/Control/nf-control-imediaposition-get_prerolltime?branch=master) method.

## Syntax


```C++
HRESULT get_PrerollTime(
   REFTIME *pllTime
);
```



## Parameters

<dl> <dt>

*pllTime* 
</dt> <dd>

Pointer to a variable that receives the preroll time, in seconds.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




