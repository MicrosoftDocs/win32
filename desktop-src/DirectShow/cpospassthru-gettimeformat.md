---
Description: 'The GetTimeFormat method retrieves the current time format. This method implements the IMediaSeeking::GetTimeFormat method.'
ms.assetid: '445c1873-da6f-42be-a4cf-0c475c5f0723'
title: 'CPosPassThru.GetTimeFormat method'
---

# CPosPassThru.GetTimeFormat method

The `GetTimeFormat` method retrieves the current time format. This method implements the [**IMediaSeeking::GetTimeFormat**](imediaseeking-gettimeformat.md) method.

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

Pointer to a variable that receives a time format GUID.

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

 

 




