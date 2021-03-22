---
description: The StartUsingOutputPin method obtains access to the pin for a streaming operation.
ms.assetid: afa627a9-00fd-4ad0-b674-9c54a5a1be55
title: CDynamicOutputPin.StartUsingOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.StartUsingOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.StartUsingOutputPin method

The `StartUsingOutputPin` method obtains access to the pin for a streaming operation.

## Syntax


```C++
virtual HRESULT StartUsingOutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                                                       |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                               |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>          | Unexpected error.<br/>                                      |
| <dl> <dt>**VFW\_E\_STATE\_CHANGED**</dt> </dl> | The filter was stopped, or the pin has begun flushing.<br/> |



 

## Remarks

Call this method before calling any methods that deliver data to the connected input pin or that change the connection's media type. For example, this rule applies to the following methods:

-   [**CDynamicOutputPin::ChangeOutputFormat**](cdynamicoutputpin-changeoutputformat.md)
-   [**CDynamicOutputPin::ChangeMediaType**](cdynamicoutputpin-changemediatype.md)
-   [**CDynamicOutputPin::DynamicReconnect**](cdynamicoutputpin-dynamicreconnect.md)
-   [**CBaseOutputPin::Deliver**](cbaseoutputpin-deliver.md)
-   [**CBaseOutputPin::DeliverEndOfStream**](cbaseoutputpin-deliverendofstream.md)
-   [**CBaseOutputPin::DeliverNewSegment**](cbaseoutputpin-delivernewsegment.md)
-   [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive)
-   [**IMemInputPin::ReceiveMultiple**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivemultiple)
-   [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream)
-   [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment)

Afterward, call the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method to release the access to the pin.

If the pin is blocked, `StartUsingOutputPin` waits for the pin to become unblocked. If the filter stops while the method is waiting, the method immediately returns VFW\_E\_STATE\_CHANGED. The pin maintains a count of how many times `StartUsingOutputPin` has been called without a corresponding call to **StopUsingOutputPin**. If another thread tries to block the pin while this count is non-zero, the pin sets its blocking status to "pending." The pin becomes blocked once all of the streaming operations have completed, in the final call to **StopUsingOutputPin**.

Do not hold the [**CDynamicOutputPin::m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md) critical section when you call this method. Otherwise, if the pin is blocked, it can never become unblocked, causing a deadlock.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




