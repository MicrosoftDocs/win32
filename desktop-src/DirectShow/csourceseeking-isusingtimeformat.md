---
description: The IsUsingTimeFormat method determines whether a specified time format is the format currently in use.
ms.assetid: 86965bfc-fc9f-42d3-bcaa-2049195b98bd
title: CSourceSeeking.IsUsingTimeFormat method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.IsUsingTimeFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.IsUsingTimeFormat method

The `IsUsingTimeFormat` method determines whether a specified time format is the format currently in use.

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

Pointer to a time format GUID. See [**Time Format GUIDs**](time-format-guids.md).

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                                                |
|-------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | The specified format is not the current format.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | The specified format is the current format.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>                      |



 

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

 

 




