---
description: The IsFormatSupported method determines whether a specified time format is supported. This method implements the IMediaSeeking::IsFormatSupported method.
ms.assetid: 79b6dfd4-7f03-479b-b855-8f389bf6cbc7
title: CSourceSeeking.IsFormatSupported method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceSeeking.IsFormatSupported
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking.IsFormatSupported method

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

Pointer to a time format GUID. See [**Time Format GUIDs**](time-format-guids.md).

</dd> </dl>

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                               | Description                             |
|-------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | The format is not supported.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | The format is supported.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/>   |



 

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

 

 




