---
Description: 'The get\_StopTime method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the IMediaPosition::get\_StopTime method.'
ms.assetid: '0ca3f047-ac43-419e-a1ed-b406f89f7af7'
title: 'CPosPassThru.get\_StopTime method'
---

# CPosPassThru.get\_StopTime method

The `get_StopTime` method retrieves the time at which the playback will stop, relative to the duration of the stream. This method implements the [**IMediaPosition::get\_StopTime**](imediaposition-get-stoptime.md) method.

## Syntax


```C++
HRESULT get_StopTime(
   REFTIME *pllTime
);
```



## Parameters

<dl> <dt>

*pllTime* 
</dt> <dd>

Pointer to a variable that receives the stop time, in seconds.

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

 

 




