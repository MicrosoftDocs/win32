---
Description: The get\_Duration method retrieves the duration of the stream. This method implements the IMediaPositionget\_Duration method.
ms.assetid: 326a8cd3-d05f-49d0-941d-08f9778e9a06
title: CPosPassThru.get\_Duration method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.get\_Duration method

The `get_Duration` method retrieves the duration of the stream. This method implements the [**IMediaPosition::get\_Duration**](/windows/win32/Control/nf-control-imediaposition-get_duration?branch=master) method.

## Syntax


```C++
HRESULT get_Duration(
   REFTIME *plength
);
```



## Parameters

<dl> <dt>

*plength* 
</dt> <dd>

Pointer to a variable that receives the total stream length, in seconds.

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

 

 




