---
Description: The GetRate method retrieves the playback rate. This method implements the IMediaSeekingGetRate method.
ms.assetid: 19de3ea3-280e-4320-9cce-2c29801bd84b
title: CPosPassThru.GetRate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.GetRate method

The `GetRate` method retrieves the playback rate. This method implements the [**IMediaSeeking::GetRate**](/windows/win32/Strmif/nf-strmif-imediaseeking-getrate?branch=master) method.

## Syntax


```C++
HRESULT GetRate(
   double *pdRate
);
```



## Parameters

<dl> <dt>

*pdRate* 
</dt> <dd>

Pointer to a variable that receives the playback rate.

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

 

 




