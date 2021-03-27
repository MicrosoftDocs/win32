---
description: The Disconnect method breaks the current pin connection. This method implements the IPin::Disconnect method.
ms.assetid: 8d92a504-98ad-4f8f-89a4-f0c80763db44
title: CDynamicOutputPin.Disconnect method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.Disconnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.Disconnect method

The `Disconnect` method breaks the current pin connection. This method implements the [**IPin::Disconnect**](/windows/desktop/api/Strmif/nf-strmif-ipin-disconnect) method.

## Syntax


```C++
HRESULT Disconnect();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                           |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The pin was not connected.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                   |



 

## Remarks

This method overrides the [**CBasePin::Disconnect**](cbasepin-disconnect.md) method to enable disconnecting while the filter is active.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




