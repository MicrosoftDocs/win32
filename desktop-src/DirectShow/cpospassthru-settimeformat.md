---
Description: 'The SetTimeFormat method sets the time format. This method implements the IMediaSeeking::SetTimeFormat method.'
ms.assetid: 'f6fc456d-51cf-4b2e-9248-afed9073d440'
title: 'CPosPassThru.SetTimeFormat method'
---

# CPosPassThru.SetTimeFormat method

The SetTimeFormat method sets the time format. This method implements the [**IMediaSeeking::SetTimeFormat**](imediaseeking-settimeformat.md) method.

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

 

 




