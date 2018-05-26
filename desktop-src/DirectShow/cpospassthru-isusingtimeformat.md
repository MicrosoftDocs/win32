---
Description: The IsUsingTimeFormat method determines whether a specified time format is the format currently in use. This method implements the IMediaSeekingIsUsingTimeFormat method.
ms.assetid: e377bcf0-0518-42b2-8975-e4c345e3fed4
title: CPosPassThru.IsUsingTimeFormat method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.IsUsingTimeFormat method

The `IsUsingTimeFormat` method determines whether a specified time format is the format currently in use. This method implements the [**IMediaSeeking::IsUsingTimeFormat**](/windows/win32/Strmif/nf-strmif-imediaseeking-isusingtimeformat?branch=master) method.

## Syntax


```C++
HRESULT IsUsingTimeFormat(
   const GUID *pFormat
);
```



## Parameters

<dl> <dt>

*pFormat* 
</dt> <dd>

Pointer to a time format GUID.

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
</dt> <dt>

[**Time Format GUIDs**](time-format-guids.md)
</dt> </dl>

 

 




