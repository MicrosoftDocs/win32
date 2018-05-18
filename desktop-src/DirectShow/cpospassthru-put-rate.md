---
Description: 'The put\_Rate method sets the playback rate. This method implements the IMediaPosition::put\_Rate method.'
ms.assetid: 'c077f344-de34-4f8a-8e08-6d7086a5a4f1'
title: 'CPosPassThru.put\_Rate method'
---

# CPosPassThru.put\_Rate method

The `put_Rate` method sets the playback rate. This method implements the [**IMediaPosition::put\_Rate**](imediaposition-put-rate.md) method.

## Syntax


```C++
HRESULT put_Rate(
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

## Remarks

Negative rates indicate reverse play. Not all media will support reverse play.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




