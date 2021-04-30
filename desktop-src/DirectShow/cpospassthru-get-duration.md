---
description: The get\_Duration method retrieves the duration of the stream. This method implements the IMediaPosition::get\_Duration method.
ms.assetid: 326a8cd3-d05f-49d0-941d-08f9778e9a06
title: CPosPassThru.get_Duration method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.get_Duration
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.get\_Duration method

The `get_Duration` method retrieves the duration of the stream. This method implements the [**IMediaPosition::get\_Duration**](/windows/desktop/api/Control/nf-control-imediaposition-get_duration) method.

## Syntax


```C++
HRESULT get_Duration(
   REFTIME *plength
);
```



## Parameters

<dl> <dt>

*plength* 
</dt> <dd>

Pointer to a variable that receives the total stream length, in seconds.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




