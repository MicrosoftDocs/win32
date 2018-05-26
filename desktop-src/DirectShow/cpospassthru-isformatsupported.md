---
Description: The IsFormatSupported method determines whether a specified time format is supported. This method implements the IMediaSeekingIsFormatSupported method.
ms.assetid: dd8751d6-8439-4155-bdaf-b152a7c6cad4
title: CPosPassThru.IsFormatSupported method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPosPassThru.IsFormatSupported method

The `IsFormatSupported` method determines whether a specified time format is supported. This method implements the [**IMediaSeeking::IsFormatSupported**](/windows/win32/Strmif/nf-strmif-imediaseeking-isformatsupported?branch=master) method.

## Syntax


```C++
HRESULT IsFormatSupported(
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

 

 




