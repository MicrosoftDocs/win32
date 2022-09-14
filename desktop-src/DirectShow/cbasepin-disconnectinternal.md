---
description: The DisconnectInternal method breaks the current pin connection.
ms.assetid: 070301ad-d079-4ad3-abdf-d5de88872e52
title: CBasePin.DisconnectInternal method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.DisconnectInternal
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.DisconnectInternal method

The `DisconnectInternal` method breaks the current pin connection.

## Syntax


```C++
HRESULT DisconnectInternal();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                         | Description                                                                        |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>             | The pin was not connected.<br/>                                              |
| <dl> <dt>**S\_OK**</dt> </dl>                | Success.<br/>                                                                |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl> | The filter is active and the pin does not support dynamic reconnection.<br/> |



 

## Remarks

The [**CBasePin::Disconnect**](cbasepin-disconnect.md) method delegates the disconnect process to this method. This method calls the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method. It also releases the reference count on the other pin, which is held by the [**CBasePin::m\_Connected**](cbasepin-m-connected.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




