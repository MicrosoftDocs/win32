---
Description: 'The SetTimeFormat method sets the time format. This method implements the IMediaSeeking::SetTimeFormat method.'
ms.assetid: 'dbc7c950-8cc2-4f8e-adfa-8f5cdc1b56c7'
title: 'CSourceSeeking.SetTimeFormat method'
---

# CSourceSeeking.SetTimeFormat method

The `SetTimeFormat` method sets the time format. This method implements the [**IMediaSeeking::SetTimeFormat**](imediaseeking-settimeformat.md) method.

## Syntax


```C++
HRESULT SetTimeFormat(
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



| Return code                                                                                  | Description                                   |
|----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Success.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Specified format is not supported.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | **NULL** pointer argument.<br/>         |



 

## Remarks

The only time format supported by the base class is TIME\_FORMAT\_MEDIA\_TIME (100-nanosecond units).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




