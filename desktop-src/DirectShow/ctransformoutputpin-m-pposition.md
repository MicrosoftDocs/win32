---
Description: 'Helper object to pass seek commands upstream.'
ms.assetid: '2ca9bae7-a133-4e09-8aa7-1c4601ec5db0'
title: 'CTransformOutputPin::m\_pPosition member'
---

# CTransformOutputPin::m\_pPosition member

Helper object to pass seek commands upstream.

## Syntax


```C++
IUnknown *m_pPosition;
```



## Remarks

When the pin is first queried for the [**IMediaPosition**](imediaposition.md) or [**IMediaSeeking**](imediaseeking.md) interface, it creates and aggregates a [**CPosPassThru**](cpospassthru.md) helper object.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




