---
description: The Active method notifies the pin that the filter is now active. This method overrides the CBasePin::Active method. If the pin is connected, this method starts the streaming thread.
ms.assetid: ea32b602-2583-4de6-96ec-6ea875c49d14
title: CSourceStream.Active method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.Active
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.Active method

The `Active` method notifies the pin that the filter is now active. This method overrides the [**CBasePin::Active**](cbasepin-active.md) method. If the pin is connected, this method starts the streaming thread.

## Syntax


```C++
HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                             | Description                            |
|-----------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The pin is already active.<br/>  |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | Could not start the thread.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




