---
Description: 'The put\_StopTime method sets the time at which the playback will stop, relative to the duration of the stream. This method implements the IMediaPosition::put\_StopTime method.'
ms.assetid: '0a344cad-df93-47f1-8c7f-5d5ef775b850'
title: 'CPosPassThru.put\_StopTime method'
---

# CPosPassThru.put\_StopTime method

The `put_StopTime` method sets the time at which the playback will stop, relative to the duration of the stream. This method implements the [**IMediaPosition::put\_StopTime**](imediaposition-put-stoptime.md) method.

## Syntax


```C++
HRESULT put_StopTime(
   REFTIME llTime
);
```



## Parameters

<dl> <dt>

*llTime* 
</dt> <dd>

Stop time as a **double** value, in seconds.

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

 

 




