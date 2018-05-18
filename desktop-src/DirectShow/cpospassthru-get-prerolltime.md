---
Description: 'The get\_PrerollTime method retrieves the amount of data that will be queued before the start position. This method implements the IMediaPosition::get\_PrerollTime method.'
ms.assetid: '37c12798-eb0d-4859-8b2e-52d6ae147863'
title: 'CPosPassThru.get\_PrerollTime method'
---

# CPosPassThru.get\_PrerollTime method

The `get_PrerollTime` method retrieves the amount of data that will be queued before the start position. This method implements the [**IMediaPosition::get\_PrerollTime**](imediaposition-get-prerolltime.md) method.

## Syntax


```C++
HRESULT get_PrerollTime(
   REFTIME *pllTime
);
```



## Parameters

<dl> <dt>

*pllTime* 
</dt> <dd>

Pointer to a variable that receives the preroll time, in seconds.

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

 

 




