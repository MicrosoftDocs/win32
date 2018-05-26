---
Description: The GetPreroll method retrieves the amount of data that will be queued before the start position. This method implements the IMediaSeekingGetPreroll method.
ms.assetid: b00de2fa-ba3c-4a16-ad67-adf3df52ef9a
title: CPosPassThru.GetPreroll method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.GetPreroll method

The `GetPreroll` method retrieves the amount of data that will be queued before the start position. This method implements the [**IMediaSeeking::GetPreroll**](/windows/win32/Strmif/nf-strmif-imediaseeking-getpreroll?branch=master) method.

## Syntax


```C++
HRESULT GetPreroll(
   LONGLONG *pllPreroll
);
```



## Parameters

<dl> <dt>

*pllPreroll* 
</dt> <dd>

Pointer to a variable that receives the preroll time, in units of the current time format.

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

 

 




