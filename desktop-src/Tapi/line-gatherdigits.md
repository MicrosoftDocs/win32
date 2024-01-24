---
description: The TAPI LINE\_GATHERDIGITS message is sent when the current buffered digit-gathering request has terminated or is canceled. The digit buffer can be examined after this message has been received by the application.
ms.assetid: 0d27904d-9743-44bf-a7bc-132459351e01
title: LINE_GATHERDIGITS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_GATHERDIGITS message

The TAPI **LINE\_GATHERDIGITS** message is sent when the current buffered digit-gathering request has terminated or is canceled. The digit buffer can be examined after this message has been received by the application.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the call.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The reason why digit gathering was terminated. This parameter must be one and only one of the [**LINEGATHERTERM\_ constants**](linegatherterm--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

The "tick count" (number of milliseconds since Windows started) at which the digit gathering completed. For TAPI versions earlier than 2.0, this parameter is unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_GATHERDIGITS** message is only sent to the application that initiated the digit gathering on the call using [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits).

If the [**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits) function is used to cancel a previous request to gather digits, TAPI sends a **LINE\_GATHERDIGITS** message with *dwParam1* set to LINEGATHERTERM\_CANCEL to the application indicating that the originally specified buffer contains the digits gathered up to the cancellation.

Because the timestamp specified by *dwParam3* may have been generated on a computer other than the one on which the application is executing, it is useful only for comparison to other similarly timestamped messages generated on the same line device ( [**LINE\_GENERATE**](line-generate.md), [**LINE\_MONITORDIGITS**](line-monitordigits.md), [**LINE\_MONITORMEDIA**](line-monitormedia.md), [**LINE\_MONITORTONE**](line-monitortone.md)), in order to determine their relative timing (separation between events). The tick count can "wrap around" after approximately 49.7 days; applications must take this into account when performing calculations.

If the service provider does not generate the timestamp (for example, if it was created using an earlier version of TAPI), then TAPI provides a timestamp at the point closest to the service provider generating the event so that the synthesized timestamp is as accurate as possible.

> [!Note]  
> When an application invokes any asynchronous operation that writes data back into application memory, the application must keep that memory available for writing until a [**LINE\_REPLY**](line-reply.md) or **LINE\_GATHERDIGITS** message is received.

 

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_GENERATE**](line-generate.md)
</dt> <dt>

[**LINE\_MONITORDIGITS**](line-monitordigits.md)
</dt> <dt>

[**LINE\_MONITORMEDIA**](line-monitormedia.md)
</dt> <dt>

[**LINE\_MONITORTONE**](line-monitortone.md)
</dt> <dt>

[**LINE\_REPLY**](line-reply.md)
</dt> <dt>

[**lineGatherDigits**](/windows/desktop/api/Tapi/nf-tapi-linegatherdigits)
</dt> </dl>

 

 




