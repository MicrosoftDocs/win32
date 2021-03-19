---
description: The GetTimeFormat method retrieves the current time format. This method implements the IMediaSeeking::GetTimeFormat method.
ms.assetid: c90804f7-9a0a-423c-8b26-87abf15eddc5
title: CSourceSeeking.GetTimeFormat method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.GetTimeFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.GetTimeFormat method

The `GetTimeFormat` method retrieves the current time format. This method implements the [**IMediaSeeking::GetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-gettimeformat) method.

## Syntax


```C++
HRESULT GetTimeFormat(
   const GUID *pFormat
);
```



## Parameters

<dl> <dt>

*pFormat* 
</dt> <dd>

Pointer to a variable that receives a time format GUID. See [**Time Format GUIDs**](time-format-guids.md).

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer value<br/> |



 

## Remarks

The only time format supported by the base class is TIME\_FORMAT\_MEDIA\_TIME (100-nanosecond units).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




