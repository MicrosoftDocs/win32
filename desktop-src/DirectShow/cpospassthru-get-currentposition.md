---
Description: 'The get\_CurrentPosition method retrieves the current position, relative to the total duration of the stream. This method implements the IMediaPosition::get\_CurrentPosition method.'
ms.assetid: '6e68af98-440d-4ecc-b1aa-d5e241de4999'
title: 'CPosPassThru.get\_CurrentPosition method'
---

# CPosPassThru.get\_CurrentPosition method

The `get_CurrentPosition` method retrieves the current position, relative to the total duration of the stream. This method implements the [**IMediaPosition::get\_CurrentPosition**](imediaposition-get-currentposition.md) method.

## Syntax


```C++
HRESULT get_CurrentPosition(
   REFTIME *pllTime
);
```



## Parameters

<dl> <dt>

*pllTime* 
</dt> <dd>

Pointer to a variable that receives the current position, in seconds.

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

 

 




