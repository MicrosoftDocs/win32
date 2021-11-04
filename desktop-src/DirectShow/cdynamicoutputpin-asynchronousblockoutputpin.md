---
description: The AsynchronousBlockOutputPin method blocks the pin. The method might return before the pin is blocked.
ms.assetid: 14cdc973-f0d3-4d1b-8491-67c1421f630b
title: CDynamicOutputPin.AsynchronousBlockOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.AsynchronousBlockOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.AsynchronousBlockOutputPin method

The `AsynchronousBlockOutputPin` method blocks the pin. The method might return before the pin is blocked.

## Syntax


```C++
HRESULT AsynchronousBlockOutputPin(
   HANDLE hNotifyCallerPinBlockedEvent
);
```



## Parameters

<dl> <dt>

*hNotifyCallerPinBlockedEvent* 
</dt> <dd>

Handle to an event. The event is signaled when the output pin is blocked, or if the caller cancels the block operation.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                                    | Description                                              |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                           | Success.<br/>                                      |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED**</dt> </dl>                   | Pin is already blocked on another thread.<br/>     |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED\_ON\_THIS\_THREAD**</dt> </dl> | Pin is already blocked on the calling thread.<br/> |



 

## Remarks

Do not call this method from the streaming thread.

If no streaming thread is using the pin, this method immediately blocks the pin. Otherwise, it sets the pin status to "pending" and returns. When the streaming operation completes, the streaming thread calls the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method, which blocks the pin and signals the **hNotifyCallerPinBlockedEvent** event. To cancel a pending block, call the [**CDynamicOutputPin::UnblockOutputPin**](cdynamicoutputpin-unblockoutputpin.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




