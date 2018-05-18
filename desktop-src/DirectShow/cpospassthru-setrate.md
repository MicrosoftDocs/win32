---
Description: 'The SetRate method sets the playback rate. This method implements the IMediaSeeking::SetRate method.'
ms.assetid: '1b38eb5d-38fd-408b-9f20-4f8d18158f92'
title: 'CPosPassThru.SetRate method'
---

# CPosPassThru.SetRate method

The `SetRate` method sets the playback rate. This method implements the [**IMediaSeeking::SetRate**](imediaseeking-setrate.md) method.

## Syntax


```C++
HRESULT SetRate(
   double dRate
);
```



## Parameters

<dl> <dt>

*dRate* 
</dt> <dd>

Playback rate. Must not be zero.

</dd> </dl>

## Return value

Returns E\_INVALIDARG if *dRate* is zero. Otherwise, returns the **HRESULT** value from the connected pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




