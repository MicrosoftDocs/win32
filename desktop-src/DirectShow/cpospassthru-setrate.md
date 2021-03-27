---
description: The SetRate method sets the playback rate. This method implements the IMediaSeeking::SetRate method.
ms.assetid: 1b38eb5d-38fd-408b-9f20-4f8d18158f92
title: CPosPassThru.SetRate method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.SetRate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.SetRate method

The `SetRate` method sets the playback rate. This method implements the [**IMediaSeeking::SetRate**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-setrate) method.

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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




