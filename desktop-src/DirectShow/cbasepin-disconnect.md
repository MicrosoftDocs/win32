---
description: CBasePin.Disconnect method - The Disconnect method breaks the current pin connection. This method implements the IPin::Disconnect method.
ms.assetid: 04e07978-fca5-419f-8807-fd7a6846eff9
title: CBasePin.Disconnect method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.Disconnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin.Disconnect method

The `Disconnect` method breaks the current pin connection. This method implements the [**IPin::Disconnect**](/windows/desktop/api/Strmif/nf-strmif-ipin-disconnect) method.

## Syntax


```C++
HRESULT Disconnect();
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

The base class delegates most of the work to the [**CBasePin::DisconnectInternal**](cbasepin-disconnectinternal.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




