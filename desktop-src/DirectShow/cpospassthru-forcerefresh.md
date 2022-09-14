---
description: The ForceRefresh method is obsolete.
ms.assetid: 9895f72b-abf8-46a8-aa75-2a30901a4c41
title: CPosPassThru.ForceRefresh method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.ForceRefresh
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.ForceRefresh method

The `ForceRefresh` method is obsolete.

## Syntax


```C++
HRESULT ForceRefresh();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

Originally this class was designed to cache pointers to the connected pin's [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) and [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interfaces. The `ForceRefresh` method released those interfaces.

As currently implemented, this class does not cache those interfaces. For compatibility, the `ForceRefresh` method is still included, but it returns S\_OK without doing anything.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




