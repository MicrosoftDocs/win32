---
description: The get\_CurrentPosition method retrieves the current position, relative to the total duration of the stream. This method implements the IMediaPosition::get\_CurrentPosition method.
ms.assetid: 6e68af98-440d-4ecc-b1aa-d5e241de4999
title: CPosPassThru.get_CurrentPosition method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.get_CurrentPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CPosPassThru.get\_CurrentPosition method

The `get_CurrentPosition` method retrieves the current position, relative to the total duration of the stream. This method implements the [**IMediaPosition::get\_CurrentPosition**](/windows/desktop/api/Control/nf-control-imediaposition-get_currentposition) method.

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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




