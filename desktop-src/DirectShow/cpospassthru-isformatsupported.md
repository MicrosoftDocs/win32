---
description: The IsFormatSupported method determines whether a specified time format is supported. This method implements the IMediaSeeking::IsFormatSupported method.
ms.assetid: dd8751d6-8439-4155-bdaf-b152a7c6cad4
title: CPosPassThru.IsFormatSupported method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.IsFormatSupported
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.IsFormatSupported method

The `IsFormatSupported` method determines whether a specified time format is supported. This method implements the [**IMediaSeeking::IsFormatSupported**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-isformatsupported) method.

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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> <dt>

[**Time Format GUIDs**](time-format-guids.md)
</dt> </dl>

 

 




