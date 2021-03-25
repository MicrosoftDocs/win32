---
description: The TAPI LINE\_GENERATE message is sent to notify the application that the current digit or tone generation has terminated.
ms.assetid: 375823c5-22c2-4010-bfb4-5b8b46141c72
title: LINE_GENERATE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_GENERATE message

The TAPI **LINE\_GENERATE** message is sent to notify the application that the current digit or tone generation has terminated. Only one such generation request can be in progress an a given call at any time. This message is also sent when digit or tone generation is canceled.


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

The reason why digit or tone generation was terminated. This parameter must be one and only one of the [**LINEGENERATETERM\_ constants**](linegenerateterm--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

The "tick count" (number of milliseconds since Windows started) at which the digit or tone generation completed. For API versions earlier than 2.0, this parameter is unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_GENERATE** message is only sent to the application that requested the digit or tone generation.

Because the timestamp specified by *dwParam3* may have been generated on a computer other than the one on which the application is executing, it is useful only for comparison to other similarly timestamped messages generated on the same line device ( [**LINE\_GATHERDIGITS**](line-gatherdigits.md), [**LINE\_MONITORDIGITS**](line-monitordigits.md), [**LINE\_MONITORMEDIA**](line-monitormedia.md), [**LINE\_MONITORTONE**](line-monitortone.md)), in order to determine their relative timing (separation between events). The tick count can "wrap around" after approximately 49.7 days; applications must take this into account when performing calculations.

If the service provider does not generate the timestamp (for example, if it was created using an earlier version of TAPI), then TAPI provides a timestamp at the point closest to the service provider generating the event so that the synthesized timestamp is as accurate as possible.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_GATHERDIGITS**](line-gatherdigits.md)
</dt> <dt>

[**LINE\_MONITORDIGITS**](line-monitordigits.md)
</dt> <dt>

[**LINE\_MONITORMEDIA**](line-monitormedia.md)
</dt> <dt>

[**LINE\_MONITORTONE**](line-monitortone.md)
</dt> </dl>

 

 




