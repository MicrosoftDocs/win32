---
description: The ConvertTimeFormat method converts from one time format to another. This method implements the IMediaSeeking::ConvertTimeFormat method.
ms.assetid: d0cb44fa-30c1-41b4-92a4-7169161e3140
title: CSourceSeeking.ConvertTimeFormat method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.ConvertTimeFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.ConvertTimeFormat method

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

Pointer to the GUID of the target format. If **NULL**, the current format is used. See [**Time Format GUIDs**](time-format-guids.md).

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

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                                  | Description                          |
|----------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Invalid argument<br/>          |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument<br/> |



 

## Remarks

The only time format supported by the base class is TIME\_FORMAT\_MEDIA\_TIME (100-nanosecond units). This method returns E\_INVALIDARG, except in the trivial case where *pTargetFormat* and *pSourceFormat* both specify TIME\_FORMAT\_MEDIA\_TIME.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




