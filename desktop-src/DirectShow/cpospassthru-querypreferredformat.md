---
Description: 'The QueryPreferredFormat method retrieves the preferred time format for the stream. This method implements the IMediaSeeking::QueryPreferredFormat method.'
ms.assetid: '8637448f-6b53-4ec9-9671-43bc8b713668'
title: 'CPosPassThru.QueryPreferredFormat method'
---

# CPosPassThru.QueryPreferredFormat method

The `QueryPreferredFormat` method retrieves the preferred time format for the stream. This method implements the [**IMediaSeeking::QueryPreferredFormat**](imediaseeking-querypreferredformat.md) method.

## Syntax


```C++
HRESULT QueryPreferredFormat(
   GUID *pFormat
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

 

 




