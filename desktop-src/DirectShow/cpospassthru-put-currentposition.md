---
Description: 'The put\_CurrentPosition method sets the current position, relative to the total duration of the stream. This method implements the IMediaPosition::put\_CurrentPosition method.'
ms.assetid: '22d7e9e4-47da-45b5-9be0-3c5128f90353'
title: 'CPosPassThru.put\_CurrentPosition method'
---

# CPosPassThru.put\_CurrentPosition method

The `put_CurrentPosition` method sets the current position, relative to the total duration of the stream. This method implements the [**IMediaPosition::put\_CurrentPosition**](imediaposition-put-currentposition.md) method.

## Syntax


```C++
HRESULT put_CurrentPosition(
   REFTIME llTime
);
```



## Parameters

<dl> <dt>

*llTime* 
</dt> <dd>

New position, in seconds.

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
</dt> </dl>

 

 




