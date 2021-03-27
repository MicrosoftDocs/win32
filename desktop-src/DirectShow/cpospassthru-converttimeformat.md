---
description: The ConvertTimeFormat method converts from one time format to another. This method implements the IMediaSeeking::ConvertTimeFormat method.
ms.assetid: e766d112-ee41-4c64-a735-b6317093518a
title: CPosPassThru.ConvertTimeFormat method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.ConvertTimeFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.ConvertTimeFormat method

The `ConvertTimeFormat` method converts from one time format to another. This method implements the [**IMediaSeeking::ConvertTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-converttimeformat) method.

## Syntax


```C++
HRESULT ConvertTimeFormat(
         LONGLONG *pTarget,
   const GUID     *pTargetFormat,
         LONGLONG Source,
   const GUID     *pSourceFormat
);
```



## Parameters

<dl> <dt>

*pTarget* 
</dt> <dd>

Pointer to a variable that receives the converted time.

</dd> <dt>

*pTargetFormat* 
</dt> <dd>

Pointer to the time format GUID of the target format. If **NULL**, the current format is used.

</dd> <dt>

*Source* 
</dt> <dd>

Time value to be converted.

</dd> <dt>

*pSourceFormat* 
</dt> <dd>

Pointer to the time format GUID of the format to convert. If **NULL**, the current format is used.

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

 

 




