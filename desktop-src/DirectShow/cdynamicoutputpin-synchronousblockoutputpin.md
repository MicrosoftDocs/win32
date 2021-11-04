---
description: The SynchronousBlockOutputPin method blocks the pin; does not return until the pin is blocked.
ms.assetid: 10fdb788-bc72-4eda-b60b-af83f954d689
title: CDynamicOutputPin.SynchronousBlockOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.SynchronousBlockOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.SynchronousBlockOutputPin method

The `SynchronousBlockOutputPin` method blocks the pin; does not return until the pin is blocked.

## Syntax


```C++
HRESULT SynchronousBlockOutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                                    | Description                                              |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                           | Success.<br/>                                      |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED**</dt> </dl>                   | Pin is already blocked on another thread.<br/>     |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED\_ON\_THIS\_THREAD**</dt> </dl> | Pin is already blocked on the calling thread.<br/> |



 

## Remarks

Do not call this method from the streaming thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




